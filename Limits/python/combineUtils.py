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
                cmd += cat+"_"+year+"=%s_%s_%s_%s.txt " %(modelname, cat, year, method)
        cmd += "> %s_%s.txt" % (modelname, method)
        print cmd
        os.system(cmd)

        runCombine("combine -M Significance " + extraoption + " " + modelname + "_" + method + ".txt -n " + modelname, "significance_" + modelname + "_" + method + ".log")

        if not unblind:
            niter = 10
        else:
            niter = 10
        if UseHybridNew:
            for idhn in range(niter):
                runCombine("combine -M HybridNew " + modelname + "_" + method + ".txt --LHCmode LHC-significance --saveToys --saveHybridResult --fullBToys " + extraoption + " -T 50 -i 50 -s -1 --fork 20 -H AsymptoticLimits --rMin -4 -n " + modelname + "_hybrid", "hybrid_" + modelname + "_" + method + "_" + str(idhn) + ".log")
            os.system("hadd -f merged_HybridNew.root higgsCombine" + modelname + "_hybrid.HybridNew.mH120*root")
            runCombine("combine -M HybridNew " + modelname + "_" + method + ".txt --LHCmode LHC-significance --readHybridResult --toysFile=merged_HybridNew.root " + extraoption + " --rMin -4 -n " + modelname + "_hybrid_total", "hybrid_total_" + modelname + "_" + method + ".log")
        #runCombine("combine -M FitDiagnostics "+ modelname + "_" + method + ".txt --expectSignal=1 --plots --saveShapes --saveWithUncertainties", "fitDiag_VBS_SSWW_" + modelname + "_" + method + ".log")
        #runCombine("python ../../../../../../../../../CombineHarvester/CombineTools/scripts/ValidateDatacards.py " + modelname + "_" + method + ".txt", "validation.out")

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
                        cmd += cat+"_"+year+"=%s_%s_%s_%s.txt " %(modelname, cat, year, method)
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
                cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/parallelScan.py -j 20 " + rootdc + " -M MultiDimFit -m 125 --redefineSignalPOIs " + modComb + " --setParameterRanges " + intervalstr + " --autoBoundsPOIs " + modComb + " " + optionalsSM + " --setParameters " + valuestr + " --freezeParameters r --setParameters r=1"
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
                        cmd += cat+"_"+year+"=VBS_SSWW_%s_%s_%s_%s.txt " %(model, cat, year, method)
                cmd += "> VBS_SSWW_%s_%s.txt" % (model, method)
                #print cmd
                os.system(cmd)
                #runCombine("combine -M Significance "+extraoption+" -n VBS_SSWW_" + modelname + "_" + method + " VBS_SSWW_" + modelname + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + method + ".log")
                #runCombine("combine -M FitDiagnostics "+extraoption+" -n VBS_SSWW_" + modelname + "_" + method + " VBS_SSWW_" + modelname + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + method + ".log")

        os.chdir("..")

def runSinglePointVBS_LS(path_, models, categories, method, runSingleCat, years, profile, unblind):
    algostring = " --algo=grid  --points "
    if ":" in models and not profile:
        #algostring += "200000 "
        if not "cqq" in models:
            algostring += "200000 "
        else:
            algostring += "100000 "
        #algostring += "10 "
        #algostring += " 50000 "
    elif ":" in models and profile:
        algostring +=     "  5000 "
        #algostring +=     "  25 "
    else:
        #algostring +=     "  5000 "
        algostring +=     "  1000 "

    optionals = " --alignEdges=1 --cminDefaultMinimizerStrategy=0 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT" #--fastScan" #--setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --fastScan" #--autoBoundsPOIs * --autoRange 3" 
    if not unblind:
        optionals += " -t -1 "
    if not ":" in models or (":" in models and profile):
        optionals += " " #" --setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND "#--fastScan" #--autoBoundsPOIs * --autoRange 3" 
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
    print setpiecs
    setpiecs.reverse()
    print setpiecs
    dirmodel = models
    drawcoeff = models
    for setpiec in setpiecs:
        if dirmodel.startswith("F") or ":" in dirmodel:
            dirmodel = dirmodel.replace(setpiec, "")
        drawcoeff = drawcoeff.replace(setpiec, "")
    print dirmodel
    path = ("%s/%s" % (path_, dirmodel) ) 
    print "==>path: ", path
    print os.path.exists(path)
    maindir = os.getcwd() + "/"
    if(os.path.exists(path)):
        print "ok i'm in the directory", path
        os.chdir(path)
        #print "We are in the right folder ",  len(categories)
        extraoption = ""
        intervals = []
        modComb = ""
        opstring = ""
        print "coeffs:", coeffs
        for idc, coeff in enumerate(coeffs):
            lower = 0
            upper = 0
            if not ":" in models:
                if coeff == "cHW":
                    lower = -30
                    upper = 30
                elif coeff == "cHWB":
                    lower = -200
                    upper = 200
                elif coeff == "cW":
                    lower = -5
                    upper = 5
                elif coeff == "cll":
                    lower = -400
                    upper = 400
                elif coeff == "cqq11":
                    lower = -10
                    upper = 10
                elif coeff == "cqq3":
                    lower = -50
                    upper = 50
                elif coeff == "cqq31":
                    lower = -1
                    upper = 1
                elif coeff.startswith("cS") or coeff.startswith("cM") or coeff.startswith("cT"):
                    lower = -60
                    upper = 50
                else:
                    lower = -100
                    upper = 100
            elif ":" in models:# and not (coeff.startswith("cS") or coeff.startswith("cT") or coeff.startswith("cM"))
                #print "\n", (models.startswith("cqq") and ":cqq" in models)
                if (models.startswith("cqq") and ":cqq" in models):
                    #print "HELLO\n"
                    if coeff == "cqq1":
                        lower = -2
                        upper = 3
                    elif coeff == "cqq31":
                        lower = -0.5
                        upper = 0.5
                    else:
                        lower = -0.2
                        upper = 0.2
                elif "cqq" in models and not coeff.startswith("cqq") and coeff == "cW":
                    #if coeff == "cHq3":
                        #lower = -100
                        #lower = 100
                    lower = -2.5
                    upper = 3.5
                    #else:
                        #lower = -4000
                        #upper = 4000
                #elif "cqq31_" in models and not coeff.startswith("cqq"):
                    #if coeff == "cHq3" or coeff == "cHl3":
                        #lower = -50
                        #upper = 50
                    #elif coeff == "cW":
                        #lower = -4
                        #upper = 6
                    #elif coeff == "cHW":
                        #lower = -400
                        #upper = 400
                    #elif coeff == "cll1":
                        #lower = -550
                        #upper = 550
                    #elif coeff == "cHq1":
                        #lower = -200
                        #upper = 200
                    #else:
                        #lower = -4000
                        #upper = 4000                      
                #elif "cqq11_" in models and not coeff.startswith("cqq"):
                    #if coeff == "cHq3":
                        #lower = -30
                        #upper = 30
                    #elif coeff == "cHl3":
                        #lower = -300
                        #upper = 300
                    #elif coeff == "cHq1":
                        #lower = -200
                        #upper = 200
                    #elif coeff == "cW":
                        #lower = -4
                        #upper = 6
                    #else:
                        #lower = -4000
                        #upper = 4000                      
                else:
                    if coeff == "cHbox":
                        lower = -40
                        upper = 40
                    elif coeff == "cHDD":
                        lower = -100
                        upper = 100
                    elif coeff == "cHl1":
                        lower = -170
                        upper = 170
                    elif coeff == "cHl3":
                        lower = -25
                        upper = 30
                    elif coeff == "cHq1":
                        lower = -15
                        upper = 15
                    elif coeff == "cHq3":
                        lower = -10
                        upper = 10
                    elif coeff == "cHWB":
                        lower = -350
                        upper = 350
                    elif coeff == "cHW":
                        lower = -20
                        upper = 20
                    elif coeff == "cll1":
                        lower = -30
                        upper = 20
                    elif coeff == "cll":
                        lower = -150
                        upper = 150
                    elif coeff == "cqq1":
                        lower = -5
                        upper = 5
                    elif coeff == "cqq3" or coeff == "cqq11" or coeff == "cqq31":
                        if "cW_" in models:
                            if coeff == "cqq31":
                                lower = -0.6
                                upper = 0.6
                            else:
                                lower = -0.3
                                upper = 0.3
                        elif "cHW_" in models:
                            lower = -3
                            upper = 3
                        elif "cll_" in models:
                            lower = -40
                            upper = 40
                        else:
                            lower = -1
                            upper = 1
                    elif coeff == "cW":
                        lower = -15
                        upper = 15
                    elif coeff.startswith("cT") or coeff.startswith("cM") or coeff.startswith("cS"):
                        lower = -10
                        upper = 10
            
            if "cll_" in models and not coeff.startswith("cqq"):
                if coeff.startswith("cT") or coeff.startswith("cS") or coeff.startswith("cM"):
                    lower = -20
                    upper = 20                    
                else:
                    lower *= 4
                    upper *= 4
            elif "cHWB_" in models and not coeff == "cHWB":
                if coeff.startswith("cT") or coeff.startswith("cS") or coeff.startswith("cM"):
                    lower *= 2.5
                    upper *= 1.5
                else:
                    lower *= 1.5
                    upper *= 1.5
            elif "cHDD_" in models and "cHbox_" in models:
                lower *= 5
                upper *= 5
            elif "cHl3_" in models and "cll1_" in models:
                lower *= 5
                upper *= 5
            lower *= 5
            upper *= 5
                
            intervals.append(str(lower) + "," + str(upper))

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
                        cmd += cat+"_"+year+"=%s_%s_%s_%s.txt " %(dirmodel, cat, year, method)
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
                #cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/parallelScan.py " + rootdc + " -j 20 -M MultiDimFit " + algostring + " -m 125 --redefineSignalPOIs " + modComb + " --freezeParameters r --setParameters r=1 --setParameterRanges " + intervalstr + " -n " + dirmodel #+ " --autoMaxPOIs r," + modComb + " --squareDistPoiStep --autoBoundsPOIs r," + modComb #### precedente 
                #cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/parallelScan.py " + rootdc + " -j 20 -M MultiDimFit " + algostring + " -m 125 --freezeParameters r --setParameters r=1 --setParameterRanges " + intervalstr 
                #cmd = "combine "
                cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/parallelScan.py -j 20 " 
                cmd += rootdc + " -M MultiDimFit " + algostring + " -m 125 "
                if not unblind:
                    cmd += " --freezeParameters r --setParameters r=1 "
                else:
                    cmd += " --freezeParameters r --setParameters r=1.5 "
                
                cmd += " --setParameterRanges " + intervalstr  
                #cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/parallelScan.py " + rootdc + " -j 20 -M MultiDimFit " + algostring + " -m 125 --freezeParameters r --setParameters r=1 --setParameterRanges " + intervalstr  
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
                    #cmd0 = cmd + " --redefineSignalPOIs " + modCombs[0] + " -n " + dirmodel + "_" + modCombs[0] + " --floatOtherPOI=1 ; hadd -f higgsCombine" + dirmodel + "_" + modCombs[0] + ".MultiDimFit.mH125.root higgsCombine" + dirmodel + "_" + modCombs[0] + ".*.MultiDimFit.mH125.root" 
                    #cmd1 = cmd + " --redefineSignalPOIs " + modCombs[1] + " -n " + dirmodel + "_" + modCombs[1] + " --floatOtherPOI=1 ; hadd -f higgsCombine" + dirmodel + "_" + modCombs[1] + ".MultiDimFit.mH125.root higgsCombine" + dirmodel + "_" + modCombs[1] + ".*.MultiDimFit.mH125.root" 
                    #print cmd0
                    #print cmd1
                    #runCombine(cmd0, "ls_k_" + dirmodel + "_" + modCombs[0] + "_" + method + ".log")
                    #runCombine(cmd1, "ls_k_" + dirmodel + "_" + modCombs[1] + "_" + method + ".log")
                    for elComb in modCombs:
                        cmdel = cmd + " --redefineSignalPOIs " + elComb + " -n " + dirmodel + "_" + elComb + " --floatOtherPOI=1 ; hadd -f higgsCombine" + dirmodel + "_" + elComb + ".MultiDimFit.mH125.root higgsCombine" + dirmodel + "_" + elComb + ".*.MultiDimFit.mH125.root" 
                        print cmdel
                        runCombine(cmdel, "ls_k_" + dirmodel + "_" + elComb + "_" + method + ".log")
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
                        #cmd1 = "python " + maindir + "drawLS.py --in0 higgsCombine" + dirmodel + "_" + modCombs[1] + ".MultiDimFit.mH125.root --in1 higgsCombine" + dirmodel + "_" + modCombs[1] + ".MultiDimFit.mH125.root --coeff " + drawcoeff.split(":")[1]
                        #cmd1 += " --1D"
                        #cmd1 += " --year " 
                        #for year in years:
                            #cmd1 += year
                            #if year != years[-1]:
                                #cmd1 += "," 
                        #print cmd1
                        #os.system(cmd1)

                        for elComb in modCombs:
                            cmdell = "python " + maindir + "drawLS.py --in0 higgsCombine" + dirmodel + "_" + elComb + ".MultiDimFit.mH125.root --in1 higgsCombine" + dirmodel + "_" + elComb + ".MultiDimFit.mH125.root --coeff " + drawcoeff.split(":")[0]
                            cmdell += " --1D"
                            cmdell += " --year " 
                        for year in years:
                            cmdell += year
                            if year != years[-1]:
                                cmdell += "," 

                        print cmdell
                        os.system(cmdell)
                        
                os.chdir(path)
                os.system("rm higgsCombine" + dirmodel + ".*.MultiDimFit.mH125.root")

        os.chdir("..")
