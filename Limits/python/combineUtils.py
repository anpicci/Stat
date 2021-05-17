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

    print "evaluate limit for model ", model
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
                cmd += "> WP_M%sW%s_%s_%s.txt" % (mass, width, chir, method)
                print cmd
                os.system(cmd)
                runCombine("combine -M Significance "+extraoption+ " VBS_SSWW_"+model + "_" + method + ".txt -t -1 --expectSignal=1", "significance_VBS_SSWW_" + model + "_" + method + ".log")
            else:
                for year in years:
                    cmd = "combineCards.py "
                    for cat in categories:
                        cmd += cat+"=VBS_SSWW_%s_%s_%s_%s.txt " %(model, cat, year, method)
                    cmd += "> VBS_SSWW_%s_%s.txt" % (model, method)
                    print cmd
                    os.system(cmd)
                    runCombine("combine -M Significance "+extraoption+ " VBS_SSWW_"+ model + "_" + method + ".txt -t -1 --expectSignal=1", "significance_VBS_SSWW_" + model + "_" + method + ".log")

                    if(runSingleCat): 
                        for cat in categories:
                            print "category: " + (cat)
                            cat = cat+"_"+year+"_"+method
                            print  "WP_M"+mass+"W"+width+"_" + chir + "_" + cat +".txt"
                            print "combine -M Significance "+extraoption + " VBS_SSWW_"+model + "_" + cat +".txt", "significance_VBS_SSWW_" + model + "_" + cat + ".log"
                            runCombine("combine -M Significance "+extraoption+" VBS_SSWW_"+model + "_"  + cat +".txt -t -1 --expectSignal=1", "significance_VBS_SSWW_" + model + "_" + cat + ".log")  

        else:
            for year in years:
                for cat in categories:
                    print "category: " + (cat)
                    cat = cat+"_"+year+"_"+method
                    if(runSingleCat): runCombine("combine -M Significance "+extraoption+ " VBS_SSWW_"+model + cat +".txt -t - --expectSignal=1", "significance_VBS_SSWW_" + model + "_" + cat + ".log")  
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
                runCombine("combine -M AsymptoticLimits "+extraoption+" -n VBS_SSWW_" + model + "_" + method + " VBS_SSWW_" + model + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + model + "_" + method + ".log")
            else:
                for year in years:
                    cmd = "combineCards.py "
                    for cat in categories:
                        cmd += cat+"=VBS_SSWW_%s_%s_%s_%s.txt " %(model, cat, year, method)
                    cmd += "> VBS_SSWW_%s_%s.txt" % (model, method)
                    print cmd
                    os.system(cmd)
                    runCombine("combine -M AsymptoticLimits "+extraoption+" -n VBS_SSWW_" + model + "_" + method + " VBS_SSWW_" + model + "_" + method + ".txt", "asymptotic_VBS_SSWW_" + model + "_" + method + ".log")

                    if(runSingleCat): 
                        for cat in categories:
                            print "category: " + (cat)
                            cat = cat+"_"+year+"_"+method
                            print  "WP_M"+mass+"W"+width+"_" + chir + "_" + cat +".txt"
                            print "combine -M Asymptotic "+extraoption+" -n VBS_SSWW_" + model + "_" + cat + " VBS_SSWW_" + model + "_" + cat +".txt", "asymptotic_VBS_SSWW_" + model + "_" + cat + ".log"
                            runCombine("combine -M AsymptoticLimits "+extraoption+" -n VBS_SSWW_" + model +  "_" + cat+ " VBS_SSWW_" + model + "_"  + cat +".txt", "asymptotic_VBS_SSWW_" + model + "_" + cat + ".log")  

        else:
            for year in years:
                for cat in categories:
                    print "category: " + (cat)
                    cat = cat+"_"+year+"_"+method
                    if(runSingleCat): runCombine("combine -M AsymptoticLimits "+extraoption+" -n VBS_SSWW_" + model +  "_" + cat + " VBS_SSWW_" + model + "_"  + cat +".txt", "asymptotic_VBS_SSWW_" + model + "_" + cat + ".log")  
        os.chdir("..")
