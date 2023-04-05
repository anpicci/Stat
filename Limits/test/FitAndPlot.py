import os
import ROOT
from Stat.Limits.variables import *
import imp
import importlib
import sys
import optparse
from FitAndPlotUtils import *
import copy

os.system("reset")

usage = "python3 FitAndPlot.py"
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
parser.add_option('--regions', dest='regions', type='string', default = 'SR,CRTT,CROS,CRF', help = 'Regions to fit')
parser.add_option('--leptons', dest='leptons', type='string', default = 'muon,electron', help = 'Channels to include')
parser.add_option('--tDMcut', dest='tDMcut', default = False, action='store_true', help='Enable tau DecayMode cut')
parser.add_option('--test', dest='test', default = False, action='store_true', help='Enable test')
parser.add_option('--vbroad', dest='vbroad', default = False, action='store_true', help='Enable very broad')
parser.add_option('--vvbroad', dest='vvbroad', default = False, action='store_true', help='Enable vvery broad')
parser.add_option('--vvvbroad', dest='vvvbroad', default = False, action='store_true', help='Enable vvvery broad')
parser.add_option('--noflat', dest='flat', default = True, action='store_false', help='Disable flattening bin')
parser.add_option('--sm', dest='sm', default = False, action='store_true', help = 'Default does not run SM significance')
parser.add_option('--vbs', dest='vbs', default = False, action='store_true', help = 'Default does not run on polarized signals')
parser.add_option('--wpwp', dest='wpwp', default = False, action='store_true', help = 'Default does not run on unpolarized signals EW+QCD')
parser.add_option('--wpwpEW', dest='wpwpEW', default = False, action='store_true', help = 'Default does not run on unpolarized signals EW')
parser.add_option('--EWvsQCD', dest='ewvsqcd', default = False, action='store_true', help = 'Default does not run EW vs QCD fit')
parser.add_option('--noFit', dest='dofit', default = True, action='store_false', help = 'Default does not run SM significance')
parser.add_option('--doPost', dest='postfit', default = False, action='store_true', help = 'Default does not run postfit plots')
parser.add_option('--notCI', dest='doCI', default = True, action='store_false', help = 'Default does not run postfit plots')
parser.add_option('-u', '--unblind', dest = 'unblind', default = False, action = 'store_true', help = 'unblinding SR, default not')
parser.add_option('--PDFWithTTDY', dest='pdfttdy', default = False, action='store_true', help = 'apply pdf to ttbar and dy')
parser.add_option('--DYrp', dest='DYrp', default = False, action='store_true', help = 'apply rateParam to dy')
parser.add_option('--noQCDScale', dest='noQCDScale', default = False, action='store_true', help = 'apply rateParam to dy')
parser.add_option('--flnN', dest='flnN', default = False, action='store_true', help = 'apply lognormal to fakes')
parser.add_option('--frp', dest='frp', default = False, action='store_true', help = 'apply rateParam to fakes')
parser.add_option('--noFakeStats', dest='nofs', default = False, action='store_true', help = 'do not apply mcstats to fakes')
parser.add_option('--profile', dest='profile', default = False, action='store_true', help = 'EFT fit with profiling')
parser.add_option('--HN', dest='HN', default = False, action='store_true', help = 'fit with HybridNew instead of AsymptoticLimits')

(opt, args) = parser.parse_args()

folder = opt.folder

tagfolder = ""
#print opt.tDMcut, opt.test
if opt.tDMcut:
    tagfolder = "_tDM"
elif opt.test:
    tagfolder = "_test"
elif opt.vbroad:
    tagfolder = "_vbroad"
elif opt.vvbroad:
    tagfolder = "_vvbroad"
elif opt.vvvbroad:
    tagfolder = "_vvvbroad"
if not opt.flat:
    tagfolder += "_noflat"

regions = opt.regions.split(",")
leptons = opt.leptons.split(",")

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

for model in models:
    sfitfolder = ""
#for fitvar, crvar in IterateVars(opt.varfit, opt.varcr):
    for fitvar, crvar in IterateVars(opt.varfit, opt.varcr):
    #for model in models:
        print "\n\nStart fitting with", fitvar, "in SR and CRs and", crvar, "in Fake CR"
        print "\tRegions:", opt.regions
        print "\tChannels:", opt.leptons
    
        #fitfolder = "FitResults_" + folder
        #fitfolder = "FITRESULTS_" + folder
        #fitfolder = "FIT_cons_" + folder
        fitfolder = "FIT_fstats_jes_sep_nottRP_" + folder
        #fitfolder = "FIT_" + folder
        #fitfolder = "FITPROVA_" + folder
        if opt.unblind:
            fitfolder += "_DF"
        else:
            fitfolder += "_TF"
        fitfolder += "/" + yeartag.replace("2016M,2017,2018", "RunII") + "_" + opt.regions.replace(",", "-") + "_" + opt.leptons.replace(",", "-") + "/"
        setmod = 'Stat.Limits.settings_' + model + "_" + fitvar + "_" + crvar
        setitle = "../python/settings_" + model + "_" + fitvar + "_" + crvar

        print "Fitting for model", model
        ### Write the file with metasettings for settings.py, and load the latter recursively
        if opt.pdfttdy:
            if not fitfolder.endswith("/"):
                fitfolder += "_"
            fitfolder += "PDFWithTTDY"
            setmod += "_PDFWithTTDY"
            setitle += "_PDFWithTTDY"
        if DYrp:
            if not fitfolder.endswith("/"):
                fitfolder += "_"
            fitfolder += "OSrp"
            setmod += "_OSrp"
            setitle += "_OSrp"
        if opt.flnN:
            if not fitfolder.endswith("/"):
                fitfolder += "_"
            fitfolder += "flnN"
            setmod += "_flnN"
            setitle += "_flnN"
        if opt.frp:
            if not fitfolder.endswith("/"):
                fitfolder += "_"
            fitfolder += "frp"
            setmod += "_frp"
            setitle += "_frp"
        if opt.noQCDScale:
            if not fitfolder.endswith("/"):
                fitfolder += "_"
            fitfolder += "noQCDS"
            setmod += "_noQCDS"
            setitle += "_noQCDS"
        if opt.nofs:
            if not fitfolder.endswith("/"):
                fitfolder += "_"
            fitfolder += "noFakeStats"
            setmod += "_noFakeStats"
            setitle += "_noFakeStats"
        if fitfolder.endswith("/"):
            fitfolder += "noaddopt"
        
        setmod += "_" + pdftype + "_" + opt.regions.replace(",", "-") + "_" + opt.leptons.replace(",", "-")
        setitle += "_" + pdftype + "_" + opt.regions.replace(",", "-") + "_" + opt.leptons.replace(",", "-") + ".py"

        fitfolder += "/" 
        
        if tagfolder == "":
            fitfolder += "nom"
        else:
            fitfolder += tagfolder.replace("_", "")
        if opt.Lambda8:
            fitfolder += "_Lambda8"
        
        sfitfolder = copy.deepcopy(fitfolder)
        fitfolder += "/" + fitvar + "_" + crvar

        postfitfolder = "Post" + fitfolder
        if not os.path.exists(fitfolder):
            os.system("mkdir -p " + fitfolder)
        if not os.path.exists(postfitfolder):
            os.system("mkdir -p " + postfitfolder)
    
        if opt.dofit:
            WriteMeta(fitvar, crvar, folder, model, opt.cut, yeartag)
            WriteSett(fitvar, crvar, folder, model, opt.cut, yeartag, opt.pdfttdy, DYrp, pdftype, opt.flnN, opt.frp, regions, leptons, setitle, opt.noQCDScale)
            #RecursiveImport(setmod)

            ### Prepare plots for the run and clean remnants from previous fits
            PrepareToRun(folder, yeartag, tagfolder, fitfolder)
            
            ### Run Significance for only-SM models
            if opt.sm:
                #RunSMSignificance(model, fitvar, crvar, folder, yeartag, opt.user, tagfolder, opt.pdfttdy, DYrp, pdftype, opt.flnN, opt.frp, opt.HN, setmod, setitle, fitfolder)
                RunSMSignificance(model, fitvar, crvar, folder, yeartag, opt.user, tagfolder, pdftype, opt.HN, setmod, fitfolder, opt.unblind)

            
            ### Run EW vs QCD VBS fit
            elif opt.ewvsqcd:
                print "model", model
                RunEWvsQCD(model, fitvar, crvar, folder, yeartag, opt.user, tagfolder, pdftype, setmod, fitfolder, opt.unblind)
            
            ### Run EFT Likelihood Scan for EFT models
            else:
                RunEFTFit(model, fitvar, crvar, folder, yeartag, opt.user, tagfolder, opt.Lambda8, pdftype, opt.profile, setmod, fitfolder, opt.unblind)
                pass
            
        ### Run Impacts, if desired
        if opt.impacts:
            #os.system("reset")
            DoImpacts(model, fitvar, crvar, yeartag, opt.user, setmod, fitfolder, opt.unblind)

        ### Run uncertainties breaking, if desired
        if opt.uncbreak:
            #os.system("reset")
            UncBreak(model, fitvar, crvar, yeartag, opt.user, setmod, fitfolder, opt.unblind)

        
        ### Run PostFit plots, if desiderd
        if opt.postfit:
            #os.system("reset")
            PrepareAndDoPostFit(model, fitvar, crvar, opt.plotvar, folder, opt.cut, yeartag, opt.user, tagfolder, opt.Lambda8, opt.pdfttdy, DYrp, opt.noQCDScale, pdftype, opt.flnN, opt.frp, setmod, setitle, fitfolder, postfitfolder, regions, leptons, opt.unblind) 
        

    #if opt.eft != "none" and not ":" in opt.eft and opt.doCI:
    #for model in models:
    #print "model in FitAndPlot", model 
    #print "FitAndPlot", opt.varfit, opt.varcr, folder, model, opt.year, tagfolder
    if opt.eft != "none" and not ":" in opt.eft and opt.doCI:
        #ProduceCLPlots(fitvar, crvar, model, opt.year, fitfolder)
        ProduceCLPlots(opt.varfit, opt.varcr, model, opt.year, sfitfolder)
