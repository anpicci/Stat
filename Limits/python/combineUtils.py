import os
import subprocess
#from Stat.Limits.settings import *
import copy
from datetime import datetime

def runCombine(cmdStr, logFile):
    "run combine for a specific case"
    #print os.getcwd()
    #print cmd
    #writer = open(logFile, 'w') 
    #process = subprocess.call(cmd, shell = True, stdout=writer)
    #logFile = logfile.replace(".log", datetime.now().time().strftime("%H%M%S%f") + ".log")
    print cmdStr + " 2>&1 | tee " + logFile
    os.system(cmdStr + " 2>&1 | tee " + logFile)
    return

def runSinglePointVBS_sign(path_, model, categories, method, runSingleCat, years, UseHybridNew, unblind):
    modelname = ""
    for ids, sigp in enumerate(model):
        if not sigp.startswith("WpWp"):
            modelname += "VBS_SSWW_" + sigp
        else:
            modelname += sigp
        if ids < len(model) - 1:
            modelname += "_"

    print "evaluate limit for model ", model
    path = "" + path_ + "/" + modelname
    print "categories:", categories
    
    if(os.path.exists(path)):
        os.chdir(path)
        
        extraoption = " --cminDefaultMinimizerStrategy 0 --expectSignal 1 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT "
        if not unblind:
            extraoption += " -t -1 "
        cmd = "combineCards.py "
        for year in years:
            for cat in categories:
                cmd += cat+year+"=%s_%s_%s_%s.txt " %(modelname, cat, year, method)
        cmd += "> %s_%s.txt" % (modelname, method)
        print cmd
        os.system(cmd)

        runCombine("combine -M Significance " + extraoption + " " + modelname + "_" + method + ".txt -n " + modelname, "significance_" + modelname + "_" + method + ".log")

        if not unblind:
            niter = 20
        else:
            niter = 30
        if UseHybridNew:
            for idhn in range(niter):
                runCombine("combine -M HybridNew " + modelname + "_" + method + ".txt --LHCmode LHC-significance --saveToys --saveHybridResult --fullBToys " + extraoption + " -T 50 -i 50 -s -1 --fork 20 -H AsymptoticLimits --rMin -4 -n " + modelname + "_hybrid", "hybrid_" + modelname + "_" + method + "_" + str(idhn) + ".log")
            os.system("hadd -f merged_HybridNew.root higgsCombineWpWpJJ_EWK_hybrid.HybridNew.mH120*root")
            runCombine("combine -M HybridNew " + modelname + "_" + method + ".txt --LHCmode LHC-significance --readHybridResult --toysFile=merged_HybridNew.root " + extraoption + " --rMin -4 -n " + modelname + "_hybrid_total", "hybrid_total_" + modelname + "_" + method + ".log")
        #runCombine("combine -M FitDiagnostics "+ modelname + "_" + method + ".txt --expectSignal=1 --plots --saveShapes --saveWithUncertainties", "fitDiag_VBS_SSWW_" + modelname + "_" + method + ".log")
    
        os.chdir("..")
    
def runSinglePointVBS_EWvsQCD(path_, model, categories, method, runSingleCat, years, unblind):
    maindir = os.getcwd() + "/"
    modelname = ""
    optionalsSM = " --algo=grid --points=50000 --cminDefaultMinimizerStrategy=0 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT "#--setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND" #--autoBoundsPOIs * --autoRange 3" #--fastScan"
    if not unblind:
        optionalsSM += " -t -1 "
    print "model", model
    modelname = model.replace(":", "_")
    #print "evaluate limit for model ", model
    path = "" + path_ + "/" + modelname
    vbsmodels = model.split(":")
    print "hello", path
    if(os.path.exists(path)):
        print "ok i'm in the directory"
        os.chdir(path)
        #print "We are in the right folder ",  len(categories)
        extraoption=""
        
        if True:
            if True:
                cmd = "combineCards.py "
                for year in years:
                    for cat in categories:
                        cmd += cat+year+"=%s_%s_%s_%s.txt " %(modelname, cat, year, method)
                cmd += "> %s_%s.txt" % (modelname, method)
                #print cmd    
                os.system(cmd)

                global_dc = modelname + "_" + str(method) + ".txt" 
                rootdc = modelname + "_" + method+ ".root"
    
                cmd = "text2workspace.py "
                cmd += "-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel "
                modComb = ""
                intervalstr = ""
                valuestr = ""
                for idvm, vbsmodel in enumerate(vbsmodels):
                    if "_DNN_" in path_:
                        cmd += "--PO 'map=.*/" + vbsmodel + ":k_" + vbsmodel.split("_")[-1] + "[1,-100.0,100.0]' "
                    else:
                        cmd += "--PO 'map=.*/" + vbsmodel + ":k_" + vbsmodel.split("_")[-1] + "[1,-200.0,200.0]' "
                    if idvm > 0:
                        modComb += ","
                        intervalstr += ":"
                        valuestr += ","
                    modComb += "k_" + vbsmodel.split("_")[-1]
                    if "_DNN_" in path_:
                        intervalstr += "k_" + vbsmodel.split("_")[-1] + "=-100.0,100.0"
                    else:
                        intervalstr += "k_" + vbsmodel.split("_")[-1] + "=-200.0,200.0"
                    valuestr += "k_" + vbsmodel.split("_")[-1] + "=1" 
                cmd += global_dc + " -o " + rootdc 
                print cmd
                os.system(cmd)
                os.system("rm higgsCombineTest*root")
                cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/parallelScan.py -j 100 " + rootdc + " -M MultiDimFit -m 125 --redefineSignalPOIs " + modComb + " --setParameterRanges " + intervalstr + " --autoBoundsPOIs " + modComb + " " + optionalsSM + " --setParameters " + valuestr# + " --freezeParameters r --setParameters r=1"
                cmd += " ; hadd -f higgsCombineTest.MultiDimFit.mH125.root higgsCombineTest.*.MultiDimFit.mH125.root"
            
                print cmd
                runCombine(cmd, "ls_k_" + model[0] + "_" + method + ".log")
                
                cmd = "python " + maindir + "drawLS.py --in0 higgsCombineTest.MultiDimFit.mH125.root --in1 higgsCombineTest.MultiDimFit.mH125.root --coeff EWK:QCD " 
                cmd += " --2D"
                cmd += " --year " 
                for year in years:
                    cmd += year
                    if year != years[-1]:
                        cmd += "," 
                print cmd
                os.system(cmd)                
                os.system("rm higgsCombineTest.*.MultiDimFit.mH125.root")
                
def runSinglePointVBS_AL(path_, model, categories, method, runSingleCat, years, unblind):
    print "evaluate limit for VBS_SSWW_" + model
    path = ("%s/VBS_SSWW_%s" % (path_, model) )
    #print "==>path: ", path
    #print os.path.exists(path)
    if(os.path.exists(path)):
        #print "ok i'm in the directory"
        os.chdir(path)
        #print "We are in the right folder ",  len(categories)
        extraoption=""
        if not unblind:
            extraoption += " -t -1 "
        if True:
            if True:
                cmd = "combineCards.py "
                for year in years:
                    for cat in categories:
                        cmd += cat+year+"=VBS_SSWW_%s_%s_%s_%s.txt " %(model, cat, year, method)
                cmd += "> VBS_SSWW_%s_%s.txt" % (model, method)
                #print cmd
                os.system(cmd)
                #runCombine("combine -M Significance "+extraoption+" -n VBS_SSWW_" + modelname + "_" + method + " VBS_SSWW_" + modelname + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + method + ".log")
                #runCombine("combine -M FitDiagnostics "+extraoption+" -n VBS_SSWW_" + modelname + "_" + method + " VBS_SSWW_" + modelname + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + method + ".log")

        os.chdir("..")

def runSinglePointVBS_LS(path_, models, categories, method, runSingleCat, years, profile, unblind):
    algostring = " --algo=grid  --points "
    if ":" in models and not profile:
        algostring += "1000000 "
        #algostring += "10 "
        #algostring += " 50000 "
    elif ":" in models and profile:
        algostring +=     "  10000 "
        #algostring +=     "  10 "
    else:
        algostring +=     "  10000 "
        #algostring +=     "  10 "

    optionals = " --alignEdges=1 --cminDefaultMinimizerStrategy=0 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT" #--fastScan" #--setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --fastScan" #--autoBoundsPOIs * --autoRange 3" 
    if not unblind:
        optionals += " -t -1 "
    if not ":" in models or (":" in models and profile):
        optionals += "--setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND "#--fastScan" #--autoBoundsPOIs * --autoRange 3" 
    print "Performing LikelihoodScan for operator ", models
    dirmodel = ""
    coeffs = models.split(":")
    setpiecs = []
    for idc, coeff in enumerate(coeffs):
        if len(coeff.split("_")) > 1:
            setpiecs.append(("_")+coeff.split("_")[-1])
        coeffs[idc] = coeff.split("_")[0].replace("F", "c")

    dirmodel = copy.deepcopy(models)
    drawcoeff = copy.deepcopy(models)

    for setpiec in setpiecs:
        if dirmodel.startswith("F") or ":F" in dirmodel:
            dirmodel = models.replace(setpiec, "")
        drawcoeff = models.replace(setpiec, "")
            
    path = ("%s/%s" % (path_, dirmodel) ) 
    print "==>path: ", path
    #print os.path.exists(path)
    maindir = os.getcwd() + "/"
    if(os.path.exists(path)):
        print "ok i'm in the directory", path
        os.chdir(path)
        #print "We are in the right folder ",  len(categories)
        extraoption = ""
        intervals = []
        modComb = ""
        opstring = ""
        for idc, coeff in enumerate(coeffs):
            if coeff.startswith("cS"):
                intervals.append("-60,50")
            elif coeff.startswith("cM"):
                intervals.append("-60,50")
            elif coeff.startswith("cT"):
                intervals.append("-60,50")
            elif coeff == ("cHW") or coeff == ("cHW_1"):
                intervals.append("-30,30")
            elif coeff.startswith("cHWB"):
                intervals.append("-200,200")
            elif coeff.startswith("cW"):
                intervals.append("-5,5")
            elif coeff.startswith("cll_1"):
                intervals.append("-300,300")
            elif coeff.startswith("cqq11") or coeff.startswith("cqq3_"):
                intervals.append("-0.1,0.1")
            elif coeff.startswith("cqq31"):
                intervals.append("-0.3,0.3")
            else:
                intervals.append("-100,100")
            if idc > 0:
                modComb += ","
                opstring += ","
            modComb += "k_" + coeff
            opstring += coeff


        if True:#len(categories) >= 1:
            if True:#len(years) >1:
                cmd = "combineCards.py "
                for year in years:
                    for cat in categories:
                        cmd += cat+year+"=%s_%s_%s_%s.txt " %(dirmodel, cat, year, method)
                global_dc = str(dirmodel) + "_" + str(method) + ".txt" 
                cmd += " > " + global_dc #%s_%s.txt" % (model, method)
                #print cmd
    
                os.system(cmd)
                
                cmd = "text2workspace.py "
                cmd += global_dc + " -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative -o "

                rootdc = dirmodel + "_" + method+ ".root"
                cmd += rootdc +" --X-allow-no-signal --PO eftOperators=" + opstring
                if len(coeffs) > 1:
                    cmd += " --PO eftAlternative"
                print cmd
                os.system(cmd)
    
                intervalstr = ""
                namedraw = ""
                labels = []
                for idc, coeff in enumerate(coeffs):
                    if idc > 0:
                        intervalstr += ":"
                        namedraw += " " 
                    intervalstr += "k_" + coeff + "=" + intervals[idc]
                    namedraw += "k_" + coeff
                    label = coeff.replace("c", "c_{") + "}"
                    if coeff.startswith("cT") or coeff.startswith("cM") or coeff.startswith("cS"):
                        label = label.replace("c_", "f_")
                        label += " [TeV^{-4}] "
                    else:
                        label += " [TeV^{-2}] "
                    labels.append(label)

                os.system("rm higgsCombine" + dirmodel + "*root")
                #cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/parallelScan.py " + rootdc + " -j 100 -M MultiDimFit " + algostring + " -m 125 --redefineSignalPOIs " + modComb + " --freezeParameters r --setParameters r=1 --setParameterRanges " + intervalstr + " -n " + dirmodel #+ " --autoMaxPOIs r," + modComb + " --squareDistPoiStep --autoBoundsPOIs r," + modComb #### precedente 
                cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/parallelScan.py " + rootdc + " -j 100 -M MultiDimFit " + algostring + " -m 125 --freezeParameters r --setParameters r=1 --setParameterRanges " + intervalstr  
                #if not ":" in models:
                    #cmd += " --autoRange 15 "
                cmd += " " + optionals 
                if not profile:
                    cmd += " --redefineSignalPOIs " + modComb + " -n " + dirmodel + " ; hadd -f higgsCombine" + dirmodel + ".MultiDimFit.mH125.root higgsCombine" + dirmodel + ".*.MultiDimFit.mH125.root" 
                    print cmd
                    runCombine(cmd, "ls_k_" + dirmodel + "_" + method + ".log")
                else:
                    modCombs = modComb.split(",")
                    print "modCombs:", modCombs, modComb
                    cmd0 = cmd + " --redefineSignalPOIs " + modCombs[0] + " -n " + dirmodel + "_" + modCombs[0] + " --floatOtherPOI=1 ; hadd -f higgsCombine" + dirmodel + "_" + modCombs[0] + ".MultiDimFit.mH125.root higgsCombine" + dirmodel + "_" + modCombs[0] + ".*.MultiDimFit.mH125.root" 
                    cmd1 = cmd + " --redefineSignalPOIs " + modCombs[1] + " -n " + dirmodel + "_" + modCombs[1] + " --floatOtherPOI=1 ; hadd -f higgsCombine" + dirmodel + "_" + modCombs[1] + ".MultiDimFit.mH125.root higgsCombine" + dirmodel + "_" + modCombs[1] + ".*.MultiDimFit.mH125.root" 
                    print cmd0
                    print cmd1
                    runCombine(cmd0, "ls_k_" + dirmodel + "_" + modCombs[0] + "_" + method + ".log")
                    runCombine(cmd1, "ls_k_" + dirmodel + "_" + modCombs[1] + "_" + method + ".log")
                #os.system("pwd")
                
                cmd = ""
                if not ":" in models:
                    cmd = "python " + maindir + "drawLS.py --in0 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --in1 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --coeff " + drawcoeff
                    #if not ":" in models:
                    cmd += " --1D"
                    #else:
                        #cmd += " --2D"
                    cmd += " --year " 
                    for year in years:
                        cmd += year
                        if year != years[-1]:
                            cmd += "," 
                    print cmd
                    os.system(cmd)
                
                else:
                    if not profile:
                        os.chdir(maindir)
                        cmd = "python mkEFTScan.py " + path + "/higgsCombine" + dirmodel + ".MultiDimFit.mH125.root -p " + namedraw + " -maxNLL 10 -cms -preliminary -lumi 138 -xlabel " + labels[0] 
                        #if ":" in models:
                        cmd += " -ylabel " + labels[1]
                        cmd += " -outdir " + path
                        print cmd
                        os.system(cmd)
                    else:
                        cmd0 = "python " + maindir + "drawLS.py --in0 higgsCombine" + dirmodel + "_" + modCombs[0] + ".MultiDimFit.mH125.root --in1 higgsCombine" + dirmodel + "_" + modCombs[0] + ".MultiDimFit.mH125.root --coeff " + drawcoeff.split(":")[0]
                        cmd1 = "python " + maindir + "drawLS.py --in0 higgsCombine" + dirmodel + "_" + modCombs[1] + ".MultiDimFit.mH125.root --in1 higgsCombine" + dirmodel + "_" + modCombs[1] + ".MultiDimFit.mH125.root --coeff " + drawcoeff.split(":")[1]
                        cmd0 += " --1D"
                        cmd1 += " --1D"
                        cmd0 += " --year " 
                        cmd1 += " --year " 
                        for year in years:
                            cmd0 += year
                            cmd1 += year
                            if year != years[-1]:
                                cmd0 += "," 
                                cmd1 += "," 
                        print cmd0
                        os.system(cmd0)
                        print cmd1
                        os.system(cmd1)
                        
                os.chdir(path)
                os.system("rm higgsCombine" + dirmodel + ".*.MultiDimFit.mH125.root")

        os.chdir("..")
