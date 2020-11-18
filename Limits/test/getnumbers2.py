import ROOT
import os
import optparse


usage = 'usage: %prog [--cat N]'
parser = optparse.OptionParser(usage)
parser.add_option("-m","--mode",dest="mode",type="string",default="gfr",help="mode: g(generate), f(fit) r(read) F(fitparallel: not compatible with r)")
parser.add_option("-s","--suffix",dest="suffix",type="string",default="",help="suffix for the files")
parser.add_option("-d","--datacarddir",dest="datacarddir",type="string",default="outstatNovFull",help="datacard directory")
(opt, args) = parser.parse_args()

masses = [700,1100,1500]
signifs = ["","_1s","_limit","_3s","_5s"]
r_in = {700:[0,10,30,75,120], 1100:[0,5,10,35,50],1500:[0,5,18,35,75]} 

pulls=[[-100 for m in xrange(len(signifs))] for r in xrange(len(masses))]
sigmas=[[-100 for m in xrange(len(signifs))] for r in xrange(len(masses))]


mode= opt.mode


generate=False

fit=False
parallelfit=False

read=False
saveplots=False

if "g" in mode:
    generate=True
if "f" in mode:
    fit=True
if "F" in mode:
    fit=True
    parallelfit=True
if "r" in mode:
    read=True
if "R" in mode:
    read=True
    saveplots=True
datacarddir="outstatNovtestwFull"
datacarddir=opt.datacarddir

suffix=""
suffix="_18_testw"
suffix="_testw"
suffix="_fulltestw"

suffix=opt.suffix

for mi in xrange(0,len(masses)):
    m = masses[mi]            
    for ri in xrange(0,len(r_in[m])):
        r=r_in[m][ri]
        if generate:
            commandgen=" combine -M GenerateOnly "+datacarddir+"/combination_Tprime"+str(m)+".txt  --toysFrequentist --bypassFrequentistFit -t 300 --saveToys --expectSignal "+str(r)+" -n r_"+str(r)+"_"+str(m)+"_toys"+suffix+" --rMax 150 --rMin -1000"
            print commandgen
            os.system(commandgen)
        if fit: 
            commandfit="combine -M FitDiagnostics "+datacarddir+"/combination_Tprime"+str(m)+".txt --skipBOnlyFit -t 300 -n r_"+str(r)+"_"+str(m)+"_toys"+suffix+" --toysFile higgsCombiner_"+str(r)+"_"+str(m)+"_toys"+suffix+".GenerateOnly.mH120.123456.root --rMax 150 --rMin -100"
            if(parallelfit):commandfit = commandfit+" &"
            print commandfit
            os.system(commandfit)
        if(read):
            f = ROOT.TFile.Open("fitDiagnosticsr_"+str(r)+"_"+str(m)+"_toys"+suffix+".root")
            tmp=f.Get("tree_fit_sb").Clone()
            h=ROOT.TH1F("h","h",20,-4,4)
            tmp.Project("h",("(r-"+str(r)+")/rErr"))
            print "m:  ", m ," r:  ", r, "  pull  ", h.GetMean() 
            if(saveplots):
                c1=ROOT.TCanvas()
                h.SetTitle("(r-"+str(r)+")/rErr")
                h.Draw()
                
                c1.SaveAs("pulls_"+str(r)+"_"+str(m)+suffix+".png")
            pulls[mi][ri]=h.GetMean()
            sigmas[mi][ri]=h.GetRMS()

if(read):
    for si in xrange(0,len(signifs)):
        #print " signif ", signifs[si]  
        pullsi= "pulls"+signifs[si]+"=[" 
        sigmasi= "sigmas"+signifs[si]+"=[" 
        for mi in xrange(0,len(masses)):
            m = masses[mi]            
            #print " mass ",m, " pull ", pulls[mi][si] 
            pullsi += str(pulls[mi][si])+","
            sigmasi += str(sigmas[mi][si])+","
        pullsi=pullsi[:-1]
        pullsi+="]"
        sigmasi=sigmasi[:-1]
        sigmasi+="]"
        print pullsi
        print sigmasi
