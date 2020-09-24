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
parser.add_option("-y","--years",dest="years",type="string",default="all",help="Indicate years of interest. Default is 2016")
parser.add_option('-m', '--method', dest='method', type='string', default = 'hist', help='Run a single method (hist, template, all)')
parser.add_option('-d', '--dir', dest='dir', type='string', default = 'outdir', help='datacards direcotry')

(opt, args) = parser.parse_args()

#points = [vec1, vec2, vec3, vec4, vec5, vec6, vec7, vec8, vec9, vec10, vec11, vec12, vec13, vec14, vec15, vec16, vec17, vec18, vec19, vec20, vec21,vec22, vec23, vec24, vec25, vec26, vec27, vec28, vec29, vec30, vec31, vec32, vec33, vec34, vec35, vec36, vec37, vec38, vec39, vec40, vec41]

#points = [vec1, vec2, vec3, vec4, vec5, vec6, vec7, vec8, vec9, vec10, vec11, vec12, vec13, vec14, vec15, vec16, vec17, vec18, vec19, vec20, vec21,vec22, vec23, vec24, vec25]
#points = [vec1, vec2, vec3]
#points = [vec26]

os.system("mkdir -p data")

if opt.years != "all": 
    y_clean = opt.years.replace(" ", "")
    years = y_clean.split(",")

categories = channels
methods = ["hist", "template"]
if opt.ch != "all": 
    ch_clean = opt.ch.replace(" ", "")
    categories = ch_clean.split(",")

if opt.method != "all": 
    meth_clean = opt.method.replace(" ", "")
    methods = meth_clean.split(",")
    
#for y in years: 
#    categories = [c + "_" + y for c in categories]
print "cats===="
print categories
 
#models=["","Wp10","Wp20","Wp30"]

for cat in categories:
    for lep in leptons:
        for method in methods:
            post = "_" + cat + "_" + lep + "_" + method;
            getLimits(opt.dir,post)

#    for cat in categories:
#        post = "_" + cat + "_" + method;
        #if opt.ch="tot"
        #post = "_" + cat + "_" + method;
#        getLimits(opt.dir, post)
