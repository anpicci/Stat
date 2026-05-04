import ROOT
import os, sys
import optparse 
import copy
#from Stat.Limits.settings import bkg, histos, years, leptons, sigpoints, lssamples_1D, syst
import collections 
import importlib

usage = 'usage: %prog -p histosPath -o outputFile'
parser = optparse.OptionParser(usage)
parser.add_option('-i', '--input', dest='path', type='string', default= "./histos2017v6/",help='Where can I find input histos?')
parser.add_option('-m', '--model', dest='model', type='string', default= "./histos2017v6/",help='model')
parser.add_option("-o","--outputFile",dest="output",type="string",default="histos_2017.root",help="Name of the output file collecting histos in Combine user frieldy schema. Default is histos.root")
parser.add_option("--ls",dest="ls",type="string", default="")
parser.add_option('--Lambda8', dest='Lambda8', default = False, action='store_true', help='add dim8 quad in 2D fits')
parser.add_option('--onlyLin', dest='onlyLin', default = False, action='store_true', help='add dim8 quad in 2D fits')
parser.add_option('--pdf', dest='pdf', type='string', default = 'total', help = 'Specify type of pdf')
parser.add_option('--settmod"', dest='settmod', type='string', default = 'total', help = 'Specify settmod')
parser.add_option('--settitle"', dest='settitle', type='string', default = 'total', help = 'Specify settitle')

(opt, args) = parser.parse_args()
sys.argv.append('-b')

pdftype = opt.pdf

setname = opt.settmod

settmod = importlib.import_module(setname)
bkg = settmod.bkg
histos = settmod.histos
years = settmod.years
leptons = settmod.leptons
sigpoints = settmod.sigpoints
lssamples_1D = settmod.lssamples_1D
syst = settmod.syst

print("lssamples:", lssamples_1D)

path = opt.path
ofilename = opt.output
print("From", path)
print("Creating output file", ofilename)
shapedir = ofilename.replace(ofilename.split("/")[-1], "")


if os.path.exists(ofilename):
    os.system("rm " + ofilename)
elif not os.path.exists(shapedir):
    os.system("mkdir "+ shapedir)
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

#print "lssamples_1D:", lssamples_1D

##print("\n\n\ninside collecthistos")
for year in years:
    #print year
    yearstring = ""
    if "UL" in path:
        yearstring = "UL" + year
    else:
        yearstring = year

    for lep in leptons:
        path_ = path + lep + '/'

        tmp_list = [f for f in os.listdir(path_) if (os.path.isfile(os.path.join(path_, f)) and f.endswith(".root") and f!=ofilename and str(year+"_") in f)]
        #print "\n", tmp_list

        sampFiles[year+lep] = []

        for fn in tmp_list:
            #print fn
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
                    ##print 'VBS_SSWW_' + sig + "_" + yearstring
                    for fn in tmp_list:
                        if fn.startswith(sigstr + "_" + yearstring):
                            isThere = True
                            sampFiles[year+lep].append([[fn], sigstr])
                            break
                    if not isThere:
                        raise RuntimeError("Signal plots are not available for " + sig + "!")

        else:
            ops = opt.ls.split(":")
            #print "OPS", ops
            setpiecs = []
            for op in ops:
                if len(op.split("_")) > 1:
                    setpiecs.append(("_")+op.split("_")[-1])
            setpiecs.sort(reverse=True)
            combo = copy.deepcopy(opt.ls)
            for setpiec in setpiecs:
                combo = combo.replace(setpiec, "")
                    
            ls_dict = lssamples_1D[combo]
            #print ls_dict

            for nout, nin in list(ls_dict.items()):
                ninlist = nin.split(",")
                sampFiles[year+lep].append([[], nout])

                for ninel in ninlist:
                    for fn in tmp_list:

                        if fn.startswith(ninel+"_"):
                            sampFiles[year+lep][-1][0].append(fn)
                            break

        for p in procs:
            #print p

            for fn in tmp_list:
                if not fn.startswith(p + "_"):
                    continue

                sampFiles[year+lep].append([[fn], p])
                break

#print 'sampFiles:'
#for k, v in sampFiles.items():
    #print k, v
    #for el in v:
        #print el     

#*******************************************************#
#                                                       #
#     FILLING IN THE INPUT ROOT FILE FOR COMBINE        #
#                                                       #
#*******************************************************#

ofile = ROOT.TFile(ofilename,"RECREATE")
for year in years:
    ##print year
    yeartag = ""
    if "vUL" in path:
        yeartag = "UL" + year
    else:
        yeartag = year
    
    for lep in leptons:
        #print "\n", lep
        for k_, h_ in histos.items():
            rootdir = k_ + "_" + lep + "_" + year
            ##print rootdir
            #if not os.path.isdir(k_+ "_" + year):
            #try:
            if not rootdir in ofile.GetListOfKeys():
                ##print "creating", rootdir
                newsubdir = ofile.mkdir(rootdir)#k_ + "_" + lep + "_" + year)
                ##print newsubdir

        path_ = path + lep + '/'
        ##print "path:", path_
        histos_data = []
        fstoopen = []

        histData = dict(list(zip(list(histos.keys()), [None]*len(list(histos.keys())))))

        for k_, h__ in histos.items():
         
        
            if lep=='emu' and not k_.startswith("CRTT"):
                continue

            for flist in sampFiles[year+lep]:
                samp = flist[1]
                #print "\nflist", flist

                #print samp, samp.startswith("VBS_SSWW_F"), h__
                if ("_FM" in samp or "_FS" in samp or "_FT" in samp):
                    h_ = h__.replace("DNN_dim6_final_2_NOMOREDY_lower_NONOISE_LCB", "DNN_dim8_final_3_NOMOREDY_lower_NONOISE_LCB_again_2")
                else:
                    h_ = copy.deepcopy(h__)
                h = None

                
                hsyst = collections.OrderedDict()
                for sysnam, systype in list(syst.items()):
                    if not (systype[0].startswith("shape") or (systype[0] == 'lnN' and systype[2] == 0.) ) or sysnam == "autoMCstat":
                    #if not systype[0].startswith("shape") or sysnam == "autoMCstat":
                        continue
                    syskey = copy.deepcopy(sysnam)
                    if sysnam.startswith("QCDScale") or (sysnam.startswith("pdf_") and pdftype.endswith("sep")) or sysnam.startswith("ISR") or sysnam.startswith("FSR") or sysnam.startswith("jes"):
                        sysname = sysnam.replace("WpWpJJ_", "").replace("_" + sysnam.split("_")[-1], "")
                    else:
                        sysname = sysnam
                    #if not sysnam.startswith("QCDscale"):
                        #sysname = sysnam.split("_")[0]
                    #else:
                        #sysname = sysname
                    if systype[0].startswith("shape") or systype[0] == 'lnN':
                        if systype[-1] == "uncorr":
                            syskey += "_" + year

            
                    hsyst[syskey] = [None, None]
                
                Error = False
                #print "\n\nflist[0]", flist[0]
                for f in flist[0]:
                    #print "f", f
                    try:
                        ifile = ROOT.TFile.Open(path_ + f)
                    except IOError:
                        print("Cannot open ", f, + "\n")
                    else:
                        pass
                        #print "\nOpening file ",  path_ + f
                    ifile.cd()
    
                    #print "We are looking for object ", h_
                    try:
                        htemp = copy.deepcopy(ifile.Get(h_).Clone())
                    except:
                        print("Problems in " + path_ + f + " searching for " + h_)
                        Error = True
                        continue
                        
                    #print "samp:", samp, samp.startswith("sm_lin_quad"), samp.startswith("quad_")
                    #print "before htemp", htemp.Integral()
                    sign = +1.
                    #if not ":" in opt.model:
                    #    pass
                    
                    if "VBS_SSWW_" in f and "_F" in f:
                        if samp.startswith("sm_lin_quad") and "_BSM_" in f:
                            if not opt.Lambda8 and ":" in opt.model: # or opt.onlyLin):
                                if "_LIN" in flist[0][1]:
                                    sign = 0.
                                else:
                                    sign = -1.
                            else:
                                if "_LIN" in flist[0][1]:
                                    sign = 1.
                                else:
                                    sign = 0.
                        elif samp.startswith("quad_"):
                            if not opt.Lambda8 and ":" in opt.model: # or opt.onlyLin:
                                sign = 0.
                            else:
                                sign = +1.
                    elif "VBS_SSWW_" in f and "_c" in f:
                        if samp.startswith("sm_lin_quad") and "_BSM_" in f:
                            if False: #opt.onlyLin:
                                if "_LIN_" in flist[0][1]:
                                    sign = 0.
                                else:
                                    sign = -1.
                            else:
                                if "_LIN" in flist[0][1]:
                                    sign = 1.
                                else:
                                    sign = 0.
                                #if not ('_cHl3_' in f or '_cqq31_' in f):
                                #sign = +1.
                                #else:
                                #    sign = 0.
                        elif samp.startswith("quad_c"):
                            if False: #opt.onlyLin:
                                sign = 0.
                            else:
                                sign = +1.
                        elif samp.startswith("quad_mixed") and ops[0] in f and ops[1] in f:
                            sign = +1.

                    toAdjust = False
                    if not (f.startswith("VBS_SSWW_") or f.startswith("WpWpJJ")):
                        toAdjust = True

                    if toAdjust: #htemp.Integral()<=0.:
                        for ibin in range(htemp.GetNbinsX()):
                            bincont = htemp.GetBinContent(ibin+1)
                            if bincont <= 0.:
                                htemp.SetBinContent(ibin+1, 0.001)
                                #print ibin, "modified"
                            
                    if sign == 0:
                        htemp.Reset("ICE")
                    else:
                        htemp.Scale(sign)
                    
                    
                    if (f.startswith("VBS_SSWW_") or f.startswith("WpWpJJ_EWK")): #"_LIN" in f or "_BSM" in f:
                        print("\nfile:", f)
                        print("error before zeroing:", [htemp.GetBinError(ibin+1) for ibin in range(htemp.GetNbinsX())])
                        for ibin in range(htemp.GetNbinsX()):
                            htemp.SetBinError(ibin+1, 0.)
                        print("error after zeroing:", [htemp.GetBinError(ibin+1) for ibin in range(htemp.GetNbinsX())])
                    

                    #print "after htemp", htemp.Integral()
                    #print "before h:", h #.GetName(), h.Integral()
                    ##print "htemp", htemp

                    if h is None:
                        h = copy.deepcopy(htemp)
                    else:
                        h.Add(htemp, 1)
                    #print "after h:", h.GetName(), h.Integral()

                    #hsyst = collections.OrderedDict()
                    #print "\nsamp:", samp

                    for sysnam, systype in list(syst.items()):
                        sysname = None
                        if not (systype[0].startswith("shape") or (systype[0] == 'lnN' and systype[2] == 0.) ) or sysnam == "autoMCstat":
                            continue

                        if sysnam.startswith("QCDScale") or (sysnam.startswith("pdf_") and pdftype.endswith("sep")) or sysnam.startswith("ISR") or sysnam.startswith("FSR") or sysnam.startswith("jes"):
                            sysname = sysnam.replace("WpWpJJ_", "").replace("_" + sysnam.split("_")[-1], "")
                        else:
                            sysname = sysnam

                        #print sysnam, sysnam.split("_"), sysnam.replace("_" + sysnam.split("_")[-1], ""), sysname
                        ##print "systype[1]", systype[1]
                        ifile.cd()
                        
                        #print "to syst?", (systype[1] == "all"), (samp in systype[1]), ('sig' in systype[1] and (f.startswith("VBS_") or f.startswith("WpWp")))
                        if systype[1] == "all" or samp in systype[1] or ('sig' in systype[1] and (f.startswith("VBS_") or f.startswith("WpWp"))):
                            #print sysnam, sysname#, systype
                            hup_ = h_ + "_" + sysname
                            hdown_ = h_ + "_" + sysname
                            hup_ += "Up"
                            hdown_ += "Down"
                            if sysnam.startswith("jes"):
                                hup_ = hup_.replace("muon_", "").replace("electron_", "")
                                hdown_ = hdown_.replace("muon_", "").replace("electron_", "")
                            sysName = sysnam
                            #print ifile
                            #print hup_, hdown_

                            if systype[0].startswith("shape") or systype[0] == 'lnN':
                                if systype[-1] == "uncorr":
                                    sysName += "_" + year
                                    
                            #print "Taking " + hup_ + " " + hdown_ 
                            huptemp = copy.deepcopy(ifile.Get(hup_).Clone())
                            hdowntemp = copy.deepcopy(ifile.Get(hdown_).Clone())
                            sign = +1.
                            '''
                            if not ":" in opt.model:
                                pass
                    
                            elif "VBS_SSWW_" in f and "_F" in f:
                                if samp.startswith("sm_lin_quad") and "_BSM_" in f:
                                    if not opt.Lambda8:
                                        sign = -1.
                                    else:
                                        sign = 0.
                                elif samp.startswith("quad_"):
                                    if not opt.Lambda8:
                                        sign = 0.
                                    else:
                                        sign = +1.
                            '''
                            if "VBS_SSWW_" in f and "_F" in f:
                                if samp.startswith("sm_lin_quad") and "_BSM_" in f:
                                    if not opt.Lambda8 and ":" in opt.model: # or opt.onlyLin):
                                        if "_LIN" in flist[0][1]:
                                            sign = 0.
                                        else:
                                            sign = -1.
                                    else:
                                        if "_LIN" in flist[0][1]:
                                            sign = +1.
                                        else:
                                            sign = 0.

                                elif samp.startswith("quad_"):
                                    if not opt.Lambda8 and ":" in opt.model: # or opt.onlyLin:
                                        sign = 0.
                                    else:
                                        sign = +1.
                            elif "VBS_SSWW_" in f and "_c" in f:
                                if samp.startswith("sm_lin_quad") and "_BSM_" in f:
                                    if False: #opt.onlyLin:
                                        if "_LIN_" in flist[0][1]:
                                            sign = 0.
                                        else:
                                            sign = -1.
                                    else:
                                        if "_LIN" in flist[0][1]:
                                            sign = 1.
                                        else:
                                            sign = 0.
                                        #if not ('_cHl3_' in f or '_cqq31_' in f):
                                        #sign = +1.
                                        #else:
                                        #    sign = 0.

                                elif samp.startswith("quad_"):
                                    if False: #opt.onlyLin:
                                        sign = 0.
                                    else:
                                        sign = +1.


                            if toAdjust:#huptemp.Integral()<=0.:
                                for ibin in range(huptemp.GetNbinsX()):
                                    bincont = huptemp.GetBinContent(ibin+1)
                                    if bincont <= 0.:
                                        huptemp.SetBinContent(ibin+1, 0.001)
                                        #print ibin, "modified"

                            if toAdjust:#hdowntemp.Integral()<=0.:
                                for ibin in range(hdowntemp.GetNbinsX()):
                                    bincont = hdowntemp.GetBinContent(ibin+1)
                                    if bincont <= 0.:
                                        hdowntemp.SetBinContent(ibin+1, 0.001)
                                        #print ibin, "modified"
                            
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
                    
                #print "\nsamp", samp#, flist[0]
                #for k, v in hsyst.items():
                    #print k, v 
               
                   
                #if "_F" in samp and not "DY" in samp:
                    ##print "h", h, h.Integral()
                    #for i in range(0, h.GetNbinsX()):
                        #content = h.GetBinContent(i)
                        ##print("content bin #" + str(i+1) + ":\t" + str(content))
                    #for khs, vhs in hsyst.items():
                        #if not None in vhs:
                            ##print "h_", khs
                            ##print "vhs[0]", vhs[0], vhs[0].Integral()
                            #for i in range(0, vhs[0].GetNbinsX()):
                                #content = vhs[0].GetBinContent(i)
                                ##print("content bin #" + str(i+1) + ":\t" + str(content))
                            ##print "vhs[1]", vhs[1], vhs[1].Integral()
                            #for i in range(0, vhs[1].GetNbinsX()):
                                #content = vhs[1].GetBinContent(i)
                                ##print("content bin #" + str(i+1) + ":\t" + str(content))
                #print "before if error h:", h.GetName(), h.Integral()
                if Error:
                    continue
                
                ofile.cd(k_ + "_" + lep + "_" + year)
                samplab = ""
                #print "\nsamp", samp
                if samp.startswith("quad_") or samp.startswith("sm_lin_"):
                    #print "after if error h:", h.GetName(), h.Integral()
                    if "_F" in samp:
                        torem = "_" + samp.split("_")[-1]
                        samplab = samp.replace("_F", "_c")
                        if not ":" in opt.model:
                            samplab = samplab.replace(torem, "")
                    else:
                        samplab = samp
                else:
                    samplab = samp
                #print "samplab", samplab

                #print "2after h:", h.GetName(), h.Integral()
                #print "h", h, h.Integral()
                h.SetName(samplab)
                #print "hname", h.GetName()
                h.Write(samplab, ROOT.TObject.kWriteDelete)

                if samp in bkg:
                    if histData[k_] is None: 
                        histData[k_] = copy.deepcopy(h)
                    else:
                        histData[k_].Add(h)
                    
                for sname, shists in list(hsyst.items()):
                    if None in shists:
                        continue
                    #print "\nsystematic:", sname, shists[0].GetName(), shists[1].GetName()
                    for i, var in enumerate(shists):
                        samplab = ""
                        if samp.startswith("quad_") or samp.startswith("sm_lin_"):
                            if "_F" in samp:
                                torem = "_" + samp.split("_")[-1]
                                samplab = samp.replace("_F", "_c")
                                if not ":" in opt.model:
                                    samplab = samplab.replace(torem, "")

                            else:
                                samplab = samp
                        else:
                            samplab = samp

                        sampsyst = samplab + "_"  + sname
                        if i == 0:
                            sampsyst += "Up"
                        elif i == 1:
                            sampsyst += "Down"
                        
                        #print sampsyst, shists[i]
                        shists[i].Write(sampsyst, ROOT.TObject.kWriteDelete) 

                #print "\nls"
                #ofile.ls()
                #continue #raise ValueError("bye")
                
                #nBinsX = h.GetNbinsX()

                #if k_ in samp:
                    #samp = samp.replace("_" + k_, "")                     
                #elif "cat" in samp:
                    #samp = samp.replace("cat_", "")             
                ##print "SAMP after channel removal ",samp
                #if(samp.startswith("data")):
                    #samp = "Data"
                    
                #if(samp.startswith("SVJ") and not (samp.endswith("Up") or samp.endswith("Down")) and mcstat == True ):
                    #for n in xrange(nBinsX):
                        #hNameUp = "%s_mcstat_%s_bin%d_Up" % ( h_, samp, n+1)
                        #hNameDown = "%s_mcstat_%s_bin%d_Down" % ( h_, samp, n+1)
                        ###print "Histogram: ", hNameUp                  
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
            ##print "Bkg integral ", histData[k_].Integral()
            bkgpdf =  histData[k_].Clone("BkgPdf")
            ##print histData[k_].Integral()

            # check for negative bins in bkg pdf 
            for i in range(0, bkgpdf.GetNbinsX()+1):
                content = bkgpdf.GetBinContent(i)
                if(content<0.):
                    bkgpdf.SetBinContent(i, 1.E-3)
            
            bkgint = float(bkgpdf.Integral())
            bkgscale = float(1./bkgint)
            bkgpdf.Scale(bkgscale)
            ###print "Bkg pdf ", bkgpdf.Integral()
            bkgpdf.Write(str(bkgpdf.GetName()), ROOT.TObject.kWriteDelete)    
            
        ##print "histData", histData
        #for kd, vd in histData.items():
            ##print kd, vd.Integral()


#ofile.Write()
ofile.Close()
