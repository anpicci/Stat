import os
import subprocess
from Stat.Limits.settings import *

def runCombine(cmdStr, logFile):
    "run combine for a specific case"

    cmd = (cmdStr)
    print os.getcwd()
    print cmd
    #writer = open(logFile, 'w') 
    #process = subprocess.call(cmd, shell = True, stdout=writer)
    print cmd + " 2>&1 | tee " + logFile
    os.system(cmd + " 2>&1 | tee " + logFile)
    return

def runSinglePointVBS_sign(path_, model, categories, method, runSingleCat):
    modelname = ""
    for ids, sigp in enumerate(model):
        modelname += "VBS_SSWW_" + sigp
        if ids < len(model) - 1:
            modelname += "_"

    print "evaluate limit for model ", model
    path = "" + path_ + "/" + modelname
    #for ids, sigp in enumerate(model):
        #path += "VBS_SSWW_" + sigp
        #if ids < len(model) - 1:
            #path += "_"
    #path = ("%s/VBS_SSWW_%s" % (path_, model) )
    print "==>path: ", path
    print os.path.exists(path)
    if(os.path.exists(path)):
        print "ok i'm in the directory"
        os.chdir(path)
        print "We are in the right folder ",  len(categories)
        
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
                runCombine("combine -M Significance "+extraoption+ " "+ modelname + "_" + method + ".txt -t -1 --expectSignal=1", "significance_" + modelname + "_" + method + ".log")
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
                    runCombine("combine -M Significance "+extraoption+ " "+ modelname + "_" + method + ".txt -t -1 --expectSignal=1", "significance_" + modelname + "_" + method + ".log")
                    #runCombine("combine -M Significance "+extraoption+ " "+ modelname + "_" + method + ".txt -t -1 ", "significance_" + modelname + "_" + method + ".log")
                    #runCombine("combine -M FitDiagnostics "+ modelname + "_" + method + ".txt --expectSignal=1 --plots --saveShapes --saveWithUncertainties", "fitDiag_VBS_SSWW_" + modelname + ".log")  

                    if(runSingleCat): 
                        for cat in categories:
                            print "category: " + (cat)
                            cat = cat+"_"+year+"_"+method
                            print ""+ modelname + "_" + cat +".txt"
                            print "combine -M Significance "+extraoption + " "+modelname + "_" + cat +".txt", "significance_" + modelname + "_" + cat + ".log"
                            #print "combine -M FitDiagnostics " + modelname + "_" + cat +".txt --expectSignal=1 --plots --saveShapes --saveWithUncertainties"
                            runCombine("combine -M Significance "+extraoption+" "+modelname + "_"  + cat +".txt -t -1 --expectSignal=1", "significance_" + modelname + "_" + cat + ".log")  
                            #runCombine("combine -M Significance "+extraoption+" "+modelname + "_"  + cat +".txt -t -1 ", "significance_" + modelname + "_" + cat + ".log")  
                            #runCombine("combine -M FitDiagnostics " + modelname + "_"  + cat +".txt --expectSignal=1 --plots --saveShapes --saveWithUncertainties", "fitDiag_VBS_SSWW_" + modelname + "_" + cat + ".log")  

        else:
            for year in years:
                for cat in categories:
                    print "category: " + (cat)
                    cat = cat+"_"+year+"_"+method
                    if(runSingleCat):
                        runCombine("combine -M Significance "+extraoption+ " "+modelname + cat +".txt -t -1 --expectSignal=1", "significance_" + modelname + "_" + cat + ".log")  
                        #runCombine("combine -M Significance "+extraoption+ " "+modelname + cat +".txt -t -1 ", "significance_" + modelname + "_" + cat + ".log")  
                        #runCombine("combine -M FitDiagnostics " + modelname + cat +".txt --expectSignal=1 --plots --saveShapes --saveWithUncertainties", "fitDiag_VBS_SSWW_" + modelname + "_" + cat + ".log")  
        os.chdir("..")


def runSinglePointVBS_AL(path_, model, categories, method, runSingleCat):

    print "evaluate limit for VBS_SSWW_" + model
    path = ("%s/VBS_SSWW_%s" % (path_, model) )
    print "==>path: ", path
    print os.path.exists(path)
    if(os.path.exists(path)):
        print "ok i'm in the directory"
        os.chdir(path)
        print "We are in the right folder ",  len(categories)
        extraoption=""
        if len(categories)>=1:
            if len(years)>1:
                cmd = "combineCards.py "
                for year in years:
                    for cat in categories:
                        cmd += cat+year+"=VBS_SSWW_%s_%s_%s_%s.txt " %(model, cat, year, method)
                cmd += "> VBS_SSWW_%s_%s.txt" % (model, method)
                print cmd
                os.system(cmd)
                #runCombine("combine -M Significance "+extraoption+" -n VBS_SSWW_" + modelname + "_" + method + " VBS_SSWW_" + modelname + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + method + ".log")
                #runCombine("combine -M FitDiagnostics "+extraoption+" -n VBS_SSWW_" + modelname + "_" + method + " VBS_SSWW_" + modelname + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + method + ".log")
            else:
                for year in years:
                    cmd = "combineCards.py "
                    for cat in categories:
                        cmd += cat+"=VBS_SSWW_%s_%s_%s_%s.txt " %(model, cat, year, method)
                    cmd += "> VBS_SSWW_%s_%s.txt" % (model, method)
                    print cmd
                    os.system(cmd)
                    #runCombine("combine -M Significance "+extraoption+" -n VBS_SSWW_" + modelname + "_" + method + " VBS_SSWW_" + modelname + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + method + ".log")
                    #runCombine("combine -M FitDiagnostics "+extraoption+" -n VBS_SSWW_" + modelname + "_" + method + " VBS_SSWW_" + modelname + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + method + ".log")

                    if(runSingleCat): 
                        for cat in categories:
                            print "category: " + (cat)
                            cat = cat+"_"+year+"_"+method
                            print  "WP_M"+mass+"W"+width+"_" + chir + "_" + cat +".txt"
                            print "combine -M Asymptotic "+extraoption+" -n VBS_SSWW_" + modelname + "_" + cat + " VBS_SSWW_" + modelname + "_" + cat +".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + cat + ".log"
                            #runCombine("combine -M Significance "+extraoption+" -n VBS_SSWW_" + modelname +  "_" + cat+ " VBS_SSWW_" + modelname + "_"  + cat +".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + cat + ".log")  
                            #runCombine("combine -M FitDiagnostics "+extraoption+" -n VBS_SSWW_" + modelname +  "_" + cat+ " VBS_SSWW_" + modelname + "_"  + cat +".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + cat + ".log")  

        else:
            for year in years:
                for cat in categories:
                    print "category: " + (cat)
                    cat = cat+"_"+year+"_"+method
                    if(runSingleCat):
                        runCombine("combine -M Significance "+extraoption+" -n VBS_SSWW_" + modelname +  "_" + cat + " VBS_SSWW_" + modelname + "_"  + cat +".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + cat + ".log")  
                        #runCombine("combine -M FitDiagnostics "+extraoption+" -n VBS_SSWW_" + modelname +  "_" + cat + " VBS_SSWW_" + modelname + "_"  + cat +".txt", "asymptotic_VBS_SSWW_" + modelname + "_" + cat + ".log")  
        os.chdir("..")

def runSinglePointVBS_LS(path_, model, categories, method, runSingleCat):
    print "performing LikelihoodScan for operator ", model
    dirmodel = model.split("_")[0].replace("F", "f")
    path = ("%s/%s" % (path_, dirmodel) ) 
    print "==>path: ", path
    print os.path.exists(path)
    maindir = os.getcwd() + "/"
    if(os.path.exists(path)):
        modComb = model.split("_")[0].replace("F", "c")
        print "ok i'm in the directory"
        os.chdir(path)
        print "We are in the right folder ",  len(categories)
        extraoption=""
        if model.startswith("FS") or model.startswith("FM"):
            interval = "-80,80"
        elif model.startswith("cHW"):
            interval = "-10,10"
        else:
            interval = "-1,1"

        print "model is", model, "interval is", interval
        if len(categories)>=1:
            if len(years)>1:
                cmd = "combineCards.py "
                for year in years:
                    for cat in categories:
                        cmd += cat+year+"=%s_%s_%s_%s.txt " %(model, cat, year, method)
                global_dc = str(model) + "_" + str(method) + ".txt" 
                cmd += " > " + global_dc #%s_%s.txt" % (model, method)
                print cmd
                os.system(cmd)
                cmd = "text2workspace.py "
                cmd += global_dc + " -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative -o "
                rootdc = model + "_" + method+ ".root"
                cmd += rootdc +" --X-allow-no-signal --PO eftOperators=" + modComb
                print(cmd)
                os.system(cmd)

                cmd = "combine -M MultiDimFit " + rootdc + "  --algo=grid --points 2000  -m 125   -t -1 --redefineSignalPOIs k_" + modComb + " --freezeParameters r  --setParameters r=1    --setParameterRanges k_" + modComb + "=" + interval + "     --verbose -1"
                runCombine(cmd, "ls_k_" + model + "_" + method + ".log")
                cmd = "python " + maindir + "drawLS.py higgsCombineTest.MultiDimFit.mH125.root higgsCombineTest.MultiDimFit.mH125.root k_" + modComb + " "
                for year in years:
                    cmd += year
                    if year != years[-1]:
                        cmd += "," 
                os.system(cmd)
                #TO BE CONTINUED
            else:
                #Combining datacards per each year
                for year in years:
                    cmd = "combineCards.py "
                    for cat in categories:
                        cmd += cat+year+"=%s_%s_%s_%s.txt " %(model, cat, year, method)
                    
                global_dc = str(model) + "_" + str(method) + ".txt" 
                cmd += "> " + global_dc #%s_%s.txt" % (model, method)
                print cmd
                os.system(cmd)


                #generating workspace
                cmd = "text2workspace.py "
                cmd += global_dc + " -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative -o "
                rootdc = model + "_" + method + ".root"
                cmd += rootdc +" --X-allow-no-signal --PO eftOperators=" + modComb
                print cmd

                os.system(cmd)


                #launching Combine
                cmd = "combine -M MultiDimFit " + rootdc + "  --algo=grid --points 2000  -m 125   -t -1 --redefineSignalPOIs k_" + modComb + " --freezeParameters r  --setParameters r=1    --setParameterRanges k_" + modComb + "=" + interval + "  --verbose -1"
                runCombine(cmd, "ls_k_" + model + "_" + method + ".log")
                cmd = "python " + maindir + "drawLS.py higgsCombineTest.MultiDimFit.mH125.root higgsCombineTest.MultiDimFit.mH125.root k_" + modComb + " "
                for year in years:
                    cmd += year
                    if year != years[-1]:
                        cmd += "," 
                os.system(cmd)

                if(runSingleCat): 
                    for cat in categories:
                        print "category: " + (cat)
                        cat = cat+"_"+year+"_"+method
                        datacat = model + "_" + cat +".txt"
                        print datacat
                        cmd = "combine -M MultiDimFit " + datacat + "  --algo=grid --points 2000  -m 125   -t -1 --redefineSignalPOIs k_" + modComb + " --freezeParameters r  --setParameters r=1    --setParameterRanges k_" + modComb + "=" + interval + "  --verbose -1"
                        print cmd
                        runCombine(cmd, "ls_k_" + model + "_" + cat + ".log")  
                        cmd = "python " + maindir + "drawLS.py higgsCombineTest.MultiDimFit.mH125.root higgsCombineTest.MultiDimFit.mH125.root k_" + modComb + " "
                        for year in years:
                            cmd += year
                            if year != years[-1]:
                                cmd += ","
                        os.system(cmd)
        else:
            for year in years:
                for cat in categories:
                    print "category: " + (cat)
                    cat = cat+"_"+year+"_"+method
                    datacat = model + "_" + cat +".txt"
                    if(runSingleCat): 
                        print datacat
                        cmd = "combine -M MultiDimFit " + datacat + " --algo=grid --points 2000  -m 125   -t -1 --redefineSignalPOIs k_" + modComb + " --freezeParameters r  --setParameters r=1    --setParameterRanges k_" + modComb + "=" + interval + "  --verbose -1"
                        print cmd
                        runCombine(cmd, "ls_k_" + model + "_" + cat + ".log")  
                        cmd = "python " + maindir + "drawLS.py higgsCombineTest.MultiDimFit.mH125.root higgsCombineTest.MultiDimFit.mH125.root k_" + modComb +" "
                        for year in years:
                            cmd += year
                            if year != years[-1]:
                                cmd += ","
                        os.system(cmd)

        os.chdir("..")

                
