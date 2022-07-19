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
print "Creating output file", ofilename
ofile = ROOT.TFile(ofilename,"RECREATE")
ofile.Close()
sampFiles = {}

procs = bkg

toremove = []
for p in procs:
    isSM = False
    
    if p.startswith("DYJets"):
        continue
    
    for sigp in sigpoints:
        for sig in sigp:
            if '_SM' in sig or sig == 'SM' or sig.startswith("WpWp"):
                if 'TT_' in sig or 'TL_' in sig or 'LL_' in sig:   
                    if (sig in p and not "QCD" in p) or 'SSWW_SM' in p:
                        isSM = True
                        break
                elif '_SM' in p:
                    isSM = True

                    break
                elif sig == "WpWpJJ" or sig == "WpWpJJ_QCD":
                    if p == "WpWpJJ_QCD":
                        isSM = True
                        break
            else:
                if 'TT_' in p or 'TL_' in p or 'LL_' in p or p=="VBS_SSWW_SM":
                    isSM = True
                    break
    if isSM:
        toremove.append(p)

for tor in toremove:
    procs.remove(tor)

# Getting list of files in histos

#print("\n\n\ninside collecthistos")
for year in years:
    yearstring = ""
    if "UL" in path:
        yearstring = "UL" + year
    else:
        yearstring = year

    for lep in leptons:
        path_ = path + lep + '/'

        tmp_list = [f for f in os.listdir(path_) if (os.path.isfile(os.path.join(path_, f)) and f.endswith(".root") and f!=ofilename and str(year+"_") in f)]

        sampFiles[year+lep] = []

        for fn in tmp_list:
            if fn.startswith("Data"):
                sampFiles[year+lep].append([[fn], "data_obs"])
                break

        if opt.ls == "":
            for sigp in sigpoints:
                for sig in sigp:
                    sigstr = ""
                    if sig.startswith("WpWp"):
                        sigstr = sig
                    else:
                        sigstr = "VBS_SSWW_" + sig

                    isThere = False
                    #print 'VBS_SSWW_' + sig + "_" + yearstring
                    for fn in tmp_list:
                        if fn.startswith(sigstr + "_" + yearstring):
                            isThere = True
                            sampFiles[year+lep].append([[fn], sigstr])
                            break
                
                    if not isThere:
                        raise RuntimeError("Signal plots are not available for " + sig + "!")

        else:
            ops = opt.ls.split(":")
            setpiecs = []
            for op in ops:
                if len(op.split("_")) > 1:
                    setpiecs.append(("_")+op.split("_")[-1])
            combo = copy.deepcopy(opt.ls)
            for setpiec in setpiecs:
                combo = combo.replace(setpiec, "")
                    
            ls_dict = lssamples_1D[combo]

            for nout, nin in ls_dict.items():
                ninlist = nin.split(",")
                sampFiles[year+lep].append([[], nout])

                for ninel in ninlist:
                    for fn in tmp_list:

                        if fn.startswith(ninel+"_"):
                            sampFiles[year+lep][-1][0].append(fn)
                            break

        for p in procs:
            for fn in tmp_list:
                if not fn.startswith(p + "_"):
                    continue

                sampFiles[year+lep].append([[fn], p])
                break
            
'''       
print 'sampFiles:'
for k, v in sampFiles.items():
    for el in v:
        print el
'''
#*******************************************************#
#                                                       #
#     FILLING IN THE INPUT ROOT FILE FOR COMBINE        #
#                                                       #
#*******************************************************#

ofile = ROOT.TFile(ofilename,"RECREATE")
for year in years:
    #print year
    yeartag = ""
    if "vUL" in path:
        yeartag = "UL" + year
    else:
        yeartag = year
    
    for lep in leptons:
        #print "\n", lep
        for k_, h_ in histos.iteritems():
            rootdir = k_ + "_" + lep + "_" + year
            #print rootdir
            #if not os.path.isdir(k_+ "_" + year):
            #try:
            if not rootdir in ofile.GetListOfKeys():
                #print "creating", rootdir
                newsubdir = ofile.mkdir(rootdir)#k_ + "_" + lep + "_" + year)
                #print newsubdir

        path_ = path + lep + '/'
        #print "path:", path_
        histos_data = []
        fstoopen = []

        histData = dict(zip(histos.keys(), [None]*len(histos.keys())))

        for k_, h_ in histos.iteritems():
            if lep=='emu' and not k_.startswith("CRTT"):
                continue

            for flist in sampFiles[year+lep]:
                #print "\nflist", flist
                h = None

                hsyst = collections.OrderedDict()
                for sysname, systype in syst.items():
                    if not systype[0].startswith("shape") or sysname == "autoMCstat":
                        continue
                    syskey = copy.deepcopy(sysname)
                    if systype[0].startswith("shape"):
                        if systype[2] == "uncorr":
                            syskey += "_" + year

                    hsyst[syskey] = [None, None]
                
                samp = flist[1]
                #print "\nsamp", samp, flist[0]
                for f in flist[0]:
                    try:
                        ifile = ROOT.TFile.Open(path_ + f)
                    except IOError:
                        print "Cannot open ", f, + "\n"
                    else:
                        pass
                        #print "Opening file ",  path_ + f
                    ifile.cd()
                
                    #print "We are looking for object ", h_
                    htemp = copy.deepcopy(ifile.Get(h_).Clone())
                    sign = +1.
                    if "VBS_SSWW_" in f and "_F" in f:
                        if samp.startswith("sm_lin_quad") and "_BSM_" in f:
                            sign = -1.
                        elif samp.startswith("quad_"):
                            sign = 0.
                    
                    if sign == 0:
                        htemp.Reset("ICE")
                    else:
                        htemp.Scale(sign)
                    
                    #print "htemp", htemp
                    if h is None:
                        h = copy.deepcopy(htemp)
                    else:
                        h.Add(htemp, 1)

                    #hsyst = collections.OrderedDict()
            
                    for sysname, systype in syst.items():
                        if not systype[0].startswith("shape") or sysname == "autoMCstat":
                            continue
                        
                        #print "systype[1]", systype[1]
                        ifile.cd()
                        
                        #print "to syst?", (systype[1] == "all"), (samp in systype[1]), ('sig' in systype[1] and (f.startswith("VBS_") or f.startswith("WpWp")))
                        if systype[1] == "all" or samp in systype[1] or ('sig' in systype[1] and (f.startswith("VBS_") or f.startswith("WpWp"))):
                            hup_ = h_ + "_" + sysname
                            hdown_ = h_ + "_" + sysname
                            hup_ += "Up"
                            hdown_ += "Down"
                            sysName = sysname
                            #print ifile
                            #print hup_, hdown_
                            if systype[0].startswith("shape"):
                                if systype[2] == "uncorr":
                                    sysName += "_" + year

                            huptemp = copy.deepcopy(ifile.Get(hup_).Clone())
                            hdowntemp = copy.deepcopy(ifile.Get(hdown_).Clone())
                            sign = +1.
                            if "VBS_SSWW_" in f and "_F" in f:
                                if samp.startswith("sm_lin_quad") and "_BSM_" in f:
                                    sign = -1.
                                elif samp.startswith("quad_"):
                                    sign = 0.
                            
                            if sign == 0:
                                huptemp.Reset("ICE")
                                hdowntemp.Reset("ICE")
                            else:
                                huptemp.Scale(sign)
                                hdowntemp.Scale(sign)
                    
                            if hsyst[sysName][0] is None:
                                hsyst[sysName][0] = copy.deepcopy(huptemp)
                            else:
                                hsyst[sysName][0].Add(huptemp, 1)

                            if hsyst[sysName][1] is None:
                                hsyst[sysName][1] = copy.deepcopy(hdowntemp)
                            else:
                                hsyst[sysName][1].Add(hdowntemp, 1)
                            
                #if "_F" in samp and not "DY" in samp:
                    #print "h", h, h.Integral()
                    #for i in range(0, h.GetNbinsX()):
                        #content = h.GetBinContent(i)
                        #print("content bin #" + str(i+1) + ":\t" + str(content))
                    #for khs, vhs in hsyst.items():
                        #if not None in vhs:
                            #print "h_", khs
                            #print "vhs[0]", vhs[0], vhs[0].Integral()
                            #for i in range(0, vhs[0].GetNbinsX()):
                                #content = vhs[0].GetBinContent(i)
                                #print("content bin #" + str(i+1) + ":\t" + str(content))
                            #print "vhs[1]", vhs[1], vhs[1].Integral()
                            #for i in range(0, vhs[1].GetNbinsX()):
                                #content = vhs[1].GetBinContent(i)
                                #print("content bin #" + str(i+1) + ":\t" + str(content))
                            

                ofile.cd(k_ + "_" + lep + "_" + year)
                samplab = ""
                if samp.startswith("quad_") or samp.startswith("sm_lin_"):
                    samplab = samp.replace("_F", "_c")
                else:
                    samplab = samp
                #print "h", h, h.Integral()
                h.SetName(samplab)
                h.Write(samplab, ROOT.TObject.kWriteDelete)

                if samp in bkg:
                    if histData[k_] is None: 
                        histData[k_] = copy.deepcopy(h)
                    else:
                        histData[k_].Add(h)

                for sname, shists in hsyst.items():
                    if None in shists:
                        continue
                    #print "systematic:", sname, shists[0].GetName(), shists[1].GetName()
                    for i, var in enumerate(shists):
                        samplab = ""
                        if samp.startswith("quad_") or samp.startswith("sm_lin_"):
                            samplab = samp.replace("_F", "_c")
                        else:
                            samplab = samp

                        sampsyst = samplab + "_"  + sname
                        if i == 0:
                            sampsyst += "Up"
                        elif i == 1:
                            sampsyst += "Down"
                        
            
                        shists[i].Write(sampsyst, ROOT.TObject.kWriteDelete) 
                        
            
                
                #nBinsX = h.GetNbinsX()

                #if k_ in samp:
                    #samp = samp.replace("_" + k_, "")                     
                #elif "cat" in samp:
                    #samp = samp.replace("cat_", "")             
                #print "SAMP after channel removal ",samp
                #if(samp.startswith("data")):
                    #samp = "Data"
                    
                #if(samp.startswith("SVJ") and not (samp.endswith("Up") or samp.endswith("Down")) and mcstat == True ):
                    #for n in xrange(nBinsX):
                        #hNameUp = "%s_mcstat_%s_bin%d_Up" % ( h_, samp, n+1)
                        #hNameDown = "%s_mcstat_%s_bin%d_Down" % ( h_, samp, n+1)
                        ##print "Histogram: ", hNameUp                  
                        #h_mcStatUp = ifile.Get(hNameUp)
                        #h_mcStatDown = ifile.Get(hNameDown)
                        #h_mcStatUp.SetName("%s_mcstat_%s_%s_%s_bin%dUp" % (samp, k_, year, samp, n+1))
                        #h_mcStatUp.Write("%s_mcstat_%s_%s_%s_bin%dUp" % (samp, k_, year, samp, n+1), ROOT.TObject.kWriteDelete)
                        #h_mcStatDown.SetName("%s_mcstat_%s_%s_%s_bin%dDown" % (samp, k_, year,  samp, n+1))
                        #h_mcStatDown.Write("%s_mcstat_%s_%s_%s_bin%dDown" % (samp, k_, year, samp, n+1), ROOT.TObject.kWriteDelete)
                

                del h, hsyst
            
            ofile.cd(k_+ "_" + lep + "_" + year)
            histData[k_].SetName("Bkg")
            histData[k_].Write("Bkg", ROOT.TObject.kWriteDelete)
            #print "Bkg integral ", histData[k_].Integral()
            bkgpdf =  histData[k_].Clone("BkgPdf")
            #print histData[k_].Integral()

            # check for negative bins in bkg pdf 
            for i in range(0, bkgpdf.GetNbinsX()+1):
                content = bkgpdf.GetBinContent(i)
                if(content<0.):
                    bkgpdf.SetBinContent(i, 1.E-3)
            
            bkgint = float(bkgpdf.Integral())
            bkgscale = float(1./bkgint)
            bkgpdf.Scale(bkgscale)
            ##print "Bkg pdf ", bkgpdf.Integral()
            bkgpdf.Write(str(bkgpdf.GetName()), ROOT.TObject.kWriteDelete)    
            
        #print "histData", histData
        #for kd, vd in histData.items():
            #print kd, vd.Integral()


#ofile.Write()
ofile.Close()
