import os
import ROOT
from Stat.Limits.variables import *
import importlib
import sys
import optparse

os.system("reset")

LineWrite = lambda fname, s : fname.write(s + "\n") 

def WriteMeta(srvar, crvar, folder, model, year = "2016M,2017,2018"):
    metasett = open("../python/metasett.txt", "w")
    LineWrite(metasett, srvar + "," + crvar)
    LineWrite(metasett, folder)
    LineWrite(metasett, model)
    LineWrite(metasett, year)
    metasett.close()

def RecursiveImport(module):
    if module in sys.modules:
        del sys.modules[module]
    globals()[module] = importlib.import_module(module)
    
def AreVarsIncluded(varlist):
    for potvar in varlist:
        IsIncluded = False
        for variable in variables:
            if potvar == variable.name:
                IsIncluded = True
                print potvar, "is acceptable as variable to fit!"
                break
        if not IsIncluded:
            return False
        else:
            return True

def IterateVars(srvarlist, crvarlist):
    print srvarlist, crvarlist
    fitvars = srvarlist.split(",")
    if not AreVarsIncluded(fitvars):
        raise RuntimeError(fitvars + " are not included in the variables! Please either insert it among the variables, or change it!")

    crvars = []
    if crvarlist == "same":
        for fitvar in fitvars:
            crvars.append(fitvar)
    else:
        crvars = crvarlist.split(",")
        if len(fitvars)!=len(crvars):
            raise RuntimeError("Number of variables for CRs (" + len(crvars) + ") must be equal to the number of variables for SR (" + len(fitvars) + ")!")

    if not AreVarsIncluded(crvars):
        raise RuntimeError(crvars + " is not included in the variables! Please either insert it among the variables, or change it!")

    return zip(fitvars, crvars)

def PrepareToRun(srvar, crvar, fold, year = "2016M,2017,2018"):
    yeartag = year.replace("2016M,2017,2018", "RunII") + "_"
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag
    os.system("python PrepareEOSfolder.py " + fold)
    os.system("rm histo" + yeartag + folder + ".root")

def RunSMSignificance(srvar, crvar, fold, year = "2016M,2017,2018", username = "apiccine"):
    yeartag = year.replace("2016M,2017,2018", "RunII") + "_"
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/plot/'
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag

    os.system("python collectHistos.py -i " + plotrepo + " -o histo" + yeartag + folder + ".root")
    os.system("python createDatacards.py -i histo" + yeartag + folder + ".root -d " + folder)
    os.system("python runCombine.py -y " + year + " -d " + folder + " -m hist")

def RunEFTFit(model, srvar, crvar, fold, year = "2016M,2017,2018", username = "apiccine"):
    yeartag = year.replace("2016M,2017,2018", "RunII") + "_"
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/plot/'
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag

    os.system("python collectHistos.py -i " + plotrepo + " -o histo" + yeartag + folder + ".root --ls " + model)
    os.system("python createDatacards.py -i histo" + yeartag + folder + ".root -d " + folder + " --ls " + model)
    os.system("python runCombine.py -y " + year + " -d " + folder + " -m hist --ls " + model)
    
def DoImpacts(model, srvar, crvar, fold, year = "2016M,2017,2018", username = "apiccine"):
    yeartag = year.replace("2016M,2017,2018", "RunII") + "_"
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag
    if model == "SM":
        dcname = "VBS_SSWW_SM_hist"
        dcpath = folder + "/VBS_SSWW_SM/" + dcname + ".txt"
    else:
        dcname = model + "_hist"
        dcpath = folder + "/" + model + "/" + dcname + ".txt"

    impactfolder = folder + "/Checks_" + model + "/"
    wscard = impactfolder + dcname + ".root"

    os.system("text2workspace.py " + dcpath + " -o wscard")
    
    os.system("combine -M FitDiagnostics -d " + wscard + " -t -1 --toysFreq --expectSignal 0 --rMin -10 --forceRecreateNLL -n _t0")
    os.system("python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py -a fitDiagnostics_t0.root -g plots_t0.root >> " + impactfolder + "fitResults_t0.log")

    os.system("combine -M FitDiagnostics -d " + wscard + " -t -1 --toysFreq --expectSignal 1 --rMin -10 --forceRecreateNLL -n _t1")
    os.system("python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> "+ impactfolder + "fitResults_t1.log")

    os.system("combineTool.py -M Impacts -d " + wscard + " -t -1 --toysFreq --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0 --parallel 10")
    os.system("combineTool.py -M Impacts -d " + wscard + " -t -1 --toysFreq --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1 --parallel 10")

    os.system("combineTool.py -M Impacts -d " + wscard + " -o " + impactfolder + "impacts_t0.json -t -1 --expectSignal 0 --rMin -10 --doFits -m 1 -n t0 --parallel 10")
    os.system("combineTool.py -M Impacts -d " + wscard + " -o " + impactfolder + "impacts_t1.json -t -1 --expectSignal 1 --rMin -10 --doFits -m 1 -n t1 --parallel 10")

    os.system("combineTool.py -M Impacts -d " + wscard + " -m 1 -n t0 -o " + impactfolder + "impacts_t0.json --parallel 10")
    os.system("combineTool.py -M Impacts -d " + wscard + " -m 1 -n t1 -o " + impactfolder + "impacts_t1.json --parallel 10")

    os.system("plotImpacts.py -i " + impactfolder + "impacts_t0.json -o " + impactfolder + "impacts_t0")
    os.system("plotImpacts.py -i " + impactfolder + "impacts_t1.json -o " + impactfodler + "impacts_t1")

    os.system("mv higgsCombine_* " + impactfolder)
    os.system("mv fitDiagnostics_t* plots_t* combine_logger.out " + impactfolder)

def PrepareAndDoPostFit(model, srvar, crvar, plotvars, fold, year = "2016M,2017,2018", username = "apiccine", unblind = False):
    pwd = os.getcwd()
    vartopost = []
    yeartag = year.replace("2016M,2017,2018", "RunII") + "_"
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/plot/'

    if plotvars == "all":
        vartopost = variables
    else:
        for var in variables:
            if var.name in plotvars.split(","):
                vartopost.append(var)

    for var in vartopost:
        varname = var.name
        folder = fold + '_' + yeartag + varname
        
        WriteMeta(varname, varname, folder, model, year)
        RecursiveImport('Stat.Limits.settings')
        os.system("python PrepareEOSfolder.py " + fold)
        os.system("rm " + yeartag + varname + ".root")
        os.system("python collectHistos.py -i " + plotrepo + " -o " + yeartag + varname + ".root")
        os.system("python createDatacards.py -i " + yeartag + varname + ".root -d " + folder)
        
        WriteMeta(srvar, crvar, folder, model, yeartag[:-1])
        RecursiveImport('Stat.Limits.settings')
        os.chdir("postdatacards")
        os.system("python createPostFit.py --vars " + varname + " --folder " + fold + " --year " + year)

        os.chdir("plotter")
        poststring = "python PreFitPostFit_v2.py --era " + yeartag[:-1] + " --folder " + fold + " --vars " + var.name + " --fitted " + srvar + "," + crvar
        if unblind:
            poststring += " -u"
        os.system(poststring)
        os.chdir(pwd)
            
