import ROOT
import os
import optparse
ROOT.gROOT.SetBatch()

usage = 'usage: %prog [--cat N]'
parser = optparse.OptionParser(usage)
parser.add_option("-m","--mode",dest="mode",type="string",default="gfr",help="mode: g(generate), f(fit) r(read) F(fitparallel: not compatible with r)")
parser.add_option("-s","--suffix",dest="suffix",type="string",default="",help="suffix for the files")
parser.add_option("-d","--datacarddir",dest="datacarddir",type="string",default="outstatNovFull",help="datacard directory")
(opt, args) = parser.parse_args()

mass_points = ['WP_M2000W20_RH', 'WP_M4000W40_RH', 'WP_M6000W60_RH']
signifs = ["","_1s","_limit","_3s","_5s"]
r_in = {'WP_M2000W20_RH':[0, 1, 3, 5, 10], 'WP_M4000W40_RH':[0, 1, 3, 5, 10], 'WP_M6000W60_RH':[0, 1, 5, 10, 20]}

ntoys = '200'
pulls=[[-100 for m in xrange(len(signifs))] for r in xrange(len(mass_points))]
sigmas=[[-100 for m in xrange(len(signifs))] for r in xrange(len(mass_points))]
pulls_fit=[[-100 for m in xrange(len(signifs))] for r in xrange(len(mass_points))]
sigmas_fit=[[-100 for m in xrange(len(signifs))] for r in xrange(len(mass_points))]
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
datacarddir=opt.datacarddir
folder = "fit_fullrun2_DD_topmass120_220"
folder = "fit_2018_DD_topmass120_220_noMCstats"
folder = "fit_v15_fullrun2_DD_DDFitWJetsTT_MttST"
folder = 'fit_v16_fullrun2_DD_DDFitWJetsTT_MttST'
folder = 'SR_all_comb_09Mar21_plot_newfit_07Mar21_split_rateparam'


ROOT.gStyle.SetOptFit(1)
gen_options = "--saveToys --toysFrequentist --bypassFrequentistFit "
suffix = ""
suffix = opt.suffix
for mi in xrange(0, len(mass_points)):
    mass_point = mass_points[mi]
    for ri in xrange(0, len(r_in[mass_point])):
        r = r_in[mass_point][ri]
        print r
        rmin = str(r - 10)
        print rmin
        rmax = str(r + 10)
        print rmax
        if generate:
            commandgen=" combine -M GenerateOnly " + folder + "/" + mass_point + "/" + mass_point + "_hist.txt -t " + ntoys + " " + gen_options + " --expectSignal " + str(r) + " -n r_" + str(r) + "_" + mass_point + "_toys" + suffix + " --rMax " + rmax + " --rMin " + rmin
            print commandgen
            os.system(commandgen)
        if fit: 
            commandfit="combine -M FitDiagnostics " + folder + "/" + mass_point + "/" + mass_point + "_hist.txt  --skipBOnlyFit -t " + ntoys + " -n r_" + str(r) + "_" + mass_point + "_toys" + suffix + " --toysFile higgsCombiner_" + str(r) + "_" + str(mass_point) + "_toys" + suffix + ".GenerateOnly.mH120.123456.root --rMax " + rmax + " --rMin " + rmin
            if(parallelfit):commandfit = commandfit+" &"
            print commandfit
            os.system(commandfit)
        if(read):
            f = ROOT.TFile.Open("fitDiagnosticsr_"+str(r)+"_"+mass_point+"_toys"+suffix+".root")
            tmp=f.Get("tree_fit_sb").Clone()
            h=ROOT.TH1F("h","h",20,-4,4)
            tmp.Project("h",("(r-"+str(r)+")/rErr"), "fit_status==0")
            print "m:  ", mass_point ," r:  ", r, "  pull  ", h.GetMean() 
            func = ROOT.TF1("gaus", "gaus(0)")
            if(saveplots):
                c1=ROOT.TCanvas()
                h.SetTitle("(r-"+str(r)+")/rErr")
                h.Fit(func, "", "", -2, 2)
                h.Draw("E")
                func.Draw("SAME")
                c1.Update()
                c1.SaveAs("pulls_"+str(r)+"_"+mass_point+suffix+"_v16.png")
            pulls_fit[mi][ri] = func.GetParameter(1)
            sigmas_fit[mi][ri] = func.GetParameter(2)
            pulls[mi][ri] = h.GetMean()
            sigmas[mi][ri] = h.GetRMS()

if(read):
    for si in xrange(0,len(signifs)):
        #print " signif ", signifs[si]  
        pullsi= "pulls"+signifs[si]+"=[" 
        sigmasi= "sigmas"+signifs[si]+"=[" 
        pulls_fiti= "pulls_fit"+signifs[si]+"=[" 
        sigmas_fiti= "sigmas_fit"+signifs[si]+"=[" 
        for mi in xrange(0,len(mass_points)):
            m = mass_points[mi]            
            #print " mass ",m, " pull ", pulls[mi][si] 
            pullsi += str(pulls[mi][si])+","
            sigmasi += str(sigmas[mi][si])+","
            pulls_fiti += str(pulls_fit[mi][si])+","
            sigmas_fiti += str(sigmas_fit[mi][si])+","
        pullsi=pullsi[:-1]
        pullsi+="]"
        sigmasi=sigmasi[:-1]
        sigmasi+="]"
        pulls_fiti=pulls_fiti[:-1]
        pulls_fiti+="]"
        sigmas_fiti=sigmas_fiti[:-1]
        sigmas_fiti+="]"
        print pullsi
        print sigmasi
        print pulls_fiti
        print sigmas_fiti
