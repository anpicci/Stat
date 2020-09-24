import ROOT
import collections
import optparse
#ROOT.gROOT.Reset();
#ROOT.gROOT.SetStyle('Plain')
#ROOT.gStyle.SetPalette(1)
#ROOT.gStyle.SetOptStat(0)
#ROOT.gROOT.SetBatch()        # don't pop up canvases
#ROOT.TH1.AddDirectory(False)
from array import array
from Stat.Limits.samples.toPlot import samples
from Stat.Limits.settings import *





pulls=[-0.42,-0.29,-0.47,-0.28]
sigmas=[0.8,0.53,0.52,0.45]

bias=[-0.42,-0.11,-0.19,-0.11]
deltar=[0.8,0.21,0.24,0.19]

points = [700,1000,1500,1700]


pval = array("f",pulls) 
sval = array("f",sigmas) 
xval = array("f",points) 
#//sbar = [ pulls[m]- for m in pulls]
xbar = array('f', [0]*len(points))
#xbar2 = array('f', [0]*len(l.v))

bval = array("f",bias) 
sbval = array("f",deltar) 

pull = ROOT.TGraphErrors(len(points),xval,pval,xbar,sval)

bsig = ROOT.TGraphErrors(len(points),xval,bval,xbar,sbval)

pull.GetYaxis().SetTitle("r-r_{in}/#sigma_{r}");
pull.GetYaxis().SetRangeUser(-2,2)
pull.SetMarkerStyle(20)


c1 = ROOT.TCanvas()
ROOT.SetOwnership(c1, False)
c1.cd()
c1.SetGrid() 
#c1.SetLogy(1)
pull.Draw("AP")
c1.SaveAs("Pulls.png")

c1.cd()
bsig.GetYaxis().SetTitle("r-r_{in}/r");
bsig.GetYaxis().SetRangeUser(-2,2)
bsig.SetMarkerStyle(20)

bsig.Draw("AP")
c1.SaveAs("Bias.png")

