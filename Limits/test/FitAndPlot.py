import os
import ROOT
from Stat.Limits.variables import *
import imp
import importlib
import sys
import optparse
from FitAndPlotUtils import *

os.system("reset")

usage = "python3 FitAndPlot.py"
parser = optparse.OptionParser(usage)

parser.add_option('--fit', dest='varfit', type='string', default = 'm_o1', help = 'Variables to fit in SR (and CR if for the latter is not specified)')
parser.add_option('--folder', dest='folder', type='string', default = 'vUL025', help = 'Analysis folder')
parser.add_option('--user', dest='user', type='string', default = 'apiccine', help = 'Username')
parser.add_option('--cr', dest='varcr', type='string', default = 'same', help = 'Variables to fit in CR (default is the same chosen for SR)')
parser.add_option('--notImpacts', dest='impacts', default = True, action='store_false', help = 'Default does impacts')
parser.add_option('--eft', dest='eft', type='string', default = 'none', help = 'EFT operators to do LS')
parser.add_option('--plot', dest='plotvar', type='string', default = 'all', help = 'Specify variables to plot in postfit')
parser.add_option('--year', dest='year', type='string', default = 'RunII', help = 'Specify year, default is RunII')
parser.add_option('--sm', dest='sm', default = False, action='store_true', help = 'Default does not run SM significance')
parser.add_option('--doPost', dest='postfit', default = False, action='store_true', help = 'Default does not run postfit plots')
parser.add_option('-u', '--unblind', dest = 'unblind', default = False, action = 'store_true', help = 'unblinding SR, default not')
(opt, args) = parser.parse_args()

folder = opt.folder

models = []
if opt.sm:
    models.append("SM")
elif opt.eft != "none":
    models = opt.eft.split(",")
else:
    raise RuntimeError("Please specify a model, with either --sm or --eft [ops]!")

yeartag = opt.year.replace("RunII", "2016M,2017,2018")

for fitvar, crvar in IterateVars(opt.varfit, opt.varcr):
    print "\n\nStart fitting with", fitvar, "in SR and", crvar, "in CRs"
    for model in models:
        print "Fitting for model", model

        ### Write the file with metasettings for settings.py, and load the latter recursively
        WriteMeta(fitvar, crvar, folder, model, yeartag)
        RecursiveImport('Stat.Limits.settings')

        ### Prepare plots for the run and clean remnants from previous fits
        PrepareToRun(fitvar, crvar, folder, yeartag)

        ### Run Significance for only-SM models
        if opt.sm:
            RunSMSignificance(fitvar, crvar, folder, yeartag, opt.user)
        ### Run EFT Likelihood Scan for EFT models
        else:
            RunEFTFit(model, fitvar, crvar, folder, yeartag, opt.user)

        ### Run Impacts, if desired
        if opt.impacts:
            DoImpacts(model, fitvar, crvar, folder, yeartag, opt.user)

        ### Run PostFit plots, if desiderd
        if opt.postfit:
            PrepareAndDoPostFit(model, fitvar, crvar, opt.plotvar, folder, yeartag, opt.user, opt.unblind)

### ordering outputs
bigdir = folder + "_fitmaterial"
if not os.path.exists(bigdir):
    os.system("mkdir " + bigdir)
os.system("mv fit_" + folder + "_* " + bigdir)
os.system("mv " + folder + "_* " + bigdir)
os.system("mv histo*root " + bigdir)

