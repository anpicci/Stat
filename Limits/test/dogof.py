import ROOT
import os
import optparse


usage = 'usage: %prog [--cat N]'
parser = optparse.OptionParser(usage)
parser.add_option("-s","--suffix",dest="suffix",type="string",default="full",help="suffix for the files")
parser.add_option("-d","--datacarddir",dest="datacarddir",type="string",default="outdduncNovtestwFull",help="datacard directory")
parser.add_option("-D","--datacard",dest="datacard",type="string",default="",help="datacard")
parser.add_option("-o","--obs",dest="obs",action="store_true",default=False,help="run on unblinded data")
parser.add_option("-n","--npseudoexperiments",dest="npe",type="string",default="100",help="number of pseudoexperiments to throw")
(opt, args) = parser.parse_args()

masses = [700]
obs= "-t -1"
if opt.obs:
    obs=""
datacarddir= opt.datacarddir
suffix=opt.suffix
s=suffix

dryrun=True
dryrun=False


for mass in masses:
    m = str(mass)
    nseeds= int(int(opt.npe)/100)
    print nseeds
    datacard=datacarddir+"/"+opt.datacard+"_hist.txt"

    commanddata=" combine -M GoodnessOfFit "+datacard+"  --algo=saturated --saveWorkspace --saveToys --toysFrequentist --bypassFrequentistFit -n gof_data_"+s+" --rMax 250 --rMin -250"
    print "commanddata ",commanddata
    if not dryrun:
        os.system(commanddata)

    for step in xrange(0, nseeds):
        npart=100
        seed=str(step)
        commandmc=" combine -M GoodnessOfFit "+datacard+" --algo=saturated --saveWorkspace --saveToys -t "+str(npart)+" --toysFrequentist --bypassFrequentistFit -n gof_"+s+ " -s "+seed+" --rMax 250 --rMin -250"
        
    
        print "commandmc ",commandmc
        if not dryrun:
            os.system(commandmc)
    #namemerge= "gof_merge"+s+".root"
    #commandmerge="hadd -f "+namemerge +" higgsCombinegof_"+s+".GoodnessOfFit.mH120.*.root"
    #print commandmerge
    #if not dryrun:
        #os.system(commandmerge)
#combine -M GoodnessOfFit outdduncxcheckNovtestwFull/TprimeLH1700/TprimeLH1700_hist.txt --algo=saturated --saveWorkspace --saveToys -t 500 --toysFrequentist --fixedSignalStrength=0 --bypassFrequentistFit -n gof_500_Full
#combine -M GoodnessOfFit outdduncxcheckNovtestwFull/TprimeLH1700/TprimeLH1700_hist.txt --algo=saturated --saveWorkspace --fixedSignalStrength=0 -n gof_data_Full
