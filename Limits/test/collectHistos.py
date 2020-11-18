import ROOT
import os, sys
import optparse 
import copy
from Stat.Limits.settings import processes, histos, years, leptons

usage = 'usage: %prog -p histosPath -o outputFile'
parser = optparse.OptionParser(usage)
parser.add_option('-i', '--input', dest='path', type='string', default= "./histos2017v6/",help='Where can I find input histos?')
parser.add_option("-o","--outputFile",dest="output",type="string",default="histos_2017.root",help="Name of the output file collecting histos in Combine user frieldy schema. Default is histos.root")
parser.add_option("-s","--stat",dest="mcstat",action='store_true', default=False)
(opt, args) = parser.parse_args()
sys.argv.append('-b')

path =  opt.path
ofilename = opt.output
mcstat = opt.mcstat
# Creating output file
ofile = ROOT.TFile(ofilename,"RECREATE")
ofile.Close()
sampFiles = {}
# Getting list of files in histos
print os.listdir(path)
for year in years:
    for lep in leptons:
        path_ = path + '/' + lep + '/'
        sampFiles[lep] = [f for f in os.listdir(path_) if (os.path.isfile(os.path.join(path_, f)) and f.endswith(".root") and f!=ofilename and year in f)]

#*******************************************************#
#                                                       #
#     FILLING IN THE INPUT ROOT FILE FOR COMBINE        #
#                                                       #
#*******************************************************#
histos_data = []
for year in years:
    for lep in leptons:
        path_ = path + '/' + lep + '/'
        for f in sampFiles[lep]: 
            try:
                ifile = ROOT.TFile.Open(path_ + f)
            except IOError:
                print "Cannot open ", f
            else:
                print "Opening file ",  f
            ifile.cd()
            samp = f.replace(".root", "").replace("_" + lep, "").replace("_" + year, "")         
            print 'ciao'
            print samp
            print "\nWe are looking into file: ", f
            ofile = ROOT.TFile(ofilename,"UPDATE")
            for k_, h_ in histos.iteritems():    
                print "We are looking for object ", h_
                h = ifile.Get(h_)
                if not os.path.isdir(k_+ "_" + year):
                    newsubdir = ofile.mkdir(k_ + "_" + lep + "_" + year)
                ofile.cd(k_ + "_" + lep + "_" + year)
                if(samp.startswith("Data")): samp = "data_obs"
                print "We are looking for histo %s for samp %s in %s" % (h_, samp, f)
                h.SetName(samp)
                h.Write(samp, ROOT.TObject.kWriteDelete)
                if(samp.startswith("Data")): histos_data.append(h)
                nBinsX = h.GetNbinsX()
                #print "SAMP ",samp
                if k_ in samp:
                    samp = samp.replace("_" + k_, "")         
                elif "cat" in samp: samp = samp.replace("cat_", "")         
                #print "SAMP after channel removal ",samp
                if(samp.startswith("data")): samp = "Data"
                #        h_ = h_[:4]
                if(samp.startswith("SVJ") and not (samp.endswith("Up") or samp.endswith("Down")) and mcstat == True ):
                    for n in xrange(nBinsX):
                        hNameUp = "%s_mcstat_%s_bin%d_Up" % ( h_, samp, n+1)
                        hNameDown = "%s_mcstat_%s_bin%d_Down" % ( h_, samp, n+1)
                        print "Histogram: ", hNameUp              
                        h_mcStatUp = ifile.Get(hNameUp)
                        h_mcStatDown = ifile.Get(hNameDown)
                        h_mcStatUp.SetName("%s_mcstat_%s_%s_%s_bin%dUp" % (samp, k_, year, samp, n+1))
                        h_mcStatUp.Write("%s_mcstat_%s_%s_%s_bin%dUp" % (samp, k_, year, samp, n+1), ROOT.TObject.kWriteDelete)
                        h_mcStatDown.SetName("%s_mcstat_%s_%s_%s_bin%dDown" % (samp, k_, year,  samp, n+1))
                        h_mcStatDown.Write("%s_mcstat_%s_%s_%s_bin%dDown" % (samp, k_, year, samp, n+1), ROOT.TObject.kWriteDelete)
            ofile.Write()
            ofile.Close()

#*******************************************************#
#                                                       #
#           CREATING TOTAL BACKGORUND HISTOS            #
#                                                       #
#*******************************************************#
print histos.keys()
for lep in leptons:
    ofile = ROOT.TFile(ofilename,"UPDATE")    
    histData = dict(zip(histos.keys(), [None]*len(histos.keys())))
    for year in years:
        path_ = path + '/' + lep + '/'
        for p in processes:
            try:
                ifile = ROOT.TFile.Open(path_ + p + "_" + year + "_" + lep + ".root")
            except IOError:
                print "Cannot open " + p + "_" + year + "_" + lep + ".root"
            else:
                print "Opening file " +  p + "_" + year + "_" + lep + ".root"
            ifile.cd()
            for k_, h_ in histos.iteritems():    
                tmphist = ifile.Get( h_)
                if histData[k_] is None: 
                    histData[k_] = copy.deepcopy(tmphist)
                else: histData[k_].Add(tmphist)

        for k_ in histos.keys():    
            print "Creating Bkg histogram "
            #if not os.path.isdir( k_ + "_" + year):
            #    newsubdir = ofile.mkdir(k_+"_" + year)
            ofile.cd(k_+ "_" + lep + "_" + year)
            histData[k_].SetName("Bkg")
            histData[k_].Write("Bkg", ROOT.TObject.kWriteDelete)
            print "Bkg integral ", histData[k_].Integral()
            bkgpdf =  histData[k_].Clone("BkgPdf")
            bkgpdf.Scale(1./ bkgpdf.Integral())
            print "Bkg pdf ", bkgpdf.Integral()
            histdata = bkgpdf.Clone("data_obs")
            histdata.Reset()
            print "data pdf ", histdata.Integral()
            histdata.FillRandom(bkgpdf, int(histData[k_].Integral()))
            print "data  ", histdata.Integral()
            #histData[k_].SetName("data_obs")
            histdata.Write("data_obs", ROOT.TObject.kWriteDelete)
            print "MCSTAT ", mcstat
        ofile.Write()
    ofile.Close()
