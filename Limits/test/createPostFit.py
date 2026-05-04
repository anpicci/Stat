import os
import string
#from Stat.Limits.settings import *
import optparse
import copy

alphabet = list(string.ascii_uppercase)

usage = "python3 FitAndPlot.py"
parser = optparse.OptionParser(usage)

parser.add_option('--var', dest='postvar', type='string', default = 'm_o1', help = 'Variable to postfit')
parser.add_option('--fitfolder', dest='fitfolder', type='string', default = 'vUL025', help = 'Fit folder')
parser.add_option('--postfolder', dest='postfolder', type='string', default = 'vUL025', help = 'PostFit folder')
parser.add_option('--year', dest='year', type='string', default = '2016M,2017,2018', help = 'Variables to postfit')
parser.add_option('--model', dest='model', type='string', default = 'sm', help = 'Variables to postfit')
parser.add_option('--settmod"', dest='settmod', type='string', default = 'total', help = 'Specify settmod')
parser.add_option("-u","--unblind",dest="unblind",action='store_true', default=False)

(opt, args) = parser.parse_args()

import importlib
setname = opt.settmod

print(setname)
settmod = importlib.import_module(setname)

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
postvar = opt.postvar
model = opt.model
lyear = opt.year
years = lyear.split(",")
yeardir = opt.year.replace("2016M,2017,2018", "RunII")

fitfolder = opt.fitfolder
fithisto = fitfolder + "/shapes/histo_" + opt.model + ".root"
#print fithisto
folders = []

postfold = opt.postfolder#'postfit' + pdftype + "_DYinOS_oneIFSR"

postfold += "/" + postvar
#print postfold
if not os.path.exists(postfold + "/shapes"):
    os.system("mkdir -p " + postfold + "/shapes")
os.system("cp " + fithisto + " " + postfold +"/shapes")

#os.system("pwd")
#print"fitfolder:", fitfolder

cards = {}

cards[postvar] = {}

modd = ""
if opt.model == "SM":
    modd += "VBS_SSWW_"
modd += opt.model
    
ofold = postfold + "/" + modd + "/"
#print "ofold", ofold

os.system("rm " + ofold + "control_*")

for c in channels:
    cardfolder = ofold
    cards[postvar][c] = [card for card in os.listdir(cardfolder) if c in card and not "RunII" in card and card.startswith(modd)]
    
#print "cards"
#for k, v in cards.items():
    #print k, v

string = "combineCards.py"
#print postfold

fitcard = postfold + "/" + modd + "/fit_" + yeardir + "_" + modd + ".txt"
fitroot = fitcard.replace("txt", "root")
#print fitcard

if opt.model == "SM":
    os.system("cp "+ fitfolder + "/VBS_SSWW_SM/VBS_SSWW_SM_hist.txt " + fitcard)
else:
    os.system("cp "+ fitfolder + "/" + modd + "/" + modd +"_hist.txt " + fitcard)

pwd = os.getcwd()
os.chdir(ofold)
print("\nI'm in", ofold)

ftstring = "text2workspace.py " + fitcard.split("/")[-1] + " -o " + fitroot.split("/")[-1]
print("Creating workspace for " + yeardir + " fit plots...")
os.system(ftstring)

fitdiagdir = "fitDiagnosticsCombined" 
if not os.path.exists(fitdiagdir):
    os.system("mkdir -p " + fitdiagdir)
else:
    os.system("rm " + fitdiagdir + "/*")
    pass

print("Creating FitDiagnostics for fitting datacard...")
fitdiagcomm = "combine -M FitDiagnostics " + fitroot.split("/")[-1] + " --out " + fitdiagdir + " --expectSignal=1 --rMin 0.0001 --saveNormalizations --saveWithUncertainties --cminDefaultMinimizerStrategy 0 --plots --toysFreq"#-n _" + tag + " --robustFit=1 "
if not opt.unblind:
    fitdiagcomm += " -t -1 "
print(fitdiagcomm)
os.system(fitdiagcomm)


for c in channels:
    print("\n c", c)
    cstring = copy.deepcopy(string)
    controlcard = "control_card_" + postvar + "_" + c + ".txt"
    controlroot = controlcard.replace("txt", "root")
    if os.path.exists(controlcard):
        os.system("rm " + controlcard)
    if os.path.exists(controlroot):
        os.system("rm " + controlroot)
    
    for idc, card in enumerate(cards[postvar][c]):
        print(c, card)
        cbin = c + "_" + card.split("_hist")[0].split("_")[-1]
        print(cbin)
        cstring += " " + cbin + "=" + card
        
    cstring += " > " + controlcard
    print(ofold)

    print("\nCreating card for " + yeardir + " " + postvar + " " + c + " control plots...")
    print(cstring)

    os.system(cstring)
        
    ctstring = "text2workspace.py " + controlcard + " -o " + controlroot
    print("\nCreating workspace for " + yeardir + " " + postvar + " " + c + " control plots...")
    print(ctstring)
    os.system(ctstring)
    
    print("PostFitShapesFromWorkspace -w " + controlroot + " -d " + controlcard + " --output histo_" + postvar + "_" + c + ".root --postfit -f " + fitdiagdir + "/fitDiagnosticsTest.root:fit_s --total-shapes")
    os.system("PostFitShapesFromWorkspace -w " + controlroot + " -d " + controlcard + " --output histo_" + postvar + "_" + c + ".root --postfit -f " + fitdiagdir + "/fitDiagnosticsTest.root:fit_s --total-shapes")

os.chdir(pwd)

