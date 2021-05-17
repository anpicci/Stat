import ROOT
from ROOT import RooRealVar, RooDataHist, RooArgList, RooGenericPdf, RooExtendPdf, RooWorkspace, RooFit
import os, sys, copy
from Stat.Limits.settings import *
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
       print "Getting histogram from ", ifile.GetName() 
       print "Histogram name: ", hName
       h = ifile.Get(hName)
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
       if '_SM' in sig:
              processes.pop(-1)

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
       carddir = outdir+  "/"  + sig + "/"

       hist_filename = os.getcwd()+"/"+ifilename
       hist = getHist(ch, sig, ifile)

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
              w.writeToFile("%sws_%s_%s_%s.root" % (carddir, sig, ch, mode), True)

              print "Workspace", "%sws_%s_%s_%s.root" % (carddir, sig, ch, mode) , "saved successfully"
                 
              workfile = "./ws_%s_%s_%s.root" % ( sig, ch, mode)
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
              procLine += ("%-43s") % ("Bkg")
              rateLine += ("%-43s") % (rates["Bkg"])
              binString += (("%-43s") % (ch) ) * (2)
              procNumbLine = 1 
       else:
              i = 1
              bkgrate = 0
              print "===> Backgrounds:  ", processes
              nproc=(len(processes)+1)
              for p in processes:
                     print "======================= p for rate", p, " syst, ", syst
                     print "ch is ", ch, " process is ", p, " ifile is ", ifile.GetName()
                     rates[p] = getRate(ch, p, ifile)
                     bkgrate =  rates[p]
                     if (p =="QCD"): print "qcd: ", bkgrate
                     if(bkgrate==0):
                            nproc=nproc -1
                            continue
                     procNumbLine += ("%-43s") % (i)
                     procLine += ("%-43s") % (p)
                     rateLine += ("%-43.2f") % (bkgrate)
                     i+=1
              binString += (("%-43s") % (ch) ) * (nproc)
       if ((not unblind) and (mode == "template")): 
              print "N.B: We are in blind mode. Using MC bkg data for data_obs"
              rates["data_obs"] = getRate(ch, "Bkg", ifile)
              print "Pseudo data rate: ", rates["data_obs"]
       else: rates["data_obs"] = getRate(ch, "data_obs", ifile)
       rates[sig] = getRate(ch, sig, ifile)
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
       card += "bin                                     %-43s\n" % (binString)
       card += "process                                 %-43s%-43s\n" % (sig, procLine) #"roomultipdf"
       card += "process                                 %-43s%-43s\n" % ("0", procNumbLine)
       card += "rate                                    %-43.6f%-43s\n" % (rates[sig], rateLine) #signalYield[m].getVal(), nevents
       card += "-----------------------------------------------------------------------------------\n"
       for sysName,sysValue  in syst.iteritems():
              print "Systematic Uncertainty: ", sysName
              if("2016" in sysName and "2016" not in ch): continue
              elif("2017" in sysName and "2017" not in ch): continue
              elif("2018" in sysName and "2018" not in ch): continue
              if("mu" in sysName and "mu" not in ch): continue
              elif("ele" in sysName and "ele" not in ch): continue
              if(sysValue[0]=="lnN"): 
                     card += "%-20s%-20s" % (sysName, sysValue[0])
                     if(sysValue[1]=="all" and len(sysValue)>2):
                            if(mode == "template"): card += "%-20s" % (sysValue[2]) * (2)
                            else:  card += "%-20s" % (sysValue[2]) * (len(processes) + 1)
                     elif(sysValue[1]=="QCD" and len(sysValue)>2):
                            if(mode == "template"):
                                   card += "%-20s" % (sysValue[2]) * (2)
                            else: 
                                   card += "%-20s" % (sysValue[2]) * (len(processes) + 1)
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
                                   card += "%-20s" % (sigSys)
                            else:  card += "%-20s" % ("-")
                            for p in processes:
                                   if (p in sysValue[1]):
                                          if (getRate(ch, p, ifile) != 0.): bkgSys = abs((getRate(ch, p+hsysNameUp, ifile) - getRate(ch, p+hsysNameDown, ifile))/ (2* getRate(ch, p, ifile)) )
                                          else: bkgSys = 1
                                          if(bkgSys<1.and bkgSys >0.): bkgSys = bkgSys + 1
                                          card += "%-20s" % (bkgSys)
                                   else:  card += "%-20s" % ("-")
              elif(sysValue[0]=="shape"):
                     print "sys shape named ", sysName
                     if("mcstat" not in sysName and 'autoMCstat' not in sysName):
                            card += "%-20s     shape     " % (sysName)
                            isbogussys=False 
                            #if(getRate(ch, sig+"_"+sysName+"Up", ifile)==0 or getRate(ch, sig+"_"+sysName+"Down", ifile)==0):isbogussys=True
                            if ("sig" in sysValue[1]) and ((getRate(ch, sig, ifile) != 0.) and not isbogussys): 
                                   #print " signal ",sig," channel, ",ch, " file ",ifile, " rate ",(getRate(ch, sig, ifile))
                                   #print " signal ",sig," channel, ",ch, " file ",ifile, " rate up ",(getRate(ch, sig+"_"+sysName+"Up", ifile))
                                   #print " signal ",sig," channel, ",ch, " file ",ifile, " rate down",(getRate(ch, sig+"_"+sysName+"Down", ifile))
                                   card += "%-20s" % ( "1") 
                            else: card += "%-20s" % ( "-") 
                            for p in processes:
                                   if (p in sysValue[1]): 
                                          if "q2SingleTop" in sysName: card += "%-20s" % ( "1") 
                                          else: card += "%-20s" % ( "1") 
                                          #print "adding to channel ", p
                                   else: card += "%-20s" % ( "-") 
                     elif("mcstat" in sysName):
                            # CAMBIARE NOME DELLA SYST                     
                            for samp in sysValue[1]:
                                   sampName = ""
                                   line = ""
                                   if (samp == "sig" or samp == "Sig"): 
                                          line = "%-20s" % ( "1") 
                                          line += "%-20s" % ("-") * (len(processes)) 
                                          sampName = sig
                                   elif(mode != "template"):
                                          line = "%-20s" % ( "-") 
                                          lineProc = ["%-20s" % ( "-") for x in xrange (len(processes))]
                                          if samp in processes: 
                                                 index = processes.index(samp)  
                                                 lineProc[index] = "1"
                                                 
                                          lineProc = "         ".join(lineProc)
                                          line += lineProc
                                          sampName =  samp
                                   else: continue
                                   for i in xrange(hist.GetNbinsX()):
                                          sysName = "mcstat_%s_%s_bin%d      "  % (ch, sampName, i+1)
                                          card += "%-20s   shape   " % (sysName)
                                          card += line
                                          card += "\n"        
              if('autoMCstat' in sysName):
                     card += "%-20s%-20s%-20d\n " % (ch, "autoMCStats", 0)
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
                                          card += "%-20s%-20s%-20s%-20s%-20d\n" % (k, "rateParam", ch, v.bkg, 1)
                                   elif ('ele' in k and 'ele' in ch):
                                          card += "%-20s%-20s%-20s%-20s%-20d\n" % (k, "rateParam", ch, v.bkg, 1)
                                   else:
                                          sameyear= ( ("2016" in k and "2016" in ch) or ("2017" in k and "2017" in ch) or ("2018" in k and "2018" in ch))
                                          if(sameyear): card += "%-20s%-20s%-20s%-20s%-20d\n" % (k, "rateParam", ch, v.bkg, 1)                                   
                            else:
                                   card += "%-20s%-20s%-20s%-20s%-20d\n" % (k, "rateParam", ch, v.bkg, 1)
                            card += "\n"

       if not os.path.isdir(outdir): os.system('mkdir ' +outdir)
       if not os.path.isdir(outdir + "/" + sig): os.system('mkdir ' +outdir + "/" + sig)


       outname =  "%s%s_%s_%s.txt" % (carddir, sig, ch, mode)
       cardfile = open(outname, 'w')
       cardfile.write(card)
       cardfile.close()
       #print card
       return card




