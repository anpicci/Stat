import os
import sys
import ROOT
import optparse
from array import array
from FitAndPlotUtils import *
#os.system("reset")
from Stat.Limits.variables import *

#print "hello"

def EvalGraph(x, graph):
    return gr.Eval(x[0])

ROOT.gROOT.SetBatch()

usage = "python3 FitAndPlot.py"
parser = optparse.OptionParser(usage)

parser.add_option('--srvar', dest='sr', type=str, default = 'm_o1', help='var in sr')
parser.add_option('--crvar', dest='cr', type=str, default = 'm_o1', help='var in cr')
parser.add_option('--npoints', dest='npoints', type='int', default = 1, help = 'Analysis folder')
parser.add_option('--folder', dest='folder', type='str', default = "vUL025", help = 'Folder to fit')
parser.add_option('--op', dest='eftop', type='str', default = "cW", help = 'EFT operator')
parser.add_option('--era', dest='era', type='str', default = "RunII", help = 'era')

(opt, args) = parser.parse_args()

varloops = IterateVars(opt.sr, opt.cr)
print varloops

gr = ROOT.TGraph()
def myfunc(x):
    #print x
    return gr.Eval(x[0])

lumi = {'2016M': 36.3, '2017': 41.48, '2018':59.83, "RunII":138}

eftop = opt.eftop.split("_")[0]

if not (opt.eftop.startswith("c") and opt.eftop.endswith("1")):
    efold = opt.eftop.split("_")[0]
else:
    efold = opt.eftop

ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetFrameBorderMode(0)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPalette(1, array('i', [0]))
ROOT.gStyle.SetTitleX(0.5) #title X location
ROOT.gStyle.SetTitleY(0.96) #title Y location
ROOT.gStyle.SetPaintTextFormat(".2f")

tdrStyle = ROOT.TStyle("tdrStyle","Style for P-TDR")
tdrStyle.SetCanvasBorderMode(0)
tdrStyle.SetCanvasColor(ROOT.kWhite)
tdrStyle.SetCanvasDefH(600) #Height of canvas
tdrStyle.SetCanvasDefW(600) #Width of canvas
tdrStyle.SetCanvasDefX(0) #Position on screen
tdrStyle.SetCanvasDefY(0)

#For the Pad:                                                                                                                   
tdrStyle.SetPadBorderMode(0)
#tdrStyle.SetPadBorderSize(Width_t size = 1)                                                                                  
tdrStyle.SetPadColor(ROOT.kWhite)
tdrStyle.SetPadGridX(1)
tdrStyle.SetPadGridY(1)
tdrStyle.SetGridColor(0)
tdrStyle.SetGridStyle(3)
tdrStyle.SetGridWidth(1)

#For the frame:                                                                                                                 
tdrStyle.SetFrameBorderMode(0)
tdrStyle.SetFrameBorderSize(1)
tdrStyle.SetFrameFillColor(0)
tdrStyle.SetFrameFillStyle(0)
tdrStyle.SetFrameLineColor(1)
tdrStyle.SetFrameLineStyle(1)
tdrStyle.SetFrameLineWidth(1)

#For the histo:                                                                                                                 
tdrStyle.SetHistFillColor(0)
#tdrStyle.SetHistFillStyle(0)                                                                                                 
tdrStyle.SetHistLineColor(1)
tdrStyle.SetHistLineStyle(0)
tdrStyle.SetHistLineWidth(1)
#tdrStyle.SetLegoInnerR(rad = 0.5)                                                                                    
#tdrStyle.SetNumberContours(number = 20)                                                                                
#tdrStyle.SetEndErrorSize(0)                                                                                                  
tdrStyle.SetErrorX(0.)
#tdrStyle.SetErrorMarker(20)                                                                                                   
tdrStyle.SetMarkerStyle(20)
#For the fit/function:                                                                                                          
tdrStyle.SetOptFit(1)
tdrStyle.SetFitFormat("5.4g")
#tdrStyle.SetFuncColor(1)                                                                                                     
tdrStyle.SetFuncStyle(1)
tdrStyle.SetFuncWidth(1)

#For the date:                                                                                                                  
tdrStyle.SetOptDate(0)
#tdrStyle.SetDateX(x = 0.01)                                                                                          
#tdrStyle.SetDateY(y = 0.01)                                                                                          
#For the statistics box:                                                                                                        
tdrStyle.SetOptFile(0)
tdrStyle.SetOptStat("") # To display the mean and RMS:   SetOptStat("mr")                                                    
#tdrStyle.SetStatColor(ROOT.kWhite)   
tdrStyle.SetStatColor(ROOT.kGray)
tdrStyle.SetStatFont(42)
tdrStyle.SetTextSize(11)
tdrStyle.SetTextAlign(11)
tdrStyle.SetStatTextColor(1)
tdrStyle.SetStatFormat("6.4g")
tdrStyle.SetStatBorderSize(0)
tdrStyle.SetStatX(1.) #Starting position on X axis                                                                            
tdrStyle.SetStatY(1.) #Starting position on Y axis                                                                            
tdrStyle.SetStatFontSize(0.025) #Vertical Size                                                                                
tdrStyle.SetStatW(0.25) #Horizontal size                                                                                      
#tdrStyle.SetStatStyle(Style_t style = 1001)  

#Margins:                                                                                                                        
tdrStyle.SetPadTopMargin(0.095)
tdrStyle.SetPadBottomMargin(0.125)
tdrStyle.SetPadLeftMargin(0.14)
tdrStyle.SetPadRightMargin(0.1)
# For the Global title:                                                                                                        
tdrStyle.SetOptTitle(0)
tdrStyle.SetTitleFont(42)
tdrStyle.SetTitleColor(1)
tdrStyle.SetTitleTextColor(1)
tdrStyle.SetTitleFillColor(10)
tdrStyle.SetTitleFontSize(0.05)
tdrStyle.SetTitleH(0.045) # Set the height of the title box                                                                  
#tdrStyle.SetTitleW(0) # Set the width of the title box                                                                     
tdrStyle.SetTitleX(0.20) # Set the position of the title box                                                                 
tdrStyle.SetTitleY(1.0) # Set the position of the title box                                                                  
#tdrStyle.SetTitleStyle(Style_t style = 1001)                                                                                
tdrStyle.SetTitleBorderSize(0)
# For the axis titles:                                                                                                         
tdrStyle.SetTitleColor(1, "XYZ")
tdrStyle.SetTitleFont(42, "XYZ")
tdrStyle.SetTitleSize(0.06, "XYZ")
tdrStyle.SetTitleXOffset(0.9)
tdrStyle.SetTitleYOffset(1.05)
tdrStyle.SetTitleYOffset(1.05)
# For the axis labels:                                                                                                         
tdrStyle.SetLabelColor(1, "XYZ")
tdrStyle.SetLabelFont(42, "XYZ")
tdrStyle.SetLabelOffset(0.007, "XYZ")
tdrStyle.SetLabelSize(0.05, "XYZ")
# For the axis:                                                                                                                
tdrStyle.SetAxisColor(1, "XYZ")
tdrStyle.SetStripDecimals(1)
tdrStyle.SetTickLength(0.03, "XYZ")
tdrStyle.SetNdivisions(510, "XYZ")
tdrStyle.SetPadTickX(0)
tdrStyle.SetPadTickY(0)
# Change for log plots:                                                                                                        
tdrStyle.SetOptLogx(0)
tdrStyle.SetOptLogy(0)
tdrStyle.SetOptLogz(0)
tdrStyle.cd()
######## FINE CONFIG  

nbins = int(len(varloops)*2 + 1)

edges = []
for idb in range(0, nbins+1):
    ide = 2
    edge = 0. + int(idb>0)*0.8 
    while ide <= idb and ide > 1:
        if ide%2 == 0:
            edge += 0.4
        else:
            edge += 0.6
        ide += 1
    edges.append(round(edge,1))

y2 = 3.84
y1 = 1.0

s1down = []
s2down = []
s1up = []
s2up = []
mins = []

labels = []

totpairs = 0

varstring = ""

for srv, crv in varloops:
    print "\n"
    print srv, crv
    ss1up = []
    ss2up = []
    ss1down = []
    ss2down = []
    smins = []
    varstring += "_" + str(srv)
    if crv != srv:
        varstring += "_" + str(crv)
    labfound = 0

    srlabel = ""
    crlabel = ""
    for varr in variables:
        if srv == varr.name:
            srlabel = varr.smtitle
            labfound += 1
        if crv == varr.name:
            crlabel = varr.smtitle
            labfound += 1
        if labfound == 2:
            break

    if srlabel != crlabel:
        labels.append(srlabel + " + " + crlabel)
    else:
        labels.append(srlabel)
    
    lspath = opt.folder + "/" + srv + "_" + crv 
    lspath += "/" + efold + "/LS_objects_k_" + eftop + ".root"
    #print opt.folder, lspath

    lsfile = ROOT.TFile.Open(lspath, "READ")
    gr = lsfile.Get("Graph")
    func = ROOT.TF1("func", myfunc, -1000, 1000, 0)
    #min1 = func.GetMinimumX(-100,+100)
    #x1 = func.GetX(y1, -100, min1)
    #x2 = func.GetX(y1, min1, +100)
    #print x1, min1, x2
    #min2 = func.GetMinimumX(x2,+100)
    #print min2
    #intmax = func.GetMaximumX(x2,min2)
    #print intmax
    #x3 = func.GetX(y1, intmax, min2)
    #x4 = func.GetX(y1, min2, +100)
    #print x3, x4
    #x = -100.
    #for ix in range(100):
        #x = func.GetX(y1, x+0.01, +100, 0.01)
        #print ix, x

    #func.SetNpx(500)
    StopIter = False
    ix = 0
    while not StopIter:
        #print s1down, s1up
        #print "iter", ix
        if ix == 0:
            ext1 = -100.
            ext2 = +100.
        else:
            ext1 = ss1up[ix-1]
            ext2 = +100.
        Min = round(func.GetMinimumX(ext1, ext2), 3)
        #print ext1, ext2, Min
        if round(Min, 3) == ext1:
            StopIter = True
            #print "bye"
            continue
        if ix != 0:
            ext3 = func.GetMaximumX(ss1up[ix-1], Min)
        else:
            ext3 = ext1

        #print ext1, ext2, ext3
        x1down = func.GetX(y1, ext3, Min)
        x1up = func.GetX(y1, Min, ext2)#, 10**(-10), 1000)
        #x1up = func.GetX(y1, min1, ext2)
        x2down = func.GetX(y2, ext3, Min)
        if x2down == ext3:
            x2down = ss2down[ix-1]
        x2up = func.GetX(y2, Min, ext2)
        #print x1down, Min, x1up
        ix += 1
        ss1down.append(round(x1down, 3))
        ss1up.append(round(x1up, 3))
        ss2down.append(round(x2down, 3))
        ss2up.append(round(x2up, 3))
        smins.append(round(Min, 3))
        #break    
    #print "ss2down", ss2down
    #print "ss1down", ss1down
    #print "smins", smins
    #print "ss1up", ss1up
    #print "ss2up", ss2up
    s1down.append(ss1down)
    s1up.append(ss1up)
    s2down.append(ss2down)
    s2up.append(ss2up)
    mins.append(smins)

    gr.Clear()
    lsfile.Close()
    totpairs += 1
    
y = []
print "\n\n"
print "s2down", s2down
print "s1down", s1down
print "mins", mins
print "s1up", s1up
print "s2up", s2up

outfolder = "CIplots/" + opt.folder
if not os.path.exists(outfolder):
    os.system("mkdir -p " + outfolder)

plotname = outfolder + "/CI_" + eftop + varstring
limitstxt = open(plotname + ".txt", "w")

Yup = ROOT.TH1F("yellow_up", "", nbins, array('d', edges))
Gup = ROOT.TH1F("green_up", "", nbins, array('d', edges))
Ydown = ROOT.TH1F("yellow_down", "", nbins, array('d', edges))
Gdown = ROOT.TH1F("green_down", "", nbins, array('d', edges))

Yup.SetLineColor(ROOT.kYellow)
Yup.SetFillStyle(1001)
Yup.SetFillColor(ROOT.kYellow)

Ydown.SetLineColor(ROOT.kYellow)
Ydown.SetFillStyle(1001)
Ydown.SetFillColor(ROOT.kYellow)

Gup.SetLineColor(ROOT.kGreen)
Gup.SetFillStyle(1001)
Gup.SetFillColor(ROOT.kGreen)

Gdown.SetLineColor(ROOT.kGreen)
Gdown.SetFillStyle(1001)
Gdown.SetFillColor(ROOT.kGreen)


for idp in range(0, totpairs):
    idbin = int(2*(idp+1))
    ss1down = s1down[idp]
    ss2down = s2down[idp]
    ss1up = s1up[idp]
    ss2up = s2up[idp]

    sigma1str = ""
    sigma2str = ""
    for idsig in range(len(ss1down)):
        if sigma1str != "":
            sigma1str += " \cup "
        if sigma2str != "":
            sigma2str += " \cup "
        sigma1str += "["
        sigma2str += "["
        sigma1str += str(ss1down[idsig]) + ", " + str(ss1up[idsig]) + "]" 
        sigma2str += str(ss2down[idsig]) + ", " + str(ss2up[idsig]) + "]"
    fstr = labels[idp] + ":\t1sigma = " + sigma1str + "\t2sigma = " + sigma2str + "\n"
    limitstxt.write(fstr)

    Gdown.SetBinContent(idbin, ss1down[0])
    Gup.SetBinContent(idbin, ss1up[0])
    Ydown.SetBinContent(idbin, ss2down[0])
    Yup.SetBinContent(idbin, ss2up[0])
    Yup.GetXaxis().SetBinLabel(idbin, labels[idp])    
    y.append(mins[idp][0])

limitstxt.close()

x = [n+1 for n in range(0, totpairs)]
xarray = array('d', x)
yarray = array('d', y)

g = ROOT.TGraph(totpairs, xarray, yarray)
g.SetMarkerColor(ROOT.kRed)
g.SetMarkerStyle(ROOT.kFullCircle)

if not os.path.exists(outfolder):
    os.system("mkdir " + outfolder)

c1 = ROOT.TCanvas("c1","c1",0,0,800,650)
c1_1 = ROOT.TPad("c1_1", "newpad",0.01,0.01,0.9,0.99)
c1_1.Draw()
c1_1.cd()
c1_1.SetTopMargin(0.1)
c1_1.SetBottomMargin(0.15)
c1_1.SetRightMargin(0.00455)#0.0045                                                                                            
c1_1.SetLeftMargin(0.15)

maxy = max([max(ss2up) for ss2up in s2up])
miny = min([min(ss2down) for ss2down in s2down])
maxx = round(max(abs(maxy), abs(miny)), 1)
b = maxx + 0.5
a = -b

Yup.GetYaxis().SetRangeUser(a,b)

Yup.Draw()
Gup.Draw("SAME")
Ydown.Draw("SAME")
Gdown.Draw("SAME")
g.Draw("P")

Yup.GetXaxis().SetNdivisions(0, 1)
Yup.GetYaxis().SetTitleOffset(1.4)
Yup.GetYaxis().SetTitle("Confidence Interval")
Yup.GetYaxis().SetLabelSize(0.045)
Yup.GetYaxis().SetTitleSize(0.05)

latexLabel = ROOT.TLatex()
latexLabel.SetTextSize(0.04)
latexLabel.SetNDC()
latexLabel.DrawLatex(0.15, 0.915, "CMS (Preliminary)")

lumiLab = ROOT.TLatex()
lumiLab.SetTextSize(0.04)
lumiLab.SetNDC()
latexLabel.DrawLatex(0.83, 0.915, "L = " + str(lumi[opt.era]) + " fb^{-1}")

latexLabel2 = ROOT.TLatex()
latexLabel2.SetNDC()
latexLabel2.SetTextSize(0.04)
latexLabel2.DrawLatex(0.89, 0.865, "13 TeV")

latexLabel3 = ROOT.TLatex()
latexLabel3.SetTextSize(0.05)
latexLabel3.SetNDC()
coeff = eftop.replace("F", "f_{").replace("c", "c_{")
coeff += "}"
print eftop, coeff

latexLabel3.DrawLatex(0.16, 0.03, coeff)

leg = ROOT.TLegend(0.48, 0.89, 0.70, 0.99)
leg.SetShadowColor(1)
leg.SetBorderSize(1)
leg.SetTextSize(0.025)
leg.SetFillColor(0)
leg.AddEntry(g, "Best fit", "p")
leg.AddEntry(Gup, "#pm1#sigma expected", "f")
leg.AddEntry(Yup, "#pm2#sigma expected", "f")
leg.Draw();

c1.SaveAs(plotname+".pdf")
c1.SaveAs(plotname+".png")
