import os
import subprocess
#from Stat.Limits.settings import *
import copy

def runCombine(cmdStr, logFile):
    "run combine for a specific case"
    #print os.getcwd()
    #print cmd
    #writer = open(logFile, 'w') 
    #process = subprocess.call(cmd, shell = True, stdout=writer)
    #print cmd + " 2>&1 | tee " + logFile
    os.system(cmdStr + " 2>&1 | tee " + logFile)
    return

def runSinglePointVBS_sign(path_, model, categories, method, runSingleCat, years):
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
    #for ids, sigp in enumerate(model):
        #path += "VBS_SSWW_" + sigp
        #if ids < len(model) - 1:
            #path += "_"
    #path = ("%s/VBS_SSWW_%s" % (path_, model) )
    #print "==>path: ", path
    #print os.path.exists(path)
    if(os.path.exists(path)):
        #print "ok i'm in the directory"
        os.chdir(path)
        #print "We are in the right folder ",  len(categories)
        
        extraoption=""
        if len(categories)>=1:
            if len(years)>1:
                cmd = "combineCards.py "
                for year in years:
                    for cat in categories:
                        cmd += cat+year+"=%s_%s_%s_%s.txt " %(modelname, cat, year, method)
                cmd += "> %s_%s.txt" % (modelname, method)
                print cmd
                os.system(cmd)
                runCombine("combine -M Significance "+extraoption+ " "+ modelname + "_" + method + ".txt -t -1  --cminDefaultMinimizerStrategy 0 --expectSignal=1  -n " + modelname, "significance_" + modelname + "_" + method + ".log")
                #runCombine("combine -M Significance "+extraoption+ " "+modelname + "_" + method + ".txt -t -1 ", "significance_" + modelname + "_" + method + ".log")
                #runCombine("combine -M FitDiagnostics "+ modelname + "_" + method + ".txt --expectSignal=1 --plots --saveShapes --saveWithUncertainties", "fitDiag_VBS_SSWW_" + modelname + "_" + method + ".log")

            else:
                for year in years:
                    cmd = "combineCards.py "
                    for cat in categories:
                        cmd += cat+"=%s_%s_%s_%s.txt " %(modelname, cat, year, method)
                    cmd += "> %s_%s.txt" % (modelname, method)
                    print cmd
                    os.system(cmd)
                    runCombine("combine -M Significance "+extraoption+ " "+ modelname + "_" + method + ".txt -t -1  --cminDefaultMinimizerStrategy 0 --expectSignal=1  -n " + modelname , "significance_" + modelname + "_" + method + ".log")
                    #runCombine("combine -M Significance "+extraoption+ " "+ modelname + "_" + method + ".txt -t -1 ", "significance_" + modelname + "_" + method + ".log")
                    #runCombine("combine -M FitDiagnostics "+ modelname + "_" + method + ".txt --expectSignal=1 --plots --saveShapes --saveWithUncertainties", "fitDiag_VBS_SSWW_" + modelname + ".log")  

                    if(runSingleCat): 
                        for cat in categories:
                            #print "category: " + (cat)
                            cat = cat+"_"+year+"_"+method
                            #print ""+ modelname + "_" + cat +".txt"
                            #print "combine -M Significance "+extraoption + " "+modelname + "_" + cat +".txt", "significance_" + modelname + "_" + cat + ".log"
                            #print "combine -M FitDiagnostics " + modelname + "_" + cat +".txt --expectSignal=1 --plots --saveShapes --saveWithUncertainties"
                            runCombine("combine -M Significance "+extraoption+" "+modelname + "_"  + cat +".txt -t -1 --cminDefaultMinimizerStrategy 0 --expectSignal=1  -n " + modelname, "significance_" + modelname + "_" + cat + ".log")  
                            #runCombine("combine -M Significance "+extraoption+" "+modelname + "_"  + cat +".txt -t -1 ", "significance_" + modelname + "_" + cat + ".log")  
                            #runCombine("combine -M FitDiagnostics " + modelname + "_"  + cat +".txt --expectSignal=1 --plots --saveShapes --saveWithUncertainties", "fitDiag_VBS_SSWW_" + modelname + "_" + cat + ".log")  

        else:
            for year in years:
                for cat in categories:
                    #print "category: " + (cat)
                    cat = cat+"_"+year+"_"+method
                    if(runSingleCat):
                        runCombine("combine -M Significance "+extraoption+ " "+modelname + cat +".txt -t -1  --cminDefaultMinimizerStrategy 0 --expectSignal=1  -n " + modelname , "significance_" + modelname + "_" + cat + ".log")  
                        #runCombine("combine -M Significance "+extraoption+ " "+modelname + cat +".txt -t -1 ", "significance_" + modelname + "_" + cat + ".log")  
                        #runCombine("combine -M FitDiagnostics " + modelname + cat +".txt --expectSignal=1 --plots --saveShapes --saveWithUncertainties", "fitDiag_VBS_SSWW_" + modelname + "_" + cat + ".log")  
        os.chdir("..")

def runSinglePointVBS_EWvsQCD(path_, model, categories, method, runSingleCat, years):
    maindir = os.getcwd() + "/"
    modelname = ""
    optionalsSM = " --algo=grid --points=100000 --alignEdges=1 --cminDefaultMinimizerStrategy=0 --setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND" #--autoBoundsPOIs * --autoRange 3" #--fastScan"
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
        
        if len(categories)>=1:
            print "hello!"
            if len(years)>1:
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
                        cmd += "--PO 'map=.*/" + vbsmodel + ":k_" + vbsmodel.split("_")[-1] + "[1,-150.0,150.0]' "
                    else:
                        cmd += "--PO 'map=.*/" + vbsmodel + ":k_" + vbsmodel.split("_")[-1] + "[1,-200.0,200.0]' "
                    if idvm > 0:
                        modComb += ","
                        intervalstr += ":"
                        valuestr += ","
                    modComb += "k_" + vbsmodel.split("_")[-1]
                    if "_DNN_" in path_:
                        intervalstr += "k_" + vbsmodel.split("_")[-1] + "=-150.0,150.0"
                    else:
                        intervalstr += "k_" + vbsmodel.split("_")[-1] + "=-200.0,200.0"
                    valuestr += "k_" + vbsmodel.split("_")[-1] + "=1" 
                cmd += global_dc + " -o " + rootdc 
                print cmd
                os.system(cmd)
            
                cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/parallelScan.py " + rootdc + " -M MultiDimFit -m 125 -t -1 --redefineSignalPOIs " + modComb + " --setParameterRanges " + intervalstr + " --autoBoundsPOIs " + modComb + " --autoRange 5 " + optionalsSM # " --setParameters " + valuestr + " --freezeParameters r --setParameters r=1"
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

def runSinglePointVBS_AL(path_, model, categories, method, runSingleCat, years):
    print "evaluate limit for VBS_SSWW_" + model
    path = ("%s/VBS_SSWW_%s" % (path_, model) )
    #print "==>path: ", path
    #print os.path.exists(path)
    if(os.path.exists(path)):
        #print "ok i'm in the directory"
        os.chdir(path)
        #print "We are in the right folder ",  len(categories)
        extraoption=""
        if len(categories)>=1:
            if len(years)>1:
                cmd = "combineCards.py "
                for year in years:
                    for cat in categories:
                        cmd += cat+year+"=VBS_SSWW_%s_%s_%s_%s.txt " %(model, cat, year, method)
                cmd += "> VBS_SSWW_%s_%s.txt" % (model, method)
                #print cmd
                os.system(cmd)
                #runCombine("combine -M Significance "+extraoption+" -n VBS_SSWW_" + modelname + "_" + method + " VBS_SSWW_" + modelname + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + method + ".log")
                #runCombine("combine -M FitDiagnostics "+extraoption+" -n VBS_SSWW_" + modelname + "_" + method + " VBS_SSWW_" + modelname + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + method + ".log")
            else:
                for year in years:
                    cmd = "combineCards.py "
                    for cat in categories:
                        cmd += cat+"=VBS_SSWW_%s_%s_%s_%s.txt " %(model, cat, year, method)
                    cmd += "> VBS_SSWW_%s_%s.txt" % (model, method)
                    #print cmd
                    os.system(cmd)
                    #runCombine("combine -M Significance "+extraoption+" -n VBS_SSWW_" + modelname + "_" + method + " VBS_SSWW_" + modelname + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + method + ".log")
                    #runCombine("combine -M FitDiagnostics "+extraoption+" -n VBS_SSWW_" + modelname + "_" + method + " VBS_SSWW_" + modelname + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + method + ".log")

                    if(runSingleCat): 
                        for cat in categories:
                            #print "category: " + (cat)
                            cat = cat+"_"+year+"_"+method
                            #print  "WP_M"+mass+"W"+width+"_" + chir + "_" + cat +".txt"
                            #print "combine -M Asymptotic "+extraoption+" -n VBS_SSWW_" + modelname + "_" + cat + " VBS_SSWW_" + modelname + "_" + cat +".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + cat + ".log"
                            #runCombine("combine -M Significance "+extraoption+" -n VBS_SSWW_" + modelname +  "_" + cat+ " VBS_SSWW_" + modelname + "_"  + cat +".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + cat + ".log")  
                            #runCombine("combine -M FitDiagnostics "+extraoption+" -n VBS_SSWW_" + modelname +  "_" + cat+ " VBS_SSWW_" + modelname + "_"  + cat +".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + cat + ".log")  

        else:
            for year in years:
                for cat in categories:
                    #print "category: " + (cat)
                    cat = cat+"_"+year+"_"+method
                    if(runSingleCat):
                        runCombine("combine -M Significance "+extraoption+" -n VBS_SSWW_" + modelname +  "_" + cat + " VBS_SSWW_" + modelname + "_"  + cat +".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + cat + ".log")  
                        #runCombine("combine -M FitDiagnostics "+extraoption+" -n VBS_SSWW_" + modelname +  "_" + cat + " VBS_SSWW_" + modelname + "_"  + cat +".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + cat + ".log")  
        os.chdir("..")

def runSinglePointVBS_LS(path_, models, categories, method, runSingleCat, years):
    algostring = " --algo=grid  --points "
    if ":" in models:
        algostring += " 200000 "
    else:
        algostring += " 5000 "
    optionals = " --alignEdges=1 --cminDefaultMinimizerStrategy=0 --setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND" #--autoBoundsPOIs * --autoRange 3" #--fastScan"

    print "Performing LikelihoodScan for operator ", models
    dirmodel = ""
    coeffs = models.split(":")
    setpiecs = []
    for idc, coeff in enumerate(coeffs):
        if len(coeff.split("_")) > 1:
            setpiecs.append(("_")+coeff.split("_")[-1])
        coeffs[idc] = coeff.split("_")[0].replace("F", "c")

    dirmodel = models
    for setpiec in setpiecs:
        dirmodel = models.replace(setpiec, "")
    
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
            if coeff.startswith("cS") or coeff.startswith("cM"):
                intervals.append("-80,80")
            elif coeff.startswith("cT"):
                intervals.append("-10,10")
            elif coeff.startswith("cHW"):
                intervals.append("-30,30")
            elif coeff.startswith("cW"):
                intervals.append("-5,5")

            if idc > 0:
                modComb += ","
                opstring += ","
            modComb += "k_" + coeff
            opstring += coeff


        if len(categories) >= 1:
            if len(years) >1:
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
                for idc, coeff in enumerate(coeffs):
                    if idc > 0:
                        intervalstr += ":"
                    intervalstr += "k_" + coeff + "=" + intervals[idc]
                
                cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/parallelScan.py " + rootdc + " -M MultiDimFit " + algostring + " -m 125 -t -1 --redefineSignalPOIs " + modComb + " --freezeParameters r --setParameters r=1 --setParameterRanges " + intervalstr + " -n " + dirmodel #+ " --autoMaxPOIs r," + modComb + " --squareDistPoiStep" 
                cmd += " " + optionals 
                cmd += " ; hadd -f higgsCombine" + dirmodel + ".MultiDimFit.mH125.root higgsCombine" + dirmodel + ".*.MultiDimFit.mH125.root" 
                print cmd
                runCombine(cmd, "ls_k_" + dirmodel + "_" + method + ".log")
                #os.system("pwd")
                
                cmd = "python " + maindir + "drawLS.py --in0 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --in1 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --coeff " + dirmodel
                if not ":" in models:
                    cmd += " --1D"
                else:
                    cmd += " --2D"
                cmd += " --year " 
                for year in years:
                    cmd += year
                    if year != years[-1]:
                        cmd += "," 
                print cmd
                os.system(cmd)
                
                
            else:
                
                for year in years:
                    cmd = "combineCards.py "
                    for cat in categories:
                        cmd += cat+year+"=%s_%s_%s_%s.txt " %(dirmodel, cat, year, method)
                    
                global_dc = str(dirmodel) + "_" + str(method) + ".txt" 
                cmd += "> " + global_dc #%s_%s.txt" % (model, method)
                #print cmd
                os.system(cmd)

                #generating workspace
                cmd = "text2workspace.py "
                cmd += global_dc + " -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative -o "
                rootdc = dirmodel + "_" + method + ".root"
                cmd += rootdc +" --X-allow-no-signal --PO eftOperators=" + opstring
                #print cmd
                os.system(cmd)

                #launching Combine
                cmd = "combine -M MultiDimFit " + rootdc + algostring +" -m 125  --cminDefaultMinimizerStrategy 0  -t -1 --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameters r=1    --setParameterRanges " + intervalstr + " -n " + dirmodel
                cmd += " " + optionals 
                if ":" in models:
                    cmd += " " + optionals 
                print cmd
                
                runCombine(cmd, "ls_k_" + dirmodel + "_" + method + ".log")
                cmd = "python " + maindir + "drawLS.py --in0 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --in1 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --coeff " + dirmodel
                if not ":" in models:
                    cmd += " --1D"
                else:
                    cmd += " --2D"
                cmd += " --year " 
                for year in years:
                    cmd += year
                    if year != years[-1]:
                        cmd += "," 
                print cmd
                os.system(cmd)
                
                if(runSingleCat): 
                    for cat in categories:
                        #print "category: " + (cat)
                        cat = cat+"_"+year+"_"+method
                        datacat = dirmodel + "_" + cat +".txt"
                        #print datacat
                        cmd = "combine -M MultiDimFit " + datacat + algostring + " -m 125  --cminDefaultMinimizerStrategy 0  -t -1 --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameters r=1    --setParameterRanges " + intervalstr + " -n " + dirmodel
                        cmd += " " + optionals                 
                        print cmd
                        runCombine(cmd, "ls_k_" + dirmodel + "_" + cat + ".log")
                        
                        cmd = "python " + maindir + "drawLS.py --in0 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --in1 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --coeff " + dirmodel
                        if not ":" in models:
                            cmd += " --1D"
                        else:
                            cmd += " --2D"
                        cmd += " --year " 
                        for year in years:
                            cmd += year
                            if year != years[-1]:
                                cmd += "," 
                        print cmd
                        os.system(cmd)
                
        else:
            for year in years:
                for cat in categories:
                    #print "category: " + (cat)
                    cat = cat+"_"+year+"_"+method
                    datacat = dirmodel + "_" + cat +".txt"
                    if(runSingleCat): 
                        #print datacat
                        cmd = "combine -M MultiDimFit " + datacat + algostring + " -m 125  --cminDefaultMinimizerStrategy 0  -t -1 --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameters r=1    --setParameterRanges " + intervalstr + " -n " + dirmodel
                        cmd += " " + optionals 
                        print cmd
                        runCombine(cmd, "ls_k_" + dirmodel + "_" + cat + ".log")  
    
                        cmd = "python " + maindir + "drawLS.py --in0 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --in1 higgsCombine" + dirmodel + ".MultiDimFit.mH125.root --coeff " + dirmodel
                        cmd += " " + optionals 
                        if not ":" in models:
                            cmd += " --1D"
                        else:
                            cmd += " --2D"
                        cmd += " --year " 
                        for year in years:
                            cmd += year
                            if year != years[-1]:
                                cmd += "," 
                        print cmd
                        os.system(cmd)
                
                    
        os.chdir("..")
