import ROOT
import os, sys
import optparse
from Stat.Limits.settings import *
from Stat.Limits.datacards import *

usage = 'usage: %prog -p histosPath -o outputFile'
parser = optparse.OptionParser(usage)
parser.add_option('-i', '--input', dest='ifile', type='string', default="histos.root",help='Where can I find input histos? Default is histos.root')
parser.add_option("-d","--outdir",dest="outdir",type="string",default="outdir",help="Name of the output directory where to store datacards. Default is outdir")
parser.add_option("-m","--mode",dest="mode",type="string",default="hist",help="Kind of shape analysis: parametric fit or fit to histos?. Default is hist")
parser.add_option("-c","--channel",dest="ch",type="string",default="all",help="Indicate channels of interest. Default is all")
parser.add_option("-u","--unblind",dest="unblind",action='store_true', default=False)
(opt, args) = parser.parse_args()
sys.argv.append('-b')

ifilename = opt.ifile
outdir = opt.outdir
mode = opt.mode
unblind = opt.unblind

if opt.ch != "all": 
    ch_clean = opt.ch.replace(" ", "")
    channels = ch_clean.split(",")

signals = []

print "Signal points: ", sigpoints

for p in sigpoints:
    model = p

    print model
    #width = p[1]
    #chir = p[2]
    print "Creating datacards for VBS_" + model#, width, chir)
    signal  = "VBS_SSWW_" + model #, width, chir) 
    print "Signal: ", signal
    signals.append(signal)

    print "Signals: ", signals


print "Fit Params", fitParam
try:
    ifile = ROOT.TFile.Open(ifilename)
except IOError:
    print "Cannot open ", ifilename
else:
    print "Opening file ",  ifilename
    ifile.cd()
    r = ROOT.gDirectory.GetListOfKeys()[0]
    r_years = [r.ReadObj().GetName()[-4:] for r in ROOT.gDirectory.GetListOfKeys() ]
    years =  list(set(r_years))

ch_year = []

for y in years:
    channels_years = [ch + '_' + y for ch in channels ]
    ch_year= ch_year + channels_years
    

print "====> CHANNELS: ", ch_year

for s in signals:
    for ch in ch_year:
        getCard(s, ch, ifilename, outdir, mode, unblind)
