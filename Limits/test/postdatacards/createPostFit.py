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
(opt, args) = parser.parse_args()

import importlib
settmod = importlib.import_module("Stat.Limits.settings_" + opt.model)
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

srvars = opt.postvars.split(",")

inf = opt.folder

lyear = opt.year
years = lyear.split(",")
yeardir = opt.year.replace("2016M,2017,2018", "RunII")

folders = [inf + '_' + yeardir + '_' + srvar for srvar in srvars]

eosspace = "/eos/home-a/apiccine"

fitfolder = '../fit_' + inf + '_' + sr_var + '_' + cr_var + '_' + yeardir

#print "\nfolders:", folders 
cards = {}


for idv, srvar in enumerate(srvars):
    cards[srvar] = {}
    for c in channels:
        if opt.model == "SM":
            cardfolder = "../" + folders[idv] + "/VBS_SSWW_SM/"
        else:
            cardfolder = "../" + folders[idv] + "/" + opt.model + "/"
        cards[srvar][c] = [card for card in os.listdir(cardfolder) if c in card and not "RunII" in card]

string = "combineCards.py"

fitcard = "fit_" + yeardir + "_" + opt.model + ".txt"
fitroot = fitcard.replace("txt", "root")
oldfitcard = yeardir + "_" + sr_var + "_" + cr_var + ".txt"

if opt.model == "SM":
    os.system("cp "+ fitfolder + "/VBS_SSWW_SM/VBS_SSWW_SM_hist.txt " + fitcard)
else:
    os.system("cp "+ fitfolder + "/" + opt.model + "/" + opt.model +"_hist.txt " + fitcard)

#fstring = "combineCards.py "
#fstring += "bin1=" + oldfitcard
#fstring += " > " + fitcard
#print("Creating card for " + yeardir + " fit plots...", fstring)
#os.system(fstring)

ftstring = "text2workspace.py " + fitcard + " -o " + fitroot
print("Creating workspace for " + yeardir + " fit plots...")
os.system(ftstring)

fitdiagdir = "fitDiagnosticsCombined_" + opt.model
if not os.path.exists(fitdiagdir):
    os.system("mkdir "+ fitdiagdir)
else:
    os.system("rm " + fitdiagdir + "/*")

os.system("combine -M FitDiagnostics " + fitroot + " --out " + fitdiagdir + " -t -1 --toysFreq --rMin 0.1 --saveNormalizations --saveWithUncertainties --cminDefaultMinimizerStrategy 0 -n _" + opt.model)# --robustFit=1 ")

for idv, srvar in enumerate(srvars):
    if opt.model == "SM":
        ofold = "../" + folders[idv] + "/VBS_SSWW_SM/"
    else:
        ofold = "../" + folders[idv] + "/" + opt.model + "/"
    for c in channels:
        tmpcards = []
        cstring = copy.deepcopy(string)
        controlcard = "control_card_" + srvar + "_" + c + "_" + opt.model + ".txt"
        controlroot = controlcard.replace("txt", "root")
        for idc, card in enumerate(cards[srvar][c]):
            print c, card
            cbin = c + "_" + card.split("_hist")[0].split("_")[-1]

            tmpcards.append(card)
            os.system("cp " + ofold + card + " . ")
            cstring += " " + cbin + "=" + card
        cstring += " > " + controlcard
        print cstring, os.getcwd()
    
        print("Creating card for " + yeardir + " " + srvar + " " + c + " control plots...")
        os.system(cstring)

        ctstring = "text2workspace.py " + controlcard + " -o " + controlroot
        print("Creating workspace for " + yeardir + " " + srvar + " " + c + " control plots...")
        os.system(ctstring)
        #print(ctstring)

        for tmpcard in tmpcards:
            os.system("rm " + tmpcard)

        #os.system("PostFitShapesFromWorkspace -w " + controlroot + " -d " + controlcard + " -o histo_" + srvar + "_" + c + ".root --postfit --sampling -f fitDiagnosticsCombined/fitDiagnosticsTest.root:fit_s --total-shapes")
        os.system("PostFitShapesFromWorkspace -w " + controlroot + " -d " + controlcard + " -o histo_" + srvar + "_" + c + "_" + opt.model + ".root --postfit -f " + fitdiagdir + "/fitDiagnostics_" + opt.model + ".root:fit_s --total-shapes")

if not os.path.exists("control_cards_" + opt.model):
    os.system("mkdir control_cards_" + opt.model)
os.system("mv control_card_*" + opt.model + "* control_cards_" + opt.model)

if not os.path.exists("fit_cards_" + opt.model):
    os.system("mkdir fit_cards_" + opt.model)
os.system("mv fit_*" + opt.model + "*root fit_cards_" + opt.model)
os.system("mv fit_*" + opt.model + "*txt fit_cards_" + opt.model)

if not os.path.exists("histos_" + opt.model):
    os.system("mkdir histos_" + opt.model)
os.system("mv histo_*" + opt.model + "*root histos_" + opt.model)

os.system("mv higgsCombine*" + opt.model + "* " + fitdiagdir)
