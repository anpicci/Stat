import os
import ROOT
from Stat.Limits.variables import *
import imp
import importlib
import sys
import optparse
from FitAndPlotUtils import *

os.system("reset")

usage = "python3 FitAndPlot_dev.py"
parser = optparse.OptionParser(usage)

cwd = os.getcwd()

parser.add_option('--fit', dest='varfit', type='string', default = 'm_o1', help = 'Variables to fit in SR (and CRif for the latter is not specified)')
parser.add_option('--folder', dest='folder', type='string', default = 'vUL025', help = 'Analysis folder')
parser.add_option('--user', dest='user', type='string', default = 'apiccine', help = 'Username')
parser.add_option('--cr', dest='varcr', type='string', default = 'same', help = 'Variables to fit in CR (default is the same chosen for SR)')
parser.add_option('--notImpacts', dest='impacts', default = True, action='store_false', help = 'Default does impacts')
parser.add_option('--notUncBreak', dest='uncbreak', default = True, action='store_false', help = 'Default does unc. breaking')
parser.add_option('--eft', dest='eft', type='string', default = 'none', help = 'EFT operators to do LS')
parser.add_option('--Lambda8', dest='Lambda8', default = False, action='store_true', help='add dim8 quad in 2D fits')
parser.add_option('--plot', dest='plotvar', type='string', default = 'all', help = 'Specify variables to plot in postfit')
parser.add_option('--year', dest='year', type='string', default = 'RunII', help = 'Specify year, default is RunII')
parser.add_option('--pol', dest='pol', type='string', default = '', help = 'Specify polarization, default is not included')
parser.add_option('--pdf', dest='pdf', type='string', default = 'total', help = 'Specify type of pdf')
parser.add_option('--cut', dest='cut', type='string', default = 'not', help = 'Specify cut, if needed')
parser.add_option('--tDMcut', dest='tDMcut', default = False, action='store_true', help='Enable tau DecayMode cut')
parser.add_option('--test', dest='test', default = False, action='store_true', help='Enable test')
parser.add_option('--flat', dest='flat', default = False, action='store_true', help='Enable flattening bin')
parser.add_option('--sm', dest='sm', default = False, action='store_true', help = 'Default does not run SM significance')
parser.add_option('--vbs', dest='vbs', default = False, action='store_true', help = 'Default does not run on polarized signals')
parser.add_option('--wpwp', dest='wpwp', default = False, action='store_true', help = 'Default does not run on unpolarized signals EW+QCD')
parser.add_option('--wpwpEW', dest='wpwpEW', default = False, action='store_true', help = 'Default does not run on unpolarized signals EW')
parser.add_option('--EWvsQCD', dest='ewvsqcd', default = False, action='store_true', help = 'Default does not run EW vs QCD fit')
parser.add_option('--noFit', dest='dofit', default = True, action='store_false', help = 'Default does not run SM significance')
parser.add_option('--doPost', dest='postfit', default = False, action='store_true', help = 'Default does not run postfit plots')
parser.add_option('--notCI', dest='doCI', default = True, action='store_false', help = 'Default does not run postfit plots')
parser.add_option('-u', '--unblind', dest = 'unblind', default = False, action = 'store_true', help = 'unblinding SR, default not')
parser.add_option('--WithFakeCR', dest='wfc', default = False, action='store_true', help = 'include Fakes CR')
parser.add_option('--PDFWithTTDY', dest='pdfttdy', default = False, action='store_true', help = 'apply pdf to ttbar and dy')
parser.add_option('--DYrp', dest='DYrp', default = False, action='store_true', help = 'apply rateParam to dy')
(opt, args) = parser.parse_args()

folder = opt.folder

tagfolder = ""
if opt.tDMcut:
    tagfolder = "_tDM"
elif opt.test:
    tagfolder = "_test"
if opt.flat:
    tagfolder += "_flat"

models = []
if opt.sm and not (opt.vbs or opt.wpwp or opt.wpwpEW):
    raise ValueError("With --sm you have to use at least one among --vbs, --wpwp, and --wpwpEW")

if opt.sm and opt.vbs:
    modtag = ""
    if opt.pol != "":
        if not (opt.pol == "TT" or opt.pol == "TL" or opt.pol == "LL"):
            raise ValueError("Polarized can be only TT, TL or LL!")
        modtag += opt.pol + "_"
    modtag += "SM"
    models.append(modtag)
elif opt.eft != "none":
    models = opt.eft.split(",")
elif opt.sm:
    if opt.wpwpEW:
        modtag = "WpWpJJ_EWK"
    elif opt.wpwp:
        modtag = "WpWpJJ"
    models.append(modtag)
elif opt.ewvsqcd:
    modtag = "WpWpJJ_EWK:WpWpJJ_QCD"
    models.append(modtag)
else:
    raise RuntimeError("Please specify a model, with either --sm or --eft [ops]!")

yeartag = opt.year.replace("RunII", "2016M,2017,2018")
DYrp = opt.DYrp
pdftype = opt.pdf

for fitvar, crvar in IterateVars(opt.varfit, opt.varcr):
    print "\n\nStart fitting with", fitvar, "in SR and", crvar, "in CRs"
    for model in models:
        if opt.dofit:
            print "Fitting for model", model
            ### Write the file with metasettings for settings.py, and load the latter recursively
            setmod = 'Stat.Limits.settings_' + model + "_" + fitvar + "_" + crvar
            if opt.wfc:
                setmod += "_WithFakeCR"
            if opt.pdfttdy:
                setmod += "_PDFWithTTDY"
            if DYrp:
                setmod += "_DYrp"
            setmod += "_" + pdftype
            WriteMeta(fitvar, crvar, folder, model, opt.cut, yeartag)
            WriteSett(fitvar, crvar, folder, model, opt.cut, yeartag, opt.wfc, opt.pdfttdy, DYrp, pdftype)
            RecursiveImport(setmod)

            ### Prepare plots for the run and clean remnants from previous fits
            print "yeartag", yeartag
            PrepareToRun(model, fitvar, crvar, folder, yeartag, tagfolder, opt.Lambda8, opt.wfc, opt.pdfttdy, DYrp, pdftype)
            
            ### Run Significance for only-SM models
            if opt.sm:
                RunSMSignificance(model, fitvar, crvar, folder, yeartag, opt.user, tagfolder, opt.wfc, opt.pdfttdy, DYrp, pdftype)
            ### Run EW vs QCD VBS fit
            elif opt.ewvsqcd:
                print "model", model
                RunEWvsQCD(model, fitvar, crvar, folder, yeartag, opt.user, tagfolder, opt.wfc, opt.pdfttdy, DYrp, pdftype)
            ### Run EFT Likelihood Scan for EFT models
            else:
                RunEFTFit(model, fitvar, crvar, folder, yeartag, opt.user, tagfolder, opt.Lambda8, opt.wfc, opt.pdfttdy, DYrp, pdftype)
                pass
            
        ### Run Impacts, if desired
        if opt.impacts:
            #os.system("reset")
            DoImpacts(model, fitvar, crvar, folder, yeartag, opt.user, tagfolder, opt.Lambda8, opt.wfc, opt.pdfttdy, DYrp, pdftype)

        ### Run uncertainties breaking, if desired
        if opt.uncbreak:
            #os.system("reset")
            UncBreak(model, fitvar, crvar, folder, yeartag, opt.user, tagfolder, opt.Lambda8, opt.wfc, opt.pdfttdy, DYrp, pdftype)
        
        ### Run PostFit plots, if desiderd
        if opt.postfit:
            #os.system("reset")
            PrepareAndDoPostFit(model, fitvar, crvar, opt.plotvar, folder, opt.cut, yeartag, opt.user, opt.unblind, tagfolder, opt.Lambda8, opt.wfc, opt.pdfttdy, DYrp, pdftype)


if opt.eft != "none" and not ":" in opt.eft and opt.doCI:
    for model in models:
        print opt.varfit, opt.varcr, folder, model, opt.year
        ProduceCLPlots(opt.varfit, opt.varcr, folder, model, opt.year, tagfolder, opt.wfc, opt.pdfttdy, DYrp, pdftype)

### ordering outputs
os.system("cd " + cwd)
