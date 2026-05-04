import os
import subprocess
import optparse
#from Stat.Limits.settings import *
from Stat.Limits.combineUtils import *

usage = 'usage: %prog [--cat N]'
parser = optparse.OptionParser(usage)
parser.add_option("-y","--years",dest="years",type="string",default="all",help="Indicate years of interest. Default is 2016")
parser.add_option('-s', '--syst', dest='syst', type='string', default = '1', help='Set the flag to 0 to remove systematics')
parser.add_option('-m', '--method', dest='method', type='string', default = 'hist', help='Run a single method (all, hist, template)')
parser.add_option('--model', dest='model', type='string', default = 'hist', help='model')
parser.add_option('-S', '--sig', dest='sig', type='int', default = 0, help='Set the flag to 1 to enable significance computation')
parser.add_option('-d', '--dir', dest='dir', type='string', default = 'outdir', help='datacards direcotry')
parser.add_option('--ls', dest='ls', type='string', default = '', help='wilson coeff')
parser.add_option("--runSingleCat",dest="runSingleCat",action='store_true', default=False)
parser.add_option('--profile', dest='profile', default = False, action='store_true', help = 'EFT fit with profiling')
parser.add_option('--settmod"', dest='settmod', type='string', default = 'total', help = 'Specify settmod')
parser.add_option('--HN', dest='HN', default = False, action='store_true', help = 'Use HybridNew')
parser.add_option("-u","--unblind",dest="unblind",action='store_true', default=False)
parser.add_option('--rint', dest='rint', type='string', default = 'None', help = 'r interval for EFT')
parser.add_option('--rfix', dest='rfix', type='string', default = 'None', help = 'r interval for EFT')
parser.add_option('--onlyLin', dest='onlyLin', default = False, action='store_true', help='add dim8 quad in 2D fits')

(opt, args) = parser.parse_args()

import importlib
setname = opt.settmod
#print setname
settmod = importlib.import_module(setname)

bkg = settmod.bkg
histos = settmod.histos
years = settmod.years
leptons = settmod.leptons
sigpoints = settmod.sigpoints
lssamples_1D = settmod.lssamples_1D
syst = settmod.syst
channels = settmod.channels

wilson = opt.ls


if opt.rint == 'None':
    rintt = None
else:
    rintt = opt.rint
if opt.rfix == 'None':
    rfixx = None
else:
    rfixx = opt.rfix

#opt.ch = channels

path_ = os.path.abspath(os.getcwd()) + '/' 
path_ += opt.dir
print path_

if opt.years != "all": 
    y_clean = opt.years.replace(" ", "")
    years = y_clean.split(",")

#categories = [ "BDT1", "BDT2", "CRBDT1", "CRBDT2"]
methods = ["hist"]#, "template"]
#if opt.ch != "all": 
#    ch_clean = [ch.replace(" ", "") for ch in channels]
#    categories = ch_clean.split(",")

if opt.method != "all": 
    meth_clean = opt.method.replace(" ", "")
    methods = meth_clean.split(",")

print "Combinining the following categories: "
for channel in channels:
    print channel

if wilson == "":
    if not ":" in opt.model:
        for point in sigpoints:
            model = point
            print "EFT fit with", model
            #width = point[1]
            #chir = point[2]
            for method in methods:
                runSinglePointVBS_sign(path_, model, channels, method, opt.runSingleCat, years, opt.HN, opt.unblind)
            
    else:
        for method in methods:
            print "Doing 2D SM fit"
            modelewqcd = ""
            for sigps in sigpoints:
                for idp, point in enumerate(sigps):
                    if idp > 0:
                        modelewqcd += ":"
                    modelewqcd += point
            runSinglePointVBS_EWvsQCD(path_, modelewqcd, channels, method, opt.runSingleCat, years, opt.unblind)
            #runSinglePointVBS_AL(path_, model, channels, method, opt.runSingleCat)
            
else:
    for method in methods:
        #print "hello", path_, wilson, channels, method, opt.runSingleCat, years
        runSinglePointVBS_LS(path_, wilson, channels, method, opt.runSingleCat, years, opt.profile, opt.unblind, rintt, rfixx, opt.onlyLin)

