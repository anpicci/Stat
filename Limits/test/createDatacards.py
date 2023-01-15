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
#parser.add_option("-u","--unblind",dest="unblind",action='store_true', default=False)
parser.add_option('--ls', dest='ls', type='string', default = '', help='wilson coeff')
parser.add_option('--settmod"', dest='settmod', type='string', default = 'total', help = 'Specify settmod')

(opt, args) = parser.parse_args()
sys.argv.append('-b')

setname = opt.settmod
settmod = importlib.import_module(setname)

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
def getCard(sig, ch, ifilename, outdir, mode = "histo"):#, unblind = False):
       
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

       #hist_filename = os.getcwd()+"/"+ifilename
       hist_filename = "../shapes/"+ifilename.split("/")[-1]
       hist = []
       for sigp in sig:
              hist.append(getHist(ch, sigp, ifile))

       #*******************************************************#
       #                                                       #
       #                   Generate workspace                  #
       #                                                       #
       #*******************************************************#
       rates = {}
       procLine = ""
       procNumbLine = ""
       rateLine = ""
       binString = ""

       if True:
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

       if True: 
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

       if True:  
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
              #print sysName, sysValue

              if(sysValue[0]=="lnN"):
                     if sysName.startswith("mischarge") and not ch.startswith("SR"):
                            continue
                     if "lumi" in sysName and "1718_" in sysName:
                            sysName = sysName.replace("APV", "").replace("_2016", "").replace("_2017", "").replace("_2018", "")
                     card += "%-25s%-25s" % (sysName, sysValue[0])
                     if len(sysValue)>2:
                            if(sysValue[1]=="all" and len(sysValue)>2):
                                   card += "%-25s" % (sysValue[2]) * (len(processes) + len(sig))
                            elif(sysValue[1]=="QCD" and len(sysValue)>2):
                                   card += "%-25s" % (sysValue[2]) * (len(processes) + len(sig))
                            else:#(sysValue[1]=="Fake"):
                                   strsys = ""
                                   for sigp in sig:
                                       if not 'sig' in sysValue[1]:
                                           strsys += "%-25s" % ("-")
                                       else:
                                           strsys += "%-25s" % (sysValue[2])
                                   for proc in processes:
                                       if proc in sysValue[1]:
                                           strsys += "%-25s" % (sysValue[2])
                                       else:
                                           strsys += "%-25s" % ("-")

                                   card += strsys#"%-25s" % ("-") * (idx_p_tot) + "%-25s" % (sysValue[2]) + "%-25s" % ("-") * (len(processes) - (idx_p + 1)) 
                                          #print "%-25s" % ("-") * (idx_p_tot) + "%-25s" % (sysValue[2]) + "%-25s" % ("-") * (len(processes) - (idx_p + 1)) 

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
                     #print "sys shape named ", sysName, sysValue
                     if("mcstat" not in sysName and 'autoMCstat' not in sysName):

                            card += "%-25s%-25s" % (sysName, sysValue[0])
                          
                            #card += "%-25s     shape     " % (sysName)
                            if ("sig" in sysValue[1]):
                                   for sigp in sig:
                                          isbogussys = False 
                                          if((getRate(ch, sigp+"_"+sysName+"Up", ifile)<0.001 or getRate(ch, sigp+"_"+sysName+"Down", ifile)<0.001)) or getRate(ch, p, ifile) <= 0.:
                                                 isbogussys = True
                            
                                          if ((getRate(ch, sigp, ifile) > 0.) and not isbogussys): 
                                          ##print " signal ",sig," channel, ",ch, " file ",ifile, " rate ",(getRate(ch, sig, ifile))
                                          ##print " signal ",sig," channel, ",ch, " file ",ifile, " rate up ",(getRate(ch, sig+"_"+sysName+"Up", ifile))
                                          ##print " signal ",sig," channel, ",ch, " file ",ifile, " rate down",(getRate(ch, sig+"_"+sysName+"Down", ifile))
                                                 card += "%-25s" % ( "1") 
                          
                                          elif isbogussys:
                                                 card += "%-25s" % ( "-")
                          
                            else:
                                   card += "%-25s" % ("-") * (len(sig))
                          
                            for p in processes:
                                   if p not in sysValue[1]:
                                          card += "%-25s" % ( "-") 
                                          continue
                                   isbogussys = False 
                                   if((getRate(ch, p+"_"+sysName+"Up", ifile)<0.001 or getRate(ch, p+"_"+sysName+"Down", ifile)<0.001)) or getRate(ch, p, ifile) <= 0.:
                                          isbogussys = True

                                   if ((getRate(ch, p, ifile) > 0.) and not isbogussys): 
                                          card += "%-25s" % ( "1") 

                                   elif isbogussys: 
                                          card += "%-25s" % ( "-")

                                          print p, "bogus", sysname
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
                      card += "%-25s%-25s%-25d%-25d " % (ch, "autoMCStats", 10, 0)
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
       #print carddir
       outname = "" + carddir
       for sigp in sig:
              print sigp
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
def getCardLS(incoeff, ch, ifilename, outdir, mode = "histo"):#, unblind = False):
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
       setpiecs.sort(reverse=True)
       if incoeff.startswith("F") or ":F" in incoeff:
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
       #print "directory with cards:", carddir

       sig = lssamp
       #hist_filename = os.getcwd()+"/"+ifilename
       hist_filename = "../shapes/"+ifilename.split("/")[-1]
       hist = []
       for sigp in sig:
              ##print getHist(ch, sigp, ifile)
              hist.append(getHist(ch, sigp, ifile))

       #*******************************************************#
       #                                                       #
       #                   Generate workspace                  #
       #                                                       #
       #*******************************************************#
       rates = OrderedDict()
       procLine = ""
       procNumbLine = ""
       rateLine = ""
       binString = ""

       if True:
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
       if True:
              rates["data_obs"] = getRate(ch, "data_obs", ifile)
       for sgs in lssamp:
              #print "sgs:", sgs
              torem = "_" + sgs.split("_")[-1]
              #print "torem:", torem
              sgslab = ""
              if sgs.startswith("quad_") or sgs.startswith("sm_lin_"):
                     sgslab = sgs.replace("_F", "_c")
                     if "_F" in sgs and not ":" in opt.ls:
                         sgslab = sgslab.replace(torem, "")
                         
              else:
                     sgslab = sgs
              #print sgslab
              rates[sgs] = getRate(ch, sgslab, ifile)
       
       ##print 'rates:'
       #for k, v in rates.items():
              ##print k + ":", v


       card  = "imax 1 number of channels \n"
       card += "jmax * number of backgrounds \n"
       card += "kmax * number of nuisance parameters\n"
       card += "-----------------------------------------------------------------------------------\n"

       if True:  
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
              if sgs.startswith("quad_") or sgs.startswith("sm_lin_"):
                     sgslab = sgs.replace("_F", "_c")
                     if "_F" in sgs and not ":" in opt.ls:
                         #print "removing"
                         sgslab = sgslab.replace(torem, "")
                         #print sgslab
              else:
                     sgslab = sgs
              
              procnameString += "%-25s" % sgslab#(sgs.replace("_F", "_c"))
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
                     if sysName.startswith("mischarge") and not ch.startswith("SR"):
                            continue
                     card += "%-25s%-25s" % (sysName, sysValue[0])
                     if len(sysValue)>2:
                            if(sysValue[1]=="all"):
                                   card += "%-25s" % (sysValue[2]) * (len(lssamp) + len(processes))# + 1)
                            elif(sysValue[1]=="QCD" and len(sysValue)>2):
                                   card += "%-25s" % (sysValue[2]) * (len(lssamp) + len(processes))#+ 1)
                            else:#(sysValue[1]=="Fake"):
                                   strsys = ""
                                   for sigp in sig:
                                       if not 'sig' in sysValue[1]:
                                           strsys += "%-25s" % ("-")
                                       else:
                                           strsys += "%-25s" % (sysValue[2])
                                   for proc in processes:
                                       if proc in sysValue[1]:
                                           strsys += "%-25s" % (sysValue[2])
                                       else:
                                           strsys += "%-25s" % ("-")

                                   card += strsys#"%-25s" % ("-") * (idx_p_tot) + "%-25s" % (sysValue[2]) + "%-25s" % ("-") * (len(processes) - (idx_p + 1)) 
                                          #print "%-25s" % ("-") * (idx_p_tot) + "%-25s" % (sysValue[2]) + "%-25s" % ("-") * (len(processes) - (idx_p + 1)) 
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
                                                 torem = "_" + sigp.split("_")[-1]
                                                 if "_F" in sigp and not ":" in opt.ls:
                                                     sigplab = sigplab.replace(torem, "")
                                          else:
                                                 sigplab = sigp
                                          
                                          isbogussys=False 
                                          if((getRate(ch, sigplab+"_"+sysName+"Up", ifile)<0.0001 or getRate(ch, sigplab+"_"+sysName+"Down", ifile)<0.0001)) or getRate(ch, p, ifile) <= 0.:
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
                            else:
                                   card += "%-25s" % ("-") * (len(sig))

                            for p in processes:
                                   ##print "sysName in p", p, sysName
                                   if p not in sysValue[1]:
                                          card += "%-25s" % ( "-") 
                                          continue
                                   isbogussys = False 
                                   if((getRate(ch, p+"_"+sysName+"Up", ifile)<0.0001 or getRate(ch, p+"_"+sysName+"Down", ifile)<0.0001)) or getRate(ch, p, ifile) <= 0.:
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
       print "carddir:", carddir
       outname =  "%s%s_%s_%s.txt" % (carddir, coeff, ch, mode)
       print 'outname:', outname
       cardfile = open(outname, 'w')
       cardfile.write(card)
       cardfile.close()

       ##print card
       return card


ifilename = opt.ifile
#outdirr = ""
#if opt.outdir.startswith("F"):
    #outdirr = opt.outdir.split("_")[0].replace("F", "f")
#else:
outdirr = opt.outdir

#outdirr += "/shapes"
if not os.path.exists(outdirr):
    os.system("mkdir -p " + outdirr)
#print "outdirr", opt.outdir, outdirr

mode = opt.mode
#unblind = opt.unblind

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
            getCardLS(wilson, ch, ifilename, outdirr, mode)#, unblind)
        else:
            getCard(signals, ch, ifilename, outdirr, mode)#, unblind)
        #for s in signals:
            #getCard(s, ch, ifilename, outdir, mode, unblind)

