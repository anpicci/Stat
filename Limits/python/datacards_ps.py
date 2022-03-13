import ROOT
from ROOT import RooRealVar, RooDataHist, RooArgList, RooGenericPdf, RooExtendPdf, RooWorkspace, RooFit
import os, sys, copy
from Stat.Limits.settings import *
from collections import OrderedDict
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
       print process
       print "Getting histogram from ", ifile.GetName() 
       print "Histogram name: ", hName
       h = ifile.Get(hName)
       print h.GetName()
       return h.Integral()

def getHist(ch, process, ifile):
       hName = ch + "/"+ process
       print "Getting histogram from ", ifile.GetName() 
       print "Histogram name: ", hName
       #print "Histo Name ", hName
       h = ifile.Get(hName)
       return h

#*******************************************************#
#                                                       #
#                      Datacard                         #
#                                                       #
#*******************************************************#
def getCard(sig, ch, ifilename, outdir, mode = "histo", unblind = False):
       print "sig:", sig
       processes = []
       for p in bkg:
              isSM = False
              for sigp in sig:
                     if '_SM' in sigp or sigp == 'SM':
                            if 'TT_' in sig or 'TL_' in sig or 'LL_' in sig:
                                   if sig in p or 'SSWW_SM' in p:
                                          isSM = True
                            elif '_SM' in p:
                                   isSM = True
                     else:
                            if 'TT_' in p or 'TL_' in p or 'LL_' in p:
                                   isSM = True

              if isSM:
                     continue

              processes.append(p)

       print "processes:", processes

       try:
              ifile = ROOT.TFile.Open(ifilename)
       except IOError:
              print "Cannot open ", ifilename
       else:
              print "Opening file ",  ifilename
              ifile.cd()
       print syst 

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
                     print "*********Number of data ", histData.Integral()
              histSig = []
              for sigp in sig:
                     histSig.append(getHist(ch, sigp, ifile))
              bkgData = RooDataHist("bkgdata", "Data (MC Bkg)",  RooArgList(mT), histBkgData, 1.)
              obsData = RooDataHist("data_obs", "(pseudo) Data",  RooArgList(mT), histData, 1.)
              sigData = []
              for hsig in histSig:
                     sigData.append(RooDataHist("sigdata", "Data (MC sig)",  RooArgList(mT), hsig, 1.))
              print "Bkg Integral: ", histData.Integral() 
              nBkgEvts = histBkgData.Integral() 
              print "Bkg Events: ", nBkgEvts

              print "Channel: ", ch
              modelBkg = fitParam[ch].modelBkg
              normzBkg = RooRealVar(modelBkg.GetName()+"_norm", "Number of background events", nBkgEvts, 0., 1.e3)
              print "NormBkg ", nBkgEvts
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
                     #print mcstatSysName
                     #print sig + "_" + mcstatSysName + "Up"
                     mcstatSigUp = []
                     mcstatSigDown = []
                     mcstatSigHistUp = []
                     mcstatSigHistDown = []
                     for idxs, sigp in enumerate(sig):
                            mcstatSigUp = getHist(ch, sigp + "_" + mcstatSysName[idxs] + "Up", ifile)
                            #print "Integral  ", mcstatSigUp.Integral()
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
                                   print "==> Trigg sys name: ", sigp + "_" + sysName + "Down"
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

              #print "Workspace", "%sws_%s_%s_%s.root" % (carddir, sig, ch, mode) , "saved successfully"
              print "Workspace", ofname , "saved successfully"
                 
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
              print "===> Backgrounds:  ", processes
              nproc=(len(processes))
              for p in processes:
                     print "======================= p for rate", p, " syst, ", syst
                     print "ch is ", ch, " process is ", p, " ifile is ", ifile.GetName()
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

       print 'rates:'
       for k, v in rates.items():
              print k + ":", v

       if ((not unblind) and (mode == "template")): 
              print "N.B: We are in blind mode. Using MC bkg data for data_obs"
              rates["data_obs"] = getRate(ch, "Bkg", ifile)
              print "Pseudo data rate: ", rates["data_obs"]
       else: 
              rates["data_obs"] = getRate(ch, "data_obs", ifile)
       for sigp in sig:
              print "sigp: ", sigp
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
       print "===> Observed data: ", rates["data_obs"]
       card += "observation       %0.d\n" % (rates["data_obs"])
       card += "-----------------------------------------------------------------------------------\n"
       card += "bin                                     %-25s\n" % (binString)
       sigLine1 = ""
       sigLine2 = ""
       sigLine3 = ""
       for idxp, sigp in enumerate(sig):
              sigLine1 += "%-25s" % (sigp)
              sigLine2 += "%-25s" % (str(-len(sig)+idxp+1))
              sigLine3 += "%-25.6f" % (rates[sigp])

       card += "process                                 %-25s%-25s\n" % (sigLine1, procLine) #"roomultipdf"
       card += "process                                 %-25s%-25s\n" % (sigLine2, procNumbLine)
       card += "rate                                    %-25s%-25s\n" % (sigLine3, rateLine) #signalYield[m].getVal(), nevents
       card += "-----------------------------------------------------------------------------------\n"

       for sysName, sysValue in syst.iteritems():
              print "Systematic Uncertainty: ", sysName
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
                     card += "%-30s%-30s" % (sysName, sysValue[0])
                     if(sysValue[1]=="all" and len(sysValue)>2):
                            if(mode == "template"):
                                   card += "%-30s" % (sysValue[2]) * (2)
                            else:  
                                   card += "%-30s" % (sysValue[2]) * (len(processes) + len(sig))
                     elif(sysValue[1]=="QCD" and len(sysValue)>2):
                            if(mode == "template"):
                                   card += "%-30s" % (sysValue[2]) * (2)
                            else: 
                                   card += "%-30s" % (sysValue[2]) * (len(processes) + len(sig))
                     elif(sysValue[1]=="Fake"):
                            if not mode == "template":
                                   card += "%-30s" % ("-") * (len(sig)) + "%-30s" % (sysValue[2]) + "%-30s" % ("-") * (len(processes) - 1) 
                     else:
                            if (sysValue[1]=="all"):
                                   sysValue[1] = copy.deepcopy(processes)
                                   for sigp in sig:
                                          sysValue[1].append(sigp)
                            hsysName =  "_" + sysName  
                            hsysNameUp = "_" + sysName + "Up"  
                            hsysNameDown = "_" + sysName + "Down" 
                            #print "Applying syst on ", sysValue[1]
                            if("sig" in sysValue[1]):
                                   for sigp in sig:
                                          if(getRate(ch, sigp, ifile) != 0.):
                                                 sigSys = abs((getRate(ch, sigp+hsysNameUp, ifile) - getRate(ch, sigp+hsysNameDown, ifile))/ (2* getRate(ch, sigp, ifile)))
                                          else:
                                                 sigSys = 1
                                          if(sigSys<1.and sigSys >0.):
                                                 sigSys = sigSys + 1
                                          card += "%-30s" % (sigSys)
                            else: 
                                   card += "%-30s" % ("-")

                            for p in processes:
                                   if (p in sysValue[1]):
                                          if (getRate(ch, p, ifile) != 0.): bkgSys = abs((getRate(ch, p+hsysNameUp, ifile) - getRate(ch, p+hsysNameDown, ifile))/ (2* getRate(ch, p, ifile)) )
                                          else: bkgSys = 1
                                          if(bkgSys<1.and bkgSys >0.): bkgSys = bkgSys + 1
                                          card += "%-30s" % (bkgSys)
                                   else:  card += "%-30s" % ("-")
              elif(sysValue[0]=="shape"):
                     print "sys shape named ", sysName
                     if("mcstat" not in sysName and 'autoMCstat' not in sysName):
                            card += "%-30s%-30s" % (sysName, sysValue[0])
                            #card += "%-30s     shape     " % (sysName)
                            isbogussys = False 
                            if(getRate(ch, sigp+"_"+sysName+"Up", ifile)==0 or getRate(ch, sigp+"_"+sysName+"Down", ifile)==0):
                                   isbogussys = True
                            if ("sig" in sysValue[1]):
                                   for sigp in sig:
                                          if ((getRate(ch, sigp, ifile) != 0.) and not isbogussys): 
                                          #print " signal ",sig," channel, ",ch, " file ",ifile, " rate ",(getRate(ch, sig, ifile))
                                          #print " signal ",sig," channel, ",ch, " file ",ifile, " rate up ",(getRate(ch, sig+"_"+sysName+"Up", ifile))
                                          #print " signal ",sig," channel, ",ch, " file ",ifile, " rate down",(getRate(ch, sig+"_"+sysName+"Down", ifile))
                                                 card += "%-30s" % ( "1") 
                                          else:
                                                 card += "%-30s" % ( "-") 
                            for p in processes:
                                   if (p in sysValue[1]): 
                                          card += "%-30s" % ( "1") 
                                   else: 
                                          card += "%-30s" % ( "-") 
                     elif("mcstat" in sysName):
                            # CAMBIARE NOME DELLA SYST                     #here
                            for samp in sysValue[1]:
                                   #sampName = ""
                                   sampName = []
                                   line = ""
                                   if (samp == "sig" or samp == "Sig"): 
                                          for sigp in sig:
                                                 line = "%-30s" % ( "1") 
                                                 sampName.append(sigp)
                                          
                                          line += "%-30s" % ("-") * (len(processes)) 
                                                 
                                   elif(mode != "template"):
                                          line = "%-30s" % ( "-") 
                                          lineProc = ["%-30s" % ( "-") for x in xrange (len(processes))]
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
                                          card += "%-30s   shape   " % (sysName)
                                          card += line
                                          card += "\n"        
              if('autoMCstat' in sysName):
                     card += "%-30s%-30s%-30d%-30d " % (ch, "autoMCStats", 10, 0)
              card += "\n"
       # End for loop on syst unc.       
       card += "\n"
       for k, v in rateParams.items():
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
                                          card += "%-30s%-30s%-30s%-30s%-30d" % (k, "rateParam", ch, v.bkg, 1)
                                   elif ('ele' in k and 'ele' in ch):
                                          card += "%-30s%-30s%-30s%-30s%-30d" % (k, "rateParam", ch, v.bkg, 1)
                                   else:
                                          sameyear= ( ("2016" in k and "2016" in ch) or ("2017" in k and "2017" in ch) or ("2018" in k and "2018" in ch))
                                          if(sameyear): card += "%-30s%-30s%-30s%-30s%-30d" % (k, "rateParam", ch, v.bkg, 1)                                   
                            else:
                                   card += "%-30s%-30s%-30s%-30s%-30d" % (k, "rateParam", ch, v.bkg, 1)
                            card += "\n"

       #if not os.path.isdir(outdir):
              #os.system('mkdir ' + outdir)
       #hereee
       #if not os.path.isdir(outdir + "/" + sig): os.system('mkdir ' +outdir + "/" + sig)
       if not os.path.isdir(carddir):
              os.system('mkdir -p ' + carddir)

       outname = "" + carddir
       for sigp in sig:
              outname += sigp + "_"
       outname += ch + "_" + mode + ".txt"
       #outname =  "%s%s_%s_%s.txt" % (carddir, sig, ch, mode)
       cardfile = open(outname, 'w')
       cardfile.write(card)
       cardfile.close()
       #print card
       return card

#*******************************************************#
#                                                       #
#                 Datacard for LS                       #
#                                                       #
#*******************************************************#
def getCardLS(coeff, ch, ifilename, outdir, mode = "histo", unblind = False):
       print "channel:", ch
       print outdir

       nop = coeff.split("_")[0]
       lssamp = ["", "", ""]
       for name, coll in lssamples_1D.items():
              if name == coeff:
                     for nout, nin in coll.items():
                            if nout == "sm":
                                   lssamp[0] = nout# lss for lss in lssamples_1D if (lss=="sm" or ("_"+coeff) in lss)]
                            elif nout.startswith("sm_lin_"):
                                   lssamp[1] = nout#.replace("_F", "_c")
                            elif nout.startswith("quad_"):
                                   lssamp[2] = nout#.replace("_F", "_c")

       processes = []
       for p in bkg:
              isSM = False
              if '_SM' in p:
                     continue

              processes.append(p)

       print "processes:", processes

       try:
              ifile = ROOT.TFile.Open(ifilename)
       except IOError:
              print "Cannot open ", ifilename
       else:
              print "Opening file ",  ifilename
              ifile.cd()
       print syst 

       workdir_ = ifilename.split("/")[:-1]
       WORKDIR = "/".join(workdir_) + "/"
       dircoeff = ""
       if coeff.startswith("F"):
              dircoeff = coeff.split("_")[0].replace("F", "f")
       else:
              dircoeff = coeff
       carddir = outdir+  "/"  + dircoeff + "/"

       sig = lssamp[0]
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
                     print "BE CAREFULL: YOU ARE UNBLINDING"
                     histData = getHist(ch, "data_obs", ifile)
                     print "*********Number of data ", histData.Integral()
              histSig = getHist(ch, sig, ifile)
              bkgData = RooDataHist("bkgdata", "Data (MC Bkg)",  RooArgList(mT), histBkgData, 1.)
              obsData = RooDataHist("data_obs", "(pseudo) Data",  RooArgList(mT), histData, 1.)
              sigData = RooDataHist("sigdata", "Data (MC sig)",  RooArgList(mT), histSig, 1.)
              print "Bkg Integral: ", histData.Integral() 
              nBkgEvts = histBkgData.Integral() 
              print "Bkg Events: ", nBkgEvts

              print "Channel: ", ch
              modelBkg = fitParam[ch].modelBkg
              normzBkg = RooRealVar(modelBkg.GetName()+"_norm", "Number of background events", nBkgEvts, 0., 1.e3)
              print "NormBkg ", nBkgEvts
              modelExt = RooExtendPdf(modelBkg.GetName()+"_ext", modelBkg.GetTitle(), modelBkg, normzBkg)

              # create workspace
              w = RooWorkspace("SVJ", "workspace")
              # Dataset
              # ATT: include isData
              getattr(w, "import")(bkgData, RooFit.Rename("Bkg"))
              getattr(w, "import")(obsData, RooFit.Rename("data_obs"))
              getattr(w, "import")(sigData, RooFit.Rename(sig))

              for i in xrange(hist.GetNbinsX()):
                     mcstatSysName = "mcstat_%s_%s_bin%d"  % (ch, sig, i+1)
                     #print mcstatSysName
                     #print sig + "_" + mcstatSysName + "Up"
                     mcstatSigUp = getHist(ch, sig + "_" + mcstatSysName + "Up", ifile)

                     #print "Integral  ", mcstatSigUp.Integral()
                     mcstatSigDown = getHist(ch, sig + "_" + mcstatSysName + "Down", ifile)
                     mcstatSigHistUp = RooDataHist(sig + "_" + mcstatSysName + "Up", "Data (MC sig)",  RooArgList(mT), mcstatSigUp, 1.)
                     mcstatSigHistDown = RooDataHist(sig + "_" + mcstatSysName + "Down", "Data (MC sig)",  RooArgList(mT), mcstatSigDown, 1.)
                     getattr(w, "import")(mcstatSigHistUp, RooFit.Rename(sig + "_" + mcstatSysName + "Up") )
                     getattr(w, "import")(mcstatSigHistDown, RooFit.Rename(sig + "_" + mcstatSysName + "Down") )

              for sysName,sysValue  in syst.iteritems():
                     if(sysValue[0]=="shape" and "mcstat" not in sysName):              
                            sysUp =  getHist(ch, sig + "_" + sysName + "Up", ifile)
                            sysDown =  getHist(ch, sig + "_" + sysName + "Down", ifile)
                            print "==> Trigg sys name: ", sig + "_" + sysName + "Down"
                            sysSigHistUp = RooDataHist(sig + "_" + sysName + "Up", sysName + " uncertainty",  RooArgList(mT), sysUp, 1.)
                            sysSigHistDown = RooDataHist(sig + "_" + sysName + "Down", sysName + " uncertainty",  RooArgList(mT), sysDown, 1.)
                            getattr(w, "import")(sysSigHistUp, RooFit.Rename(sig + "_" + sysName + "Up") )
                            getattr(w, "import")(sysSigHistDown, RooFit.Rename(sig + "_" + sysName + "Down") )
              #else: getattr(w, "import")(setToys, RooFit.Rename("data_obs"))
              getattr(w, "import")(modelBkg, RooFit.Rename(modelBkg.GetName()))
              #getattr(w, "import")(modelAlt, RooFit.Rename(modelAlt.GetName()))
              getattr(w, "import")(normzBkg, RooFit.Rename(normzBkg.GetName()))
              w.writeToFile("%sws_%s_%s_%s.root" % (carddir, coeff, ch, mode), True)

              print "Workspace", "%sws_%s_%s_%s.root" % (carddir, coeff, ch, mode) , "saved successfully"
                 
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
              i = 0
              bkgrate = 0
              print "===> Backgrounds:  ", processes
              nproc=(len(processes))
              for p in processes:
                     print "======================= p for rate", p, " syst, ", syst
                     print "ch is ", ch, " process is ", p, " ifile is ", ifile.GetName()
                     rates[p] = getRate(ch, p, ifile)
                     bkgrate =  rates[p]
                     if (p =="QCD"): print "qcd: ", bkgrate
                     if(bkgrate==0):
                            nproc = nproc -1
                            continue
                     procNumbLine += ("%-25s") % (i + len(lssamp))
                     procLine += ("%-25s") % (p)
                     rateLine += ("%-25f") % (bkgrate)
                     i+=1
              binString += (("%-25s") % (ch) ) * (nproc + len(lssamp))
              print 'rates:'
              for k, v in rates.items():
                     print k + ":", v

       if ((not unblind) and (mode == "template")): 
              print "N.B: We are in blind mode. Using MC bkg data for data_obs"
              rates["data_obs"] = getRate(ch, "Bkg", ifile)
              print "Pseudo data rate: ", rates["data_obs"]
       else:
              rates["data_obs"] = getRate(ch, "data_obs", ifile)
       for sgs in lssamp:
              rates[sgs] = getRate(ch, sgs, ifile)
       
       print 'rates:'
       for k, v in rates.items():
              print k + ":", v

       card  = "imax 1 number of channels \n"
       card += "jmax * number of backgrounds \n"
       card += "kmax * number of nuisance parameters\n"
       card += "-----------------------------------------------------------------------------------\n"

       if(mode == "template"):
              #              card += "shapes   %s  %s    %s    %s    %s\n" % (sig, ch, ifilename, "$CHANNEL/$PROCESS", "$CHANNEL/$PROCESS_SYSTEMATIC")
              #              card += "shapes            %-15s  %-5s    %s%s.root    %s\n" % (sig, ch, WORKDIR, ch, "SVJ:$PROCESS")
              card += "shapes   %s  %s    %s    %s\n" % (modelBkg.GetName(), ch, workfile, "SVJ:$PROCESS")
              card += "shapes   %s  %s    %s    %s    %s\n" % (sig, ch, workfile, "SVJ:$PROCESS", "SVJ:$PROCESS_$SYSTEMATIC")
              card += "shapes   %s  %s    %s    %s\n" % ("data_obs", ch, workfile, "SVJ:$PROCESS")

       else:  
              card += "shapes   *      *   %s    %s    %s\n" % (hist_filename, "$CHANNEL/$PROCESS", "$CHANNEL/$PROCESS_$SYSTEMATIC")
              card += "shapes   data_obs      *   %s    %s\n" % (hist_filename, "$CHANNEL/$PROCESS")
       card += "-----------------------------------------------------------------------------------\n"
       card += "bin               %s\n" % ch

       print "===> Observed data: ", rates["data_obs"]
       card += "observation       %0.d\n" % (rates["data_obs"])
       card += "-----------------------------------------------------------------------------------\n"
       card += "bin                                     %-25s\n" % (binString)
       #card += "process                                 "
       procnameString = "process                                 "
       procidxString = "process                                 "
       rateString = "rate                                    "
       
       for sidx, sgs in enumerate(lssamp):
              procnameString += "%-25s" % (sgs.replace("_F", "_c"))
              procidxString += "%-25s" % (sidx)
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

       for sysName,sysValue  in syst.iteritems():
              print "Systematic Uncertainty: ", sysName
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
                     card += "%-30s%-30s" % (sysName, sysValue[0])
                     if len(sysValue)>2:
                            if(sysValue[1]=="all"):
                                   if(mode == "template"):
                                          card += "%-30s" % (sysValue[2]) * (2)
                                   else:  card += "%-30s" % (sysValue[2]) * (len(lssamp) + len(processes))# + 1)
                            elif(sysValue[1]=="QCD" and len(sysValue)>2):
                                   if(mode == "template"):
                                          card += "%-30s" % (sysValue[2]) * (2)
                                   else: 
                                          card += "%-30s" % (sysValue[2]) * (len(lssamp) + len(processes))#+ 1)
                            else:#(sysValue[1]=="Fake"):
                                   idx_p = processes.index(sysValue[1])
                                   idx_p_tot = idx_p + len(lssamp)
                                   if not mode == "template":
                                          card += "%-30s" % ("-") * (idx_p_tot) + "%-30s" % (sysValue[2]) + "%-30s" % ("-") * (len(processes) - (idx_p + 1)) 
                     else:
                            if (sysValue[1]=="all"):
                                   sysValue[1] = copy.deepcopy(processes)
                                   sysValue[1].append(sig)
                            hsysName =  "_" + sysName  
                            hsysNameUp = "_" + sysName + "Up"  
                            hsysNameDown = "_" + sysName + "Down" 
                            #print "Applying syst on ", sysValue[1]
                            if("sig" in sysValue[1]):
                                   if(getRate(ch, sig, ifile) != 0.): sigSys = abs((getRate(ch, sig+hsysNameUp, ifile) - getRate(ch, sig+hsysNameDown, ifile))/ (2* getRate(ch, sig, ifile)))
                                   else: sigSys = 1  
                                   if(sigSys<1.and sigSys >0.): sigSys = sigSys + 1
                                   card += "%-30s" % (sigSys)
                            else:  card += "%-30s" % ("-")
                            for p in processes:
                                   if (p in sysValue[1]):
                                          if (getRate(ch, p, ifile) != 0.): bkgSys = abs((getRate(ch, p+hsysNameUp, ifile) - getRate(ch, p+hsysNameDown, ifile))/ (2* getRate(ch, p, ifile)) )
                                          else: bkgSys = 1
                                          if(bkgSys<1.and bkgSys >0.): bkgSys = bkgSys + 1
                                          card += "%-30s" % (bkgSys)
                                   else:  card += "%-30s" % ("-")
              elif(sysValue[0]=="shape"):
                     print "sys shape named ", sysName
                     if("mcstat" not in sysName and 'autoMCstat' not in sysName):
                            card += "%-30s     shape     " % (sysName)
                            isbogussys=False 
                            #if(getRate(ch, sig+"_"+sysName+"Up", ifile)==0 or getRate(ch, sig+"_"+sysName+"Down", ifile)==0):isbogussys=True
                            if ("sig" in sysValue[1]) and ((getRate(ch, sig, ifile) != 0.) and not isbogussys): 
                                   #print " signal ",sig," channel, ",ch, " file ",ifile, " rate ",(getRate(ch, sig, ifile))
                                   #print " signal ",sig," channel, ",ch, " file ",ifile, " rate up ",(getRate(ch, sig+"_"+sysName+"Up", ifile))
                                   #print " signal ",sig," channel, ",ch, " file ",ifile, " rate down",(getRate(ch, sig+"_"+sysName+"Down", ifile))
                                   card += "%-30s" % ( "1") 
                            else: card += "%-30s" % ( "-") 
                            for p in processes:
                                   if (p in sysValue[1]): 
                                          if "q2SingleTop" in sysName: card += "%-30s" % ( "1") 
                                          else: card += "%-30s" % ( "1") 
                                          #print "adding to channel ", p
                                   else: card += "%-30s" % ( "-") 
                     elif("mcstat" in sysName):
                            # CAMBIARE NOME DELLA SYST                     
                            for samp in sysValue[1]:
                                   sampName = ""
                                   line = ""
                                   if (samp == "sig" or samp == "Sig"): 
                                          line = "%-30s" % ( "1") 
                                          line += "%-30s" % ("-") * (len(processes)) 
                                          sampName = sig
                                   elif(mode != "template"):
                                          line = "%-30s" % ( "-") 
                                          lineProc = ["%-30s" % ( "-") for x in xrange (len(processes))]
                                          if samp in processes: 
                                                 index = processes.index(samp)  
                                                 lineProc[index] = "1"
                                                 
                                          lineProc = "         ".join(lineProc)
                                          line += lineProc
                                          sampName =  samp
                                   else: continue
                                   for i in xrange(hist.GetNbinsX()):
                                          sysName = "mcstat_%s_%s_bin%d      "  % (ch, sampName, i+1)
                                          card += "%-30s   shape   " % (sysName)
                                          card += line
                                          card += "\n"        
              if('autoMCstat' in sysName):
                     card += "%-30s%-30s%-30d%-30d\n " % (ch, "autoMCStats", 10, 0)
              card += "\n"
       # End for loop on syst unc.       
       for k, v in rateParams.items():
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
                                          card += "%-30s%-30s%-30s%-30s%-30d\n" % (k, "rateParam", ch, v.bkg, 1)
                                   elif ('ele' in k and 'ele' in ch):
                                          card += "%-30s%-30s%-30s%-30s%-30d\n" % (k, "rateParam", ch, v.bkg, 1)
                                   else:
                                          sameyear= ( ("2016" in k and "2016" in ch) or ("2017" in k and "2017" in ch) or ("2018" in k and "2018" in ch))
                                          if(sameyear): card += "%-30s%-30s%-30s%-30s%-30d\n" % (k, "rateParam", ch, v.bkg, 1)                                   
                            else:
                                   card += "%-30s%-30s%-30s%-30s%-30d\n" % (k, "rateParam", ch, v.bkg, 1)
                            card += "\n"

       if not os.path.isdir(outdir): os.system('mkdir ' +outdir)
       if not os.path.isdir(outdir + "/" + dircoeff): os.system('mkdir ' +outdir + "/" + dircoeff)


       outname =  "%s%s_%s_%s.txt" % (carddir, coeff, ch, mode)
       print 'outname:', outname
       cardfile = open(outname, 'w')
       cardfile.write(card)
       cardfile.close()

       #print card
       return card
