import ROOT
import collections
import optparse
#ROOT.gROOT.Reset();
#ROOT.gROOT.SetStyle('Plain')
ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch()        # don't pop up canvases
#ROOT.TH1.AddDirectory(False)
from array import array
from Stat.Limits.samples import *
from Stat.Limits.settings import *

class limit(object):
    pass

def readFile(filename, cat):
    v = []
    o = []
    u1 = []
    u2 = []
    d1 = []
    d2 = []
    ifile = open(filename)
    print "Reading ", filename
    for l in ifile.readlines():
        if l.strip()== "": continue
        else:
            print l
            l_split = l.split()
            if l.startswith("y_vals_" + cat):
                v = [float(i) for i in l_split[1:] if float(i)!= 0.0]
            elif l.startswith("y_observed_" + cat):
                o = [float(i) for i in l_split[1:] if float(i)!= 0.0]
            elif l.startswith("y_up_points1_" + cat):
                u1 = [float(i) for i in l_split[1:] if float(i)!= 0.0]
            elif l.startswith("y_up_points2_" + cat):
                u2 = [float(i) for i in l_split[1:] if float(i)!= 0.0]
            elif l.startswith("y_down_points1_" + cat):
                d1 = [float(i) for i in l_split[1:] if float(i)!= 0.0]
            elif l.startswith("y_down_points2_" + cat):
                d2 = [float(i) for i in l_split[1:] if float(i)!= 0.0]
            #print l
    limits = limit()
    limits.v = v
    limits.o = o
    limits.u1 = u1
    limits.u2 = u2
    limits.d1 = d1
    limits.d2 = d2
    return limits

#def plotLimits(cat, year, method):
usage = 'usage: %prog --method method'
parser = optparse.OptionParser(usage)
parser.add_option("-r","--ratio",dest="ratio",action='store_true', default=False)
parser.add_option("-o","--obs",dest="addobserved",action='store_true', default=False)
parser.add_option("-c","--compare",dest="compare", type='string', default = '', help='give a limit to compare with')
parser.add_option('-m', '--method', dest='method', type='string', default = 'hist', help='Run a single method (all, hist, template)')
parser.add_option('-y', '--year', dest='year', type='string', default = 'all', help='Run a single method (Run2, 2016, 2017, 2018, 2016_2017,2016_2017_2018)')
parser.add_option('-v', '--variable', dest='variable', type='string', default = 'mZprime', help='Plot limit against variable v (mZPrime, mDark, rinv, alpha)')
parser.add_option('-l', '--label', dest='label', type='string', default = '', help='Label to be added to canvas name')
(opt, args) = parser.parse_args()

addobserved=opt.addobserved
#addobserved=False

theo = not opt.ratio
'''
for year in years:
    for ch in channels:
        l = readFile("data/limit_%s_%s_%s.txt" % (ch, year, opt.method), "%s_%s_%s" %(ch, year, opt.method))
'''

l = readFile("data/limit_%s.txt" % (opt.method), "%s" %(opt.method))                                                                                                                         

if opt.compare!="":
    lc = readFile("%s" % opt.compare, "hist")

model=""
xvalues_ = []
widths = []
chirs = []

for point in sigpoints:
    var = point[0]
    mass = point[0]
    width = point[1]
    chir = point[2]
    if opt.variable == "width": var = point[1]
    elif opt.variable == "chir": var = point[2]
    if model!="":
        var=var.split(model)[0]
    xvalues_.append(int(var))
    widths.append(int(width))
    chirs.append(chir)

print "Mass points: ", xvalues_

print "Reading file: ", ("data/limit_%s.txt" % (opt.method))
ebar_d1 = [l.o[i] for i in xrange(len(l.v))]
ebar_u1 = [l.u1[i] - l.v[i] for i in xrange(len(l.v))]
ebar_u2 = [l.u2[i] - l.v[i] for i in xrange(len(l.v))]
ebar_d1 = [l.v[i] - l.d1[i] for i in xrange(len(l.v))]
ebar_d2 = [l.v[i] - l.d2[i] for i in xrange(len(l.v))]

if opt.compare!="":
    print "Reading file: ", ( (opt.compare))
    ebar_c_d1 = [lc.o[i] for i in xrange(len(l.v))]
    ebar_c_u1 = [lc.u1[i] - l.v[i] for i in xrange(len(l.v))]
    ebar_c_u2 = [lc.u2[i] - l.v[i] for i in xrange(len(l.v))]
    ebar_c_d1 = [lc.v[i] - l.d1[i] for i in xrange(len(l.v))]
    ebar_c_d2 = [lc.v[i] - l.d2[i] for i in xrange(len(l.v))]

#print "u2 ", l.u2
#print "u1 ", l.u1
#print "median ", l.v
#print "d1 ", l.d1
#print "d2 ", l.d2

#print "U2 ", ebar_u2
#print "U1 ", ebar_u1

med_values = array('f', l.v)
obs_values = array('f', l.o)
if opt.compare!="":
    com_values = array('f', lc.v)

print "Median values: ", med_values
xvalues = array('f', xvalues_)

#y_theo = {str(mass):samples["SVJ_mZprime%d_mDark20_rinv03_alphapeak" % (mass)].sigma for mass in xvalues_ }
y_theo = {mass: sample_dict["WP_M%dW%d_%s_2016" %(mass, width, chir)].sigma for mass, width, chir in zip(xvalues_, widths, chirs) }

#y_theo = [s.sigma for s in samples.itervalues() ]
y_th_xsec = collections.OrderedDict(sorted(y_theo.items()))


print "theory xsec: ", y_th_xsec
#print y_th_xsec.values()
#print l.v

y_xsec_vals = array('f', [l.v[i]*y_th_xsec.values()[i] for i in xrange(len(l.v) ) ])
obs_xsec_vals = array('f', [l.o[i]*y_th_xsec.values()[i] for i in xrange(len(l.v) ) ])
if opt.compare!="":
    com_xsec_vals = array('f', [lc.v[i]*y_th_xsec.values()[i] for i in xrange(len(lc.v) ) ])
    

print "corrected values: ", y_xsec_vals
y_th_xsec_vals = array('f', [th for th in y_th_xsec.itervalues()])

y_bars_d1 =  array('f', ebar_d1)
y_bars_d2 =  array('f', ebar_d2)
y_bars_u1 =  array('f', ebar_u1)
y_bars_u2 =  array('f', ebar_u2)

if theo:
    y_bars_d1 =  array('f', [ebar_d1[i]*y_th_xsec.values()[i] for i in xrange(len(l.v) ) ])
    y_bars_d2 =  array('f', [ebar_d2[i]*y_th_xsec.values()[i] for i in xrange(len(l.v) ) ])
    y_bars_u1 =  array('f', [ebar_u1[i]*y_th_xsec.values()[i] for i in xrange(len(l.v) ) ])
    y_bars_u2 =  array('f', [ebar_u2[i]*y_th_xsec.values()[i] for i in xrange(len(l.v) ) ])

#print "Error bars d1: ", ebar_d1
#print "Error bars xsec d1: ", y_bars_d1

#print "Error bars d2: ", ebar_d2
#print "Error bars xsec d2: ", y_bars_d2

#print "Error bars u1: ", ebar_u1
#print "Error bars xsec u1: ", y_bars_u1

#print "Error bars u2: ", ebar_u2
#print "Error bars xsec u2: ", y_bars_u2


x_bars_1 = array('f', [0]*len(l.v))
x_bars_2 = array('f', [0]*len(l.v))

# need to pick up 
#y_theo = [ s.sigma for s in samples]



print xvalues
print obs_values
obs = ROOT.TGraph( len(l.v), xvalues , obs_values)
if theo: obs = ROOT.TGraph( len(l.v), xvalues ,obs_xsec_vals)
obs.SetLineWidth(2);
#obs.SetLineStyle(2);
obs.SetLineColor(ROOT.kBlack);
obs.SetFillColor(0);
obs.GetXaxis().SetRangeUser(110, 150);

if(opt.compare!=""):
    com = ROOT.TGraph( len(l.v), xvalues , com_values)
    if theo: com = ROOT.TGraph( len(l.v), xvalues ,com_xsec_vals)
    com.SetLineWidth(2);
    #com.SetLineStyle(2);
    com.SetLineColor(ROOT.kOrange-1);
    com.SetFillColor(0);
    com.GetXaxis().SetRangeUser(110, 150);
    

median = ROOT.TGraph( len(l.v), xvalues , med_values)
if theo: median = ROOT.TGraph( len(l.v), xvalues , y_xsec_vals)
median.SetLineWidth(2);
median.SetLineStyle(2);
median.SetLineColor(ROOT.kBlue);
median.SetFillColor(0);
median.GetXaxis().SetRangeUser(110, 150);

theory = ROOT.TGraph( len(l.v), xvalues , y_th_xsec_vals);
theory.SetLineWidth(2);
theory.SetLineStyle(1);
theory.SetLineColor(ROOT.kRed);
theory.SetFillColor(ROOT.kWhite);

band_1sigma = ROOT.TGraphAsymmErrors(len(l.v), xvalues, med_values, x_bars_1, x_bars_2, y_bars_d1, y_bars_u1)
if theo: band_1sigma = ROOT.TGraphAsymmErrors(len(l.v), xvalues, y_xsec_vals, x_bars_1, x_bars_2, y_bars_d1, y_bars_u1)
#band_1sigma = ROOT.TGraphAsymmErrors(len(l.v), masses_value, med_values, 0, 0, 0, 0)
band_1sigma.SetFillColor(ROOT.kGreen + 1)
band_1sigma.SetLineColor(ROOT.kGreen + 1)
band_1sigma.SetMarkerColor(ROOT.kGreen + 1)


band_2sigma = ROOT.TGraphAsymmErrors(len(l.v), xvalues, med_values, x_bars_1, x_bars_2, y_bars_d2, y_bars_u2)
if theo: band_2sigma = ROOT.TGraphAsymmErrors(len(l.v), xvalues,  y_xsec_vals, x_bars_1, x_bars_2, y_bars_d2, y_bars_u2)
band_2sigma.SetTitle("")
band_2sigma.SetFillColor(ROOT.kOrange)
band_2sigma.SetLineColor(ROOT.kOrange)
band_2sigma.SetMarkerColor(ROOT.kOrange)
band_2sigma.GetXaxis().SetTitle("#it{m}_{W'} [GeV]");
band_2sigma.GetXaxis().SetTitleOffset(0.80);
band_2sigma.GetXaxis().SetLabelSize(0.037);
band_2sigma.GetXaxis().SetTitleSize(0.049);

band_2sigma.GetYaxis().SetTitle("#sigma #times BR(W' #rightarrow tb) [pb]");
band_2sigma.GetYaxis().SetTitleOffset(0.75);
band_2sigma.GetYaxis().SetTitleSize(0.054);
band_2sigma.GetYaxis().SetLabelSize(0.041);
band_2sigma.GetYaxis().SetTitleFont(42);

minBand2sigma = min(y_bars_d2)
minTheory = min(y_th_xsec_vals)
minY = min(minBand2sigma, minTheory) 
band_2sigma.SetMinimum(minY)
#band_2sigma.SetMinimum(0.001)

legend = ROOT.TLegend(0.485,0.5,0.93,0.90)
legend.SetTextSize(0.039);
legend.SetFillStyle(0);
legend.SetBorderSize(0);
legend.SetHeader("95% CL upper limits");
# uncomment for ob as well

#legend.AddEntry(obs,"Observed","ex0p");
if(addobserved):
    legend.AddEntry(obs,"CL_{S} sign. injected");
if(opt.compare!=""):
    legend.AddEntry(com,"alternative model");
legend.AddEntry(median,"Median expected");
legend.AddEntry(band_1sigma,"68% expected");
legend.AddEntry(band_2sigma,"95% expected");
legend.AddEntry(theory, "Theoretical #sigma");
# m_legend.AddEntry(theo, "Theoretical #sigma");
legend.SetEntrySeparation(0.3);
legend.SetFillColor(0);

c1 = ROOT.TCanvas()
ROOT.SetOwnership(c1, False)
c1.cd()
c1.SetGrid() 
c1.SetLogy(1)
maxY=med_values[0]+y_bars_u2[0]
minY=med_values[-1]+y_bars_d2[-1]
if(theo):
    maxY=y_xsec_vals[0]+y_bars_u2[0]
    minY=y_xsec_vals[-1]+y_bars_d2[-1]

band_2sigma.GetYaxis().SetRangeUser(minY*0.1, maxY*200.)
c1.Update()
band_2sigma.GetXaxis().SetRangeUser(xvalues_[0], xvalues_[-1])
band_2sigma.Draw("A3")
band_1sigma.Draw("3")
band_1sigma.SetMaximum(300)
median.Draw("L")
if(addobserved):
    obs.Draw("L")
if(opt.compare!=""):
    com.Draw("L")

theory.Draw("L same");
legend.Draw("Same");

lumiTextSize     = 0.6;
lumiTextOffset   = 0.2;
# float cmsTextSize      = 0.75;
# float cmsTextOffset    = 0.1;  // only used in outOfFrame version

pad = ROOT.TPad("pad","pad",0, 0. , 1, 1.);
ROOT.SetOwnership(pad, False)
pad.SetBorderMode(0);

pad.SetTickx(0);
pad.SetTicky(0);
# pad.Draw();
#pad.cd();
t = pad.GetTopMargin();
r = pad.GetRightMargin();
cmsText     = ROOT.TString("CMS")
cmsTextFont   = 61; 
cmsTextSize      = 0.75;

#lumiText = ROOT.TString("41.5 fb^{-1} (13 TeV)")
lumiText = "137.19 fb^{-1} (13 TeV)"
if (opt.year == "2016"):lumiText = "35.92 fb^{-1} (13 TeV)"
elif (opt.year == "2017"):lumiText = "41.53 fb^{-1} (13 TeV)"
elif (opt.year == "2018"):lumiText = "59.74 fb^{-1} (13 TeV)"
elif (opt.year == "Run2"):lumiText = "137.19 fb^{-1} (13 TeV)"
latex_lumi = ROOT.TLatex();
latex_lumi.SetNDC();
latex_lumi.SetTextAngle(0);
latex_lumi.SetTextColor(ROOT.kBlack);

latex_lumi.SetTextFont(42);
latex_lumi.SetTextAlign(31);
latex_lumi.SetTextSize(lumiTextSize*t*0.55);
latex_lumi.DrawLatex(1-r,1-t+lumiTextOffset*t,lumiText);

#latex_cms = ROOT.TLatex()
#latex_cms.SetTextFont(cmsTextFont);
#latex_cms.SetTextSize(cmsTextSize*t);
#latex_cms.SetTextAlign(11);

#l_ch = ROOT.TLatex();
#l_ch.SetNDC();
#l_ch.SetTextSize(lumiTextSize*t*0.71);
#l_ch.SetTextFont(42);
#l_ch.SetTextAlign(11);

l = ROOT.TLatex();
l.SetNDC();
l.SetTextSize(lumiTextSize*t*0.8);
l.SetTextAlign(11); # align left
# l.DrawLatex(0.13,1-t+lumiTextOffset*t*,"CMS");

l.DrawLatex(0.15,0.83,"CMS");

l_preliminary = ROOT.TLatex();
l_preliminary.SetNDC();
l_preliminary.SetTextAlign(31); # align right
l_preliminary.SetTextSize(lumiTextSize*t*0.65);
l_preliminary.SetTextFont(52);
l_preliminary.SetTextAlign(11); # align left
l_preliminary.DrawLatex(0.17,1-t+lumiTextOffset*t,"Work in progress");
l_preliminary.DrawLatex(0.13, 0.81,"");

#l_label = ROOT.TLatex();
#l_label.SetNDC();
#l_label.SetTextAlign(31); # align right
#l_label.SetTextSize(lumiTextSize*t*0.71); #0.5
#l_label.SetTextFont(42);
#l_label.SetTextAlign(11);

c1.Update()
extrastr=opt.label.replace("/", "")
#extrastr+="_nocut_old"
if(addobserved):extrastr=extrastr+"obs"
ofileName = "plots/test_limitPlot_%s_%s.pdf" % (opt.year, opt.method+extrastr)
if theo: ofileName = "plots/test_limitPlot_%s_%s_xsec.pdf" % (opt.year, opt.method+extrastr)

c1.SaveAs(ofileName)

ofileName = "plots/test_limitPlot_%s_%s.png" % (opt.year, opt.method+extrastr)
if theo: ofileName = "plots/test_limitPlot_%s_%s_xsec.png" % (opt.year, opt.method+extrastr)

c1.SaveAs(ofileName)
