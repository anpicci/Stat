import os
import subprocess
import optparse
from Stat.Limits.settings import *
from Stat.Limits.combineUtils import *

usage = 'usage: %prog [--cat N]'
parser = optparse.OptionParser(usage)
parser.add_option("-y","--years",dest="years",type="string",default="all",help="Indicate years of interest. Default is 2016")
parser.add_option('-s', '--syst', dest='syst', type='string', default = '1', help='Set the flag to 0 to remove systematics')
parser.add_option('-m', '--method', dest='method', type='string', default = 'hist', help='Run a single method (all, hist, template)')
parser.add_option('-S', '--sig', dest='sig', type='int', default = 0, help='Set the flag to 1 to enable significance computation')
parser.add_option('-d', '--dir', dest='dir', type='string', default = 'outdir', help='datacards direcotry')
parser.add_option('',"--runSingleCat",dest="runSingleCat",action='store_true', default=False)
(opt, args) = parser.parse_args()

wilson = 'cHW'

opt.ch = channels

path_ = os.path.abspath(os.getcwd()) + '/' 
path_ += opt.dir

if opt.years != "all": 
    y_clean = opt.years.replace(" ", "")
    years = y_clean.split(",")

#categories = [ "BDT1", "BDT2", "CRBDT1", "CRBDT2"]
methods = ["hist", "template"]
#if opt.ch != "all": 
#    ch_clean = [ch.replace(" ", "") for ch in channels]
#    categories = ch_clean.split(",")

if opt.method != "all": 
    meth_clean = opt.method.replace(" ", "")
    methods = meth_clean.split(",")

print "Combinining the following categories: ", channels


for point in sigpoints:
    model = point
    print model
    #width = point[1]
    #chir = point[2]
    for method in methods:
        runSinglePointVBS_sign(path_, model, channels, method, opt.runSingleCat)
        #runSinglePointVBS_AL(path_, model, channels, method, opt.runSingleCat)
'''
for method in methods:
    runSinglePointVBS_LS(path_, wilson, channels, method, opt.runSingleCat)
'''
