import ROOT
import sys
import copy
import optparse
import array
import os
import numpy as np
from operator import itemgetter
#os.system("reset")

ROOT.gROOT.SetBatch()

lumi = {
    '2016': 36.3,
    "2017": 41.5,
    "2018": 59.8,
    "2017,2018": 101.4,
    "2016M,2017,2018": 138,
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

import ctypes

def print_graph_points(graph, label):
    n_points = graph.GetN()
    print(label, "number of points:", n_points)
    for i in range(n_points):
        x = ctypes.c_double(0)
        y = ctypes.c_double(0)
        graph.GetPoint(i, x, y)
        print("Point", i, ":", x.value, y.value)

import ctypes

def print_intercepts(graph, label):
    n_points = graph.GetN()
    points = []
    for i in range(n_points):
        x_val = ctypes.c_double(0)
        y_val = ctypes.c_double(0)
        graph.GetPoint(i, x_val, y_val)
        points.append((x_val.value, y_val.value))
    
    # For points where x is positive and negative, find the one with y closest to 0
    points_xpos = [pt for pt in points if pt[0] > 0]
    points_xneg = [pt for pt in points if pt[0] < 0]
    
    best_xpos = min(points_xpos, key=lambda p: abs(p[1])) if points_xpos else None
    best_xneg = min(points_xneg, key=lambda p: abs(p[1])) if points_xneg else None

    # For points where y is positive and negative, find the one with x closest to 0
    points_ypos = [pt for pt in points if pt[1] > 0]
    points_yneg = [pt for pt in points if pt[1] < 0]
    
    best_ypos = min(points_ypos, key=lambda p: abs(p[0])) if points_ypos else None
    best_yneg = min(points_yneg, key=lambda p: abs(p[0])) if points_yneg else None

    # Print the results:
    if best_xpos:
        print(label, "for x > 0: point with y closest to 0 =", best_xpos)
    else:
        print(label, "for x > 0: no points found.")

    if best_xneg:
        print(label, "for x < 0: point with y closest to 0 =", best_xneg)
    else:
        print(label, "for x < 0: no points found.")

    if best_ypos:
        print(label, "for y > 0: point with x closest to 0 =", best_ypos)
    else:
        print(label, "for y > 0: no points found.")

    if best_yneg:
        print(label, "for y < 0: point with x closest to 0 =", best_yneg)
    else:
        print(label, "for y < 0: no points found.")

'''
def print_intercepts(graph, label):
    n_points = graph.GetN()
    x_vals = []
    y_vals = []
    for i in range(n_points):
        x = ctypes.c_double(0)
        y = ctypes.c_double(0)
        graph.GetPoint(i, x, y)
        x_vals.append(x.value)
        y_vals.append(y.value)
    
    # Find the point with y closest to 0 (gives corresponding x)
    min_y_idx = min(range(n_points), key=lambda i: abs(y_vals[i]))
    closest_x = x_vals[min_y_idx]
    closest_y = y_vals[min_y_idx]
    
    # Find the point with x closest to 0 (gives corresponding y)
    min_x_idx = min(range(n_points), key=lambda i: abs(x_vals[i]))
    closest_y2 = y_vals[min_x_idx]
    closest_x2 = x_vals[min_x_idx]
    
    print(label, "-> Closest to y=0: x =", closest_x, " (at y =", closest_y, ")")
    print(label, "-> Closest to x=0: y =", closest_y2, " (at x =", closest_x2, ")")
'''

'''
def print_intercepts(graph, label, tol=1e-5):
    n_points = graph.GetN()
    x_vals = []
    y_vals = []
    for i in range(n_points):
        x = ctypes.c_double(0)
        y = ctypes.c_double(0)
        # Use ctypes.pointer instead of ctypes.byref
        graph.GetPoint(i, ctypes.pointer(x), ctypes.pointer(y))
        x_vals.append(x.value)
        y_vals.append(y.value)
    
    # Find the x-value where y crosses zero (y=0 intercept)
    x_at_y0 = []
    for i in range(n_points - 1):
        if (y_vals[i] * y_vals[i+1] < 0) or (abs(y_vals[i]) < tol):
            if abs(y_vals[i+1] - y_vals[i]) > tol:
                t = -y_vals[i] / (y_vals[i+1] - y_vals[i])
                x_interp = x_vals[i] + t * (x_vals[i+1] - x_vals[i])
                x_at_y0.append(x_interp)
    
    # Find the y-value where x crosses zero (x=0 intercept)
    y_at_x0 = []
    for i in range(n_points - 1):
        if (x_vals[i] * x_vals[i+1] < 0) or (abs(x_vals[i]) < tol):
            if abs(x_vals[i+1] - x_vals[i]) > tol:
                t = -x_vals[i] / (x_vals[i+1] - x_vals[i])
                y_interp = y_vals[i] + t * (y_vals[i+1] - y_vals[i])
                y_at_x0.append(y_interp)
    
    print(label, "-> y=0 crossing (x values):", x_at_y0)
    print(label, "-> x=0 crossing (y values):", y_at_x0)
'''

def draw1D():
    _file0 = ROOT.TFile.Open(opt.in0, "READ")
    _file1 = ROOT.TFile.Open(opt.in1, "READ")
    variable = "k_" + str(opt.coeff).replace("F", "c")
    year = str(opt.year)

    nvariable = variable.replace("cS", "FS").replace("cM", "FM").replace("cT", "FT")

    limit = _file0.Get("limit")

    cc = ROOT.TCanvas("cc","", 800, 600);

    print(" expected = ", _file0.GetName())

    #n = limit.Draw("2*deltaNLL:r","deltaNLL<10 && deltaNLL>-30","l");
  
    toDraw = ROOT.TString(ROOT.Form("2*deltaNLL:"+variable))
  
    n = limit.Draw( toDraw.Data(), "deltaNLL<10 && deltaNLL>-10", "l")
    graphScan = ROOT.TGraph(n,limit.GetV2(),limit.GetV1())
    graphScan.RemovePoint(0)
  
    graphScanData = ROOT.TGraph()
    limitData = _file1.Get("limit")  
    print(" observed = ", _file1.GetName(), "\n")
    #     n_data = limitData.Draw("2*deltaNLL:r","deltaNLL<40 && deltaNLL>-30","l")
    n_data = limitData.Draw(  toDraw.Data() , "deltaNLL<10 && deltaNLL>-10", "l")
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
    
    print(" (expected) MC   at minimum:   ",   mc_min_x, "\n")
    print(" (observed) data at minimum:   ", data_min_x, "\n")
  
  
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
    NCont = 200
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
    if not ("EW" in xNameVar or "QCD" in xNameVar):
        xNameVar = str(xNameVar.replace(xNameVar[0], xNameVar[0] + "_{") + "}").replace("F", "f")
    else:
        xNameVar = xNameVar.replace("EWK", "#mu_{EW}").replace("QCD", "#mu_{QCD}")
    if not ("EW" in yNameVar or "QCD" in yNameVar):
        yNameVar = str(yNameVar.replace(yNameVar[0], yNameVar[0] + "_{") + "}").replace("F", "f")
    else:
        yNameVar = yNameVar.replace("EWK", "#mu_{EW}").replace("QCD", "#mu_{QCD}").replace(xNameVar[0], xNameVar[0] + "_{")
    #variable = "k_" + str(opt.coeff)
    year = str(opt.year)

    lambdas = {
        "c": "/#Lambda^{2}",
        "f": "/#Lambda^{4}",
    }

    for cinit, lambpow in list(lambdas.items()): 
        if xNameVar.startswith(cinit):
            xNameVar += lambpow
        if yNameVar.startswith(cinit):
            yNameVar += lambpow
    #nvariable = variable.replace("cS", "fS").replace("cM", "fM").replace("cT", "fT")

    limit = _file0.Get("limit")
    limitData = _file1.Get("limit")

    
    whatToDraw = variables +":2*deltaNLL"
    if ":F" in opt.coeff:
        cutToDraw = "(deltaNLL<20 && deltaNLL>-20)" # && (" + opt.cut + ")"
    else:
        cutToDraw = "(deltaNLL<40 && deltaNLL>-40)" # && (" + opt.cut + ")"
    #cutToDraw = "(deltaNLL<5) && deltaNLL>-5" # && (" + opt.cut + ")"
    n = limit.Draw(whatToDraw, cutToDraw, "colz") #"colz")
    nData = limitData.Draw(whatToDraw, cutToDraw, "colz") #"colz")
    
    x = np.ndarray((n), 'd', limit.GetV1())
    y = np.ndarray((n), 'd', limit.GetV2())
    z_ = np.ndarray((n), 'd', limit.GetV3())
    z = np.array([i-min(z_) for i in z_]) #shifting likelihood toward 0                                                        
    graphScan = ROOT.TGraph2D(n,x,y,z)

    xData = np.ndarray((nData), 'd', limitData.GetV1())
    yData = np.ndarray((nData), 'd', limitData.GetV2())
    zData_ = np.ndarray((nData), 'd', limitData.GetV3())
    zData = np.array([i-min(zData_) for i in zData_]) #shifting likelihood toward 0                                            
    graphScanData = ROOT.TGraph2D(nData,xData,yData,zData)

    #n_points = graphScanData.GetN()
    #for i in range(n_points):
    #    x = graphScanData.GetX()[i]
    #    y = graphScanData.GetY()[i]
    #    z = graphScanData.GetZ()[i]
    #    if z == 0:
    #        graphScanData.SetPoint(i, x, y, 100)  # Set the z-value to 100 if it's originally 0


    ##---- 2D likelihood thresholds
    
    contours = array.array('d', np.array([2.30, 5.99])) ###1sigma, 2sigma
    
    cc2 = ROOT.TCanvas("cc2","",1000,1200)
    
    # Draw contours from the TGraph2D for contLevel 1 of graphScanData
    cont2_observed = graphScanData.GetContourList(contours[1])
    print("cont2_observed", cont2_observed, cont2_observed.GetSize())
    graph2_observed = None #ROOT.TMultiGraph()
    for i in range(cont2_observed.GetSize()):
        if i != cont2_observed.GetSize()-1:
            continue
            #graph2_observed = cont2_observed.At(i)
        #else:
        temp2_observed = cont2_observed.At(i)
        temp2_observed.SetLineColor(ROOT.kBlack)
        temp2_observed.SetLineStyle(2)  # Dash-dot line style                                                                                                                                                                                 
        temp2_observed.SetLineWidth(3)
        temp2_observed.GetXaxis().SetLabelSize(0.05) #SetLabelSize(0.03)
        temp2_observed.GetYaxis().SetLabelSize(0.05) #SetLabelSize(0.03)
        graph2_observed = temp2_observed #.Add(cont2_observed.At(i))
        temp2_observed.Draw("AL")
        if graph2_observed:
            print_intercepts(graph2_observed, "Observed (95%)")
            #print_graph_points(graph2_observed, "Observed (95%)")
            
        # Set line style and color for the second contour of graphScanData
    
    #graph2_observed.SetLineColor(ROOT.kBlack)
    #graph2_observed.SetLineStyle(1)  # Dash-dot line style
    #graph2_observed.SetLineWidth(3) 
    #graph2_observed.GetXaxis().SetLabelSize(0.05) #SetLabelSize(0.03) 
    #graph2_observed.GetYaxis().SetLabelSize(0.05) #SetLabelSize(0.03) 
    
    # Draw the second contour line of graphScanData
    #if i == 0:
    #graph2_observed.Draw("AL")  # Draw as a line plot
    #graph2_observed.Draw("L SAME")  # Draw as a line plot
    

    #else:
    #graph2_observed.Draw("L SAME")  # Draw as a line plot
        
    # Draw contours from the TGraph2D for contLevel 0 of graphScanData
    cont1_observed = graphScanData.GetContourList(contours[0])
    print("cont1_observed", cont1_observed, cont1_observed.GetSize())
    graph1_observed = None
    for i in range(cont1_observed.GetSize()):
        #if i != 0:
        #    continue
        graph1_observed = cont1_observed.At(i)
        # Set line style and color for the first contour of graphScanData
        graph1_observed.SetLineColor(ROOT.kBlack)
        graph1_observed.SetLineStyle(1)
        graph1_observed.SetLineWidth(3) 
        graph1_observed.GetXaxis().SetLabelSize(0.05) #SetLabelSize(0.03)
        graph1_observed.GetYaxis().SetLabelSize(0.05) #SetLabelSize(0.03)
        # Draw the first contour line of graphScanData
        graph1_observed.Draw("L SAME")  # Draw as a line plot, on top of the second contour
        if graph1_observed:
            print_intercepts(graph1_observed, "Observed (68%)")
            #print_graph_points(graph1_observed, "Observed (68%)")
            
    # Draw contours from the TGraph2D for contLevel 1 of graphScan
    #print("hi", graphScan.GetContourList(2.3))
    #return 
    cont2_expected = graphScan.GetContourList(contours[1])
    print("cont2_expected", cont2_expected, cont2_expected.GetSize())
    graph2_expected = None
    for i in range(cont2_expected.GetSize()):
        graph2_expected = cont2_expected.At(i)
        # Set line style and color for the second contour of graphScan
        graph2_expected.SetLineColor(ROOT.kRed)
        graph2_expected.SetLineStyle(2)
        graph2_expected.SetLineWidth(3)
        graph2_expected.GetXaxis().SetLabelSize(0.05) #SetLabelSize(0.03)
        graph2_expected.GetYaxis().SetLabelSize(0.05) #SetLabelSize(0.03)
        # Draw the second contour line of graphScan
        graph2_expected.Draw("L SAME")  # Draw as a line plot, on top of the first contour
        if graph2_expected:
            print_intercepts(graph2_expected, "Expected (95%)")
            #print_graph_points(graph2_expected, "Expected (95%)")
            
    # Draw contours from the TGraph2D for contLevel 0 of graphScan
    cont1_expected = graphScan.GetContourList(contours[0])
    print("cont1_expected", cont1_expected, cont1_expected.GetSize())
    graph1_expected = None
    for i in range(cont1_expected.GetSize()):
        graph1_expected = cont1_expected.At(i)
        # Set line style and color for the first contour of graphScan
        graph1_expected.SetLineColor(ROOT.kRed)
        graph1_expected.SetLineStyle(1)
        graph1_expected.SetLineWidth(3) 
        graph1_expected.GetXaxis().SetLabelSize(0.05) #SetLabelSize(0.03)
        graph1_expected.GetYaxis().SetLabelSize(0.05) #SetLabelSize(0.03)
        # Draw the first contour line of graphScan
        graph1_expected.Draw("L SAME")  # Draw as a line plot, on top of the second contour
        if graph1_expected:
            print_intercepts(graph1_expected, "Expected (68%)")
            #print_graph_points(graph1_expected, "Expected (68%)")
            
    # Set axis titles
    cc2.SetLeftMargin(0.1)  # Adjust margin to make room for axis titles
    cc2.SetRightMargin(0.05)
    cc2.SetBottomMargin(0.11)
    cc2.SetTopMargin(0.16)#0.055)
    cc2.SetGrid()
    ROOT.gStyle.SetGridWidth(1)
    ROOT.gStyle.SetGridStyle(2)
    ROOT.gStyle.SetGridColor(ROOT.kGray)
    cc2.Modified()
    cc2.Update()

    # Create and draw axis titles
    xAxisTitle = ROOT.TLatex()
    xAxisTitle.SetTextFont(42)
    xAxisTitle.SetTextSize(0.05)
    xAxisTitle.SetTextAlign(22)
    xAxisTitle.DrawLatexNDC(0.9, 0.03, xNameVar)

    yAxisTitle = ROOT.TLatex()
    yAxisTitle.SetTextFont(42)
    yAxisTitle.SetTextSize(0.05)
    yAxisTitle.SetTextAlign(22)
    yAxisTitle.SetTextAngle(90)
    yAxisTitle.DrawLatexNDC(0.031, 0.9, yNameVar)

    zAxisTitle = ROOT.TLatex()
    zAxisTitle.SetTextFont(42)
    zAxisTitle.SetTextSize(0.055)
    zAxisTitle.SetTextAlign(22)
    zAxisTitle.SetTextAngle(90)
    #zAxisTitle.DrawLatexNDC(0.9, 0.5, "- 2#Delta logL")
    #graphScan.GetZaxis().SetRangeUser(0,100.0)
    
    # Create a legend
    legend = ROOT.TLegend(0.095, 0.85, 0.955, 0.94)  # Define legend position
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)

    #legend.SetNColumns(legend.GetNRows())
    # Draw the legend on the canvas
    #legend.Draw()
    
    cc2.Update()
    
    cross11 = ROOT.TGraph()
    if opt.coeff.startswith("c") or opt.coeff.startswith("F"):
        cross11.SetPoint(0,0,0)
    else:
        cross11.SetPoint(0,1,1)
    cross11.SetMarkerStyle(34)
    cross11.SetMarkerSize(2)
    cross11.SetMarkerColor(ROOT.kBlue)
    cross11.SetLineColor(ROOT.kBlue)

    
    #xmin = array.array('d', [0.])
    #ymin = array.array('d', [0.])

    #limit.SetBranchAddress("k_" + xName, xmin)
    #limit.SetBranchAddress("k_" + yName, ymin)
    #print limit.GetEntry(0)
    limit.GetEntry(0)
    #xmin = array.array('d', [getattr(limit, 'k_' + xName)])
    #ymin = array.array('d', [getattr(limit, 'k_' + yName)])
    #print xmin, ymin

    limitData.GetEntry(0)
    #xminData = array.array('d', [getattr(limitData, 'k_' + xName)])
    #yminData = array.array('d', [getattr(limitData, 'k_' + yName)])

    # Convert TGraph points to numpy arrays
    x_values = np.array(graphScan.GetX())
    y_values = np.array(graphScan.GetY())
    z_values = np.array(graphScan.GetZ())
    x_values_data = np.array(graphScanData.GetX())
    y_values_data = np.array(graphScanData.GetY())
    z_values_data = np.array(graphScanData.GetZ())
    
    # Find the index of the minimum z value in graphScan
    min_z_index = np.argmin(z_values)
    # Find the index of the minimum z value in graphScanData
    min_zData_index = np.argmin(z_values_data)
    
    # Get the corresponding x, y pairs for the minimum z values
    xmin_at_min_z = x_values[min_z_index]
    ymin_at_min_z = y_values[min_z_index]
    xminData_at_min_zData = x_values_data[min_zData_index]
    yminData_at_min_zData = y_values_data[min_zData_index]

    crossMin = ROOT.TGraph()
    crossMin.SetPoint(0, xmin_at_min_z, ymin_at_min_z)
    crossMin.SetMarkerStyle(20)
    crossMin.SetMarkerSize(1.5)
    crossMin.SetMarkerColor(ROOT.kRed)
    crossMin.SetLineColor(ROOT.kRed)
    crossMin.SetLineWidth(3)


    crossMinData = ROOT.TGraph()
    crossMinData.SetPoint(0, xminData_at_min_zData, yminData_at_min_zData)
    crossMinData.SetMarkerStyle(20)
    crossMinData.SetMarkerSize(1.5)
    crossMinData.SetMarkerColor(ROOT.kBlack)
    crossMinData.SetLineColor(ROOT.kBlack)
    crossMinData.SetLineWidth(3)

    #crossMin.Draw("P")
    #crossMinData.Draw("P")
    cross11.Draw("P")


    #leg = ROOT.TLegend(0.25,0.095,0.75,0.145)
    #leg.SetBorderSize(0)
    #legend.AddEntry(crossMin,"Expected Best fit","P")
    #legend.AddEntry(crossMinData,"Observed Best fit","P")
    # Add entries for each contour line
    legend.AddEntry(graph1_expected, "Expected (68%)", "l")  # "l" for line
    legend.AddEntry(graph2_expected, "Expected (95%)", "l")
    legend.AddEntry("", "", "")
    legend.AddEntry(graph1_observed, "Observed (68%)", "l")
    legend.AddEntry(graph2_observed, "Observed (95%)", "l")
    legend.AddEntry(cross11,"SM","P")
    legend.SetNColumns(3) #legend.GetNRows())
    legend.SetTextSize(0.035)
    legend.Draw()

    cc2.Update()

    cc2.SetTicks()
    #   cc2.SetFillColor(0)
    #   cc2.SetBorderMode(0)
    #   cc2.SetBorderSize(2)
    #   cc2.SetTickx(1)
    #   cc2.SetTicky(1)
    #   cc2.SetFrameBorderMode(0)

    
    #tex = ROOT.TLatex(0.94,0.92,"13 TeV")
    tex = ROOT.TLatex(0.80,0.955,"13 TeV")
    tex.SetNDC()
    tex.SetTextAlign(31)
    tex.SetTextFont(42)
    tex.SetTextSize(0.04)
    tex.SetLineWidth(2)
     
    #tex2 = ROOT.TLatex(0.14,0.92,"CMS Preliminary")
    tex2 = ROOT.TLatex(0.1,0.955,"CMS")
    tex2.SetNDC()
    tex2.SetTextFont(61)
    tex2.SetTextSize(0.05)
    tex2.SetLineWidth(2)
     
    texPre = ROOT.TLatex(0.19,0.955,"Preliminary")
    texPre.SetNDC()
    texPre.SetTextFont(52)
    texPre.SetTextSize(0.04)
    texPre.SetLineWidth(2)
     
    #   tex3 = ROOT.TLatex(0.236,0.92,"L = 12.9 fb^{-1}  Preliminary")
    #   tex3 = ROOT.TLatex(0.236,0.92,"L = 15.2 fb^{-1}")
    #   tex3 = ROOT.TLatex(0.55,0.92,"L = 15.2 fb^{-1}   (13 TeV)")
    #   float lumi = 15.2
    nameLabel = "L = " + str(lumi[year]) + " fb^{-1} (13 TeV)"
    tex3 = ROOT.TLatex(0.62, 0.955, nameLabel)
    #   tex3 = ROOT.TLatex(0.55,0.92,"L = 2.3 fb^{-1}   (13 TeV)")
    #     tex3 = ROOT.TLatex(0.55,0.92,"L = 12.9 fb^{-1}   (13 TeV)")
    tex3.SetNDC()
    tex3.SetTextFont(42)
    tex3.SetTextSize(0.04)
    tex3.SetLineWidth(2)
    
    #   tex.Draw("same")
    tex2.Draw("same")
    #texPre.Draw("same")
    tex3.Draw("same")
    #--- fix Z-axis (begin)
    cc2.Update()
    
    
    #cc.SaveAs("prova.png")
    #cc3.SaveAs("prova3.png")
    cc2.SaveAs(os.path.dirname(opt.in1) + "/LSprov_" + str(opt.coeff) + ".png")
    cc2.SaveAs(os.path.dirname(opt.in1) + "/LSprov_" + str(opt.coeff) + ".pdf")
    cc2.SaveAs(os.path.dirname(opt.in1) + "/LSprov_" + str(opt.coeff) + ".root")
    

print(opt.oneD, opt.twoD)
if opt.oneD:
    draw1D()
elif opt.twoD:
    draw2D()
