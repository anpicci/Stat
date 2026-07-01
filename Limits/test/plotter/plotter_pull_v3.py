# -*- coding: utf-8 -*- #
from ROOT import *
from collections import defaultdict
from array import array
from tdrStyle import *
import math
import os
setTDRStyle()

blind = False

new_dic = defaultdict(dict)



"""

    to run this plotter type:
    python plotter.py 
    the argument of the function are specified at the bottom

    example: region = SR_Y2016combined_signal_region_prefit, ovvero la regione di combine che si vuole plottare
                        dovrà essere generalizzata la cosa per Full Run 2
    
               fitdiag_file = ./inputs/PostFit_histograms.root
"""


def plotter_pull_v3(flavor,fitdiag_file,SignalFile,region,lumi,Mass,outdir="./output",sb=True,year=161718,LogX=True):


    #   OPENING THE INPUT FIL
    f_mlfit = TFile(fitdiag_file,'READ') 
    f_mlfit_signal = TFile(SignalFile,'READ') 

    #   DATA HISTOGRAM 
    h_data = f_mlfit.Get(region+"_prefit/data_obs")  

    #   LIST OF BACKGROUNDS AND COLORS
    mainbkgs = {
            "SR":["TTtW","DY","Other"],
            "DYcr":["TTtW","DY","Other"],
            "TOPcr":["TTtW","DY","Other"],
            }
    processes = [
        'Other', 
        'TTtW',
        'DY',
    ]
    colors = {
    'Other' : kAzure-4,
    'TTtW'  : kRed-7,
    'DY'    : kGreen+1,
    }



    binLowE = []
    binLowE2 = []
#   MllJBin=[0.,0.2,0.4,0.6,0.8,1.,1.4,2.,10.]    # merged binning 
#    MllJBin=[0.,0.2,0.4,0.6,0.8,1.,1.4,2.,3.5,10.] # finer binning  
    #  MllJBin=[0.,200.,400.,600.,800.,1000.,1400.,2000.,10000.]  ### better not to use this GeV binning.

    # Pre-Fit HISTO FILLING
    h_prefit = {}

    #   TOTAL BKG CONTRIBUTION
    h_prefit['total'] = f_mlfit.Get(region+"_prefit/TotalBkg")

    for i in range(1,h_prefit['total'].GetNbinsX()+2):
        binLowE.append(h_prefit['total'].GetBinLowEdge(i))
    print(binLowE)
 
#    for i in range(0,10):
 #     binLowE2.append(MllJBin[i])
#    print(binLowE2)


    h_all_prefit = TH1F("h_all_prefit","h_all_prefit",len(binLowE)-1,array('d',binLowE))
    h_other_prefit = TH1F("h_other_prefit","h_other_prefit",len(binLowE)-1,array('d',binLowE))




    h_stack_prefit = THStack("h_stack_prefit","h_stack_prefit")
    for process in processes: 
        h_prefit[process] = f_mlfit.Get(region+"_prefit/"+process)
        if (not h_prefit[process]): continue
        if (str(h_prefit[process].Integral())=="nan"): continue
        for i in range(1,h_prefit[process].GetNbinsX()+1):
            content = h_prefit[process].GetBinContent(i)
            width = h_prefit[process].GetBinLowEdge(i+1)-h_prefit[process].GetBinLowEdge(i)
            h_prefit[process].SetBinContent(i,content) #*width
        h_prefit[process].SetLineColor(colors[process])
        h_prefit[process].SetFillColor(colors[process])
        h_all_prefit.Add(h_prefit[process])
        if (not process in mainbkgs[region]):
            h_other_prefit.Add(h_prefit[process])
        h_stack_prefit.Add(h_prefit[process])
        #print(content)




    # Post-Fit HISTO FILLING
    h_postfit = {}    
    h_postfit['totalsig'] = f_mlfit_signal.Get(region+"_postfit/TotalSig")                       ####EDIT    total signal      postfit
#    h_postfit['totalsig'] = f_mlfit.Get(region+"_postfit/TotalSig")                       ####EDIT    total signal      postfit
    h_postfit['total'] = f_mlfit.Get(region+"_postfit/TotalProcs")                        ####EDIT    total bkgs+signal postfit

    h_all_postfit = TH1F("h_all_postfit","h_all_postfit",len(binLowE)-1,array('d',binLowE))
    h_other_postfit = TH1F("h_other_postfit","h_other_postfit",len(binLowE)-1,array('d',binLowE))
    #h_minor_postfit = TH1F("h_minor_postfit","h_minor_postfit",len(binLowE)-1,array('d',binLowE))

    h_stack_postfit = THStack("h_stack_postfit","h_stack_postfit")                    
    h_postfit['totalv2'] = f_mlfit.Get(region+"_postfit/TotalBkg")                       ####EDIT  total bkgs postfit

    for i in range(1, h_postfit['totalv2'].GetNbinsX()+1):
        error = h_postfit['totalv2'].GetBinError(i)
        content = h_postfit['totalv2'].GetBinContent(i)

    for process in processes:
        h_postfit[process] = f_mlfit.Get(region+"_postfit/"+process)                       ####EDIT  qui post-fit histo per ogni processo in esame

        if (not h_postfit[process]): continue
        if (str(h_postfit[process].Integral())=="nan"): continue
        for i in range(1,h_postfit[process].GetNbinsX()+1):
          error = h_postfit[process].GetBinError(i)
          content = h_postfit[process].GetBinContent(i)
          width = h_postfit[process].GetBinLowEdge(i+1)-h_postfit[process].GetBinLowEdge(i)
          h_postfit[process].SetBinContent(i,content) #*width
        h_postfit[process].SetLineColor(1)
        h_postfit[process].SetFillColor(colors[process])
        h_all_postfit.Add(h_postfit[process])
        if (not process in mainbkgs[region]):
            h_other_postfit.Add(h_postfit[process])

        h_stack_postfit.Add(h_postfit[process])


#######################################################
#    if asymbins is True:
#      #h_stack_postfit2 = TH1F("h_stack_postfit2","h_stack_postfit2")
#      h_postfit2['totalsig'] = TH1F("h_postfit2","h_postfit2",len(binLowE2)-1,array('d',binLowE2))
#      h_data2= TH1F("h_data2","h_data2",len(binLowE2)-1,array('d',binLowE2))
#      for i in range(0,9):
#        h_postfit2['totalsig'].SetBinContent(i,h_postfit['totalsig'].GetBinContent(i))
#        h_postfit2['totalsig'].SetBinError(i,h_postfit['totalsig'].GetBinError(i))
#        h_data2.SetBinContent(i,h_data.GetBinContent(i))
#        h_data2.SetBinError(i,h_data.GetBinError(i))
#########################################################






    # CANVAS DRAWING

    gStyle.SetOptStat(0)
    
    c = TCanvas("c","c",600,800)
    SetOwnership(c,False)
    c.cd()
    c.SetLogy()
    if LogX is True:
      c.SetLogx()
    c.SetBottomMargin(0.38)
    c.SetRightMargin(0.06)
    c.SetTickx(1);
    c.SetTicky(1);
 
    dummy = h_all_prefit.Clone("dummy")

    dummy.SetFillColor(0)
    dummy.SetLineColor(0)
    dummy.SetLineWidth(0)
    dummy.SetMarkerSize(0)
    dummy.SetMarkerColor(0)
    dummy.GetYaxis().SetTitle("Events ") #/ GeV
    dummy.GetXaxis().SetTitle("")
    dummy.GetXaxis().SetTitleSize(0)
    dummy.GetXaxis().SetLabelSize(0)
    
    if LogX is True:
      dummy.GetXaxis().SetRangeUser(0.4,10)

    if region is 'SR':
        dummy.SetMaximum(50*dummy.GetMaximum())
    else:
        dummy.SetMaximum(25*dummy.GetMaximum())
    dummy.SetMinimum(0.1) #0.002
    dummy.GetYaxis().SetTitleOffset(1.15)
    dummy.Draw()

    h_other_prefit.SetLineColor(1)
    h_other_prefit.SetFillColor(33)
    #h_other_prefit.Scale(1,"width")

    h_all_prefit.SetLineColor(2)
    h_all_prefit.SetLineWidth(2)

    h_all_postfit.SetLineColor(kAzure-4)
    h_all_postfit.SetLineWidth(2)

    h_stack_postfit.Draw("histsame")

    #if region in 'signal':                                                          ####EDIT

#    h_postfit['totalsig'].Scale(1)
#    h_postfit['totalsig'].SetFillColor(0);
#    h_postfit['totalsig'].SetFillStyle(3144);
    if sb is True:
      h_postfit['totalsig'].SetLineColor(kOrange)
      h_postfit['totalsig'].SetLineStyle(1)
      h_postfit['totalsig'].SetLineWidth(2)
      h_postfit['totalsig'].Draw("samehist")
      

    #else:
    #    h_other_prefit.Draw("histsame")
    #    h_all_prefit.Draw("histsame")
    #    h_all_postfit.Draw("histsame")


    h_data.SetMarkerStyle(20)
    h_data.SetLineColor(1)
    h_data.SetMarkerSize(1.2)
    #h_data.Scale(1,"width")
    if not blind:
      h_data.Draw("epsame")


    #if region in 'signal' :
    legend = TLegend(0.60, 0.70, 0.92, .92);
    #legend.SetTextSize(0.04)
    legend.SetFillStyle(0);
    legend.SetBorderSize(0);
    legend.AddEntry(h_data, "Data", "elp")

    legend.AddEntry(h_postfit['DY'], "Drell-Yan", "f")
    legend.AddEntry(h_postfit['TTtW'], "t#bar{t}+tW", "f")
    legend.AddEntry(h_postfit['Other'], "Other", "f")
    if sb:
      legend.AddEntry(h_postfit['totalsig'], "#Lambda=13, M="+str(Mass)+" TeV (prefit)", "l")           ###### qui conviene mettere SOLO il segnale 
#    else:
#        legend = TLegend(.5,.65,.90,.90)
#        legend.AddEntry(h_data,"Data","elp")
#        legend.AddEntry(h_all_postfit, "Post-fit ("+legname+")", "l")
#        legend.AddEntry(h_all_prefit, "Pre-fit ("+legname+")", "l")
#        legend.AddEntry(h_other_prefit, "Other Backgrounds", "f")

    legend.SetShadowColor(0);
    legend.SetFillColor(0);
    legend.SetLineColor(0);
    legend.Draw("same")
    latex2 = TLatex()
    latex2.SetNDC()
    latex2.SetTextSize(0.6*c.GetTopMargin())
    latex2.SetTextFont(42)
    latex2.SetTextAlign(31) # align right
    latex2.DrawLatex(0.94, 0.95,"{LUMI} fb^{{-1}} (13 TeV)".format(LUMI=lumi))
    latex2.SetTextSize(0.6*c.GetTopMargin())
    latex2.SetTextFont(62)
    latex2.SetTextAlign(11) # align right
    latex2.DrawLatex(0.175, 0.85, "CMS #it{#bf{Preliminary}}")
    latex2.SetTextSize(0.6*c.GetTopMargin())
    latex2.SetTextFont(52)
    latex2.SetTextAlign(11)
    offset = 0.005
    #latex2.DrawLatex(0.28+offset, 0.85, "Preliminary")
    categoryLabel = TLatex();
    categoryLabel.SetNDC();
    categoryLabel.SetTextSize(0.5*c.GetTopMargin());
    categoryLabel.SetTextFont(42);
    categoryLabel.SetTextAlign(11);

    if region is "SR":                                          ## questo andrà modificato per mettere un label per ogni regione
      categoryLabel.DrawLatex(0.175,0.82,"Signal region");
      categoryLabel.Draw("same");
    elif region is "DYcr":
      categoryLabel.DrawLatex(0.175,0.82,"DY control region");
      categoryLabel.Draw("same");
    else:
      categoryLabel.DrawLatex(0.175,0.82,"Top control region");
      categoryLabel.Draw("same");
   
    gPad.RedrawAxis()
    pad2 = TPad("pad2", "pad2", 0.0, 0.0, 1.0, 1.0)
    SetOwnership(pad2,False)
    pad2.SetTopMargin(0.63)
    pad2.SetBottomMargin(0.25)
    pad2.SetRightMargin(0.06)
    pad2.SetFillColor(0)
    #pad2.SetGridy(1)
    pad2.SetFillStyle(0)
    if LogX is True:
      pad2.SetLogx()
    pad2.Draw()
    pad2.cd(0)



    ############ RATIO PLOT
    met = []; dmet = [];
    ratio_pre = []; ratio_pre_hi = []; ratio_pre_lo = [];
    ratio_post = []; ratio_post_hi = []; ratio_post_lo = [];
    # cutstring = "("
    for i in range(1,h_all_prefit.GetNbinsX()+1):
      ndata = h_data.GetBinContent(i)
      if (ndata>0.0):
        e_data_hi = h_data.GetBinError(i)/ndata
        e_data_lo = h_data.GetBinError(i)/ndata
      else:
        e_data_hi = 0.0
        e_data_lo = 0.0
      n_all_pre = h_all_prefit.GetBinContent(i)
      n_other_pre = h_other_prefit.GetBinContent(i)
      n_all_post = h_all_postfit.GetBinContent(i)
      # cutstring=cutstring+str((n_all_post-n_other_pre)/(n_all_pre-n_other_pre))+"*(met>"+str(h_all_prefit.GetBinLowEdge(i))+"&&met<="+str(h_all_prefit.GetBinLowEdge(i+1))+")"
      # if i<h_all_prefit.GetNbinsX():
      #   cutstring+="+"
      met.append(h_all_prefit.GetBinCenter(i))
      dmet.append((h_all_prefit.GetBinLowEdge(i+1)-h_all_prefit.GetBinLowEdge(i))/2)
      if (n_all_pre>0.0):
        ratio_pre.append(ndata/n_all_pre)
        ratio_pre_hi.append(ndata*e_data_hi/n_all_pre)
        ratio_pre_lo.append(ndata*e_data_lo/n_all_pre)
      else:
        ratio_pre.append(0.0)
        ratio_pre_hi.append(0.0)
        ratio_pre_lo.append(0.0)
      if (n_all_post>0.0):
        ratio_post.append(ndata/n_all_post)
        ratio_post_hi.append(ndata*e_data_hi/n_all_post)
        ratio_post_lo.append(ndata*e_data_lo/n_all_post)
      else:
        ratio_post.append(0.0)
        ratio_post_hi.append(0.0)
        ratio_post_lo.append(0.0)
    # cutstring+=")"
    #print 'cutstring for',region,cutstring
    a_met = array("d", met)
    v_met = TVectorD(len(a_met),a_met)
    a_dmet = array("d", dmet)
    v_dmet = TVectorD(len(a_dmet),a_dmet)
    a_ratio_pre = array("d", ratio_pre)
    a_ratio_pre_hi = array("d", ratio_pre_hi)
    a_ratio_pre_lo = array("d", ratio_pre_lo)
    v_ratio_pre = TVectorD(len(a_ratio_pre),a_ratio_pre)
    v_ratio_pre_hi = TVectorD(len(a_ratio_pre_hi),a_ratio_pre_hi)
    v_ratio_pre_lo = TVectorD(len(a_ratio_pre_lo),a_ratio_pre_lo)
    a_ratio_post = array("d", ratio_post)
    a_ratio_post_hi = array("d", ratio_post_hi)
    a_ratio_post_lo = array("d", ratio_post_lo)
    v_ratio_post = TVectorD(len(a_ratio_post),a_ratio_post)
    v_ratio_post_hi = TVectorD(len(a_ratio_post_hi),a_ratio_post_hi)
    v_ratio_post_lo = TVectorD(len(a_ratio_post_lo),a_ratio_post_lo)
    g_ratio_pre = TGraphAsymmErrors(v_met,v_ratio_pre,v_dmet,v_dmet,v_ratio_pre_lo,v_ratio_pre_hi)
    g_ratio_pre.SetLineColor(2)
    g_ratio_pre.SetMarkerColor(2)
    g_ratio_pre.SetMarkerStyle(25)
    g_ratio_post = TGraphAsymmErrors(v_met,v_ratio_post,v_dmet,v_dmet,v_ratio_post_lo,v_ratio_post_hi)
    #g_ratio_post.SetLineColor(4)
    g_ratio_post.SetLineColor(kAzure-4)
    #g_ratio_post.SetMarkerColor(4)
    g_ratio_post.SetMarkerColor(kAzure-4)
    g_ratio_post.SetMarkerStyle(20)
    ratiosys = h_postfit['totalv2'].Clone();
    for hbin in range(0,ratiosys.GetNbinsX()+1):
      ratiosys.SetBinContent(hbin+1,1.0)
      if (h_postfit['totalv2'].GetBinContent(hbin+1)>0):
        ratiosys.SetBinError(hbin+1,h_postfit['totalv2'].GetBinError(hbin+1)/h_postfit['totalv2'].GetBinContent(hbin+1))
        #print hbin+1, h_data.GetBinContent(hbin+1), h_postfit['totalv2'].GetBinContent(hbin+1),h_postfit['totalv2'].GetBinError(hbin+1)
      else:
        ratiosys.SetBinError(hbin+1,0)

    dummy2 = TH1F("dummy2","dummy2",len(binLowE)-1,array('d',binLowE))
    for i in range(1,dummy2.GetNbinsX()):
      dummy2.SetBinContent(i,1.0)
    dummy2.GetYaxis().SetTitle("Data / Pred.")
        #dummy2.GetXaxis().SetTitle("E_{T}^{miss} [GeV]")
    dummy2.GetXaxis().SetTitle("")
    dummy2.SetLineColor(0)
    dummy2.SetMarkerColor(0)
    dummy2.SetLineWidth(0)
    dummy2.SetMarkerSize(0)
    if LogX is True:
      dummy2.GetXaxis().SetRangeUser(0.4,10)
    dummy2.GetYaxis().SetLabelSize(0.04)
    #if region is 'signal':
    dummy2.GetYaxis().SetLabelSize(0.03)
    dummy2.GetXaxis().SetLabelSize(0)
    dummy2.GetYaxis().SetNdivisions(5);
    dummy2.GetYaxis().CenterTitle()
    dummy2.GetYaxis().SetTitleSize(0.03)
    dummy2.GetYaxis().SetTitleOffset(1.6)
    if region is 'signal':
      dummy2.SetMaximum(1.20)
      dummy2.SetMinimum(0.80)
    else:
      dummy2.SetMaximum(1.40)
      dummy2.SetMinimum(0.6)
    dummy2.SetMaximum(1.5)
    dummy2.SetMinimum(0.5)
    dummy2.Draw("hist")
    ratiosys.SetFillColor(kGray) #SetFillColor(ROOT.kYellow)
    ratiosys.SetLineColor(kGray) #SetLineColor(1)
    ratiosys.SetLineWidth(1)
    ratiosys.SetMarkerSize(0)
    ratiosys.Draw("e2same")
    f1 = TF1("f1","1",-5000,5000);
    f1.SetLineColor(1);
    f1.SetLineStyle(2);
    f1.SetLineWidth(2);
    f1.Draw("same")
    if not blind:
      g_ratio_pre.Draw("epsame")
      g_ratio_post.Draw("epsame")
    ###old#legend2 = TLegend(0.147651,0.2314815,0.6979866,0.2810847,"","brNDC");
    legend2 = TLegend(0.227651,0.2534815,0.5079866,0.2810847,"","brNDC");
    #legend2 = TLegend(0.727651,0.3734815,0.9579866,0.4810847,"","brNDC");
    legend2.AddEntry(g_ratio_post, "#scale[1.2]{Post-fit}", "ple")
    legend2.AddEntry(g_ratio_pre, "#scale[1.2]{Pre-fit}", "ple")#ple
    legend2.SetNColumns(2)
    legend2.SetShadowColor(0);
    legend2.SetFillColor(0);
    legend2.SetLineColor(0);
    legend2.Draw("same")
    pad = TPad("pad", "pad", 0.0, 0.0, 1.0, 1.0)
    SetOwnership(pad,False)
    pad.SetTopMargin(0.76)
    pad.SetRightMargin(0.06)
    pad.SetFillColor(0)
    #pad.SetGridy(1)
    pad.SetFillStyle(0)
    if LogX is True:
      pad.SetLogx()
    pad.Draw()
    pad.cd(0)
    ##Compute the pulls
    h_prefit_pull = {}    
    h_prefit_pull['total_pre_pull'] = f_mlfit.Get(region+"_prefit/TotalBkg") 


    data_pull = h_data.Clone("pull")
    data_pull.Add(h_prefit_pull['total_pre_pull'],-1)
    data_pull.Sumw2()
    addedsqrt = 0
    mean = 0
    sigma = 0
    sigmaBILL = 0
    chi2 = 0
    TH1.StatOverflows(1)

    dummy_pull = TH1F("dummy33","dummy33",len(binLowE)-1,array('d',binLowE))
    pull_count = TH1F("pull","pull",100,-5,5)

    for hbin in range(0,data_pull.GetNbinsX()+1):
      if (h_prefit_pull['total_pre_pull'].GetBinContent(hbin)>0):

        addedsqrt +=  (data_pull.GetBinContent(hbin)*data_pull.GetBinContent(hbin))/(h_prefit_pull['total_pre_pull'].GetBinError(hbin)*h_prefit_pull['total_pre_pull'].GetBinError(hbin))
        sigma = math.sqrt(h_prefit_pull['total_pre_pull'].GetBinError(hbin)* h_prefit_pull['total_pre_pull'].GetBinError(hbin) + h_data.GetBinError(hbin)*h_data.GetBinError(hbin))
        data_pull.SetBinContent(hbin,data_pull.GetBinContent(hbin)/sigma)

        mean  += data_pull.GetBinContent(hbin)
        chi2  += (data_pull.GetBinContent(hbin)*data_pull.GetBinContent(hbin))
        #sigma += ((data_pull.GetBinContent(hbin)-0.242807588371)*(data_pull.GetBinContent(hbin)-0.242807588371))
        if (hbin > 2):
          pull_count.Fill(data_pull.GetBinContent(hbin))
          print " pull: ", data_pull.GetBinContent(hbin)
    pull_count.SaveAs("pullPre_"+flavor+region+".root")
    #data_pull.SaveAs("test_"+flavor+region+".root")
    #print "MEAN: ", mean
    #print "CHI2: ", math.sqrt(chi2)/data_pull.GetNbinsX()
    #print "Added", sqrt(addedsqrt), "divided: ", sqrt(addedsqrt)/data_pull.GetNbinsX()
    #print "Added2", addedsqrt, "divided: ", addedsqrt/data_pull.GetNbinsX()
    data_pull.SetLineColor(kAzure-4)
    data_pull.SetFillColor(kAzure-4)
    data_pull.SetMarkerColor(kAzure-4)
    data_pull_sig = h_data.Clone("pull")
    data_pull_sig.Sumw2()
    for hbin in range(0,data_pull_sig.GetNbinsX()+1):
      if (h_postfit['totalv2'].GetBinContent(hbin)>0):
        #print "bin",hbin,"data pull diff", data_pull_sig.GetBinContent(hbin), "sys", h_postfit['totalv2'].GetBinError(hbin)
        data_pull_sig.SetBinContent(hbin,data_pull_sig.GetBinContent(hbin)/h_postfit['totalv2'].GetBinError(hbin))
        data_pull_sig.SetBinError(hbin,0)
    data_pull_sig.SetLineColor(2)
    data_pull_sig.SetFillColor(2)
    data_pull_sig.SetFillStyle(3004)
    data_pull_sig.SetMarkerColor(2)
    legend3 = TLegend(0.20,0.21,0.60,0.23,"","brNDC");
    legend3.AddEntry(data_pull    , "Background only", "f")
    legend3.SetNColumns(2)
    legend3.SetShadowColor(0);
    legend3.SetFillColor(0);
    legend3.SetLineColor(0);

    dummy3 = TH1F("dummy3","dummy3",len(binLowE)-1,array('d',binLowE))

    for i in range(1,dummy3.GetNbinsX()):
      dummy3.SetBinContent(i,1.0)
    dummy3.GetYaxis().SetTitle("#frac{(Data-Pred.)}{#sigma}")



    if flavor is "electron":
      dummy3.GetXaxis().SetTitle("m(eeJ) (TeV)")
    elif flavor is "muon":
      dummy3.GetXaxis().SetTitle("m(#mu#muJ) (TeV)")
    elif flavor is "elemu":
      dummy3.GetXaxis().SetTitle("m(e#muJ) (TeV)")



    dummy3.SetLineColor(0)
    dummy3.SetMarkerColor(0)
    dummy3.SetLineWidth(0)
    dummy3.SetMarkerSize(0)
    if LogX is True:
      dummy3.GetXaxis().SetRangeUser(0.4,10)
    dummy3.GetYaxis().SetLabelSize(0.04)
    if region is 'signal':
      dummy3.GetYaxis().SetLabelSize(0.03)
    dummy3.GetYaxis().SetNdivisions(5);
    dummy3.GetYaxis().CenterTitle()
    dummy3.GetYaxis().SetTitleSize(0.03)
    dummy3.GetYaxis().SetTitleOffset(1.3)
    dummy3.SetMaximum(3.5)
    dummy3.SetMinimum(-3.5)
    dummy3.Draw("hist")
    data_pull.Draw("hist same")
    latex_chi = TLatex()
    latex_chi.SetNDC()
    latex_chi.SetTextSize(0.025)
    #latex_chi.DrawLatex(0.16,0.20,"#Chi^{2} = "+str(round(addedsqrt/data_pull.GetNbinsX(),2)) + "      Mean = "+ str(round(mean,2)))
    #latex_chi.DrawLatex(0.16,0.20,"#Chi^{2} = "+str(round(addedsqrt/data_pull.GetNbinsX(),2)) )
    #latex_chi.DrawLatex(0.16,0.19,"Mean = "+str(round(mean,2)))
    #latex_chi.Draw("same")
    pad2.RedrawAxis("G sameaxis")
    gPad.RedrawAxis()





### save plots and close
    import os
    if not os.path.exists(outdir):
      os.makedirs(outdir)
    c.SaveAs(outdir+region+"_"+flavor+"_"+str(lumi)+"fb_"+str(Mass)+"TeV.pdf")
    c.SaveAs(outdir+region+"_"+flavor+"_"+str(lumi)+"fb_"+str(Mass)+"TeV.png")
    c.SaveAs(outdir+region+"_"+flavor+"_"+str(lumi)+"fb_"+str(Mass)+"TeV.C")
    c.SaveAs(outdir+region+"_"+flavor+"_"+str(lumi)+"fb_"+str(Mass)+"TeV.root")
    c.Close()
    f_mlfit.Close()






##### what to run the function on:
######plotter_pull_v3("electron","./inputs/eejj_SR_PostFit_histograms_bkgOnly_PLOT.root","./inputs/eejj_SR_PostFit_histograms_L20_M1_PLOT.root","SR",138,1,"/eos/user/m/mpresill/www/HN/approval_plots/")
######plotter_pull_v3("muon","./inputs/mumujj_SR_PostFit_histograms_bkgOnly_PLOT.root","./inputs/mumujj_SR_PostFit_histograms_L20_M1_PLOT.root","SR",138,1,"/eos/user/m/mpresill/www/HN/approval_plots/")
#####
######plotter_pull_v3("electron","./inputs/eejj_SR_PostFit_histograms_bkgOnly_PLOT.root","./inputs/eejj_SR_PostFit_histograms_L20_M2_PLOT.root","SR",138,2,"/eos/user/m/mpresill/www/HN/approval_plots/")
######plotter_pull_v3("muon","./inputs/mumujj_SR_PostFit_histograms_bkgOnly_PLOT.root","./inputs/mumujj_SR_PostFit_histograms_L20_M2_PLOT.root","SR",138,2,"/eos/user/m/mpresill/www/HN/approval_plots/")

#plotter_pull_v3("electron","./inputs/eejj_SR_PostFit_histograms_bkgOnly_PLOT.root","./inputs/eejj_SR_PostFit_histograms_L13_M2_PLOT.root","SR",138,2,"/eos/user/m/mpresill/www/HN/approval_plots/")
#plotter_pull_v3("muon","./inputs/mumujj_SR_PostFit_histograms_bkgOnly_PLOT.root","./inputs/mumujj_SR_PostFit_histograms_L13_M2_PLOT.root","SR",138,2,"/eos/user/m/mpresill/www/HN/approval_plots/")
#
###DY cr
#plotter_pull_v3("electron","./inputs/eejj_DYcr_PostFit_histograms_bkgOnly_PLOT.root","./inputs/eejj_SR_PostFit_histograms_L20_M2_PLOT.root","DYcr",138,2,"/eos/user/m/mpresill/www/HN/approval_plots/",False)
#plotter_pull_v3("muon","./inputs/mumujj_DYcr_PostFit_histograms_bkgOnly_PLOT.root","./inputs/mumujj_SR_PostFit_histograms_L20_M2_PLOT.root","DYcr",138,2,"/eos/user/m/mpresill/www/HN/approval_plots/",False)
###TOP cr
#plotter_pull_v3("elemu","./inputs/mumujj_TOPcr_PostFit_histograms_bkgOnly_PLOT.root","./inputs/mumujj_SR_PostFit_histograms_L20_M2_PLOT.root","TOPcr",138,2,"/eos/user/m/mpresill/www/HN/approval_plots/",False)



########### THESE ARE FOR FINER BINNING SCENARIO:

plotter_pull_v3("electron","./inputs_finer_binning/eejj_PostFit_histograms_bkgOnly_PLOT_SR.root","./inputs_finer_binning/eejj_PostFit_histograms_L13_M05_PLOT_SR.root","SR",138,0.5,"/eos/user/m/mpresill/www/HN/limits/finer_binning/pull_update/prefitPulls/")
plotter_pull_v3("muon","./inputs_finer_binning/mumujj_PostFit_histograms_bkgOnly_PLOT_SR.root","./inputs_finer_binning/mumujj_PostFit_histograms_L13_M05_PLOT_SR.root","SR",138,0.5,"/eos/user/m/mpresill/www/HN/limits/finer_binning/pull_update/prefitPulls/")

##DY cr
#plotter_pull_v3("electron","./inputs_finer_binning/eejj_PostFit_histograms_bkgOnly_PLOT_DYcr.root","./inputs_finer_binning/eejj_PostFit_histograms_L13_M05_PLOT_SR.root","DYcr",138,0.5,"/eos/user/m/mpresill/www/HN/limits/finer_binning/pull_update/",False)
#plotter_pull_v3("muon","./inputs_finer_binning/mumujj_PostFit_histograms_bkgOnly_PLOT_DYcr.root","./inputs_finer_binning/mumujj_PostFit_histograms_L13_M05_PLOT_SR.root","DYcr",138,0.5,"/eos/user/m/mpresill/www/HN/limits/finer_binning/pull_update/",False)
##TOP cr
#plotter_pull_v3("elemu","./inputs_finer_binning/mumujj_PostFit_histograms_bkgOnly_PLOT_TOPcr.root","./inputs_finer_binning/mumujj_PostFit_histograms_L13_M05_PLOT_SR.root","TOPcr",138,0.5,"/eos/user/m/mpresill/www/HN/limits/finer_binning/pull_update/",False)
