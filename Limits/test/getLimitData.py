#! /usr/bin/env python
import sys
import os
import commands
import string
import optparse
from Stat.Limits.limitsUtils import *
from Stat.Limits.settings import *

usage = 'usage: %prog [--cat N]'
parser = optparse.OptionParser(usage)
parser.add_option("-c","--channel",dest="ch",type="string",default="all",help="Indicate channels of interest. Default is all")
parser.add_option('-m', '--method', dest='method', type='string', default = 'hist', help='Run a single method (hist, template, all)')
parser.add_option('-d', '--dir', dest='dir', type='string', default = 'outdir', help='datacards direcotry')
parser.add_option('',"--runSingleCat",dest="runSingleCat",action='store_true', default=False)
(opt, args) = parser.parse_args()
runSingleCat = opt.runSingleCat

os.system("mkdir -p data")

categories = channels
methods = ["hist", "template"]
if opt.ch != "all": 
    ch_clean = opt.ch.replace(" ", "")
    categories = ch_clean.split(",")

if opt.method != "all": 
    meth_clean = opt.method.replace(" ", "")
    methods = meth_clean.split(",")
    
print "cats===="
print categories
 
if runSingleCat:
    for cat in categories: 
        for method in methods:
            for year in years: 
                post = "_" + cat + "_" + str(year) + '_' + method
                getLimits(opt.dir, post)
else:
    for method in methods:
        post = "_" + method
        getLimits(opt.dir,post)
