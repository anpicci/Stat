import ROOT
import sys
import copy

cc = ROOT.TCanvas("cc","", 800, 600);

lumi = {
    '2016': 35.9,
    "2017": 41.53,
    "2018": 59.7,
}

n = 0
n_data = 0
  
_file0 = ROOT.TFile.Open(str(sys.argv[1]), "READ")
_file1 = ROOT.TFile.Open(str(sys.argv[2]), "READ")
variable = str(sys.argv[3])
year = str(sys.argv[4])

limit = _file0.Get("limit")

print " expected = ", _file0.GetName()

  #   n = limit.Draw("2*deltaNLL:r","deltaNLL<10 && deltaNLL>-30","l");
  
toDraw = ROOT.TString(ROOT.Form("2*deltaNLL:"+variable))
  
n = limit.Draw( toDraw.Data(), "deltaNLL<50 && deltaNLL>-30", "l")
graphScan = ROOT.TGraph(n,limit.GetV2(),limit.GetV1())
graphScan.RemovePoint(0)
  
graphScanData = ROOT.TGraph()
limitData = _file1.Get("limit")  
print " observed = ", _file1.GetName(), "\n"
#     n_data = limitData.Draw("2*deltaNLL:r","deltaNLL<40 && deltaNLL>-30","l")
n_data = limitData.Draw(  toDraw.Data() , "deltaNLL<50 && deltaNLL>-30", "l")
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

    if x_value in x_std: #(std::find(x_std.begin(), x_std.end(), x_value) != x_std.end()) {
        
        graphScan.RemovePoint(ip)
        #       print "removed ", ip, "\n"
        ip += -1

    else:
        x_std.append(copy.deepcopy(x_value))
        x_y_map.append([copy.deepcopy(x_value), copy.deepcopy(y_value)])

    ip += 1

graphScan.Set(0)
    
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
  
graphScan.GetXaxis().SetTitle(variable)
graphScan.GetYaxis().SetTitle("-2 #Delta lnL")
  
graphScan.Draw("al")
#   graphScan  .Draw("aPl")
graphScan.GetYaxis().SetRangeUser(-0.1, 10.)

if graphScanData: 
    graphScanData.Draw("l")
  
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
  
  
cc.SaveAs("LS_" + str(variable) + ".png")

try:
    wait = input("Press Enter to continue.")
except:
    print "Goodbye!"
