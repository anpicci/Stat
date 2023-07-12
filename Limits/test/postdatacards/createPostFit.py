import os
import string
#from Stat.Limits.settings import *
import optparse
import copy

alphabet = list(string.ascii_uppercase)

usage = "python3 FitAndPlot.py"
parser = optparse.OptionParser(usage)

parser.add_option('--vars', dest='postvars', type='string', default = 'm_o1', help = 'Variables to postfit')
parser.add_option('--folder', dest='folder', type='string', default = 'vUL025', help = 'Variables to postfit')
parser.add_option('--year', dest='year', type='string', default = '2016M,2017,2018', help = 'Variables to postfit')
parser.add_option('--model', dest='model', type='string', default = 'sm', help = 'Variables to postfit')
parser.add_option('--tag', dest='tag', type='string', default = '', help = 'Variables to postfit')
parser.add_option('--tagfold', dest='tagfold', type='string', default = '', help = 'Variables to postfit')
parser.add_option('-u', '--unblind', dest = 'unblind', default = False, action = 'store_true', help = 'unblinding SR, default not')

(opt, args) = parser.parse_args()

import importlib
settmod = importlib.import_module("Stat.Limits.settings_" + opt.tag)
bkg = settmod.bkg
histos = settmod.histos
years = settmod.years
leptons = settmod.leptons
sigpoints = settmod.sigpoints
lssamples_1D = settmod.lssamples_1D
syst = settmod.syst
sr_var = settmod.sr_var
cr_var = settmod.cr_var
channels = settmod.channels
tag = opt.tag
postvars = opt.postvars.split(",")
tagfolder = opt.tagfold.replace("_", "")
inf = opt.folder
model = opt.model
lyear = opt.year
years = lyear.split(",")
yeardir = opt.year.replace("2016M,2017,2018", "RunII")

fitfolder = '../fit_' + inf + '/' + sr_var + '_' + cr_var + '_' + yeardir + "/" + tagfolder
fithisto = fitfolder + "/shapes/histo_" + opt.model + ".root"

folders = []
for postvar in postvars:
    postfold = 'postfit_' + inf + '/' + sr_var + '_' + cr_var + '_' + yeardir
    if tagfolder == "none":
        postfold += "/nom"
    else:
        postfold +="/" + tagfolder.replace("_", "") + "/" + postvar
    folders.append(postfold)
    os.system("cp " + fithisto + " ../" + postfold +"/shapes")

os.system("pwd")
print "\nfolders:", folders 
print"fitfolder:", fitfolder

cards = {}

for idv, postvar in enumerate(postvars):
    cards[postvar] = {}
    print postvar

    for c in channels:
        #print "channel", c
        if opt.model == "SM":
            cardfolder = "../" + folders[idv] + "/VBS_SSWW_SM/"
        else:
            cardfolder = "../" + folders[idv] + "/" + opt.model + "/"
        #print cardfolder
        cards[postvar][c] = [card for card in os.listdir(cardfolder) if c in card and not "RunII" in card]

    #print cards

    string = "combineCards.py"
    postfold = 'postfit_' + inf + '/' + sr_var + '_' + cr_var + '_' + yeardir
    if tagfolder == "none":
        postfold += "/nom"
    else:
        postfold +="/" + tagfolder.replace("_", "") + "/" + postvar
    
    fitcard = "fit_" + yeardir + "_" + tag + ".txt"
fitroot = fitcard.replace("txt", "root")
oldfitcard = yeardir + "_" + sr_var + "_" + cr_var + ".txt"
print oldfitcard, fitcard

#if opt.model == "SM":
    #os.system("cp "+ fitfolder + "/VBS_SSWW_SM/VBS_SSWW_SM_hist.txt " + fitcard)
#else:
    #os.system("cp "+ fitfolder + "/" + opt.model + "/" + opt.model +"_hist.txt " + fitcard)

#fstring = "combineCards.py "
#fstring += "bin1=" + oldfitcard
#fstring += " > " + fitcard
#print("Creating card for " + yeardir + " fit plots...", fstring)
#os.system(fstring)

ftstring = "text2workspace.py " + fitcard + " -o " + fitroot
print("Creating workspace for " + yeardir + " fit plots...")
os.system(ftstring)

fitdiagdir = "fitDiagnosticsCombined_" + tag
if not os.path.exists(fitdiagdir):
    os.system("mkdir "+ fitdiagdir)
else:
    os.system("rm " + fitdiagdir + "/*")

fdcommand = "combine -M FitDiagnostics " + fitroot + " --out " + fitdiagdir 
if not opt.unblind:
    fdcommand += " -t -1 "
fdcommand += " --expectSignal=1 --toysFreq --rMin 0.0001 --saveNormalizations --saveWithUncertainties --cminDefaultMinimizerStrategy 0 -n _" + tag + " --robustFit=1 ")
print "Creating FitDiagnostics for fitting datacard..."
print fdcommand #"combine -M FitDiagnostics " + fitroot + " --out " + fitdiagdir + " -t -1 --toysFreq --expectSignal=1 --rMin 0.0001 --saveNormalizations --saveWithUncertainties --cminDefaultMinimizerStrategy 0 -n _" + tag + " --robustFit=1 "
os.system(fdcommand)#"combine -M FitDiagnostics " + fitroot + " --out " + fitdiagdir + " -t -1 --expectSignal=1 --toysFreq --rMin 0.0001 --saveNormalizations --saveWithUncertainties --cminDefaultMinimizerStrategy 0 -n _" + tag + " --robustFit=1 ")

for idv, postvar in enumerate(postvars):
    if opt.model == "SM":
        ofold = "../" + folders[idv] + "/VBS_SSWW_SM/"
    else:
        ofold = "../" + folders[idv] + "/" + opt.model + "/"
    print ofold, os.getcwd()

    for c in channels:
        tmpcards = []
        cstring = copy.deepcopy(string)
        controlcard = "control_card_" + postvar + "_" + c + "_" + tag + ".txt"
        controlroot = controlcard.replace("txt", "root")
        for idc, card in enumerate(cards[postvar][c]):
            #print c, card

            cbin = c + "_" + card.split("_hist")[0].split("_")[-1]
            newcard = card.replace(".txt", "_" + tag + ".txt")
            tmpcards.append(newcard)
            os.system("cp " + ofold + card + " ./" + newcard)
            cstring += " " + cbin + "=" + newcard
        cstring += " > " + controlcard
    
        print("Creating card for " + yeardir + " " + postvar + " " + c + " control plots...")
        print cstring
        os.system(cstring)

        ctstring = "text2workspace.py " + controlcard + " -o " + controlroot
        print("Creating workspace for " + yeardir + " " + postvar + " " + c + " control plots...")
        print(ctstring)
        os.system(ctstring)
        
        for tmpcard in tmpcards:
            os.system("rm " + tmpcard)

        #os.system("PostFitShapesFromWorkspace -w " + controlroot + " -d " + controlcard + " -o histo_" + postvar + "_" + c + ".root --postfit --sampling -f fitDiagnosticsCombined/fitDiagnosticsTest.root:fit_s --total-shapes")
        os.system("PostFitShapesFromWorkspace -w " + controlroot + " -d " + controlcard + " -o histo_" + postvar + "_" + c + "_" + tag + ".root --postfit -f " + fitdiagdir + "/fitDiagnostics_" + tag + ".root:fit_s --total-shapes")

if not os.path.exists("control_cards_" + opt.model):
    os.system("mkdir control_cards_" + opt.model)
else:
    os.system("rm control_cards_" + opt.model + "/" + "control_card_*" + tag + "*")
os.system("mv control_card_*" + tag + "* control_cards_" + opt.model)

if not os.path.exists("fit_cards_" + opt.model):
    os.system("mkdir fit_cards_" + opt.model)
else:
    os.system("rm fit_cards_" + opt.model + "/fit_*" + tag + "*root")
    os.system("rm fit_cards_" + opt.model + "/fit_*" + tag + "*txt")
os.system("mv fit_*" + tag + "*root fit_cards_" + opt.model)
os.system("mv fit_*" + tag + "*txt fit_cards_" + opt.model)

if not os.path.exists("histos_" + opt.model):
    os.system("mkdir histos_" + opt.model)
else:
    os.system("rm histos_" + opt.model + "/histo_*" + tag + "*root")
os.system("mv histo_*" + tag + "*root histos_" + opt.model)

os.system("mv higgsCombine*" + tag + "* " + fitdiagdir)
