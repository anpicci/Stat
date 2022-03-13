import ROOT
import os, sys
import optparse 
import copy
from Stat.Limits.settings import bkg, histos, years, leptons, sigpoints, lssamples_1D, syst
import collections 

usage = 'usage: %prog -p histosPath -o outputFile'
parser = optparse.OptionParser(usage)
parser.add_option('-i', '--input', dest='path', type='string', default= "./histos2017v6/",help='Where can I find input histos?')
parser.add_option("-o","--outputFile",dest="output",type="string",default="histos_2017.root",help="Name of the output file collecting histos in Combine user frieldy schema. Default is histos.root")
parser.add_option("-s","--stat",dest="mcstat",action='store_true', default=False)
parser.add_option("-u","--unblind",dest="unblind",action='store_true', default=False)
parser.add_option("--ls",dest="ls",type="string", default="")
(opt, args) = parser.parse_args()
sys.argv.append('-b')

path =  opt.path
ofilename = opt.output
mcstat = opt.mcstat
unblind = opt.unblind
print("ATTENTION UNBLIND OPTION IS " + str(unblind))
# Creating output file
ofile = ROOT.TFile(ofilename,"RECREATE")
ofile.Close()
sampFiles = {}

procs = bkg

# Getting list of files in histos
print path

for year in years:
    yearstring = ""
    if "UL" in path:
        yearstring = "UL" + year
    else:
        yearstring = year

    for lep in leptons:
        path_ = path + lep + '/'

        tmp_list = [f for f in os.listdir(path_) if (os.path.isfile(os.path.join(path_, f)) and f.endswith(".root") and f!=ofilename and year in f)]

        sampFiles[year+lep] = []

        for fn in tmp_list:
            isSig = False
            isLS = False

            if fn.startswith("Data"):
                sampFiles[year+lep].append([fn, fn])

            if fn.startswith('VBS_SSWW_'):
                for sigp in sigpoints:
                    for sig in sigp:
                        print sig

                        if fn.startswith('VBS_SSWW_' + sig + "_" + yearstring):
                            isSig = True
                            sampFiles[year+lep].append([fn, fn])

                        if opt.ls != "":
                            #print sig
                            if not (sig.startswith(opt.ls)):# or sig.startswith('F')):
                                continue

                            sig_splitted = sig.replace("_SM", "").replace("_BSM", "").split("_")
                            sig_op = sig_splitted[0]
                            
                            if len(sig_splitted) > 1:
                                sig_op += "_" + sig_splitted[1]
                        
                            ls_dict = lssamples_1D[sig_op]

                            for nout, nin in ls_dict.items():
                                if fn.startswith(nin+"_"):
                                    sampFiles[year+lep].append([fn, nout])
                                    isLS = True
                                    break

                        if isSig or isLS:
                            break
            
                if (isSig or isLS) and not (fn.startswith("VBS_SSWW_SM_" + year)):
                    continue

            for p in procs:
                if not fn.startswith(p + "_"):
                    continue

                isSM = False

                for sigp in sigpoints:
                    if p.startswith("DYJets"):
                        break
                    for sig in sigp:
                        if '_SM' in sig or sig == 'SM':
                            if 'TT_' in sig or 'TL_' in sig or 'LL_' in sig:
                                if sig in p or 'SSWW_SM' in p:
                                    isSM = True
                                    break
                            elif '_SM' in p:
                                isSM = True
                                break
                        else:
                            if 'TT_' in p or 'TL_' in p or 'LL_' in p:
                                isSM = True
                                break
                
                if isSM:
                    continue

                sampFiles[year+lep].append([fn, fn])
                break


print 'sampFiles:'
for k, v in sampFiles.items():
    for el in v:
        print el

#*******************************************************#
#                                                       #
#     FILLING IN THE INPUT ROOT FILE FOR COMBINE        #
#                                                       #
#*******************************************************#

ofile = ROOT.TFile(ofilename,"RECREATE")
for year in years:
    print year
    yeartag = ""
    if "vUL" in path:
        yeartag = "UL" + year
    else:
        yeartag = year
    
    for lep in leptons:
        for k_, h_ in histos.iteritems():
            rootdir = k_ + "_" + lep + "_" + year
            #print rootdir
            #if not os.path.isdir(k_+ "_" + year):
            #try:
            if not rootdir in ofile.GetListOfKeys():
                print "creating", rootdir
                newsubdir = ofile.mkdir(rootdir)#k_ + "_" + lep + "_" + year)
                #print newsubdir

        path_ = path + lep + '/'
        #print "path:", path_
        histos_data = []
        for flist in sampFiles[year+lep]: 
            f = flist[0]
            #print f
            try:
                ifile = ROOT.TFile.Open(path_ + f)
            except IOError:
                print "\nCannot open ", f
            else:
                print "\nOpening file ",  f
            ifile.cd()

            samp = ""
            if flist[0] == flist[1]:
                samp = f.replace(".root", "").replace(lep, "").replace("_" + yeartag + "_", "")
            else:
                samp = flist[1]
            print samp

            print "\nWe are looking into file: ", f
   
            for k_, h_ in histos.iteritems():
                if lep=='emu' and not k_.startswith("CRTT"):
                    continue

                print "We are looking for object ", h_
                h = ifile.Get(h_)
                hsyst = collections.OrderedDict()

                for sysname, systype in syst.items():
                    if not systype[0] == "shape" or sysname == "autoMCstat":
                        continue
                    if systype[1] == "all" or samp in systype[1] or ('sig' in systype[1] and samp.startswith("VBS_")):
                        hup_ = h_ + "_" + sysname + "Up"
                        hdown_ = h_ + "_" + sysname + "Down"
                        #print hup_, hdown_
                        #print ifile.Get(hup_).GetName()
                        #print ifile.Get(hdown_).GetName()
                        hsyst[sysname] = [ifile.Get(hup_), ifile.Get(hdown_)]

                ofile.cd(k_ + "_" + lep + "_" + year)
                print "We are looking for histo %s for samp %s in %s" % (h_, samp, f)
                h.SetName(samp)

                if(samp.startswith("Data")):
                    print "\nis data!"
                    print h
                    if (k_.startswith("SR") and unblind) or k_.startswith("CR"):
                        print("passed", h.Integral())
                        h.Write("data_obs", ROOT.TObject.kWriteDelete)
                    else:
                        continue

                else:
                    h.Write(samp, ROOT.TObject.kWriteDelete)

                    for sname, shists in hsyst.items():
                        print "systematic:", sname, shists[0].GetName(), shists[1].GetName()

                        for i, var in enumerate(shists):
                            sampsyst = samp + "_"  + sname
                            if i == 0:
                                sampsyst += "Up"
                            elif i == 1:
                                sampsyst += "Down"
                            shists[i].Write(sampsyst, ROOT.TObject.kWriteDelete) 

                print h.GetName()
                nBinsX = h.GetNbinsX()

                if k_ in samp:
                    samp = samp.replace("_" + k_, "")         
                elif "cat" in samp:
                    samp = samp.replace("cat_", "")         
                #print "SAMP after channel removal ",samp
                if(samp.startswith("data")):
                    samp = "Data"
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
                

                #h.Delete()
#ofile.Write()
ofile.Close()

#*******************************************************#
#                                                       #
#           CREATING TOTAL BACKGORUND HISTOS            #
#                                                       #
#*******************************************************#
print '**********************************************************'
print '**********************************************************'
print '**********************************************************'
print '**********************************************************'
print '**********************************************************'
print '**********************************************************'
print histos.keys()
for lep in leptons:
    ofile = ROOT.TFile(ofilename,"UPDATE")    
    for year in years:
        yearstring = ""
        if "vUL" in path:
            yearstring = "UL" + year
        else:
            yearstring = year

        histData = dict(zip(histos.keys(), [None]*len(histos.keys())))
        path_ = path + lep + '/'
        for p in bkg:
            print p
            isSM = False

            for sigp in sigpoints:
                if p.startswith("DYJets"):
                    break
                for sig in sigp:
                    if '_SM' in sig or sig == 'SM':
                        if 'TT_' in sig or 'TL_' in sig or 'LL_' in sig:
                            if sig in p or 'SSWW_SM' in p:
                                isSM = True
                                break
                        elif '_SM' in p:
                            isSM = True
                            break
                    else:
                        if 'TT_' in p or 'TL_' in p or 'LL_' in p:
                            isSM = True
                            break

            if isSM:
                continue


            try:
                ifile = ROOT.TFile.Open(path_ + p + "_" + yearstring + "_" + lep + ".root")
            except IOError:
                print "Cannot open " + p + "_" + year + "_" + lep + ".root"
            else:
                print "Opening file " +  p + "_" + year + "_" + lep + ".root"
            print "bkg:", p

            ifile.cd()
            for k_, h_ in histos.iteritems():
                #if lep=='emu' and not k_.startswith('CRTT'):
                    #continue
                print k_, h_
                tmphist = ifile.Get( h_)
                print tmphist.Integral()
                if histData[k_] is None: 
                    histData[k_] = copy.deepcopy(tmphist)
                else:
                    histData[k_].Add(tmphist)

        for key, value in histData.items():
            print key, value

        for k_ in histos.keys():    
            print "Creating Bkg histogram ", k_
            #if not os.path.isdir( k_ + "_" + year):
            #    newsubdir = ofile.mkdir(k_+"_" + year)
            ofile.cd(k_+ "_" + lep + "_" + year)
            histData[k_].SetName("Bkg")
            histData[k_].Write("Bkg", ROOT.TObject.kWriteDelete)
            print "Bkg integral ", histData[k_].Integral()
            bkgpdf =  histData[k_].Clone("BkgPdf")
            bkgpdf.Write(str(bkgpdf.GetName()), ROOT.TObject.kWriteDelete)
            # check for negative bins in bkg pdf 
            for i in range(0, bkgpdf.GetNbinsX()+1):
                content = bkgpdf.GetBinContent(i)
                if(content<0.):
                    bkgpdf.SetBinContent(i, 1.E-3)
            bkgint = float(bkgpdf.Integral())
            bkgscale = float(1./bkgint)
            #bkgpdf.Scale(1./ bkgpdf.Integral())
            bkgpdf.Scale(bkgscale)
            print "Bkg pdf ", bkgpdf.Integral()
            if not (k_.startswith("CR")) and not unblind:# or k_.startswith("CR"):
                print "\nCreating data_obs blinded"
                histdata = bkgpdf.Clone("data_obs")
                histdata.Reset()
                print "data pdf ", histdata.Integral()
                histdata.FillRandom(bkgpdf, int(histData[k_].Integral()))
                #histdata.Scale(bkgint)
                print "data  ", histdata.Integral()
                histData[k_].SetName("data_obs")
                histdata.Write("data_obs", ROOT.TObject.kWriteDelete)
        #ofile.Write()
    ofile.Close()
