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


def runSinglePoint(path_, mZprime, mDark, rinv, alpha, categories, method, runSingleCat):
    print "evaluate limit for mZprime = ", mZprime, " GeV, mDark = ", mDark, " GeV, rinv = ", rinv, " , alpha = ", alpha
    path = ("%s/%s_mDark%s_rinv%s_alpha%s" % (path_, mZprime, mDark, rinv, alpha) )
    print "path: ", path
    if(os.path.exists(path)):
        os.chdir(path)
        
        if len(categories)>1: 
            cmd = "combineCards.py SVJ_mZprime%s_mDark%s_rinv%s_alpha%s_*_%s.txt > SVJ_mZprime%s_mDark%s_rinv%s_alpha%s_%s.txt" % (mZprime, mDark, rinv, alpha, method, mZprime, mDark, rinv, alpha, method)
            print cmd
            os.system(cmd)
            runCombine("combine -M Asymptotic  -n SVJ_mZprime" + mZprime + "_mDark" + mDark + "_rinv" + rinv + "_alpha" + alpha + " -\
m " + mZprime + " SVJ_mZprime" + mZprime + "_mDark" + mDark + "_rinv" + rinv + "_alpha" + alpha  + "_"  + method + ".txt", "asymptotic_mZprime" + mZprime + "_mDark" + mDark + "_rinv" + rinv + "_alpha" + alpha  + "_" + method + ".log")
            
            for cat in categories:
                print "category: " + (cat)
                cat = cat+"_"+method
                
                if(runSingleCat): runCombine("combine -M Asymptotic -S " + opt.syst + " -n SVJ_mZprime" + mZprime + "_mDark" + mDark + "_rinv" + rinv + "_alpha" + alpha + "_" + cat + " -m" + mZprime + " SVJ_mZprime" + mZprime + "_mDark" + mDark + "_rinv" + rinv + "_alpha" + alpha  + "_" + cat +".txt", "asymptotic_mZprime" + mZprime + "_mDark" + mDark + "_rinv" + rinv + "_alpha" + alpha  + "_" + cat + ".log")  
                    
                #if(runSingleCat and opt.sig > 0): 
                     #   runCombine("combine -M ProfileLikelihood -S " + opt.syst + " -n SVJ" + post + " -m %s --signif --pvalue -t 1000 --toysFreq --expectSignal=1 SVJ" + post + ".txt", "profileLikelihood" + post + ".log")

            
        os.chdir("..")



def runSinglePointWprime(path_, mWprime, width, chir, categories, method, runSingleCat):
    mass=mWprime
    print "evaluate limit for mWprime = ", mWprime, " GeV"
    path = ("%s/WP_M%sW%s_%s" % (path_, mass, width, chir) )
    print "==>path: ", path
    print os.path.exists(path)
    if(os.path.exists(path)):
        print "ok i'm in the directory"
        os.chdir(path)
        print "We are in the right folder ",  len(categories)
        extraoption=""
        if len(categories)>1:
            for year in years:
                cmd = "combineCards.py "
                for cat in categories:
                    cmd += cat+"=WP_M%sW%s_%s_%s_%s_%s.txt " %(mass, width, chir, cat, year, method)
                cmd += "> WP_M%sW%s_%s_%s.txt" % (mass, width, chir, method)
                print cmd
                os.system(cmd)
                runCombine("combine -M AsymptoticLimits "+extraoption+" -n WP_M"+mass+"W"+width+ "_" + chir + "_" + method + " -m" + mass + " WP_M"+mass+"W"+width+"_" + chir + "_" + method + ".txt", "asymptotic_WP_M" + mass + "W" + width + "_" + chir + "_" + method + ".log")
                
                if(runSingleCat): 
                    for cat in categories:
                        print "category: " + (cat)
                        cat = cat+"_"+year+"_"+method
                        print  "WP_M"+mass+"W"+width+"_" + chir + "_" + cat +".txt"
                        print "combine -M Asymptotic "+extraoption+" -n WP_M"+mass+"W"+width+ "_" + chir + "_" + cat + " -m" + mass + " WP_M"+mass+"W"+width+"_" + chir + "_" + cat +".txt", "asymptotic_WP_M" + mass + "W" + width + "_" + chir + "_" + cat + ".log"
                        runCombine("combine -M AsymptoticLimits "+extraoption+" -n WP_M"+mass+"W"+width+ "_" + chir +  "_" + cat+ " -m" + mass + " WP_M"+mass+"W"+width+"_" + chir + "_"  + cat +".txt", "asymptotic_WP_M" + mass + "W" + width + "_" + chir + "_" + cat + ".log")  

        else:
            for year in years:
                for cat in categories:
                    print "category: " + (cat)
                    cat = cat+"_"+year+"_"+method
                    if(runSingleCat): runCombine("combine -M AsymptoticLimits "+extraoption+" -n WP_M"+mass+"W"+width+ "_" + chir +  "_" + cat+ " -m" + mass + " WP_M"+mass+"W"+width+"_" + chir + "_"  + cat +".txt", "asymptotic_WP_M" + mass + "W" + width + "_" + chir + "_" + cat + ".log")  
        os.chdir("..")


