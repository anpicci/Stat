import ROOT
import os, sys
import optparse
from Stat.Limits.settings import *
from Stat.Limits.datacards_ps import *
#from Stat.Limits.datacards import *

usage = 'usage: %prog -p histosPath -o outputFile'
parser = optparse.OptionParser(usage)
parser.add_option('-i', '--input', dest='ifile', type='string', default="histos.root",help='Where can I find input histos? Default is histos.root')
parser.add_option("-d","--outdir",dest="outdir",type="string",default="outdir",help="Name of the output directory where to store datacards. Default is outdir")
parser.add_option("-m","--mode",dest="mode",type="string",default="hist",help="Kind of shape analysis: parametric fit or fit to histos?. Default is hist")
parser.add_option("-c","--channel",dest="ch",type="string",default="all",help="Indicate channels of interest. Default is all")
parser.add_option("-u","--unblind",dest="unblind",action='store_true', default=False)
parser.add_option('--ls', dest='ls', type='string', default = '', help='wilson coeff')
(opt, args) = parser.parse_args()
sys.argv.append('-b')

ifilename = opt.ifile
outdir = ""
if opt.outdir.startswith("F"):
    outdir = opt.outdir.split("_")[0].replace("F", "f")
else:
    outdir = opt.outdir

print outdir

#os.system("rm " + outdir + "/*/*")

mode = opt.mode
unblind = opt.unblind

wilson = opt.ls

print outdir


if opt.ch != "all": 
    ch_clean = opt.ch.replace(" ", "")
    channels = ch_clean.split(",")

signals = []

print "Signal points: ", sigpoints

if wilson == "":
    model = ""
    for sigp in sigpoints:
        for idp, p in enumerate(sigp):
            model += p
            if idp < len(sigp) - 1:
                model += "_"
            if not p.startswith("WpWp"):
                signal  = "VBS_SSWW_" + p
            else:
                signal  = p
            signals.append(signal)

        #width = p[1]
        #chir = p[2]
        print "Creating datacards for VBS_" + model#, width, chir)
        print "Signals: ", signals


#print "Fit Params", fitParam
try:
    ifile = ROOT.TFile.Open(ifilename)
except IOError:
    print "Cannot open ", ifilename
else:
    pass

ch_year = []

print channels

for y in years:
    channels_years = [ch + '_' + y for ch in channels ]
    ch_year = ch_year + channels_years
    
#print "====> CHANNELS: ", ch_year

for ch in ch_year:
    if wilson != "":
        getCardLS(wilson, ch, ifilename, outdir, mode, unblind)
    else:
        getCard(signals, ch, ifilename, outdir, mode, unblind)
        #for s in signals:
            #getCard(s, ch, ifilename, outdir, mode, unblind)

