import os
import ROOT
from Stat.Limits.variables import *
from Stat.Limits.settings import syst, systgroups, years
import importlib
import sys
import optparse

LineWrite = lambda fname, s : fname.write(s + "\n") 

colors = ["920", "632", "416", "600", "400", "616", "432", "800", "820", "840", "860", "880", "900"]

optionalss = "--robustFit=1 --cminDefaultMinimizerStrategy=0 --setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND"# --fastScan"
optionals_fd = optionalss
#optionals_fd = " --robustFit=1 --cminDefaultMinimizerStrategy=0 --setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --setRobustFitStrategy=1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND"# --fastScan"

def WriteMeta(srvar, crvar, folder, model, cut, year = "2016M,2017,2018"):
    metasett = open("../python/metasett.txt", "w")
    LineWrite(metasett, srvar + "," + crvar)
    LineWrite(metasett, folder)
    LineWrite(metasett, model)
    LineWrite(metasett, year)
    LineWrite(metasett, cut)
    metasett.close()

def RecursiveImport(module):
    if module in sys.modules:
        del sys.modules[module]
    globals()[module] = importlib.import_module(module)
    
def AreVarsIncluded(varlist):
    varexcluded = ""
    for potvar in varlist:
        IsIncluded = False
        for variable in variables:
            if potvar == variable.name:
                IsIncluded = True
                print potvar, "is acceptable as variable to fit!"
                break
        if not IsIncluded:
            varexcluded = potvar
            return False, varexcluded
        else:
            return True, varexcluded

def IterateVars(srvarlist, crvarlist):
    print srvarlist, crvarlist
    fitvars = srvarlist.split(",")
    if not AreVarsIncluded(fitvars)[0]:
        raise RuntimeError(AreVarsIncluded(fitvars)[1] + " are not included in the variables! Please either insert it among the variables, or change it!")

    crvars = []
    if crvarlist == "same":
        for fitvar in fitvars:
            crvars.append(fitvar)
    else:
        crvars = crvarlist.split(",")
        if len(fitvars)!=len(crvars):
            raise RuntimeError("Number of variables for CRs (" + len(crvars) + ") must be equal to the number of variables for SR (" + len(fitvars) + ")!")

    if not AreVarsIncluded(crvars)[0]:
        raise RuntimeError(AreVarsIncluded(crvars)[1] + " is not included in the variables! Please either insert it among the variables, or change it!")

    return zip(fitvars, crvars)

def PrepareToRun(model, srvar, crvar, fold, year = "2016M,2017,2018"):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag
    os.system("python PrepareEOSfolder.py " + fold)
    os.system("rm histo_" + folder + "_" + model + ".root")

def RunSMSignificance(model, srvar, crvar, fold, year = "2016M,2017,2018", username = "apiccine"):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/plot/'
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag

    try:
        os.system("python collectHistos.py -i " + plotrepo + " -o histo_" + folder + "_" + model + ".root")
    except:
        raise RuntimeError("Problems when collecting histos for the fit")
    os.system("python createDatacards.py -i  histo_" + folder + "_SM.root -d " + folder)
    os.system("python runCombine.py -y " + year + " -d " + folder + " -m hist")

def RunEFTFit(model, srvar, crvar, fold, year = "2016M,2017,2018", username = "apiccine"):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/plot/'
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag

    os.system("python collectHistos.py -i " + plotrepo + " -o histo_" + folder + "_" + model + ".root --ls " + model)
    os.system("python createDatacards.py -i histo_" + folder + "_" + model + ".root -d " + folder + " --ls " + model)
    os.system("python runCombine.py -y " + year + " -d " + folder + " -m hist --ls " + model)
    
def DoImpacts(model, srvar, crvar, fold, year = "2016M,2017,2018", username = "apiccine"):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag
    if model == "SM":
        dcname = "VBS_SSWW_SM_hist"
        dcpath = folder + "/VBS_SSWW_SM/" + dcname + ".txt"
    else:
        dcname = model + "_hist"
        dcpath = folder + "/" + model + "/" + dcname + ".txt"

    impactfolder = folder + "/Checks_" + model + "/"
    if not os.path.exists(impactfolder):
        os.system("mkdir " + impactfolder)
    wscard = impactfolder + dcname + ".root"

    os.system("text2workspace.py " + dcpath + " -o " + wscard)

    os.system("combine -M FitDiagnostics -d " + wscard + " -t -1 --expectSignal 0 --rMin -10  --cminDefaultMinimizerStrategy 0 -n _t0")
    os.system("python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py -a fitDiagnostics_t0.root -g plots_t0.root >> " + impactfolder + "fitResults_t0.log")

    os.system("combine -M FitDiagnostics -d " + wscard + " -t -1 --expectSignal 1 --rMin 0.1 --cminDefaultMinimizerStrategy 0 -n _t1")
    os.system("python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> "+ impactfolder + "fitResults_t1.log")

    os.system("combineTool.py -M Impacts -d " + wscard + " -t -1 --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0 --parallel 10")

    os.system("combineTool.py -M Impacts -d " + wscard + " -t -1 --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1 --parallel 10")

    os.system("combineTool.py -M Impacts -d " + wscard + " -o " + impactfolder + "impacts_t0.json -t -1 --expectSignal 0 --rMin -10 --doFits -m 1 -n t0 --parallel 10")
    os.system("combineTool.py -M Impacts -d " + wscard + " -o " + impactfolder + "impacts_t1.json -t -1 --expectSignal 1 --rMin -10 --doFits -m 1 -n t1 --parallel 10")

    os.system("combineTool.py -M Impacts -d " + wscard + " -m 1 -n t0 -o " + impactfolder + "impacts_t0.json --parallel 10")
    os.system("combineTool.py -M Impacts -d " + wscard + " -m 1 -n t1 -o " + impactfolder + "impacts_t1.json --parallel 10")

    os.system("plotImpacts.py -i " + impactfolder + "impacts_t0.json -o " + impactfolder + "impacts_t0")
    os.system("plotImpacts.py -i " + impactfolder + "impacts_t1.json -o " + impactfolder + "impacts_t1")

    os.system("mv higgsCombine_* " + impactfolder)
    os.system("mv fitDiagnostics_t* plots_t* combine_logger.out " + impactfolder)
    '''
    impactfolder = folder + "/Checks_" + model + "/"
    if not os.path.exists(impactfolder):
        os.system("mkdir " + impactfolder)
    wscard = impactfolder + dcname + ".root"

    os.system("text2workspace.py " + dcpath + " -o " + wscard)

    os.system("combine -M FitDiagnostics -d " + wscard + " -t -1 --expectSignal 0 --rMin -10 -n _t0 " + optionals_fd)
    os.system("python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py -a fitDiagnostics_t0.root -g plots_t0.root >> " + impactfolder + "fitResults_t0.log")
    
    os.system("combine -M FitDiagnostics -d " + wscard + " -t -1 --expectSignal 1 --rMin 0.1 -n _t1 " + optionals_fd)
    os.system("python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> "+ impactfolder + "fitResults_t1.log")
    
    os.system("combineTool.py -M Impacts -d " + wscard + " -t -1 --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0 --parallel 10 " + optionalss)
    
    os.system("combineTool.py -M Impacts -d " + wscard + " -t -1 --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1 --parallel 10 " + optionalss)
    
    os.system("combineTool.py -M Impacts -d " + wscard + " -o " + impactfolder + "impacts_t0.json -t -1 --expectSignal 0 --rMin -10 --doFits -m 1 -n t0 --parallel 10 " + optionalss)
    os.system("combineTool.py -M Impacts -d " + wscard + " -o " + impactfolder + "impacts_t1.json -t -1 --expectSignal 1 --rMin -10 --doFits -m 1 -n t1 --parallel 10 " + optionalss)
    
    os.system("combineTool.py -M Impacts -d " + wscard + " -m 1 -n t0 -o " + impactfolder + "impacts_t0.json --parallel 10 " + optionalss)
    os.system("combineTool.py -M Impacts -d " + wscard + " -m 1 -n t1 -o " + impactfolder + "impacts_t1.json --parallel 10 " + optionalss)

    os.system("plotImpacts.py -i " + impactfolder + "impacts_t0.json -o " + impactfolder + "impacts_t0")
    os.system("plotImpacts.py -i " + impactfolder + "impacts_t1.json -o " + impactfolder + "impacts_t1")
   
    os.system("mv higgsCombine_* " + impactfolder)
    os.system("mv fitDiagnostics_t* plots_t* combine_logger.out " + impactfolder)
    '''
def PrepareAndDoPostFit(model, srvar, crvar, plotvars, fold, cut, year = "2016M,2017,2018", username = "apiccine", unblind = False):
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
        print varname, folder

        WriteMeta(varname, varname, folder, model, cut, year)
        RecursiveImport('Stat.Limits.settings')

        #os.system("python PrepareEOSfolder.py " + fold)
        os.system("rm " + yeartag + varname + ".root")
        
        appendix = ""
        
        if not "SM" in model and not model.startswith("WpWp"):
            appendix += " --ls " + model
        
        os.system("python collectHistos.py -i " + plotrepo + " -o " + yeartag + varname + ".root" + appendix)
        os.system("python createDatacards.py -i " + yeartag + varname + ".root -d " + folder + appendix)
    
        WriteMeta(srvar, crvar, folder, model, cut, yeartag[:-1])
        RecursiveImport('Stat.Limits.settings')
        os.chdir("postdatacards")
    
        os.system("python createPostFit.py --vars " + varname + " --folder " + fold + " --year " + year + " --model " + model)
        
        os.chdir("plotter")
    
        poststring = "python PreFitPostFit_v2.py --era " + yeartag[:-1] + " --folder " + fold + " --vars " + var.name + " --fitted " + srvar + "," + crvar + " --model " + model
        if unblind:
            poststring += " -u"
        os.system(poststring)
        os.chdir(pwd)
    
def ProduceCLPlots(srvars, crvars, folder, eftop, era):
    command = "python ciplots.py --sr " + srvars + " --cr " + crvars + " --folder " + folder + " --op " + eftop + " --era " + era
    os.system(command)

def UncBreak(model, srvar, crvar, fold, year = "2016M,2017,2018", username = "apiccine"):
    yeartag = year.replace("2016M,2017,2018", "RunII") + "_"
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag
    file_to_move = []

    if model == "SM":
        dcname = "VBS_SSWW_SM_hist"
        dcpath = folder + "/VBS_SSWW_SM/" + dcname + ".txt"
    else:
        dcname = model + "_hist"
        dcpath = folder + "/" + model + "/" + dcname + ".txt"

    print "datacard:", dcpath
    
    with open(dcpath, 'a') as dcfile:
        dcfile.write("\n")
        for systgroup, subsysts in systgroups.items():
            sysrow = systgroup + "\t="
            approw = ""
            for idsy, systname in enumerate(subsysts):
                if "norm " in systgroup:
                    approw += " " + systname
                elif syst[systname][0] == "lnN":
                    approw += " " + systname
                elif syst[systname][0] == "shape":
                    if syst[systname][-1] == "corr":
                        approw += " " + systname
                    elif syst[systname][-1] == "uncorr":
                        for year in years:
                            approw += " " + systname + "_" + year
            sysrow += approw
            dcfile.write("\n" + sysrow)
    
    impactfolder = folder + "/Checks_" + model + "/"
    if not os.path.exists(impactfolder):
        os.system("mkdir " + impactfolder)
    wscard = impactfolder + dcname + ".root"
    os.system("text2workspace.py " + dcpath + " -o " + wscard)
    
    total = dcname + ".total"
    totalfile = "higgsCombine" + total + ".MultiDimFit.mH120.root"
    #print("combine " + wscard + " -M MultiDimFit -t -1 -m 120 --rMin -2 --rMax 2 --points 200 --saveWorkspace -n " + total + " --algo grid  --cminDefaultMinimizerStrategy 1 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT")
    os.system("combine " + wscard + " -M MultiDimFit -t -1 -m 120 --rMin -2 --rMax 2 --points 200 --saveWorkspace -n " + total + " --algo grid  --cminDefaultMinimizerStrategy 1 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT")
    file_to_move.append(totalfile)

    md = "combine " + totalfile + " -M MultiDimFit -t -1 -m 120 --rMin -2 --rMax 2 --points 200 --algo grid  --cminDefaultMinimizerStrategy 0 --snapshotName MultiDimFit --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT"
    
    plotcomm = "plot1DScan.py " + totalfile + " --main-label \"Total uncert.\" --others "
    bdstr = " -o freeze_ALL_st --breakdown \""
    freeze = md + " --freezeNuisanceGroups "

    for idsy, systgroup in enumerate(systgroups.keys()):
        groupname = systgroup.split(" ")[0]    
        if idsy > 0:
            if idsy < len(systgroups):# - 1:
                freeze += ","
            bdstr += ","
        bdstr += groupname
        if idsy < len(systgroups):# - 1:
            freeze += groupname
            freezename = dcname + ".freeze_" + groupname
            freezefile = "higgsCombine" + freezename + ".MultiDimFit.mH120.root"
            freezecommand = freeze + " -n " + freezename
            os.system(freezecommand)
            file_to_move.append(freezefile)
            plotcomm += "\'" + freezefile + ":Freeze " + groupname + ":" + colors[idsy] + "\' "
        
    freezeall = md + " --freezeParameters allConstrainedNuisances -n"
    freezeallname = dcname + ".freeze_all" 
    freezeallfile = "higgsCombine" + freezeallname + ".MultiDimFit.mH120.root"
    freezeall += " " + freezeallname
    #print(freezeall)
    os.system(freezeall)
    file_to_move.append(freezeallfile)
    plotcomm += "\'" + freezeallfile + ":Freeze all:" + colors[len(systgroup)] + "\' "
    bdstr += ",MCstat,Stat\""

    file_to_move.append("freeze_ALL_st.png")
    file_to_move.append("freeze_ALL_st.pdf")
    file_to_move.append("freeze_ALL_st.root")
    plotcomm += bdstr
    os.system(plotcomm)

    for ftm in file_to_move:
        os.system("mv ./" + ftm + " " + impactfolder)
