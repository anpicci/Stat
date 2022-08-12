import ROOT
import sys
import copy
import optparse
import array
import os
from operator import itemgetter
#os.system("reset")

ROOT.gROOT.SetBatch()

lumi = {
    '2016': 36.3,
    "2017": 41.5,
    "2018": 59.8,
    "2017,2018": 101.4,
    "2016M,2017,2018": 137.7,
}

n = 0
n_data = 0

usage = "python drawLS.py"
parser = optparse.OptionParser(usage)

parser.add_option('--in0', dest='in0', type='string', default = 'higgsCombineTest.MultiDimFit.mH125.root', help = 'File for blinded analysis')
parser.add_option('--in1', dest='in1', type='string', default = 'higgsCombineTest.MultiDimFit.mH125.root', help = 'file for unblinded analysis (before unblinding, dummy)')
parser.add_option('--coeff', dest='coeff', type='string', default = 'cW', help = 'Wilson coefficient(s), separated by :')
parser.add_option('--year', dest='year', type='string', default = '2017,2018', help = 'Fit epoch')
parser.add_option('--cut', dest='cut', type='string', default = '1', help = 'Cut')
parser.add_option('--1D', dest='oneD', default = False, action='store_true', help = '1D likelihood')
parser.add_option('--2D', dest='twoD', default = False, action='store_true', help = '2D likelihood')
(opt, args) = parser.parse_args()

if opt.twoD:
    opt.oneD = False

ROOT.gROOT.LoadMacro("/afs/cern.ch/work/a/apiccine/CMSSW_10_2_13/src/Stat/Limits/test/tdrstyle.C")
ROOT.gROOT.ProcessLine("setTDRStyle();")

def draw1D():
    _file0 = ROOT.TFile.Open(opt.in0, "READ")
    _file1 = ROOT.TFile.Open(opt.in1, "READ")
    variable = "k_" + str(opt.coeff).replace("F", "c")
    year = str(opt.year)

    nvariable = variable.replace("cS", "FS").replace("cM", "FM").replace("cT", "FT")

    limit = _file0.Get("limit")

    cc = ROOT.TCanvas("cc","", 800, 600);

    print " expected = ", _file0.GetName()

    #n = limit.Draw("2*deltaNLL:r","deltaNLL<10 && deltaNLL>-30","l");
  
    toDraw = ROOT.TString(ROOT.Form("2*deltaNLL:"+variable))
  
    n = limit.Draw( toDraw.Data(), "deltaNLL<10 && deltaNLL>-30", "l")
    graphScan = ROOT.TGraph(n,limit.GetV2(),limit.GetV1())
    graphScan.RemovePoint(0)
  
    graphScanData = ROOT.TGraph()
    limitData = _file1.Get("limit")  
    print " observed = ", _file1.GetName(), "\n"
    #     n_data = limitData.Draw("2*deltaNLL:r","deltaNLL<40 && deltaNLL>-30","l")
    n_data = limitData.Draw(  toDraw.Data() , "deltaNLL<10 && deltaNLL>-30", "l")
    graphScanData = ROOT.TGraph(n_data,limitData.GetV2(),limitData.GetV1())
    graphScanData.RemovePoint(0)
    graphScanData.SetTitle("")
    graphScanData.SetMarkerStyle(21)
    graphScanData.SetLineWidth(2)
    graphScanData.SetMarkerColor(ROOT.kRed)
    graphScanData.SetLineColor(ROOT.kRed)

    cc.SetGrid()

    graphScan.SetTitle("")
    graphScan.SetMarkerStyle(21)
    graphScan.SetLineWidth(2)
    graphScan.SetMarkerColor(ROOT.kBlue)
    graphScan.SetLineColor(ROOT.kBlue)

    #   graphScan.Draw("APL")

    #----
    cc.SetTicks()
    cc.SetFillColor(0)
    cc.SetBorderMode(0)
    cc.SetBorderSize(2)
    cc.SetTickx(1)
    cc.SetTicky(1)
    cc.SetRightMargin(0.05)
    cc.SetBottomMargin(0.12)
    cc.SetFrameBorderMode(0)

    tex = ROOT.TLatex(0.94,0.92,"13 TeV")
    tex.SetNDC()
    tex.SetTextAlign(31)
    tex.SetTextFont(42)
    tex.SetTextSize(0.04)
    tex.SetLineWidth(2)

    tex2 = ROOT.TLatex(0.14,0.92,"CMS")
    tex2.SetNDC()
    tex2.SetTextFont(61)
    tex2.SetTextSize(0.04)
    tex2.SetLineWidth(2)
    
    tex3 = ROOT.TLatex(0.236,0.92,"L = " + str(lumi[year]) + " fb^{-1}  Preliminary")
    tex3.SetNDC()
    tex3.SetTextFont(52)
    tex3.SetTextSize(0.035)
    tex3.SetLineWidth(2)
    
    minX = 999.
    maxX = -999.


    #---- clean duplicate (it happens during lxbatch scan)
    x_std = []
    #std::vector <double> x_std
    x_y_map = []
    #std::map <double, double> x_y_map
    x_value = ROOT.Double()
    y_value = ROOT.Double()

    ip = 0

    while ip < graphScan.GetN():
        #print "ip: ", ip
        graphScan.GetPoint(ip, x_value, y_value)
        #print "GetPoint: ", graphScan.GetPoint(ip, x_value, y_value)
        #print " x_value = ", x_value, "\n"
        #ip += 1

        #print x_value_double, x_value
        if x_value in x_std: #(std::find(x_std.begin(), x_std.end(), x_value) != x_std.end()) {
            graphScan.RemovePoint(ip)
            #print "removed ", ip, "\n"
            #ip += -1

        else:
            x_std.append(copy.deepcopy(x_value))
            x_y_map.append([copy.deepcopy(x_value), copy.deepcopy(y_value)])
            ip += 1

    
    graphScan.Set(0)
    
    x_y_map = sorted(x_y_map, key=itemgetter(0))

    if len(x_y_map) > 0:
        mc_min_x = -100.
        minimum = 1000.

        #---- fix the 0 of the likelihood scan
        for it in x_y_map:# (std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
            if it[1] < minimum:
                minimum = it[1]
                mc_min_x = it[0]

        for it in x_y_map:#(std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
            it[1] =  it[1] - minimum
  
        #---- (end) fix the 0 of the likelihood scan
  
        ip = 0
        for it in x_y_map:#(std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
            graphScan.SetPoint(ip, it[0], it[1])
            ip += 1
  
        #---- just for horizonthal lines
        for it in x_y_map:#(std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
            if it[0] < minX:
                minX = it[0]

            if it[0] > maxX:
                maxX = it[0]
        #---- (end) just for horizonthal lines
  
    x_std = []
    x_y_map = []

    ip = 0

    while ip < graphScanData.GetN():#
        graphScanData.GetPoint (ip, x_value, y_value)
        #     print " x_value = ", x_value, "\n"
        if x_value in x_std: #(std::find(x_std.begin(), x_std.end(), x_value) != x_std.end()) {
            graphScanData.RemovePoint(ip)
            ip += -1

        else:
            x_std.append(copy.deepcopy(x_value))
            x_y_map.append(copy.deepcopy([x_value, y_value]))

        ip += 1
  
    graphScanData.Set(0)
  
    x_y_map = sorted(x_y_map, key=itemgetter(0))

    if len(x_y_map) > 0:
        #---- fix the 0 of the likelihood scan
        data_min_x = -100.
        minimum = 1000.

        for it in x_y_map: #(std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
            if it[1] < minimum:
                minimum = it[1]
                data_min_x = it[0]

        for it in x_y_map: #(std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
            it[1] =  it[1] - minimum

        #---- (end) fix the 0 of the likelihood scan
    

        ip = 0
        for it in x_y_map:#(std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
            graphScanData.SetPoint(ip, it[0] , it[1])
            ip += 1
  
    #---- plot ----
  
    graphScan.GetXaxis().SetTitle(variable.replace("k_", ""))
    graphScan.GetYaxis().SetTitle("-2 #Delta lnL")
    
    graphScan.Draw("al")
    #   graphScan  .Draw("aPl")
    graphScan.GetYaxis().SetRangeUser(-0.1, 10.)

    if graphScanData: 
        graphScanData.Draw("al")
  
    tex.Draw("same")
    tex2.Draw("same")
    tex3.Draw("same")
  
  
    #  2deltaLogL = 1.00
    #  2deltaLogL = 3.84
  
    #   line1 = ROOT.TLine((limit.GetV2())[0],1.0,(limit.GetV2())[n-1],1.0)
    line1 = ROOT.TLine(minX,1.0,maxX,1.0)
    line1.SetLineWidth(2)
    line1.SetLineStyle(2)
    line1.SetLineColor(ROOT.kRed)
    line1.Draw() 
  
    #   line2 = ROOT.TLine((limit.GetV2())[0],3.84,(limit.GetV2())[n-1],3.84)
    line2 = ROOT.TLine(minX,3.84,maxX,3.84)
    line2.SetLineWidth(2)
    line2.SetLineStyle(2)
    line2.SetLineColor(ROOT.kRed)
    line2.Draw()
  
    leg = ROOT.TLegend(0.43,0.75,0.63,0.9)
    leg.AddEntry(graphScan,"Expected","l")
    if graphScanData:
        leg.AddEntry(graphScanData,"Observed","l")

  
    #   leg.AddEntry(graphScan,"Old","l")
    #   if (graphScanData) {
    #     leg.AddEntry(graphScanData,"New","l")
    #   }

    #   leg.AddEntry(graphScan,"Obs 2015 alone","l")
    #   if (graphScanData) {
    #     leg.AddEntry(graphScanData,"Obs 2015 with CR 2016","l")
    #   }

    #   leg.AddEntry(graphScan,"Obs 2016 alone","l")
    #   if (graphScanData) {
    #     leg.AddEntry(graphScanData,"Obs 2016 with CR 2015","l")
    #   }
    #   
  
  
    leg.SetFillColor(0)
    leg.Draw()
  
    print " (expected) MC   at minimum:   ",   mc_min_x, "\n"
    print " (observed) data at minimum:   ", data_min_x, "\n"
  
  
    #   print " data at 0:   ", graphScanData.Eval(0), "\n"
    #   print " MC   at 0:   ", graphScan    .Eval(0), "\n"

    #   print " significance data at 0:   ", sqrt(graphScanData.Eval(0)), "\n"
    #   print " significance MC   at 0:   ", sqrt(graphScan    .Eval(0)), "\n"
  
  
    cc.SaveAs("LS_" + str(nvariable) + ".png")
    cc.SaveAs("LS_" + str(nvariable) + ".pdf")

    outfile = ROOT.TFile.Open("LS_objects_"+nvariable+".root" ,"RECREATE")
    outfile.cd()
    line1.Write()
    line2.Write()
    graphScan.Write()
    outfile.Close()

    #try:
    #wait = input("Press Enter to continue.")
    #except:
    #print "Goodbye!"
    
def draw2D():
    NRGBs = 3
    NCont = 255
    stops = array.array('d', [0.00, 0.5, 1.00])
    red = array.array('d', [1.00, 0.0, 0.00])
    green = array.array('d', [0.0, 1.00, 0.00])
    blue = array.array('d', [1.00, 0., 1.00])
    
    ROOT.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
    ROOT.gStyle.SetNumberContours(NCont)

    cc3 = ROOT.TCanvas("cc3","",800,600)

    _file0 = ROOT.TFile.Open(opt.in0, "READ")
    _file1 = ROOT.TFile.Open(opt.in1, "READ")

    coeffs = opt.coeff.split(":")
    
    variables = ""
    for idc, coeff in enumerate(coeffs):
        coeffs[idc] = "k_" + coeff.replace("F", "c")
        if idc > 0:
            variables += ":"
        variables += coeffs[idc]
        
    xName, yName = variables.replace("k_", "").split(":")
    xNameVar, yNameVar = opt.coeff.split(":")
    xNameVar = xNameVar.replace("EWK", "#mu_{EW}").replace("QCD", "#mu_{QCD}")
    yNameVar = yNameVar.replace("EWK", "#mu_{EW}").replace("QCD", "#mu_{QCD}")

    #variable = "k_" + str(opt.coeff)
    year = str(opt.year)

    #nvariable = variable.replace("cS", "fS").replace("cM", "fM").replace("cT", "fT")

    limit = _file0.Get("limit")
    limitData = _file1.Get("limit")

    
    whatToDraw = variables +":2*deltaNLL"
    cutToDraw = "(deltaNLL<10) && (" + opt.cut + ")"
    n = limit.Draw(whatToDraw, cutToDraw, "colz")
    
    cc = ROOT.TCanvas("cc","",800,600)
    graphScan = ROOT.TGraph2D(n,limit.GetV1(),limit.GetV2(),limit.GetV3())

    graphScan.SetTitle("")
    graphScan.SetMarkerStyle(21)
    graphScan.SetMarkerColor(ROOT.kRed)
    graphScan.SetLineColor(ROOT.kRed)
    
    #graphScan.Draw("colz")
    
    graphScan.GetXaxis().SetTitle(xNameVar)
    graphScan.GetYaxis().SetTitle(yNameVar)
    graphScan.GetZaxis().SetTitle("- 2#Delta logL")
    graphScan.GetZaxis().SetRangeUser(0,10.0)
    
    ##---- 2D likelihood thresholds
    
    contours = array.array('d', [2.30, 5.99]) ###1sigma, 2sigma
    #graphScan.Draw("colz")
    graphScan.GetHistogram().GetXaxis().SetTitle(xNameVar)
    graphScan.GetHistogram().GetYaxis().SetTitle(yNameVar)
    graphScan.GetHistogram().GetZaxis().SetTitle("- 2#Delta logL")
    graphScan.GetHistogram().GetZaxis().SetRangeUser(0,10.0)

    
    if True:
        for i in range(graphScan.GetHistogram().GetSize()):
            if (graphScan.GetHistogram().GetBinContent(i+1) == 0):
                graphScan.GetHistogram().SetBinContent(i+1, 100)
            #print " [ " + str(i) + " ] = " + str(graphScan.GetHistogram().GetBinContent(i+1))
 
    #graphScan.Draw("colz")
    
    cc2 = ROOT.TCanvas("cc2","",800,600)
    #cc2.SetRightMargin(0.19)

    #graphScan.Draw("contz")
    #graphScan.Draw("colz")
    
    HistStreamFn_ph2 = graphScan.GetHistogram().Clone("testhisto_ph2")
    HistStreamFn_ph2.SetContour(2, contours)
    HistStreamFn_ph2.SetLineWidth(2)
    HistStreamFn_ph2.SetLineStyle(2)
    
    HistStreamFn_ph2.GetZaxis().SetRangeUser(0,10.0)
    HistStreamFn_ph2.Draw("CONT1 LIST SAME")
    cc2.Update()
    cc.cd()
    HistStreamFn_ph2.Draw("CONT Z LIST")
    cc.Update()
    
    conts = ROOT.gROOT.GetListOfSpecials().FindObject("contours")
    print " conts = " + str(conts.GetSize())
    
    gr_1sigma = conts.At(0)
    gr_2sigma = conts.At(1)
    #print gr_1sigma, gr_1sigma.GetSize()
    #print gr_2sigma, gr_2sigma.GetSize()

    cc2.cd()

    for obj in gr_1sigma:
        obj.SetLineWidth(3)
        #obj.SetLineStyle(1)
        obj.SetLineColor(ROOT.kGreen)
        #obj.SetFillColor(ROOT.kGreen)
        obj.Draw("C")

    
    for obj in gr_2sigma:
        obj.SetLineWidth(3)
        #obj.SetLineStyle(7)
        obj.SetLineColor(ROOT.kBlue)
        #obj.SetFillColor(ROOT.kBlue)
        obj.Draw("C")

    cross11 = ROOT.TGraph()
    if opt.coeff.startswith("c") or opt.coeff.startswith("F"):
        cross11.SetPoint(0,0,0)
    else:
        cross11.SetPoint(0,1,1)
    cross11.SetMarkerStyle(22)
    cross11.SetMarkerSize(2)
    cross11.SetMarkerColor(ROOT.kBlack)
    cross11.SetLineColor(ROOT.kBlack)
    cross11.Draw("P")

    xmin = array.array('d', [0.])
    ymin = array.array('d', [0.])

    limit.SetBranchAddress("k_" + xName, xmin)
    limit.SetBranchAddress("k_" + yName, ymin)
    limit.GetEntry(0)
    #print xmin, ymin

    crossMin = ROOT.TGraph()
    crossMin.SetPoint(0, xmin[0], ymin[0])
    crossMin.SetMarkerStyle(20)
    crossMin.SetMarkerSize(1)
    crossMin.SetMarkerColor(ROOT.kRed)
    crossMin.SetLineColor(ROOT.kRed)
    crossMin.SetLineWidth(3)
    crossMin.Draw("P")

    leg = ROOT.TLegend(0.85,0.80,0.96,0.95)
    leg.SetBorderSize(1)
    leg.AddEntry(gr_1sigma[-1],"1 #sigma","l")
    leg.AddEntry(gr_2sigma[-1],"2 #sigma","l")
    leg.AddEntry(crossMin,"Best fit","P")
    leg.AddEntry(cross11,"SM","P")
    leg.Draw()

    cc2.SetTicks()
    #   cc2.SetFillColor(0)
    #   cc2.SetBorderMode(0)
    #   cc2.SetBorderSize(2)
    #   cc2.SetTickx(1)
    #   cc2.SetTicky(1)
    #   cc2.SetRightMargin(0.05)
    #     cc2.SetBottomMargin(0.12)
    #   cc2.SetFrameBorderMode(0)
    cc2.SetTopMargin(0.12)
    cc2.SetBottomMargin(0.14)

    #tex = ROOT.TLatex(0.94,0.92,"13 TeV")
    tex = ROOT.TLatex(0.80,0.92,"13 TeV")
    tex.SetNDC()
    tex.SetTextAlign(31)
    tex.SetTextFont(42)
    tex.SetTextSize(0.04)
    tex.SetLineWidth(2)
     
    #tex2 = ROOT.TLatex(0.14,0.92,"CMS Preliminary")
    tex2 = ROOT.TLatex(0.16,0.92,"CMS")
    tex2.SetNDC()
    tex2.SetTextFont(61)
    tex2.SetTextSize(0.04)
    tex2.SetLineWidth(2)
     
    texPre = ROOT.TLatex(0.23,0.92,"Preliminary")
    texPre.SetNDC()
    texPre.SetTextFont(52)
    texPre.SetTextSize(0.035)
    texPre.SetLineWidth(2)
     
    #   tex3 = ROOT.TLatex(0.236,0.92,"L = 12.9 fb^{-1}  Preliminary")
    #   tex3 = ROOT.TLatex(0.236,0.92,"L = 15.2 fb^{-1}")
    #   tex3 = ROOT.TLatex(0.55,0.92,"L = 15.2 fb^{-1}   (13 TeV)")
    #   float lumi = 15.2
    nameLabel = "L = " + str(lumi[year]) + " fb^{-1}   (13 TeV)"
    tex3 = ROOT.TLatex(0.55, 0.92, nameLabel)
    #   tex3 = ROOT.TLatex(0.55,0.92,"L = 2.3 fb^{-1}   (13 TeV)")
    #     tex3 = ROOT.TLatex(0.55,0.92,"L = 12.9 fb^{-1}   (13 TeV)")
    tex3.SetNDC()
    tex3.SetTextFont(52)
    tex3.SetTextSize(0.035)
    tex3.SetLineWidth(2)
    
    #   tex.Draw("same")
    tex2.Draw("same")
    texPre.Draw("same")
    tex3.Draw("same")
    #--- fix Z-axis (begin)
    cc2.Update()
    
    #cc.SaveAs("prova.png")
    #cc3.SaveAs("prova3.png")
    cc2.SaveAs("LS_" + str(opt.coeff) + ".png")
    cc2.SaveAs("LS_" + str(opt.coeff) + ".pdf")

print opt.oneD, opt.twoD
if opt.oneD:
    draw1D()
elif opt.twoD:
    draw2D()
