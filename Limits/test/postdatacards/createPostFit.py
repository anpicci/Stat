import os
import string
from Stat.Limits.settings import *
import optparse

#os.system("reset")
alphabet = list(string.ascii_uppercase)

usage = "python3 FitAndPlot.py"
parser = optparse.OptionParser(usage)

parser.add_option('--vars', dest='postvars', type='string', default = 'm_o1', help = 'Variables to postfit')
parser.add_option('--folder', dest='folder', type='string', default = 'vUL025', help = 'Variables to postfit')
parser.add_option('--year', dest='year', type='string', default = '2016M,2017,2018', help = 'Variables to postfit')
(opt, args) = parser.parse_args()

srvars = opt.postvars.split(",")

inf = opt.folder

lyear = opt.year
years = lyear.split(",")
yeardir = opt.year.replace("2016M,2017,2018", "RunII")

folders = [inf + '_' + yeardir + '_' + srvar for srvar in srvars]
eosspace = "/eos/home-a/apiccine"

fitfolder = '../fit_' + inf + '_' + sr_var + '_' + cr_var + '_' + yeardir + "_"

print "\nfolders:", folders 
cards = {}
for idv, srvar in enumerate(srvars):
    cards[srvar] = {}
    for c in channels:
        cards[srvar][c] = [card for card in os.listdir("../" + folders[idv] + "/VBS_SSWW_SM/") if c in card and not "RunII" in card]

print cards

string = "combineCards.py"

fitcard = "fit_" + yeardir + ".txt"
fitroot = fitcard.replace("txt", "root")
oldfitcard = yeardir + "_" + sr_var + "_" + cr_var + ".txt"
os.system("cp "+ fitfolder + "/VBS_SSWW_SM/VBS_SSWW_SM_hist.txt " + fitcard)

#fstring = "combineCards.py "
#fstring += "bin1=" + oldfitcard
#fstring += " > " + fitcard
#print("Creating card for " + yeardir + " fit plots...")
#os.system(fstring)

ftstring = "text2workspace.py " + fitcard + " -o " + fitroot
print("Creating workspace for " + yeardir + " fit plots...")
os.system(ftstring)

fitdiagdir = "fitDiagnosticsCombined"
if not os.path.exists(fitdiagdir):
    os.system("mkdir "+ fitdiagdir)
else:
    os.system("rm " + fitdiagdir + "/*")

os.system("combine -M FitDiagnostics " + fitroot + " --out " + fitdiagdir + " -t -1 --toysFreq --rMin -10 --saveNormalizations --saveWithUncertainties --cminDefaultMinimizerStrategy 0")# --robustFit=1 ")

for idv, srvar in enumerate(srvars):
    ofold = "../" + folders[idv] + "/VBS_SSWW_SM/"
    for c in channels:
        tmpcards = []
        cstring = string
        controlcard = "control_card_" + srvar + "_" + c + ".txt"
        controlroot = controlcard.replace("txt", "root")
        for idc, card in enumerate(cards[srvar][c]):
            print c, card
            cbin = c + "_" + card.split("_hist")[0].split("_")[-1]

            tmpcards.append(card)
            os.system("cp " + ofold + card + " . ")
            cstring += " " + cbin + "=" + card
        cstring += " > " + controlcard
        print cstring

        print("Creating card for " + yeardir + " " + srvar + " " + c + " control plots...")
        os.system(cstring)

        ctstring = "text2workspace.py " + controlcard + " -o " + controlroot
        print("Creating workspace for " + yeardir + " " + srvar + " " + c + " control plots...")
        os.system(ctstring)
        
        for tmpcard in tmpcards:
            os.system("rm " + tmpcard)

        os.system("PostFitShapesFromWorkspace -w " + controlroot + " -d " + controlcard + " -o histo_" + srvar + "_" + c + ".root --postfit --sampling -f fitDiagnosticsCombined/fitDiagnosticsTest.root:fit_s --total-shapes")

if not os.path.exists("control_cards"):
    os.system("mkdir control_cards")
os.system("mv control_card_* control_cards")

if not os.path.exists("fit_cards"):
    os.system("mkdir fit_cards")
os.system("mv fit_*root fit_cards")
os.system("mv fit_*txt fit_cards")

if not os.path.exists("histos"):
    os.system("mkdir histos")
os.system("mv histo_*root histos")

os.system("mv higgsCombine* fitDiagnosticsCombined")
