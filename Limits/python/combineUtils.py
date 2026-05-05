import os
import subprocess
#from Stat.Limits.settings import *
import copy
import json
from datetime import datetime

def writeCombinationJson(jsonPath, categories, years, coeffs):
    binOpsMap = {}
    for year in years:
        for category in categories:
            binOpsMap[category + "_" + year] = list(coeffs)
    with open(jsonPath, "w") as jsonFile:
        json.dump(binOpsMap, jsonFile, indent=2, sort_keys=True)

def runCombine(cmdStr, logFile):
    "run combine for a specific case"
    #print os.getcwd()
    #print cmd
    #writer = open(logFile, 'w') 
    #process = subprocess.call(cmd, shell = True, stdout=writer)
    #logFile = logfile.replace(".log", datetime.now().time().strftime("%H%M%S%f") + ".log")
    print(cmdStr + " 2>&1 | tee " + logFile)
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

    print("evaluate limit for model", model)
    print("categories:", categories)
    path = "" + path_ + "/" + modelname
    
    if(os.path.exists(path)):
        os.chdir(path)
        
        extraoption = " --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT --expectSignal 1 " #--cminDefaultMinimizerStrategy 0 
        if not unblind:
            extraoption += " -t -1 --toysFreq " 
        cmd = "combineCards.py "
        for year in years:
            for cat in categories:
                cmd += cat+"_"+year+"=%s_%s_%s_%s.txt " %(modelname, cat, year, method)
        cmd += "> %s_%s.txt" % (modelname, method)
        print(cmd)
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
        #runCombine("python3 ../../../../../../../../../CombineHarvester/CombineTools/scripts/ValidateDatacards.py " + modelname + "_" + method + ".txt", "validation.out")

        os.chdir("..")
    
def runSinglePointVBS_EWvsQCD(path_, model, categories, method, runSingleCat, years, unblind):
    maindir = os.getcwd() + "/"
    modelname = ""
    optionalsSM = " --algo=grid --points=50000 --cminDefaultMinimizerStrategy=0 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT "#--setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND" #--autoBoundsPOIs * --autoRange 3" #--fastScan"
    if not unblind:
        optionalsSM += " -t -1 --toysFreq "

    modelname = model.replace(":", "_")
    #print "evaluate limit for model ", model
    path = "" + path_ + "/" + modelname
    vbsmodels = model.split(":")
    print("model", model)
    print("hello", path)
    if(os.path.exists(path)):
        print("ok i'm in the directory")
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
                print(cmd)
                os.system(cmd)
                os.system("rm higgsCombineTest*root")
                cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/parallelScan.py -j 100 " + rootdc + " -M MultiDimFit -m 125 --redefineSignalPOIs " + modComb + " --setParameterRanges " + intervalstr + " --autoBoundsPOIs " + modComb + " " + optionalsSM + " --setParameters " + valuestr + " --freezeParameters r --setParameters r=1"
                cmd += " ; hadd -f higgsCombineTest.MultiDimFit.mH125.root higgsCombineTest.*.MultiDimFit.mH125.root"
            
                print(cmd)
                runCombine(cmd, "ls_k_" + model[0] + "_" + method + ".log")
                
                cmd = "python3 " + maindir + "drawLS.py --in0 higgsCombineTest.MultiDimFit.mH125.root --in1 higgsCombineTest.MultiDimFit.mH125.root --coeff EWK:QCD " 
                cmd += " --2D"
                cmd += " --year " 
                for year in years:
                    cmd += year
                    if year != years[-1]:
                        cmd += "," 
                print(cmd)
                os.system(cmd)                
                os.system("rm higgsCombineTest.*.MultiDimFit.mH125.root")
                
def runSinglePointVBS_AL(path_, model, categories, method, runSingleCat, years, unblind):
    print("evaluate limit for VBS_SSWW_" + model)
    path = ("%s/VBS_SSWW_%s" % (path_, model) )
    #print "==>path: ", path
    #print os.path.exists(path)
    if(os.path.exists(path)):
        #print "ok i'm in the directory"
        os.chdir(path)
        #print "We are in the right folder ",  len(categories)
        extraoption=""
        if not unblind:
            extraoption += " -t -1 --toysFreq "
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

def runSinglePointVBS_LS(path_, models, categories, method, runSingleCat, years, profile, unblind, rint=None, rfix=None, onlyLin=False):
    algostring = " --algo=grid  --points "
    jobs = ""

    if ":" in models and not profile:
        algostring += "20000 "
        jobs = "100"
        #algostring += "1000 "
        #jobs = "50"
        #algostring += "10 "
    elif ":" in models and profile:
        if unblind:
            algostring +=     "  2000 "
            jobs = "50"
        else:
            algostring +=     "  1000 "
            jobs = "25"
        #algostring +=     "  25 "
    else:
        algostring +=     "  4000 "
        jobs = "100"
        #algostring +=     "  7500 "

    print("\n\nnumber of points:", algostring, "\nnumber of jobs:", jobs)
    optionals = " --alignEdges=1 --cminDefaultMinimizerStrategy=0  --setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance=0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --pointsRandProf=25 " # --verbose=3

    pmodel = ''
    if not onlyLin:
        optionals += "--X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT "
        pmodel ='HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative_comb:analiticAnomalousCouplingEFTNegative_comb'
    else:
        pmodel ='HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingLinearEFTNegative_comb:analiticAnomalousCouplingLinearEFTNegative_comb --PO reuseCompleteDatacards'

    if not unblind:
        optionals += " -t -1 --toysFreq "
    #if not ":" in models or (":" in models and profile):
        #optionals += " " #" --setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND "#--fastScan" #--autoBoundsPOIs * --autoRange 3" 
    print("Performing LikelihoodScan for operator ", models)
    dirmodel = ""
    coeffs = models.split(":")
    setpiecs = []
    for idc, coeff in enumerate(coeffs):
        if len(coeff.split("_")) > 1:
            setpiecs.append(("_")+coeff.split("_")[-1])
        coeffs[idc] = coeff.split("_")[0].replace("F", "c")

    dirmodel = copy.deepcopy(models)
    drawcoeff = copy.deepcopy(models)
    print(setpiecs)
    setpiecs.reverse()
    print(setpiecs)
    dirmodel = models
    drawcoeff = models
    for setpiec in setpiecs:
        if dirmodel.startswith("F") or ":" in dirmodel:
            dirmodel = dirmodel.replace(setpiec, "")
        drawcoeff = drawcoeff.replace(setpiec, "")
    print(dirmodel)
    path = ("%s/%s" % (path_, dirmodel) ) 
    print("==>path: ", path)
    print(os.path.exists(path))
    maindir = os.getcwd() + "/"
    if(os.path.exists(path)):
        print("ok i'm in the directory", path)
        os.chdir(path)
        #print "We are in the right folder ",  len(categories)
        extraoption = ""
        intervals = []
        modComb = ""
        opstring = ""
        print("coeffs:", coeffs)
        for idc, coeff in enumerate(coeffs):
            lower = 0
            upper = 0
            '''
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
                    lower = -2
                    upper = 2
                elif coeff == "cqq11":
                    lower = -2
                    upper = 2
                elif coeff == "cqq3":
                    lower = -2
                    upper = 2
                elif coeff == "cqq31":
                    lower = -1
                    upper = 1
                elif coeff.startswith("cS") or coeff.startswith("cM") or coeff.startswith("cT"):
                    lower = -60
                    upper = 50
                else:
                    lower = -200
                    upper = 200
            '''
            if True: #" in models:# and not (coeff.startswith("cS") or coeff.startswith("cT") or coeff.startswith("cM"))
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
                    lower = -1.5
                    upper = 1.5
                else:
                    if coeff == "cHbox":
                        lower = -100
                        upper = 100
                    elif coeff == "cHDD":
                        lower = -100
                        upper = 100
                    elif coeff == "cHl1":
                        lower = -80
                        upper = 80
                    elif coeff == "cHl3":
                        lower = -15
                        upper = 20
                    elif coeff == "cHq1":
                        lower = -15
                        upper = 15
                    elif coeff == "cHq3":
                        lower = -6.
                        upper = 6.
                    elif coeff == "cHWB":
                        lower = -250
                        upper = 250
                    elif coeff == "cHW":
                        lower = -20
                        upper = 20
                    elif coeff == "cll1":
                        lower = -30
                        upper = 20
                    elif coeff == "cll":
                        lower = -500
                        upper = 500
                    elif coeff == "cqq1":
                        lower = -2
                        upper = 2
                    elif coeff == "cqq3":
                        lower = -0.25
                        upper = 0.25
                    elif coeff == "cqq11":
                        lower = -0.25
                        upper = 0.25
                    elif coeff == "cqq31":
                        lower = -0.4
                        upper = 0.4
                    elif coeff == "cqq1":
                        lower = -1.5
                        upper = 1.5
                    elif coeff == "cW":
                        lower = -1.5
                        upper = 1.5
                    elif coeff.startswith("cT"):# or coeff.startswith("cM") or coeff.startswith("cS"):
                        if coeff.startswith("cT1"):
                            lower = -1
                            upper = 1
                        else:
                            lower = -3
                            upper = 3
                    elif coeff.startswith("cS"):
                        if coeff.startswith("cS0"):
                            lower = -30
                            upper = 30
                        else:
                            lower = -80
                            upper = 80
                    elif coeff.startswith("cM"):# or coeff.startswith("cT"):
                        if coeff.startswith("cM7"):
                            lower = -50
                            upper = 50
                        elif coeff.startswith("cM1"):
                            lower = -30
                            upper = 30
                        else:
                            lower = -20
                            upper = 20

            if "cll_" in models and not coeff.startswith("cqq"):
                if coeff.startswith("cT") or coeff.startswith("cS") or coeff.startswith("cM"):
                    lower = -20
                    upper = 20                    
                else:
                    lower *= 4
                    upper *= 4
            #elif "cHWB_" in models and not coeff == "cHWB":
                #if coeff.startswith("cT") or coeff.startswith("cS") or coeff.startswith("cM"):
                    #lower *= 2.5
                    #upper *= 1.5
                #else:
                    #lower *= 1.5
                    #upper *= 1.5
            elif "cHDD_" in models and "cHbox_" in models:
                pass #lower *= 5
                #upper *= 5
            elif "cHl3_" in models and "cll1_" in models:
                lower *= 5
                upper *= 5
            if ":" in models:
                if profile:
                    lower *= 5
                    upper *= 5
                elif coeff.startswith("cT") or coeff.startswith("cS") or coeff.startswith("cM"):
                    lower *= 10
                    upper *= 10
                else:
                    lower *= 1.1
                    lower *= 1.1
            if onlyLin:
                lower *= 10
                upper *= 10

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
                print(cmd)
    
                os.system(cmd)
                
                jsonCombPath = "jsonComb.json"
                writeCombinationJson(jsonCombPath, categories, years, coeffs)

                cmd = "text2workspace.py "
                cmd += global_dc + " -P " + pmodel + " -o "

                rootdc = dirmodel + "_" + method+ ".root"
                cmd += rootdc + " --X-allow-no-signal --PO fileCombination=" + jsonCombPath + " --PO eftOperators=" + opstring
                if not onlyLin:
                    cmd += " --PO reuseCompleteDatacards"
                print("\n\n\n\nTEXT2WS\n\n\n\n", cmd)
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
                
                #cmd = "combine "
                cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/parallelScan.py -j " + jobs + "  " 
                cmd += rootdc + " -M MultiDimFit " + algostring + " -m 125 "
                if not unblind:
                    cmd += " --freezeParameters r --setParameters r=1 "
                else:
                    #cmd += " --freezeParameters r --setParameters r=1.5 "
                    print("\n\n rfix", rfix, "rint", rint) #, "rfix - rint", float(rfix) - float(rint), "rfix + rint", float(rfix) + float(rint), "\n\n"
                    if rfix != None:
                        cmd += " --setParameters r=" + rfix 
                        for coeff in coeffs:
                            cmd += ",k_" + coeff + "=0"
                    else:
                        cmd += " --setParameters "
                        for coeff in coeffs:
                            if cmd.endswith("0"):
                                cmd += ","
                            cmd += "k_" + coeff + "=0"

                    if rint != None:
                        if rfix == None:
                            rfixx = 0
                        else:
                            rfixx = rfix
                        rmin = str( round(float(rfixx) - float(rint) , 2) )
                        rmax = str( round(float(rfixx) + float(rint) , 2) )
                        cmd += " --rMin " + rmin + " --rMax " + rmax + " "
                    else:
                        cmd += " --freezeParameters r "
                cmd += " --setParameterRanges " + intervalstr
                #cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/parallelScan.py " + rootdc + " -j " + jobs + "  -M MultiDimFit " + algostring + " -m 125 --freezeParameters r --setParameters r=1 --setParameterRanges " + intervalstr  
                #if not ":" in models:
                    #cmd += " --autoRange 15 "
                cmd += " " + optionals 
                if not profile:
                    cmd += " --redefineSignalPOIs " + modComb + " -n " + dirmodel 
                    if not cmd.startswith("combine"):
                        cmd += " ; hadd -f higgsCombine" + dirmodel + ".MultiDimFit.mH125.root higgsCombine" + dirmodel + ".*.MultiDimFit.mH125.root" 
                    print(cmd)
                    runCombine(cmd, "ls_k_" + dirmodel + "_" + method + ".log")
                else:
                    modCombs = modComb.split(",")
                    print("modCombs:", modCombs, modComb)
                    #cmd0 = cmd + " --redefineSignalPOIs " + modCombs[0] + " -n " + dirmodel + "_" + modCombs[0] + " --floatOtherPOI=1 ; hadd -f higgsCombine" + dirmodel + "_" + modCombs[0] + ".MultiDimFit.mH125.root higgsCombine" + dirmodel + "_" + modCombs[0] + ".*.MultiDimFit.mH125.root" 
                    #cmd1 = cmd + " --redefineSignalPOIs " + modCombs[1] + " -n " + dirmodel + "_" + modCombs[1] + " --floatOtherPOI=1 ; hadd -f higgsCombine" + dirmodel + "_" + modCombs[1] + ".MultiDimFit.mH125.root higgsCombine" + dirmodel + "_" + modCombs[1] + ".*.MultiDimFit.mH125.root" 
                    #print cmd0
                    #print cmd1
                    #runCombine(cmd0, "ls_k_" + dirmodel + "_" + modCombs[0] + "_" + method + ".log")
                    #runCombine(cmd1, "ls_k_" + dirmodel + "_" + modCombs[1] + "_" + method + ".log")
                    for elComb in modCombs:
                        cmdel = cmd + " --redefineSignalPOIs " + elComb + " -n " + dirmodel + "_" + elComb + " --floatOtherPOI=1 ; hadd -f higgsCombine" + dirmodel + "_" + elComb + ".MultiDimFit.mH125.root higgsCombine" + dirmodel + "_" + elComb + ".*.MultiDimFit.mH125.root" 
                        print(cmdel)
                        runCombine(cmdel, "ls_k_" + dirmodel + "_" + elComb + "_" + method + ".log")
                #os.system("pwd")
                
                cmd = ""
                if not ":" in models:
                    cmd = "python3 " + maindir + "drawLS.py --in0 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --in1 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --coeff " + drawcoeff
                    #if not ":" in models:
                    cmd += " --1D"
                    #else:
                        #cmd += " --2D"
                    cmd += " --year " 
                    for year in years:
                        cmd += year
                        if year != years[-1]:
                            cmd += "," 
                    print(cmd)
                    ###os.system(cmd)
                
                else:
                    if not profile:
                        os.chdir(maindir)
                        print("pwd")
                        os.system("pwd")
                        cmd = "python3 mkEFTScan.py " + path + "/higgsCombine" + dirmodel + ".MultiDimFit.mH125.root -p " + namedraw + " -maxNLL 10 -xlabel " + labels[0] 

                        cmd += " -ylabel " + labels[1]
                        cmd += " -outdir " + path
                        print("\n\n\n\n\nLABELS", labels)
                        #cmd += " -cms -lumi 138 "
                        
                        #cmd = "python3 " + maindir + "drawLS.py --in0 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --in1 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --coeff " + dirmodel
                        #cmd += " --2D"
                        #cmd += " --year " 
                        #for year in years:
                        #    cmd += year
                        #    if year != years[-1]:
                        #        cmd += "," 

                        #os.chdir(maindir)
                        #cmd = "python3 mkEFTScanNoGrad.py " + path + "/higgsCombine" + dirmodel + ".MultiDimFit.mH125.root -p " + namedraw + " -maxNLL 10 -cms -preliminary -lumi 138 -xlabel " + labels[0] 
                        #if ":" in models:
                        #cmd += " -ylabel " + labels[1]
                        #cmd += " -outdir " + path
                        
                        os.system("pwd")
                        print(cmd)
                        ###os.system(cmd)
                    else:
                        modCombs = modComb.split(",")
                        #cmd1 = "python3 " + maindir + "drawLS.py --in0 higgsCombine" + dirmodel + "_" + modCombs[1] + ".MultiDimFit.mH125.root --in1 higgsCombine" + dirmodel + "_" + modCombs[1] + ".MultiDimFit.mH125.root --coeff " + drawcoeff.split(":")[1]
                        #cmd1 += " --1D"
                        #cmd1 += " --year " 
                        #for year in years:
                            #cmd1 += year
                            #if year != years[-1]:
                                #cmd1 += "," 
                        #print cmd1
                        #os.system(cmd1)

                        for ellComb in modCombs:
                            cmdell = "python3 " + maindir + "drawLS.py --in0 higgsCombine" + dirmodel + "_" + ellComb + ".MultiDimFit.mH125.root --in1 higgsCombine" + dirmodel + "_" + ellComb + ".MultiDimFit.mH125.root --coeff " + ellComb.split("_")[-1]
                            cmdell += " --1D"
                            cmdell += " --year " 
                            for year in years:
                                cmdell += year
                                if year != years[-1]:
                                    cmdell += "," 

                            print(cmdell)
                            ###os.system(cmdell)
                        
                os.chdir(path)
                ###os.system("rm higgsCombine" + dirmodel + ".*.MultiDimFit.mH125.root")

        os.chdir("..")
