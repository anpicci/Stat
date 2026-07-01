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
parser.add_option('--settmod', dest='settmod', type='string', default = 'total', help = 'Specify settmod')
parser.add_option('--mcstat', dest='mcstat', type='string', default = '10', help='Default no merging bins')

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
mcstatt = int(opt.mcstat)

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
       try:
           h = ifile.Get(hName)
       except:
           raise RuntimeError("Problems when getting rates from histogram " + hName + " from ", ifile.GetName())
       else:
           pass
       ##print h.GetName()
       return h.Integral()

def getHist(ch, process, ifile):
       hName = ch + "/"+ process
       ##print "Getting histogram from ", ifile.GetName() 
       ##print "Histogram name: ", hName
       ##print "Histo Name ", hName
       try:
           h = ifile.Get(hName)
       except:
           raise RuntimeError("Problems when getting histogram " + hName + " from ", ifile.GetName())
       else:
           pass
       return h

def hasHist(ch, process, ifile):
       hName = ch + "/" + process
       h = ifile.Get(hName)
       return bool(h)

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
              print("Cannot open ", ifilename)
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
                     if (p =="QCD"): print("qcd: ", bkgrate)

                     #if(bkgrate<=0.):
                            #nproc = nproc - 1
                            #continue

                     procNumbLine += ("%-35s") % (i)
                     procLine += ("%-35s") % (p)
                     rateLine += ("%-35f") % (bkgrate)
                     i+=1
              binString += (("%-35s") % (ch) ) * (nproc + len(sig))

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
       card += "%-50s%-35s\n" % ("bin", binString)

       sigLine1 = ""
       sigLine2 = ""
       sigLine3 = ""
       for idxp, sigp in enumerate(sig):
              sigLine1 += "%-35s" % (sigp)
              sigLine2 += "%-35s" % (str(-len(sig)+idxp+1))
              sigLine3 += "%-35.6f" % (rates[sigp])

       card += "%-50s%-35s%-35s\n" % ("process", sigLine1, procLine) #"roomultipdf"
       card += "%-50s%-35s%-35s\n" % ("process", sigLine2, procNumbLine)
       card += "%-50s%-35s%-35s\n" % ("rate", sigLine3, rateLine) #signalYield[m].getVal(), nevents
       card += "-----------------------------------------------------------------------------------\n"

       for sysname, sysValue in syst.items():
              sysName = ""
              #### insert year in sysName if sys in uncorr, o
              if sysValue[0].startswith("shape") or sysValue[0] == 'lnN':
                     ##print syst[sysname]
                     if sysValue[-1] == "uncorr":
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
                     #print "\n\nhello\t", sysName, sysValue
                     if sysName.startswith("mischarge") and not ch.startswith("SR"):
                            continue
                     if "lumi" in sysName and "1718_" in sysName:
                            #sysName = sysName.replace("APV", "").replace("_2016", "").replace("_2017", "").replace("_2018", "")
                            sysName = sysName.replace("_2016M", "").replace("_2017", "").replace("_2018", "")
                     card += "%-35s%-35s" % (sysName, sysValue[0])
                     if sysValue[2] != 0.: #len(sysValue)>2:
                            if(sysValue[1]=="all" and len(sysValue)>2):
                                   card += "%-35s" % (sysValue[2]) * (len(processes) + len(sig))
                            elif(sysValue[1]=="QCD" and len(sysValue)>2):
                                   card += "%-35s" % (sysValue[2]) * (len(processes) + len(sig))
                            else:#(sysValue[1]=="Fake"):
                                   strsys = ""
                                   for sigp in sig:
                                       if not 'sig' in sysValue[1]:
                                           strsys += "%-35s" % ("-")
                                       else:
                                           strsys += "%-35s" % (sysValue[2])
                                   for proc in processes:
                                       if proc in sysValue[1]:
                                           strsys += "%-35s" % (sysValue[2])
                                       else:
                                           strsys += "%-35s" % ("-")

                                   card += strsys#"%-35s" % ("-") * (idx_p_tot) + "%-35s" % (sysValue[2]) + "%-35s" % ("-") * (len(processes) - (idx_p + 1)) 
                                          #print "%-35s" % ("-") * (idx_p_tot) + "%-35s" % (sysValue[2]) + "%-35s" % ("-") * (len(processes) - (idx_p + 1)) 

                     else:
                            #print "\n\n\nHELLO!\t" + sysName 
                            if (sysValue[1]=="all"):
                                   sysValue[1] = copy.deepcopy(processes)
                                   sysValue[1].append(sig)

                            hsysName =  "_" + sysname  
                            hsysNameUp = "_" + sysname + "Up"  
                            hsysNameDown = "_" + sysname + "Down" 
                            ##print "Applying syst on ", sysValue[1]
                            if ("sig" in sysValue[1]):
                                   for sigp in sig:
                                       sigplab = ""
                                       if sigp.startswith("quad_") or sigp.startswith("sm_lin_"):
                                           sigplab = sigp.replace("_F", "_c")
                                           torem = "_" + sigp.split("_")[-1]
                                           if "_F" in sigp and not ":" in opt.ls:
                                               sigplab = sigplab.replace(torem, "")
                                       else:
                                           sigplab = sigp
                     
                                       histoIntegral =  getRate(ch, sigplab, ifile)
                                       #print "histoUp:", ch, (sigplab + "_" + sysName + "Up")
                                       histoUpIntegral =  getRate(ch, sigplab + "_" + sysName + "Up", ifile)
                                       histoDownIntegral =  getRate(ch, sigplab + "_" + sysName + "Down", ifile)
                     
                                       #print "histoIntegral", histoIntegral
                                       #print "histoIntegralUp", histoUpIntegral
                                       #print "histoIntegralDown", histoDownIntegral
                                       if histoIntegral > 0. and histoUpIntegral > 0.:
                                           diffUp = (histoUpIntegral - histoIntegral)/histoIntegral
                                       else: 
                                           diffUp = 0.

                                       if histoIntegral > 0. and histoDownIntegral > 0.:
                                           diffDo = (histoDownIntegral - histoIntegral)/histoIntegral
                                       else:
                                           diffDo = 0.

                                       #print "diffUp:", diffUp
                                       #print "diffDo:", diffDo

                                       lnNUp = 1. + diffUp
                                       lnNDo = 1. + diffDo

                                       if lnNUp == 0:
                                           lnNUp = 1.
                                       if lnNDo==0:
                                            lnNDo = 1.


                                       if abs(lnNUp - 1.) < 5.e-4:
                                           lnNUp = 1.

                                       if abs(lnNDo - 1.) < 5.e-4:
                                           lnNDo = 1.

                                       #print "lnNUp:", lnNUp
                                       #print "lnNDo:", lnNDo

                                       if (abs(lnNUp - 1.) < 5.e-4 and abs(lnNDo - 1.) < 5.e-4) or (abs(lnNUp) < 0.1 or abs(lnNDo) < 0.1) or (abs(lnNUp) > 2. or abs(lnNDo) > 2.):
                                           card += "%-35s" % ( "-")
                                           print(("%-35s" % ( "-")))
                                       else:
                                           card += "%-35s" % (str(round(lnNUp, 4)) + "/" + str(round(lnNDo, 4)))
                                           print(("%-35s" % (str(round(lnNUp, 4)) + "/" + str(round(lnNDo, 4)))))

                            else:  
                                card += "%-35s" % ("-") * (len(sig))

                            for p in processes:
                                   if (p in sysValue[1]):
                                       histoIntegral =  getRate(ch, p, ifile)
                                       histoUpIntegral =  getRate(ch, p + "_" + sysName + "Up", ifile)
                                       histoDownIntegral =  getRate(ch, p + "_" + sysName + "Down", ifile)
                     
                                       if histoIntegral > 0. and histoUpIntegral > 0.:
                                           diffUp = (histoUpIntegral - histoIntegral)/histoIntegral
                                       else: 
                                           diffUp = 0.

                                       if histoIntegral > 0. and histoDownIntegral > 0.:
                                           diffDo = (histoDownIntegral - histoIntegral)/histoIntegral
                                       else:
                                           diffDo = 0.

                                       lnNUp = 1. + diffUp
                                       lnNDo = 1. + diffDo

                                       if lnNUp == 0:
                                           lnNUp = 1.
                                       if lnNDo==0:
                                            lnNDo = 1.

                                       if abs(lnNUp - 1.) < 5.e-4:
                                           lnNUp = 1.

                                       if abs(lnNDo - 1.) < 5.e-4:
                                           lnNDo = 1.


                                       if abs(lnNUp - 1.) < 5.e-4 and abs(lnNDo - 1.) < 5.e-4 or (abs(lnNUp) < 0.1 or abs(lnNDo) < 0.1) or (abs(lnNUp) > 2. or abs(lnNDo) > 2.):
                                           card += "%-35s" % ( "-")
                                       else:
                                           card += "%-35s" % (str(round(lnNUp, 4)) + "/" + str(round(lnNDo, 4)))


                                   else:  
                                          card += "%-35s" % ("-")

              elif(sysValue[0].startswith("shape")):
                     #print "sys shape named ", sysName, sysValue
                     if("mcstat" not in sysName and 'autoMCstat' not in sysName):

                            card += "%-35s%-35s" % (sysName, sysValue[0])
                          
                            #card += "%-35s     shape     " % (sysName)
                            if ("sig" in sysValue[1]):
                                   for sigp in sig:
                                          hasNominal = getRate(ch, sigp, ifile) > 0.
                                          hasUpShape = hasHist(ch, sigp + "_" + sysName + "Up", ifile)
                                          hasDownShape = hasHist(ch, sigp + "_" + sysName + "Down", ifile)
                                          if hasNominal and hasUpShape and hasDownShape:
                                                 card += "%-35s" % ( "1") 
                                          else:
                                                 card += "%-35s" % ( "-")
                          
                            else:
                                   card += "%-35s" % ("-") * (len(sig))
                          
                            for p in processes:
                                   if p not in sysValue[1]:
                                          card += "%-35s" % ( "-") 
                                          continue
                                   isbogussys = False 
                                   if((getRate(ch, p+"_"+sysName+"Up", ifile)<0.001 or getRate(ch, p+"_"+sysName+"Down", ifile)<0.001)) or getRate(ch, p, ifile) <= 0.:
                                          isbogussys = True

                                   if ((getRate(ch, p, ifile) > 0.) and not isbogussys): 
                                          card += "%-35s" % ( "1") 

                                   elif isbogussys: 
                                          card += "%-35s" % ( "-")

                                          print(p, "bogus", sysname)
                     elif("mcstat" in sysName):
                            # CAMBIARE NOME DELLA SYST                     #here
                            for samp in sysValue[1]:
                                   #sampName = ""
                                   sampName = []
                                   line = ""
                                   if (samp == "sig" or samp == "Sig"): 
                                          for sigp in sig:
                                                 line = "%-35s" % ( "1") 
                                                 sampName.append(sigp)
                                          
                                          line += "%-35s" % ("-") * (len(processes)) 
                                                 
                                   elif(mode != "template"):
                                          line = "%-35s" % ( "-") 
                                          lineProc = ["%-35s" % ( "-") for x in range (len(processes))]
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
                                   for i in range(hist.GetNbinsX()):
                                          sysName = "mcstat_%s_%s_bin%d      "  % (ch, sampNameLine, i+1)
                                          card += "%-35s   shape   " % (sysName)
                                          card += line
                                          card += "\n"        
              if('autoMCstat' in sysName):
                  if len(sig) > 1:
                      card += "%-35s%-35s%-35d%-35d " % (ch, "autoMCStats", mcstatt, 0)
                  else:
                      card += "%-35s%-35s%-35d%-35d " % (ch, "autoMCStats", mcstatt, 0)
              card += "\n"
       # End for loop on syst unc.       
       card += "\n"
       for k, v in list(rateParams.items()):
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
                                          card += "%-35s%-35s%-35s%-35s%-35d" % (k, "rateParam", ch, v.bkg, 1)
                                   elif ('ele' in k and 'ele' in ch):
                                          card += "%-35s%-35s%-35s%-35s%-35d" % (k, "rateParam", ch, v.bkg, 1)
                                   else:
                                          sameyear= ( ("2016" in k and "2016" in ch) or ("2017" in k and "2017" in ch) or ("2018" in k and "2018" in ch))
                                          if(sameyear): card += "%-35s%-35s%-35s%-35s%-35d" % (k, "rateParam", ch, v.bkg, 1)                                   
                            else:
                                   card += "%-35s%-35s%-35s%-35s%-35d" % (k, "rateParam", ch, v.bkg, 1)
                            card += "\n"

       if not os.path.isdir(carddir):
              os.system('mkdir -p ' + carddir)

       outname = "" + carddir
       for sigp in sig:
              outname += sigp + "_"
       outname += ch + "_" + mode + ".txt"
       cardfile = open(outname, 'w')
       cardfile.write(card)
       cardfile.close()
       return card


#*******************************************************#
#                                                       #
#                 Datacard for LS                       #
#                                                       #
#*******************************************************#
def getCardLS(incoeff, ch, ifilename, outdir, mode = "histo"):#, unblind = False):
       year = ch.split("_")[-1]

       ops = incoeff.split(":")
       setpiecs = []
       for op in ops:
              if len(op.split("_")) > 1:
                     setpiecs.append(("_")+op.split("_")[-1])
       coeff = copy.deepcopy(incoeff)
       setpiecs.reverse()
       if ":" in incoeff or incoeff.startswith("F"):# or ":F" in incoeff:
              for setpiec in setpiecs:
                     coeff = coeff.replace(setpiec, "")

       lssamp = []
       for name, coll in list(lssamples_1D.items()):
              for nout, nin in list(coll.items()):
                     lssamp.append(nout)

       try:
              ifile = ROOT.TFile.Open(ifilename)
       except IOError:
              print("Cannot open ", ifilename)
       else:
              ifile.cd()

       workdir_ = ifilename.split("/")[:-1]
       WORKDIR = "/".join(workdir_) + "/"
       dircoeff = ""
       dircoeff = coeff
       carddir = outdir+  "/"  + dircoeff + "/"

       sig = lssamp
       hist_filename = "../shapes/"+ifilename.split("/")[-1]
       hist = []
       for sigp in sig:
              hist.append(getHist(ch, sigp, ifile))

       rates = OrderedDict()
       procLine = ""
       procNumbLine = ""
       rateLine = ""
       binString = ""

       if True:
              i = 1
              bkgrate = 0
              nproc=(len(processes))
              for p in processes:
                     rates[p] = getRate(ch, p, ifile)
                     bkgrate = rates[p]
                     procNumbLine += ("%-35s") % (i)
                     procLine += ("%-35s") % (p)
                     rateLine += ("%-35f") % (bkgrate)
                     i+=1
              binString += (("%-35s") % (ch) ) * (nproc + len(lssamp))

       if True:
              rates["data_obs"] = getRate(ch, "data_obs", ifile)
       for sgs in lssamp:
              torem = "_" + sgs.split("_")[-1]
              sgslab = ""
              if sgs.startswith("quad_") or sgs.startswith("sm_lin_"):
                     sgslab = sgs.replace("_F", "_c")
                     if "_F" in sgs and not ":" in opt.ls:
                         sgslab = sgslab.replace(torem, "")
                         
              else:
                     sgslab = sgs
              rates[sgs] = getRate(ch, sgslab, ifile)

       card  = "imax 1 number of channels \n"
       card += "jmax * number of backgrounds \n"
       card += "kmax * number of nuisance parameters\n"
       card += "-----------------------------------------------------------------------------------\n"

       if True:  
              card += "shapes   *      *   %s    %s    %s\n" % (hist_filename, "$CHANNEL/$PROCESS", "$CHANNEL/$PROCESS_$SYSTEMATIC")
              card += "shapes   data_obs      *   %s    %s\n" % (hist_filename, "$CHANNEL/$PROCESS")
       card += "-----------------------------------------------------------------------------------\n"
       card += "bin               %s\n" % ch

       card += "observation       %0.d\n" % (rates["data_obs"])
       card += "-----------------------------------------------------------------------------------\n"
       card += "%-35s%-35s%-35s\n" % ("bin", "", binString)
       procnameString = "%-35s%-35s" % ("process", "")
       procidxString = "%-35s%-35s" % ("process", "")
       rateString = "%-35s%-35s" % ("rate", "")
       
       for sidx, sgs in enumerate(lssamp):
              if sgs.startswith("quad_") or sgs.startswith("sm_lin_"):
                     sgslab = sgs.replace("_F", "_c")
                     if "_F" in sgs and not ":" in opt.ls:
                         sgslab = sgslab.replace(torem, "")
              else:
                     sgslab = sgs
              
              procnameString += "%-35s" % sgslab
              procidxString += "%-35s" % (str(-len(lssamp)+sidx+1))
              rateString += "%-35.6f" % (rates[sgs])

       procnameString += "%-35s\n" % (procLine)
       procidxString += "%-35s\n" % (procNumbLine)
       rateString += "%-35s\n" % (rateLine)

       card += procnameString + procidxString + rateString

       card += "-----------------------------------------------------------------------------------\n"

       for sysname,sysValue  in syst.items():
              sysName = ""
              if sysValue[0].startswith("shape") or sysValue[0] == 'lnN':
                     if sysValue[-1] == "uncorr":
                            sysName = sysname + "_" + str(year)
                     else:
                            sysName = sysname
              else:
                     sysName = sysname

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
                     if "lumi" in sysName and "1718_" in sysName:
                            sysName = sysName.replace("_2016M", "").replace("_2017", "").replace("_2018", "")
                     card += "%-35s%-35s" % (sysName, sysValue[0])
                     if sysValue[2] != 0.:
                            if(sysValue[1]=="all"):
                                   card += "%-35s" % (sysValue[2]) * (len(lssamp) + len(processes))
                            elif(sysValue[1]=="QCD" and len(sysValue)>2):
                                   card += "%-35s" % (sysValue[2]) * (len(lssamp) + len(processes))
                            else:
                                   strsys = ""
                                   for sigp in sig:
                                       if not 'sig' in sysValue[1]:
                                           strsys += "%-35s" % ("-")
                                       else:
                                           strsys += "%-35s" % (sysValue[2])
                                   for proc in processes:
                                       if proc in sysValue[1]:
                                           strsys += "%-35s" % (sysValue[2])
                                       else:
                                           strsys += "%-35s" % ("-")

                                   card += strsys
                     else:
                            if (sysValue[1]=="all"):
                                   sysValue[1] = copy.deepcopy(processes)
                                   sysValue[1].append(sig)

                            hsysName =  "_" + sysname  
                            hsysNameUp = "_" + sysname + "Up"  
                            hsysNameDown = "_" + sysname + "Down" 
                            if ("sig" in sysValue[1]):
                                   for sigp in sig:
                                       sigplab = ""
                                       if sigp.startswith("quad_") or sigp.startswith("sm_lin_"):
                                           sigplab = sigp.replace("_F", "_c")
                                           torem = "_" + sigp.split("_")[-1]
                                           if "_F" in sigp and not ":" in opt.ls:
                                               sigplab = sigplab.replace(torem, "")
                                       else:
                                           sigplab = sigp
                     
                                       histoIntegral =  getRate(ch, sigplab, ifile)
                                       histoUpIntegral =  getRate(ch, sigplab + "_" + sysName + "Up", ifile)
                                       histoDownIntegral =  getRate(ch, sigplab + "_" + sysName + "Down", ifile)
                     
                                       if histoIntegral > 0. and histoUpIntegral > 0.:
                                           diffUp = (histoUpIntegral - histoIntegral)/histoIntegral
                                       else: 
                                           diffUp = 0.

                                       if histoIntegral > 0. and histoDownIntegral > 0.:
                                           diffDo = (histoDownIntegral - histoIntegral)/histoIntegral
                                       else:
                                           diffDo = 0.

                                       lnNUp = 1. + diffUp
                                       lnNDo = 1. + diffDo

                                       if lnNUp == 0:
                                           lnNUp = 1.
                                       if lnNDo==0:
                                            lnNDo = 1.

                                       if abs(lnNUp - 1.) < 5.e-4:
                                           lnNUp = 1.

                                       if abs(lnNDo - 1.) < 5.e-4:
                                           lnNDo = 1.

                                       if abs(lnNUp - 1.) < 5.e-4 and abs(lnNDo - 1.) < 5.e-4 or (abs(lnNUp) < 0.1 or abs(lnNDo) < 0.1) or (abs(lnNUp) > 2. or abs(lnNDo) > 2.):
                                           card += "%-35s" % ( "-")
                                       else:
                                           card += "%-35s" % (str(round(lnNUp, 4)) + "/" + str(round(lnNDo, 4)))

                            else:  
                                card += "%-35s" % ("-") * (len(sig))

                            for p in processes:
                                   if (p in sysValue[1]):
                                       histoIntegral =  getRate(ch, p, ifile)
                                       histoUpIntegral =  getRate(ch, p + "_" + sysName + "Up", ifile)
                                       histoDownIntegral =  getRate(ch, p + "_" + sysName + "Down", ifile)
                     
                                       if histoIntegral > 0. and histoUpIntegral > 0.:
                                           diffUp = (histoUpIntegral - histoIntegral)/histoIntegral
                                       else: 
                                           diffUp = 0.

                                       if histoIntegral > 0. and histoDownIntegral > 0.:
                                           diffDo = (histoDownIntegral - histoIntegral)/histoIntegral
                                       else:
                                           diffDo = 0.

                                       lnNUp = 1. + diffUp
                                       lnNDo = 1. + diffDo

                                       if lnNUp == 0:
                                           lnNUp = 1.
                                       if lnNDo==0:
                                            lnNDo = 1.

                                       if abs(lnNUp - 1.) < 5.e-4:
                                           lnNUp = 1.

                                       if abs(lnNDo - 1.) < 5.e-4:
                                           lnNDo = 1.

                                       if abs(lnNUp - 1.) < 5.e-4 and abs(lnNDo - 1.) < 5.e-4 or (abs(lnNUp) < 0.1 or abs(lnNDo) < 0.1) or (abs(lnNUp) > 2. or abs(lnNDo) > 2.):
                                           card += "%-35s" % ( "-")
                                       else:
                                           card += "%-35s" % (str(round(lnNUp, 4)) + "/" + str(round(lnNDo, 4)))


                                   else:  
                                          card += "%-35s" % ("-")
              elif(sysValue[0].startswith("shape")):
                     if("mcstat" not in sysName and 'autoMCstat' not in sysName):
                            card += "%-35s%-35s" % (sysName, sysValue[0])
                            if ("sig" in sysValue[1]):
                                   for sigp in sig:
                                          sigplab = ""
                                          if sigp.startswith("quad_") or sigp.startswith("sm_lin_"):
                                                 sigplab = sigp.replace("_F", "_c")
                                                 torem = "_" + sigp.split("_")[-1]
                                                 if "_F" in sigp and not ":" in opt.ls:
                                                     sigplab = sigplab.replace(torem, "")
                                          else:
                                                 sigplab = sigp

                                          hasNominal = getRate(ch, sigplab, ifile) > 0.
                                          hasUpShape = hasHist(ch, sigplab + "_" + sysName + "Up", ifile)
                                          hasDownShape = hasHist(ch, sigplab + "_" + sysName + "Down", ifile)
                                          if hasNominal and hasUpShape and hasDownShape:
                                                 card += "%-35s" % ( "1")
                                          else:
                                                 card += "%-35s" % ( "-") 
                            else:
                                   card += "%-35s" % ("-") * (len(sig))

                            for p in processes:
                                   if p not in sysValue[1]:
                                          card += "%-35s" % ( "-") 
                                          continue
                                   isbogussys = False 
                                   if((getRate(ch, p+"_"+sysName+"Up", ifile)<0.0001 or getRate(ch, p+"_"+sysName+"Down", ifile)<0.0001)) or getRate(ch, p, ifile) <= 0.:
                                          isbogussys = True

                                   if ((getRate(ch, p, ifile) > 0.) and not isbogussys): 
                                          card += "%-35s" % ( "1") 
                                   elif isbogussys:
                                          card += "%-35s" % ( "-") 

                     elif("mcstat" in sysName):
                            for samp in sysValue[1]:
                                   sampName = []
                                   line = ""
                                   if (samp == "sig" or samp == "Sig"): 
                                          for sigp in sig:
                                                 line = "%-35s" % ( "1") 
                                                 sampName.append(sig)
                                   elif(mode != "template"):
                                          line = "%-35s" % ( "-") 
                                          lineProc = ["%-35s" % ( "-") for x in range (len(processes))]
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

                                   for i in range(hist.GetNbinsX()):
                                          sysName = "mcstat_%s_%s_bin%d      "  % (ch, sampNameLine, i+1)
                                          card += "%-35s%-35s" % (sysName, sysValue[0])
                                          card += line
                                          card += "\n"        
              if('autoMCstat' in sysName):
                     card += "%-35s%-35s%-35d%-35d\n " % (ch, "autoMCStats", mcstatt, 0)
              card += "\n"

       for k, v in list(rateParams.items()):
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
                                          card += "%-35s%-35s%-35s%-35s%-35d\n" % (k, "rateParam", ch, v.bkg, 1)
                                   elif ('ele' in k and 'ele' in ch):
                                          card += "%-35s%-35s%-35s%-35s%-35d\n" % (k, "rateParam", ch, v.bkg, 1)
                                   else:
                                          sameyear= ( ("2016" in k and "2016" in ch) or ("2017" in k and "2017" in ch) or ("2018" in k and "2018" in ch))
                                          if(sameyear): card += "%-35s%-35s%-35s%-35s%-35d\n" % (k, "rateParam", ch, v.bkg, 1)                                   
                            else:
                                   card += "%-35s%-35s%-35s%-35s%-35d\n" % (k, "rateParam", ch, v.bkg, 1)
                            card += "\n"

       if not os.path.isdir(outdir): 
              os.system('mkdir ' +outdir)
       if not os.path.isdir(outdir + "/" + dircoeff): 
              os.system('mkdir ' +outdir + "/" + dircoeff)

       outname =  "%s%s_%s_%s.txt" % (carddir, coeff, ch, mode)
       cardfile = open(outname, 'w')
       cardfile.write(card)
       cardfile.close()

       return card


ifilename = opt.ifile
outdirr = opt.outdir

if not os.path.exists(outdirr):
    os.system("mkdir -p " + outdirr)

mode = opt.mode
wilson = opt.ls

if opt.ch != "all": 
    ch_clean = opt.ch.replace(" ", "")
    channels = ch_clean.split(",")

signals = []

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

try:
    ifile = ROOT.TFile.Open(ifilename)
except IOError:
    print("Cannot open ", ifilename)
else:
    pass

for y in years:
    channels_years = [ch + '_' + y for ch in channels ]
    for ch in channels_years:
        if wilson != "":
            getCardLS(wilson, ch, ifilename, outdirr, mode)
        else:
            getCard(signals, ch, ifilename, outdirr, mode)