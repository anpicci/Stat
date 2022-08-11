import ROOT
import os, sys, copy
import optparse
from ROOT import RooRealVar, RooDataHist, RooArgList, RooGenericPdf, RooExtendPdf, RooWorkspace, RooFit
#from Stat.Limits.settings import *
#from Stat.Limits.datacards_ps import *
#from Stat.Limits.datacards import *
from collections import OrderedDict
import importlib

usage = 'usage: %prog -p histosPath -o outputFile'
parser = optparse.OptionParser(usage)
parser.add_option('-i', '--input', dest='ifile', type='string', default="histos.root",help='Where can I find input histos? Default is histos.root')
parser.add_option("-d","--outdir",dest="outdir",type="string",default="outdir",help="Name of the output directory where to store datacards. Default is outdir")
parser.add_option("-m","--mode",dest="mode",type="string",default="hist",help="Kind of shape analysis: parametric fit or fit to histos?. Default is hist")
parser.add_option("--model",dest="model",type="string",default="",help="model")
parser.add_option("-c","--channel",dest="ch",type="string",default="all",help="Indicate channels of interest. Default is all")
parser.add_option("-u","--unblind",dest="unblind",action='store_true', default=False)
parser.add_option('--ls', dest='ls', type='string', default = '', help='wilson coeff')
(opt, args) = parser.parse_args()
sys.argv.append('-b')

settmod = importlib.import_module("Stat.Limits.settings_" + opt.model)
bkg = settmod.bkg
histos = settmod.histos
years = settmod.years
leptons = settmod.leptons
sigpoints = settmod.sigpoints
lssamples_1D = settmod.lssamples_1D
syst = settmod.syst
channels = settmod.channels
rateParams = settmod.rateParams
lssamples_1D = settmod.lssamples_1D

processes = bkg

toremove = []
for p in processes:
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
    processes.remove(tor)

#from fits import *

#*******************************************************#
#                                                       #
#   getRate(process, ifile)                             #
#                                                       #
#   getCard(sig, ch, ifilename, outdir)                 #
#                                                       #
#*******************************************************#


#*******************************************************#
#                                                       #
#                     Utility Functions                 #
#                                                       #
#*******************************************************#
def getRate(ch, process, ifile):
       hName = ch + "/"+ process
       #print process
       #print "Getting histogram from ", ifile.GetName() 
       #print "Histogram name: ", hName
       ##print ifile.Get(hName)
       h = ifile.Get(hName)
       ##print h.GetName()
       return h.Integral()

def getHist(ch, process, ifile):
       hName = ch + "/"+ process
       ##print "Getting histogram from ", ifile.GetName() 
       ##print "Histogram name: ", hName
       ##print "Histo Name ", hName
       h = ifile.Get(hName)
       return h

#*******************************************************#
#                                                       #
#                      Datacard                         #
#                                                       #
#*******************************************************#
def getCard(sig, ch, ifilename, outdir, mode = "histo", unblind = False):
       
       year = ch.split("_")[-1]
       ##print "sig:", sig

       ##print "processes:", processes

       try:
              ifile = ROOT.TFile.Open(ifilename)
       except IOError:
              print "Cannot open ", ifilename
       else:
              ##print "Opening file ",  ifilename
              ifile.cd()
       ##print syst 
       
       workdir_ = ifilename.split("/")[:-1]
       WORKDIR = "/".join(workdir_) + "/"

       carddir = outdir + "/"
       for ids, sigp in enumerate(sig):
              carddir += sigp
              if ids < len(sig) - 1:
                     carddir += "_"

       carddir += "/"

       hist_filename = os.getcwd()+"/"+ifilename
       hist = []
       for sigp in sig:
              hist.append(getHist(ch, sigp, ifile))

       #*******************************************************#
       #                                                       #
       #                   Generate workspace                  #
       #                                                       #
       #*******************************************************#
       if(mode == "template"):
              histBkgData = getHist(ch, "Bkg", ifile)
              histData = histBkgData
              if (unblind):  
                     print "BE CAREFUL: YOU ARE UNBLINDING"
                     histData = getHist(ch, "data_obs", ifile)
                     #print "*********Number of data ", histData.Integral()
              histSig = []
              for sigp in sig:
                     histSig.append(getHist(ch, sigp, ifile))
              bkgData = RooDataHist("bkgdata", "Data (MC Bkg)",  RooArgList(mT), histBkgData, 1.)
              obsData = RooDataHist("data_obs", "(pseudo) Data",  RooArgList(mT), histData, 1.)
              sigData = []
              for hsig in histSig:
                     sigData.append(RooDataHist("sigdata", "Data (MC sig)",  RooArgList(mT), hsig, 1.))
              ##print "Bkg Integral: ", histData.Integral() 
              nBkgEvts = histBkgData.Integral() 
              ##print "Bkg Events: ", nBkgEvts

              ##print "Channel: ", ch
              modelBkg = fitParam[ch].modelBkg
              normzBkg = RooRealVar(modelBkg.GetName()+"_norm", "Number of background events", nBkgEvts, 0., 1.e3)
              ##print "NormBkg ", nBkgEvts
              modelExt = RooExtendPdf(modelBkg.GetName()+"_ext", modelBkg.GetTitle(), modelBkg, normzBkg)

              # create workspace
              w = RooWorkspace("SVJ", "workspace")
              # Dataset
              # ATT: include isData
              getattr(w, "import")(bkgData, RooFit.Rename("Bkg"))
              getattr(w, "import")(obsData, RooFit.Rename("data_obs"))
              for idxs, sigp in enumerate(sig):
                     getattr(w, "import")(sigData[idxs], RooFit.Rename(sigp))

              for i in xrange(hist.GetNbinsX()):
                     mcstatSysName = []
                     for sigp in sig:
                            mcstatSysName.append("mcstat_%s_%s_bin%d"  % (ch, sigp, i+1))
                     ##print mcstatSysName
                     ##print sig + "_" + mcstatSysName + "Up"
                     mcstatSigUp = []
                     mcstatSigDown = []
                     mcstatSigHistUp = []
                     mcstatSigHistDown = []
                     for idxs, sigp in enumerate(sig):
                            mcstatSigUp = getHist(ch, sigp + "_" + mcstatSysName[idxs] + "Up", ifile)
                            ##print "Integral  ", mcstatSigUp.Integral()
                            mcstatSigDown.append(getHist(ch, sigp + "_" + mcstatSysName[idxs] + "Down", ifile))
                            mcstatSigHistUp.append(RooDataHist(sigp + "_" + mcstatSysName[idxs] + "Up", "Data (MC sig)",  RooArgList(mT), mcstatSigUp[idxs], 1.))
                            mcstatSigHistDown.append(RooDataHist(sigp + "_" + mcstatSysName[idxs] + "Down", "Data (MC sig)",  RooArgList(mT), mcstatSigDown[idxs], 1.))
                            getattr(w, "import")(mcstatSigHistUp[idxs], RooFit.Rename(sigp + "_" + mcstatSysName[idxs] + "Up") )
                            getattr(w, "import")(mcstatSigHistDown[idxs], RooFit.Rename(sigp + "_" + mcstatSysName[idxs] + "Down") )

              for sysName,sysValue  in syst.iteritems():
                     if(sysValue[0]=="shape" and "mcstat" not in sysName):            
                            for idxs, sigp in enumerate(sig):
                                   sysUp =  getHist(ch, sigp + "_" + sysName + "Up", ifile)
                                   sysDown =  getHist(ch, sigp + "_" + sysName + "Down", ifile)
                                   ##print "==> Trigg sys name: ", sigp + "_" + sysName + "Down"
                                   sysSigHistUp = RooDataHist(sigp + "_" + sysName + "Up", sysName + " uncertainty",  RooArgList(mT), sysUp, 1.)
                                   sysSigHistDown = RooDataHist(sigp + "_" + sysName + "Down", sysName + " uncertainty",  RooArgList(mT), sysDown, 1.)
                                   getattr(w, "import")(sysSigHistUp, RooFit.Rename(sigp + "_" + sysName + "Up") )
                                   getattr(w, "import")(sysSigHistDown, RooFit.Rename(sigp + "_" + sysName + "Down") )
              #else: getattr(w, "import")(setToys, RooFit.Rename("data_obs"))
              getattr(w, "import")(modelBkg, RooFit.Rename(modelBkg.GetName()))
              #getattr(w, "import")(modelAlt, RooFit.Rename(modelAlt.GetName()))
              getattr(w, "import")(normzBkg, RooFit.Rename(normzBkg.GetName()))
              ofname = carddir + "ws_"
              for sigp in sig:
                     ofname += sigp + "_"
              ofname += ch + "_" + mode + ".root"
              #w.writeToFile("%sws_%s_%s_%s.root" % (carddir, sig, ch, mode), True)
              w.writeToFile(ofname, True)

              ##print "Workspace", "%sws_%s_%s_%s.root" % (carddir, sig, ch, mode) , "saved successfully"
              ##print "Workspace", ofname , "saved successfully"
                 
              workfile = "./ws_" #"%s_%s_%s.root" % ( sig, ch, mode)
              for sigp in sig:
                     workfile += sigp + "_"
              workfile += ch + "_" + mode + ".root"
              # ======   END MODEL GENERATION   ======       
       rates = {}
       procLine = ""
       procNumbLine = ""
       rateLine = ""
       binString = ""
       if(mode == "template"):       
              processes.append("Bkg")
              processes[:-1] = []
              rates["Bkg"] = nBkgEvts
              procLine += ("%-25s") % ("Bkg")
              rateLine += ("%-25s") % (rates["Bkg"])
              binString += (("%-25s") % (ch) ) * (2)
              procNumbLine = 1 
       else:
              i = 1
              bkgrate = 0
              ##print "===> Backgrounds:  ", processes
              nproc=(len(processes))
              
              for p in processes:
                     ##print "======================= p for rate", p, " syst, ", syst
                     ##print "ch is ", ch, " process is ", p, " ifile is ", ifile.GetName()
                     rates[p] = getRate(ch, p, ifile)

                     bkgrate = rates[p]
                     if (p =="QCD"): print "qcd: ", bkgrate

                     #if(bkgrate<=0.):
                            #nproc = nproc - 1
                            #continue

                     procNumbLine += ("%-25s") % (i)
                     procLine += ("%-25s") % (p)
                     rateLine += ("%-25f") % (bkgrate)
                     i+=1
              binString += (("%-25s") % (ch) ) * (nproc + len(sig))

       ##print 'rates:'
       #for k, v in rates.items():
              ##print k + ":", v

       if ((not unblind) and (mode == "template")): 
              ##print "N.B: We are in blind mode. Using MC bkg data for data_obs"
              rates["data_obs"] = getRate(ch, "Bkg", ifile)
              ##print "Pseudo data rate: ", rates["data_obs"]
       else: 
              rates["data_obs"] = getRate(ch, "data_obs", ifile)
       ##print("sig",sig)
       for sigp in sig:
              ##print "sigp: ", sigp
              ##print ch, sigp, ifile
              rates[sigp] = getRate(ch, sigp, ifile)
       card  = "imax 1 number of channels \n"
       card += "jmax * number of backgrounds \n"
       card += "kmax * number of nuisance parameters\n"
       card += "-----------------------------------------------------------------------------------\n"

       if(mode == "template"):
              #              card += "shapes   %s  %s    %s    %s    %s\n" % (sig, ch, ifilename, "$CHANNEL/$PROCESS", "$CHANNEL/$PROCESS_SYSTEMATIC")
              #              card += "shapes            %-15s  %-5s    %s%s.root    %s\n" % (sig, ch, WORKDIR, ch, "SVJ:$PROCESS")
              card += "shapes   %s  %s    %s    %s\n" % (modelBkg.GetName(), ch, workfile, "SVJ:$PROCESS")
              for sigp in sig:
                     card += "shapes   %s  %s    %s    %s    %s\n" % (sigp, ch, workfile, "SVJ:$PROCESS", "SVJ:$PROCESS_$SYSTEMATIC")
              card += "shapes   %s  %s    %s    %s\n" % ("data_obs", ch, workfile, "SVJ:$PROCESS")

       else:  
              card += "shapes   *      *   %s    %s    %s\n" % (hist_filename, "$CHANNEL/$PROCESS", "$CHANNEL/$PROCESS_$SYSTEMATIC")
              card += "shapes   data_obs      *   %s    %s\n" % (hist_filename, "$CHANNEL/$PROCESS")
       card += "-----------------------------------------------------------------------------------\n"
       card += "bin               %s\n" % ch
       ##print "===> Observed data: ", rates["data_obs"]
       card += "observation       %0.d\n" % (rates["data_obs"])
       card += "-----------------------------------------------------------------------------------\n"
       card += "%-50s%-25s\n" % ("bin", binString)

       sigLine1 = ""
       sigLine2 = ""
       sigLine3 = ""
       for idxp, sigp in enumerate(sig):
              sigLine1 += "%-25s" % (sigp)
              sigLine2 += "%-25s" % (str(-len(sig)+idxp+1))
              sigLine3 += "%-25.6f" % (rates[sigp])

       card += "%-50s%-25s%-25s\n" % ("process", sigLine1, procLine) #"roomultipdf"
       card += "%-50s%-25s%-25s\n" % ("process", sigLine2, procNumbLine)
       card += "%-50s%-25s%-25s\n" % ("rate", sigLine3, rateLine) #signalYield[m].getVal(), nevents
       card += "-----------------------------------------------------------------------------------\n"

       for sysname, sysValue in syst.iteritems():
              sysName = ""
              #### insert year in sysName if sys in uncorr, o
              if sysValue[0].startswith("shape"):
                     ##print syst[sysname]
                     if sysValue[2] == "uncorr":
                            sysName = sysname + "_" + str(year)
                     else:
                            sysName = sysname
              else:
                     sysName = sysname

              ##print "Systematic Uncertainty: ", sysName
              if("2016" in sysName and "2016" not in ch): 
                     continue
              elif("2017" in sysName and "2017" not in ch):
                     continue
              elif("2018" in sysName and "2018" not in ch): 
                     continue
              if("mu" in sysName and "mu" not in ch):
                     continue
              elif("ele" in sysName and "ele" not in ch): 
                     continue

              if(sysValue[0]=="lnN"): 
                     if "lumi" in sysName and "1718_" in sysName:
                            sysName = sysName.replace("APV", "").replace("_2016", "").replace("_2017", "").replace("_2018", "")
                     card += "%-25s%-25s" % (sysName, sysValue[0])
                     if(sysValue[1]=="all" and len(sysValue)>2):
                            if(mode == "template"):
                                   card += "%-25s" % (sysValue[2]) * (2)
                            else:  
                                   card += "%-25s" % (sysValue[2]) * (len(processes) + len(sig))
                     elif(sysValue[1]=="QCD" and len(sysValue)>2):
                            if(mode == "template"):
                                   card += "%-25s" % (sysValue[2]) * (2)
                            else: 
                                   card += "%-25s" % (sysValue[2]) * (len(processes) + len(sig))
                     elif(sysValue[1]=="Fake"):
                            if not mode == "template":
                                   card += "%-25s" % ("-") * (len(sig)) + "%-25s" % (sysValue[2]) + "%-25s" % ("-") * (len(processes) - 1) 
                     else:
                            if (sysValue[1]=="all"):
                                   sysValue[1] = copy.deepcopy(processes)
                                   for sigp in sig:
                                          sysValue[1].append(sigp)
                            hsysName =  "_" + sysname  
                            hsysNameUp = "_" + sysname + "Up"  
                            hsysNameDown = "_" + sysname + "Down" 
                            #hsysName =  "_" + sysName  
                            #hsysNameUp = "_" + sysName + "Up"  
                            #hsysNameDown = "_" + sysName + "Down" 
                            ##print hsysName, hsysNameUp, hsysNameDown
                            ##print "Applying syst on ", sysValue[1]
                            if("sig" in sysValue[1]):
                                   for sigp in sig:
                                          if(getRate(ch, sigp, ifile) != 0.):
                                                 sigSys = abs((getRate(ch, sigp+hsysNameUp, ifile) - getRate(ch, sigp+hsysNameDown, ifile))/ (2* getRate(ch, sigp, ifile)))
                                          else:
                                                 sigSys = 1
                                          if(sigSys<1.and sigSys >0.):
                                                 sigSys = sigSys + 1
                                          card += "%-25s" % (sigSys)
                            else: 
                                   card += "%-25s" % ("-")

                            for p in processes:
                                   if (p in sysValue[1]):
                                          if (getRate(ch, p, ifile) != 0.): bkgSys = abs((getRate(ch, p+hsysNameUp, ifile) - getRate(ch, p+hsysNameDown, ifile))/ (2* getRate(ch, p, ifile)) )
                                          else: bkgSys = 1
                                          if(bkgSys<1.and bkgSys >0.): bkgSys = bkgSys + 1
                                          card += "%-25s" % (bkgSys)
                                   else:  card += "%-25s" % ("-")
              elif(sysValue[0].startswith("shape")):
                     ##print "sys shape named ", sysName
                     if("mcstat" not in sysName and 'autoMCstat' not in sysName):
                            card += "%-25s%-25s" % (sysName, sysValue[0])
                            #card += "%-25s     shape     " % (sysName)
                            if ("sig" in sysValue[1]):
                                   for sigp in sig:
                                          isbogussys = False 
                                          if(getRate(ch, sigp+"_"+sysName+"Up", ifile)<0.001 or getRate(ch, sigp+"_"+sysName+"Down", ifile)<0.001):
                                                 isbogussys = True
                            
                                          if ((getRate(ch, sigp, ifile) > 0.) and not isbogussys): 
                                          ##print " signal ",sig," channel, ",ch, " file ",ifile, " rate ",(getRate(ch, sig, ifile))
                                          ##print " signal ",sig," channel, ",ch, " file ",ifile, " rate up ",(getRate(ch, sig+"_"+sysName+"Up", ifile))
                                          ##print " signal ",sig," channel, ",ch, " file ",ifile, " rate down",(getRate(ch, sig+"_"+sysName+"Down", ifile))
                                                 card += "%-25s" % ( "1") 
                                          elif isbogussys:
                                                 card += "%-25s" % ( "-")
                                          
                            for p in processes:
                                   if p not in sysValue[1]:
                                          card += "%-25s" % ( "-") 
                                          continue
                                   isbogussys = False 
                                   if(getRate(ch, p+"_"+sysName+"Up", ifile)<0.001 or getRate(ch, p+"_"+sysName+"Down", ifile)<0.001):
                                          isbogussys = True

                                   if ((getRate(ch, p, ifile) > 0.) and not isbogussys): 
                                          card += "%-25s" % ( "1") 
                                   elif isbogussys: 
                                          card += "%-25s" % ( "-") 
                     elif("mcstat" in sysName):
                            # CAMBIARE NOME DELLA SYST                     #here
                            for samp in sysValue[1]:
                                   #sampName = ""
                                   sampName = []
                                   line = ""
                                   if (samp == "sig" or samp == "Sig"): 
                                          for sigp in sig:
                                                 line = "%-25s" % ( "1") 
                                                 sampName.append(sigp)
                                          
                                          line += "%-25s" % ("-") * (len(processes)) 
                                                 
                                   elif(mode != "template"):
                                          line = "%-25s" % ( "-") 
                                          lineProc = ["%-25s" % ( "-") for x in xrange (len(processes))]
                                          if samp in processes: 
                                                 index = processes.index(samp)  
                                                 lineProc[index] = "1"
                                                 
                                          lineProc = "         ".join(lineProc)
                                          line += lineProc
                                          sampName.append(samp)
                                   else: 
                                          continue
                                   
                                   sampNameLine = ""
                                   for ids, sampn in enumerate(sampName):
                                          sampNameLine += sampn 
                                          if ids < (len(sampName) - 1):
                                                 sampNameLine += "_"
                                   for i in xrange(hist.GetNbinsX()):
                                          sysName = "mcstat_%s_%s_bin%d      "  % (ch, sampNameLine, i+1)
                                          card += "%-25s   shape   " % (sysName)
                                          card += line
                                          card += "\n"        
              if('autoMCstat' in sysName):
                  if len(sig) > 1:
                      card += "%-25s%-25s%-25d%-25d " % (ch, "autoMCStats", 10, 0)
                  else:
                      card += "%-25s%-25s%-25d%-25d " % (ch, "autoMCStats", 1000000, 0)
              card += "\n"
       # End for loop on syst unc.       
       card += "\n"
       for k, v in rateParams.items():
              rpyear = k.split("_")[-1]
              for ch_ in v.chs:
                     if("2016" in k and "2016" not in ch):
                            continue
                     elif("2017" in k and "2017" not in ch):
                            continue
                     elif("2018" in k and "2018" not in ch):
                            continue
                     if("mu" in k and "mu" not in ch):
                            continue
                     elif("ele" in k and "ele" not in ch):
                            continue
                     if (ch_==("_").join(ch.split("_")[:-1])): 
                            if(("2016" in k) or ("2017" in k) or ("2018" in k)):
                                   if ('mu' in k and 'mu' in ch):
                                          card += "%-25s%-25s%-25s%-25s%-25d" % (k, "rateParam", ch, v.bkg, 1)
                                   elif ('ele' in k and 'ele' in ch):
                                          card += "%-25s%-25s%-25s%-25s%-25d" % (k, "rateParam", ch, v.bkg, 1)
                                   else:
                                          sameyear= ( ("2016" in k and "2016" in ch) or ("2017" in k and "2017" in ch) or ("2018" in k and "2018" in ch))
                                          if(sameyear): card += "%-25s%-25s%-25s%-25s%-25d" % (k, "rateParam", ch, v.bkg, 1)                                   
                            else:
                                   card += "%-25s%-25s%-25s%-25s%-25d" % (k, "rateParam", ch, v.bkg, 1)
                            card += "\n"

       #if not os.path.isdir(outdir):
              #os.system('mkdir ' + outdir)
       #hereee
       #if not os.path.isdir(outdir + "/" + sig): os.system('mkdir ' +outdir + "/" + sig)
       if not os.path.isdir(carddir):
              os.system('mkdir -p ' + carddir)
       #else:
              #os.system("rm " + carddir + "/*")

       outname = "" + carddir
       for sigp in sig:
              outname += sigp + "_"
       outname += ch + "_" + mode + ".txt"
       #outname =  "%s%s_%s_%s.txt" % (carddir, sig, ch, mode)
       cardfile = open(outname, 'w')
       cardfile.write(card)
       cardfile.close()
       ##print card
       return card


#*******************************************************#
#                                                       #
#                 Datacard for LS                       #
#                                                       #
#*******************************************************#
def getCardLS(incoeff, ch, ifilename, outdir, mode = "histo", unblind = False):
       ##print incoeff, ch, ifilename, outdir, mode, unblind
       year = ch.split("_")[-1]
       ##print "channel:", ch
       ##print outdir

       ops = incoeff.split(":")
       setpiecs = []
       for op in ops:
              if len(op.split("_")) > 1:
                     setpiecs.append(("_")+op.split("_")[-1])
       coeff = copy.deepcopy(incoeff)
       for setpiec in setpiecs:
              coeff = coeff.replace(setpiec, "")

       lssamp = []
       for name, coll in lssamples_1D.items():
              for nout, nin in coll.items():
                     lssamp.append(nout)

       ##print lssamp

       ##print "processes:", processes

       try:
              ifile = ROOT.TFile.Open(ifilename)
       except IOError:
              print "Cannot open ", ifilename
       else:
              ##print "Opening file ",  ifilename
              ifile.cd()
       ##print syst 

       workdir_ = ifilename.split("/")[:-1]
       WORKDIR = "/".join(workdir_) + "/"
       dircoeff = ""
       dircoeff = coeff
       carddir = outdir+  "/"  + dircoeff + "/"
       print carddir

       sig = lssamp
       hist_filename = os.getcwd()+"/"+ifilename
       hist = []
       for sigp in sig:
              ##print getHist(ch, sigp, ifile)
              hist.append(getHist(ch, sigp, ifile))

       #*******************************************************#
       #                                                       #
       #                   Generate workspace                  #
       #                                                       #
       #*******************************************************#
       if(mode == "template"):
              histBkgData = getHist(ch, "Bkg", ifile)
              histData = histBkgData
              if (unblind):  
                     print "BE CAREFULL: YOU ARE UNBLINDING"
                     histData = getHist(ch, "data_obs", ifile)
                     print "*********Number of data ", histData.Integral()

              histSig = []
              for sigp in sig:
                     histSig.append(getHist(ch, sigp, ifile))
              bkgData = RooDataHist("bkgdata", "Data (MC Bkg)",  RooArgList(mT), histBkgData, 1.)
              obsData = RooDataHist("data_obs", "(pseudo) Data",  RooArgList(mT), histData, 1.)
              sigData = []
              for hsig in histSig:
                     sigData.append(RooDataHist("sigdata", "Data (MC sig)",  RooArgList(mT), hsig, 1.))
              ##print "Bkg Integral: ", histData.Integral() 
              nBkgEvts = histBkgData.Integral() 
              ##print "Bkg Events: ", nBkgEvts

              ##print "Channel: ", ch
              modelBkg = fitParam[ch].modelBkg
              normzBkg = RooRealVar(modelBkg.GetName()+"_norm", "Number of background events", nBkgEvts, 0., 1.e3)
              ##print "NormBkg ", nBkgEvts
              modelExt = RooExtendPdf(modelBkg.GetName()+"_ext", modelBkg.GetTitle(), modelBkg, normzBkg)

              # create workspace
              w = RooWorkspace("SVJ", "workspace")
              # Dataset
              # ATT: include isData
              getattr(w, "import")(bkgData, RooFit.Rename("Bkg"))
              getattr(w, "import")(obsData, RooFit.Rename("data_obs"))
              for idxs, sigp in enumerate(sig):
                     getattr(w, "import")(sigData[idxs], RooFit.Rename(sigp))

              for i in xrange(hist.GetNbinsX()):
                     mcstatSysName = []
                     for sigp in sig:
                            mcstatSysName.append("mcstat_%s_%s_bin%d"  % (ch, sigp, i+1))
                     ##print mcstatSysName
                     ##print sig + "_" + mcstatSysName + "Up"
                     mcstatSigUp = []
                     mcstatSigDown = []
                     mcstatSigHistUp = []
                     mcstatSigHistDown = []
                     for idxs, sigp in enumerate(sig):
                            mcstatSigUp = getHist(ch, sigp + "_" + mcstatSysName[idxs] + "Up", ifile)
                            ##print "Integral  ", mcstatSigUp.Integral()
                            mcstatSigDown.append(getHist(ch, sigp + "_" + mcstatSysName[idxs] + "Down", ifile))
                            mcstatSigHistUp.append(RooDataHist(sigp + "_" + mcstatSysName[idxs] + "Up", "Data (MC sig)",  RooArgList(mT), mcstatSigUp[idxs], 1.))
                            mcstatSigHistDown.append(RooDataHist(sigp + "_" + mcstatSysName[idxs] + "Down", "Data (MC sig)",  RooArgList(mT), mcstatSigDown[idxs], 1.))
                            getattr(w, "import")(mcstatSigHistUp[idxs], RooFit.Rename(sigp + "_" + mcstatSysName[idxs] + "Up") )
                            getattr(w, "import")(mcstatSigHistDown[idxs], RooFit.Rename(sigp + "_" + mcstatSysName[idxs] + "Down") )

              for sysName,sysValue  in syst.iteritems():
                     if(sysValue[0].startswith("shape") and "mcstat" not in sysName):              
                            for idxs, sigp in enumerate(sig):
                                   sysUp =  getHist(ch, sigp + "_" + sysName + "Up", ifile)
                                   sysDown =  getHist(ch, sigp + "_" + sysName + "Down", ifile)
                                   ##print "==> Trigg sys name: ", sigp + "_" + sysName + "Down"
                                   sysSigHistUp = RooDataHist(sigp + "_" + sysName + "Up", sysName + " uncertainty",  RooArgList(mT), sysUp, 1.)
                                   sysSigHistDown = RooDataHist(sigp + "_" + sysName + "Down", sysName + " uncertainty",  RooArgList(mT), sysDown, 1.)
                                   getattr(w, "import")(sysSigHistUp, RooFit.Rename(sigp + "_" + sysName + "Up") )
                                   getattr(w, "import")(sysSigHistDown, RooFit.Rename(sigp + "_" + sysName + "Down") )

              #else: getattr(w, "import")(setToys, RooFit.Rename("data_obs"))
              getattr(w, "import")(modelBkg, RooFit.Rename(modelBkg.GetName()))
              #getattr(w, "import")(modelAlt, RooFit.Rename(modelAlt.GetName()))
              getattr(w, "import")(normzBkg, RooFit.Rename(normzBkg.GetName()))
              w.writeToFile("%sws_%s_%s_%s.root" % (carddir, coeff, ch, mode), True)

              ##print "Workspace", "%sws_%s_%s_%s.root" % (carddir, coeff, ch, mode) , "saved successfully"
                 
              workfile = "./ws_%s_%s_%s.root" % ( coeff, ch, mode)
              # ======   END MODEL GENERATION   ======       
       rates = OrderedDict()
       procLine = ""
       procNumbLine = ""
       rateLine = ""
       binString = ""
       if(mode == "template"):       
              processes.append("Bkg")
              processes[:-1] = []
              rates["Bkg"] = nBkgEvts
              procLine += ("%-25s") % ("Bkg")
              rateLine += ("%-25s") % (rates["Bkg"])
              binString += (("%-25s") % (ch) ) * (2)
              procNumbLine = 1 
       else:
              #i = 0
              i = 1
              bkgrate = 0
              ##print "===> Backgrounds:  ", processes
              nproc=(len(processes))
              for p in processes:
                     ##print "======================= p for rate", p, " syst, ", syst
                     ##print "ch is ", ch, " process is ", p, " ifile is ", ifile.GetName()
                     rates[p] = getRate(ch, p, ifile)
                     bkgrate = rates[p]
                     
                     #if(bkgrate==0):
                            #nproc = nproc -1
                            #continue
                     
                     #procNumbLine += ("%-25s") % (i + len(lssamp))
                     procNumbLine += ("%-25s") % (i)
                     procLine += ("%-25s") % (p)
                     rateLine += ("%-25f") % (bkgrate)
                     i+=1
              binString += (("%-25s") % (ch) ) * (nproc + len(lssamp))
              ##print 'rates:'
              #for k, v in rates.items():
                     ##print k + ":", v

       if ((not unblind) and (mode == "template")): 
              ##print "N.B: We are in blind mode. Using MC bkg data for data_obs"
              rates["data_obs"] = getRate(ch, "Bkg", ifile)
              #print "Pseudo data rate: ", rates["data_obs"]
       else:
              rates["data_obs"] = getRate(ch, "data_obs", ifile)
       for sgs in lssamp:
              sgslab = ""
              if sgs.startswith("quad_") or sgs.startswith("sm_lin_"):
                     sgslab = sgs.replace("_F", "_c")
              else:
                     sgslab = sgs

              rates[sgs] = getRate(ch, sgslab, ifile)
       
       ##print 'rates:'
       #for k, v in rates.items():
              ##print k + ":", v


       card  = "imax 1 number of channels \n"
       card += "jmax * number of backgrounds \n"
       card += "kmax * number of nuisance parameters\n"
       card += "-----------------------------------------------------------------------------------\n"

       if(mode == "template"):
              #              card += "shapes   %s  %s    %s    %s    %s\n" % (sig, ch, ifilename, "$CHANNEL/$PROCESS", "$CHANNEL/$PROCESS_SYSTEMATIC")
              #              card += "shapes            %-15s  %-5s    %s%s.root    %s\n" % (sig, ch, WORKDIR, ch, "SVJ:$PROCESS")
              card += "shapes   %s  %s    %s    %s\n" % (modelBkg.GetName(), ch, workfile, "SVJ:$PROCESS")
              for sigp in sig:
                     card += "shapes   %s  %s    %s    %s    %s\n" % (sigp, ch, workfile, "SVJ:$PROCESS", "SVJ:$PROCESS_$SYSTEMATIC")
              card += "shapes   %s  %s    %s    %s\n" % ("data_obs", ch, workfile, "SVJ:$PROCESS")

       else:  
              card += "shapes   *      *   %s    %s    %s\n" % (hist_filename, "$CHANNEL/$PROCESS", "$CHANNEL/$PROCESS_$SYSTEMATIC")
              card += "shapes   data_obs      *   %s    %s\n" % (hist_filename, "$CHANNEL/$PROCESS")
       card += "-----------------------------------------------------------------------------------\n"
       card += "bin               %s\n" % ch

       ##print "===> Observed data: ", rates["data_obs"]
       card += "observation       %0.d\n" % (rates["data_obs"])
       card += "-----------------------------------------------------------------------------------\n"
       card += "%-25s%-25s%-25s\n" % ("bin", "", binString)
       #card += "process                                 "
       procnameString = "%-25s%-25s" % ("process", "")
       #procnameString = "process                                 "
       procidxString = "%-25s%-25s" % ("process", "")
       #procidxString = "process                                 "
       rateString = "%-25s%-25s" % ("rate", "")
       #rateString = "rate                                    "
       
       for sidx, sgs in enumerate(lssamp):
              procnameString += "%-25s" % (sgs.replace("_F", "_c"))
              #procidxString += "%-25s" % (sidx)
              procidxString += "%-25s" % (str(-len(lssamp)+sidx+1))
              rateString += "%-25.6f" % (rates[sgs])
              #card += "%-25s" % (sgs)

       #card += "%-25s\n" % (procLine) #"roomultipdf"
       procnameString += "%-25s\n" % (procLine) #"roomultipdf"
       procidxString += "%-25s\n" % (procNumbLine)
       rateString += "%-25s\n" % (rateLine)
       #card += "process                                 "
       #for sidx, sgs in enumerate(lssamp):
              #card += "%-25s" % (sidx)
       #card += "%-25s\n" % (procNumbLine)

       #card += "rate                                    "

       #for sgs in lssamp:
       #"%-25.6f%-25s\n" % (rates[sig], rateLine) #signalYield[m].getVal(), nevents
       card += procnameString + procidxString + rateString

       card += "-----------------------------------------------------------------------------------\n"

       for sysname,sysValue  in syst.iteritems():
              sysName = ""
              #### insert year in sysName if sys in uncorr, o
              if sysValue[0].startswith("shape"):
                     ##print syst[sysname]
                     if sysValue[2] == "uncorr":
                            sysName = sysname + "_" + str(year)
                     else:
                            sysName = sysname
              else:
                     sysName = sysname

              ##print "Systematic Uncertainty: ", sysName
              if("2016" in sysName and "2016" not in ch):
                     continue
              elif("2017" in sysName and "2017" not in ch):
                     continue
              elif("2018" in sysName and "2018" not in ch):
                     continue

              if("mu" in sysName and "mu" not in ch):
                     continue
              elif("ele" in sysName and "ele" not in ch):
                     continue

              if(sysValue[0]=="lnN"): 
                     card += "%-25s%-25s" % (sysName, sysValue[0])
                     if len(sysValue)>2:
                            if(sysValue[1]=="all"):
                                   if(mode == "template"):
                                          card += "%-25s" % (sysValue[2]) * (2)
                                   else:  card += "%-25s" % (sysValue[2]) * (len(lssamp) + len(processes))# + 1)
                            elif(sysValue[1]=="QCD" and len(sysValue)>2):
                                   if(mode == "template"):
                                          card += "%-25s" % (sysValue[2]) * (2)
                                   else: 
                                          card += "%-25s" % (sysValue[2]) * (len(lssamp) + len(processes))#+ 1)
                            else:#(sysValue[1]=="Fake"):
                                   idx_p = processes.index(sysValue[1])
                                   idx_p_tot = idx_p + len(lssamp)
                                   if not mode == "template":
                                          card += "%-25s" % ("-") * (idx_p_tot) + "%-25s" % (sysValue[2]) + "%-25s" % ("-") * (len(processes) - (idx_p + 1)) 
                     else:
                            if (sysValue[1]=="all"):
                                   sysValue[1] = copy.deepcopy(processes)
                                   sysValue[1].append(sig)

                            hsysName =  "_" + sysname  
                            hsysNameUp = "_" + sysname + "Up"  
                            hsysNameDown = "_" + sysname + "Down" 
                            ##print "Applying syst on ", sysValue[1]
                            if("sig" in sysValue[1]):
                                   for sigp in sig:
                                          if(getRate(ch, sig, ifile) != 0.):
                                                 sigSys = abs((getRate(ch, sig+hsysNameUp, ifile) - getRate(ch, sig+hsysNameDown, ifile))/ (2* getRate(ch, sig, ifile)))
                                          else: 
                                                 sigSys = 1  
                                          if(sigSys<1.and sigSys >0.):
                                                 sigSys = sigSys + 1
                                          card += "%-25s" % (sigSys)
                            else:  
                                   card += "%-25s" % ("-")

                            for p in processes:
                                   if (p in sysValue[1]):
                                          if (getRate(ch, p, ifile) != 0.):
                                                 bkgSys = abs((getRate(ch, p+hsysNameUp, ifile) - getRate(ch, p+hsysNameDown, ifile))/ (2* getRate(ch, p, ifile)) )
                                          else:
                                                 bkgSys = 1
                                          if(bkgSys<1.and bkgSys >0.):
                                                 bkgSys = bkgSys + 1
                                          card += "%-25s" % (bkgSys)
                                   else:  
                                          card += "%-25s" % ("-")
              elif(sysValue[0].startswith("shape")):
                     ##print "\nsys shape named ", sysName
                     if("mcstat" not in sysName and 'autoMCstat' not in sysName):
                            card += "%-25s%-25s" % (sysName, sysValue[0])
                            if ("sig" in sysValue[1]):
                                   for sigp in sig:
                                          #card += "%-25s" % ( "-") 
                                          
                                          sigplab = ""
                                          if sigp.startswith("quad_") or sigp.startswith("sm_lin_"):
                                                 sigplab = sigp.replace("_F", "_c")
                                          else:
                                                 sigplab = sigp
                                          
                                          isbogussys=False 
                                          if(getRate(ch, sigplab+"_"+sysName+"Up", ifile)<0.0001 or getRate(ch, sigplab+"_"+sysName+"Down", ifile)<0.0001):
                                                 isbogussys=True
                                          if ((getRate(ch, sigplab, ifile) > 0.) and not isbogussys): 
                                                 ##print " signal ",sig," channel, ",ch, " file ",ifile, " rate ",(getRate(ch, sig, ifile))
                                                 ##print " signal ",sig," channel, ",ch, " file ",ifile, " rate up ",(getRate(ch, sig+"_"+sysName+"Up", ifile))
                                                 ##print " signal ",sig," channel, ",ch, " file ",ifile, " rate down",(getRate(ch, sig+"_"+sysName+"Down", ifile))
                                                 card += "%-25s" % ( "1")
                                                 pass
                                          elif isbogussys: 
                                                 card += "%-25s" % ( "-") 
                                          ##print sigplab, sysName, "is bogus?", isbogussys
                            for p in processes:
                                   ##print "sysName in p", p, sysName
                                   if p not in sysValue[1]:
                                          card += "%-25s" % ( "-") 
                                          continue
                                   isbogussys = False 
                                   if(getRate(ch, p+"_"+sysName+"Up", ifile)<0.0001 or getRate(ch, p+"_"+sysName+"Down", ifile)<0.0001):
                                          isbogussys = True

                                   if ((getRate(ch, p, ifile) > 0.) and not isbogussys): 
                                          card += "%-25s" % ( "1") 
                                   elif isbogussys:
                                          ##print "hello", p, sysName, "is bogus"
                                          card += "%-25s" % ( "-") 

                     elif("mcstat" in sysName):
                            # CAMBIARE NOME DELLA SYST                     
                            for samp in sysValue[1]:
                                   sampName = []
                                   line = ""
                                   if (samp == "sig" or samp == "Sig"): 
                                          for sigp in sig:
                                                 line = "%-25s" % ( "1") 
                                                 #line += "%-25s" % ("-") * (len(processes)) 
                                                 sampName.append(sig)
                                   elif(mode != "template"):
                                          line = "%-25s" % ( "-") 
                                          lineProc = ["%-25s" % ( "-") for x in xrange (len(processes))]
                                          if samp in processes: 
                                                 index = processes.index(samp)  
                                                 lineProc[index] = "1"
                                                 
                                          lineProc = "         ".join(lineProc)
                                          line += lineProc
                                          sampName =  samp
                                   else: 
                                          continue

                                   sampNameLine = ""
                                   for ids, sampn in enumerate(sampName):
                                          sampNameLine += sampn 
                                          if ids < (len(sampName) - 1):
                                                 sampNameLine += "_"

                                   for i in xrange(hist.GetNbinsX()):
                                          sysName = "mcstat_%s_%s_bin%d      "  % (ch, sampNameLine, i+1)
                                          card += "%-25s%-25s" % (sysName, sysValue[0])
                                          card += line
                                          card += "\n"        
              if('autoMCstat' in sysName):
                     card += "%-25s%-25s%-25d%-25d\n " % (ch, "autoMCStats", 10, 0)
              card += "\n"
       # End for loop on syst unc.       
       for k, v in rateParams.items():
              rpyear = k.split("_")[-1]
              for ch_ in v.chs:
                     if("2016" in k and "2016" not in ch):
                            continue
                     elif("2017" in k and "2017" not in ch):
                            continue
                     elif("2018" in k and "2018" not in ch):
                            continue
                     if("mu" in k and "mu" not in ch):
                            continue
                     elif("ele" in k and "ele" not in ch):
                            continue
                     if (ch_==("_").join(ch.split("_")[:-1])): 
                            if(("2016" in k) or ("2017" in k) or ("2018" in k)):
                                   if ('mu' in k and 'mu' in ch):
                                          card += "%-25s%-25s%-25s%-25s%-25d\n" % (k, "rateParam", ch, v.bkg, 1)
                                   elif ('ele' in k and 'ele' in ch):
                                          card += "%-25s%-25s%-25s%-25s%-25d\n" % (k, "rateParam", ch, v.bkg, 1)
                                   else:
                                          sameyear= ( ("2016" in k and "2016" in ch) or ("2017" in k and "2017" in ch) or ("2018" in k and "2018" in ch))
                                          if(sameyear): card += "%-25s%-25s%-25s%-25s%-25d\n" % (k, "rateParam", ch, v.bkg, 1)                                   
                            else:
                                   card += "%-25s%-25s%-25s%-25s%-25d\n" % (k, "rateParam", ch, v.bkg, 1)
                            card += "\n"

       if not os.path.isdir(outdir): 
              os.system('mkdir ' +outdir)
       if not os.path.isdir(outdir + "/" + dircoeff): 
              os.system('mkdir ' +outdir + "/" + dircoeff)
       #else:
              #os.system('rm ' +outdir + "/" + dircoeff + "/*")

       outname =  "%s%s_%s_%s.txt" % (carddir, coeff, ch, mode)
       ##print 'outname:', outname
       cardfile = open(outname, 'w')
       cardfile.write(card)
       cardfile.close()

       ##print card
       return card


ifilename = opt.ifile
outdirr = ""
if opt.outdir.startswith("F"):
    outdirr = opt.outdir.split("_")[0].replace("F", "f")
else:
    outdirr = opt.outdir

#print opt.outdir, outdirr

#os.system("rm " + outdir + "/*/*")

mode = opt.mode
unblind = opt.unblind

wilson = opt.ls

#print outdir


if opt.ch != "all": 
    ch_clean = opt.ch.replace(" ", "")
    channels = ch_clean.split(",")

signals = []

#print "Signal points: ", sigpoints

if wilson == "":
    modell = ""
    for sigp in sigpoints:
        for idp, p in enumerate(sigp):
            modell += p
            if idp < len(sigp) - 1:
                modell += "_"
            if not p.startswith("WpWp"):
                signal  = "VBS_SSWW_" + p
            else:
                signal  = p
            signals.append(signal)

        #width = p[1]
        #chir = p[2]
        #print "Creating datacards for VBS_" + modell#, width, chir)
        #print "Signals: ", signals


#print "Fit Params", fitParam
try:
    ifile = ROOT.TFile.Open(ifilename)
except IOError:
    print "Cannot open ", ifilename
else:
    pass

#print channels

for y in years:
    channels_years = [ch + '_' + y for ch in channels ]
    for ch in channels_years:
        if wilson != "":
            getCardLS(wilson, ch, ifilename, outdirr, mode, unblind)
        else:
            getCard(signals, ch, ifilename, outdirr, mode, unblind)
        #for s in signals:
            #getCard(s, ch, ifilename, outdir, mode, unblind)
