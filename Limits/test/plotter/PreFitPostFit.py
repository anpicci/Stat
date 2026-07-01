from ROOT import *
from collections import defaultdict, OrderedDict
from array import array
from tdrStyle import *
import math
import os
import optparse
from Stat.Limits.settings import *
from samplesUL import *
setTDRStyle()
gROOT.SetBatch() # don't pop up canvases

os.system("reset")

usage = 'python3 PreFitPostFit_v2.py'
parser = optparse.OptionParser(usage)

parser.add_option('-y', '--era', dest='era', type=str, default = 'RunII', help='Please enter desired years')
parser.add_option('-u', '--unblind', dest = 'unblind', default = False, action = 'store_true', help = 'unblinding SR, default not')

(opt, args) = parser.parse_args()

blind = (not opt.unblind)

new_dic = defaultdict(dict)
years = opt.era.replace("RunII", "2016M,2017,2018").split(",")
infile = "../postfit_histo_"

indir = "vUL025"
eosspace = "/eos/home-a/apiccine/VBS/nosynch/"
sfolder = eosspace + indir + "/stack/"
prefolder = sfolder + "prefit"
postfolder = sfolder + "postfit"
if not os.path.exists(prefolder):
    os.system("mkdir " + prefolder)
if not os.path.exists(postfolder):
    os.system("mkdir " + postfolder)


histofolders = {}

lumi = {'UL2016M': 36.3, 'UL2017': 41.48, 'UL2018':59.83, "ULRunII":137.13}

processes = []
sigs = []
for sigp in sigpoints:
    sigs = ["VBS_SSWW_" + sig for sig in sigp]
    #for sig in sigs:
        #processes.append(sig)

for bk in bkg:
    if bk in processes:
        continue
    if bk in sigs:
        continue
    if "VBS" in bk and ("_LL_" in bk or "_TT_" in bk or "_TL_" in bk):
        continue
    processes.append(bk)

ychannels = {}

for year in years:
    ychannels[year] = []
    for ch in channels:
        key = ch + year
        ychannels[year].append(key)

def plotPreFitPostFit_v2(region, channel, variable, outdir, year, sb = False, isUL = True, LogX = False):
    print region, variable, outdir, year
    fitfile = infile + variable + ".root"
    f_mlfit = TFile(fitfile,'READ')
    h_data = f_mlfit.Get("binA_" + region + "_prefit/data_obs")  ### : here we have to specify the path of the TH1F with data. 
    
    binLowE = []

    # Pre-Fit
    h_prefit = OrderedDict()
    tothistname = "binA_"+region+"_prefit/TotalBkg"
    h_prefit['totalb'] = f_mlfit.Get(tothistname)                       ####### EDIT. PATH TOTALE BACKGROUNDS DELLA CATEGORIA CHE SI VUOLE PLOTTARE
    totnbins = h_prefit['totalb'].GetNbinsX()

    for i in range(1,totnbins+2):
        binLowE.append(h_prefit['totalb'].GetBinLowEdge(i))

    h_all_prefit = TH1F("h_all_prefit", "h_all_prefit", totnbins, array('d',binLowE))
    #h_other_prefit = TH1F("h_other_prefit","h_other_prefit", totnbins, array('d',binLowE))
    h_stack_prefit = THStack("h_stack_prefit","h_stack_prefit")

    for process in processes: 
        histname = "binA_"+region+"_prefit/" + process
        yproctag = process 
        if yproctag.startswith("Fake"):
            if "muon" in region:
                yproctag += "Mu"
            elif "electron" in region:
                yproctag += "Ele"
        yproctag += "_"
        if isUL:
            yproctag += "UL"
        yproctag += year
        color = merge_dict[yproctag].color

        try:
            f_mlfit.Get(histname).GetEntries()
        except:
            h_prefit[process] = TH1F(process, var + "_" + channel, totnbins, array('d',binLowE))
        else:
            h_prefit[process] = f_mlfit.Get(histname)

        for i in range(1,totnbins+1):
            content = h_prefit[process].GetBinContent(i)
            #width = h_prefit[process].GetBinLowEdge(i+1)-h_prefit[process].GetBinLowEdge(i)
            h_prefit[process].SetBinContent(i,content)#*width)

        h_prefit[process].SetLineColor(color)
        h_prefit[process].SetFillColor(color)

        h_all_prefit.Add(h_prefit[process])
        #if (not process in mainbkgs[region]):
            #h_other_prefit.Add(h_prefit[process])
        h_stack_prefit.Add(h_prefit[process])

    # Post-Fit
    h_postfit = OrderedDict()#{}
    tothistname = "binA_"+region+"_postfit/TotalBkg"
    totsighistname = "binA_"+region+"_postfit/TotalSig"
    totsbhistname = "binA_"+region+"_postfit/TotalProcs"
    h_postfit['totalsig'] = f_mlfit.Get(totsighistname)                     ####EDIT    total signal 
    h_postfit['totalb'] = f_mlfit.Get(tothistname)                        ####EDIT    total bkgs 
    h_postfit['totalsb'] = f_mlfit.Get(totsbhistname)               ####EDIT  total s+b

    h_all_postfit = TH1F("h_all_postfit","h_all_postfit",totnbins, array('d',binLowE))
    #h_other_postfit = TH1F("h_other_postfit","h_other_postfit",len(binLowE)-1,array('d',binLowE))
    #h_minor_postfit = TH1F("h_minor_postfit","h_minor_postfit",len(binLowE)-1,array('d',binLowE))'
    h_stack_postfit = THStack("h_stack_postfit","h_stack_postfit")                    

    #for i in range(1, h_postfit['totalsb'].GetNbinsX()+1):
        #error = h_postfit['totalsb'].GetBinError(i)
        #content = h_postfit['totalsb'].GetBinContent(i)

    for process in processes:
        histname = "binA_"+region+"_postfit/" + process
        #h_postfit[process] = f_mlfit.Get(histname)                       ####EDIT  qui post-fit histo per ogni processo in esame

        yproctag = process 
        if yproctag.startswith("Fake"):
            if "muon" in region:
                yproctag += "Mu"
            elif "electron" in region:
                yproctag += "Ele"
        yproctag += "_"
        if isUL:
            yproctag += "UL"
        yproctag += year
        color = merge_dict[yproctag].color

        try:
            f_mlfit.Get(histname).GetEntries()
        except:
            h_postfit[process] = TH1F(process, var + "_" + channel, totnbins, array('d',binLowE))
        else:
            h_postfit[process] = f_mlfit.Get(histname)

        #if (not h_postfit[process]):
            #continue
        #if (str(h_postfit[process].Integral())=="nan"): 
            #continue

        for i in range(1, totnbins+1):
            error = h_postfit[process].GetBinError(i)
            content = h_postfit[process].GetBinContent(i)
            width = h_postfit[process].GetBinLowEdge(i+1)-h_postfit[process].GetBinLowEdge(i)
            h_postfit[process].SetBinContent(i,content)#*width)

        h_postfit[process].SetLineColor(1)
        h_postfit[process].SetFillColor(color)

        h_all_postfit.Add(h_postfit[process])
        #if (not process in mainbkgs[region]):
            #h_other_postfit.Add(h_postfit[process])
        h_stack_postfit.Add(h_postfit[process])


    gStyle.SetOptStat(0)

    H=600
    W=700
    L = 0.12*W
    R = 0.08*W
    c = TCanvas("c","c",50,50,W,H)
    #c = TCanvas("c","c",600,800)
    SetOwnership(c, False)
    c.cd()
    if LogX is True:
        c.SetLogx()
    c.SetLogy()

    c.SetBottomMargin(0.38)
    c.SetRightMargin(0.06)
    c.SetTickx(1)
    c.SetTicky(1)

    dummy = h_all_prefit.Clone("dummy")
    dummy.SetFillColor(0)
    dummy.SetLineColor(0)
    dummy.SetLineWidth(0)
    dummy.SetMarkerSize(0)
    dummy.SetMarkerColor(0)
    dummy.GetYaxis().SetTitle("Events ")
    dummy.GetXaxis().SetTitle("")
    dummy.GetXaxis().SetTitleSize(0)
    dummy.GetXaxis().SetLabelSize(0)

    if LogX is True:
        dummy.GetXaxis().SetRangeUser(0.4,10)

    #if region is 'signal':
        #dummy.SetMaximum(50*dummy.GetMaximum())
    #else:
    dummy.SetMaximum(25*dummy.GetMaximum())
    dummy.SetMinimum(0.1)
    dummy.GetYaxis().SetTitleOffset(1.15)
    dummy.Draw()
    
    #h_other_prefit.SetLineColor(1)
    #h_other_prefit.SetFillColor(33)
    #h_other_prefit.Scale(1,"width")

    h_all_prefit.SetLineColor(2)
    h_all_prefit.SetLineWidth(2)

    h_all_postfit.SetLineColor(kAzure-4)
    h_all_postfit.SetLineWidth(2)

    h_stack_postfit.Draw("histsame")

    if sb is True:
        h_postfit['totalsig'].SetLineColor(kOrange)
        h_postfit['totalsig'].SetLineStyle(1)
        h_postfit['totalsig'].SetLineWidth(2)
        h_postfit['totalsig'].Draw("samehist")

    h_data.SetMarkerStyle(20)
    h_data.SetLineColor(1)
    h_data.SetMarkerSize(1.2)
    if not "SR" in region:
        h_data.Draw("epsame")

    legend = TLegend(0.60, 0.70, 0.92, .92)
    #legend.SetTextSize(0.04)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.AddEntry(h_data, "Data", "elp")

    for process in processes:
        yproctag = process 
        if yproctag.startswith("Fake"):
            if "muon" in region:
                yproctag += "Mu"
            elif "electron" in region:
                yproctag += "Ele"
        yproctag += "_"
        if isUL:
            yproctag += "UL"
        yproctag += year
        proclabel = merge_dict[yproctag].leglabel
        legend.AddEntry(h_postfit[process], proclabel, "f")

    ysigtag = sigs[0] + "_"
    if isUL:
        ysigtag += "UL"
    ysigtag += year
    siglabel = merge_dict[ysigtag].leglabel
    legend.AddEntry(h_postfit['totalsig'], siglabel, "f")

    legend.SetShadowColor(0)
    legend.SetFillColor(0)
    legend.SetLineColor(0)
    legend.Draw("same")
    latex2 = TLatex()
    latex2.SetNDC()
    latex2.SetTextSize(0.6*c.GetTopMargin())
    latex2.SetTextFont(42)
    latex2.SetTextAlign(31) # align right
    latex2.DrawLatex(0.94, 0.95, str(lumi["UL"+year]) + " fb^{-1} (13 TeV)")
    latex2.SetTextSize(0.6*c.GetTopMargin())
    latex2.SetTextFont(62)
    latex2.SetTextAlign(11) # align right
    latex2.DrawLatex(0.175, 0.85, "CMS #it{#bf{Preliminary}}")
    latex2.SetTextSize(0.6*c.GetTopMargin())
    latex2.SetTextFont(52)
    latex2.SetTextAlign(11)
    offset = 0.005
    #latex2.DrawLatex(0.28+offset, 0.85, "Preliminary")
    channelLabel = TLatex()
    channelLabel.SetNDC()
    channelLabel.SetTextSize(0.5*c.GetTopMargin())
    channelLabel.SetTextFont(42)
    channelLabel.SetTextAlign(11)

    genreg = region.split("_")[0]
    
    chlab = channels_labels[genreg]

    channelLabel.DrawLatex(0.175, 0.82, chlab)
    channelLabel.Draw("same")

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

    ########### Ratio plot ###############
    met = []
    dmet = []
    ratio_pre = []
    ratio_pre_hi = []
    ratio_pre_lo = []
    ratio_post = []
    ratio_post_hi = []
    ratio_post_lo = [];

    for i in range(1,h_all_prefit.GetNbinsX()+1):
        ndata = h_data.GetBinContent(i)
        if (ndata > 0.0):
            e_data_hi = h_data.GetBinError(i)/ndata
            e_data_lo = h_data.GetBinError(i)/ndata
        else:
            e_data_hi = 0.0
            e_data_lo = 0.0
        n_all_pre = h_all_prefit.GetBinContent(i)
        n_all_post = h_all_postfit.GetBinContent(i)

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

    ratiosys = h_postfit['totalb'].Clone()
    for hbin in range(0,ratiosys.GetNbinsX()+1):
        ratiosys.SetBinContent(hbin+1,1.0)
        if (h_postfit['totalb'].GetBinContent(hbin+1)>0):
            ratiosys.SetBinError(hbin+1,h_postfit['totalb'].GetBinError(hbin+1)/h_postfit['totalb'].GetBinContent(hbin+1))
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
    dummy2.GetYaxis().SetLabelSize(0.03)
    dummy2.GetXaxis().SetLabelSize(0)
    dummy2.GetYaxis().SetNdivisions(5);
    dummy2.GetYaxis().CenterTitle()
    dummy2.GetYaxis().SetTitleSize(0.03)
    dummy2.GetYaxis().SetTitleOffset(1.6)
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
    if not blind and "SR" in region:
        g_ratio_pre.Draw("epsame")
        g_ratio_post.Draw("epsame")

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



    ##Compute the pulls
    pull_count = TH1F("pull_count","pull",100,-5,5)
    data_pull = h_data.Clone("pull")
    data_pull.Add(h_postfit['totalb'], -1)
    data_pull.Sumw2()
    
    addedsqrt = 0
    mean = 0
    sigma = 0
    sigmaBILL = 0
    chi2 = 0
    TH1.StatOverflows(1)

    #pull_count = TH1F("pull_count","pull",100,-5,5)

    for hbin in range(0, data_pull.GetNbinsX()+1):
        if (h_postfit['totalb'].GetBinContent(hbin)>0):
            if (math.fabs(h_data.GetBinError(hbin)*h_data.GetBinError(hbin) - h_postfit['totalb'].GetBinError(hbin)* h_postfit['totalb'].GetBinError(hbin)) < 0.001) or (h_postfit['totalb'].GetBinError(hbin) > h_data.GetBinError(hbin) ):
                data_pull.SetBinContent(hbin,0)
            else:
                sigmaBILL = math.sqrt(h_data.GetBinError(hbin)*h_data.GetBinError(hbin) - h_postfit['totalb'].GetBinError(hbin)*h_postfit['totalb'].GetBinError(hbin))
                #sigmaBILL = math.sqrt(h_data.GetBinError(hbin)*h_data.GetBinError(hbin) + h_postfit['totalb'].GetBinError(hbin)*h_postfit['totalb'].GetBinError(hbin))
                data_pull.SetBinContent(hbin,(h_data.GetBinContent(hbin) -  h_postfit['totalb'].GetBinContent(hbin))/sigmaBILL)
                #print ("data: ", h_data.GetBinContent(hbin)) 
                #print (" +-, ", h_data.GetBinError(hbin))
                #print ("MC: ", h_postfit['totalb'].GetBinContent(hbin))
                #print (" +-, ", h_postfit['totalb'].GetBinError(hbin))
            data_pull.SetBinError(hbin,0)

        if (hbin > 2):
            pull_count.Fill(data_pull.GetBinContent(hbin))
            print " pull: ", data_pull.GetBinContent(hbin)

            if (abs(data_pull.GetBinContent(hbin)) >= 2):
                print " ATTENZIONE "
                print ">>>>>>>>>>>>>>"
                print " data yield : ", h_data.GetBinContent(hbin)  
                print " +- ", h_data.GetBinError(hbin)
                print " BKG error : ", h_postfit['totalb'].GetBinContent(hbin) 
                print " +- ", h_postfit['totalb'].GetBinError(hbin)
                print "<<<<<<<<<<<<<<"

    #print "MEAN: ", mean
    #print "CHI2: ", math.sqrt(chi2)/data_pull.GetNbinsX()
    #print "Added", sqrt(addedsqrt), "divided: ", sqrt(addedsqrt)/data_pull.GetNbinsX()
    #print "Added2", addedsqrt, "divided: ", addedsqrt/data_pull.GetNbinsX()
    data_pull.SetLineColor(kAzure-4)
    data_pull.SetFillColor(kAzure-4)
    data_pull.SetMarkerColor(kAzure-4)
    pull_count.SaveAs(postfolder + "/pull_"+region+"_"+variable+".root")
    data_pull.SaveAs(postfolder + "/test_"+region+"_"+variable+".root")
    
    data_pull_sig = h_data.Clone("pull_sig")
    data_pull_sig.Sumw2()

    for hbin in range(0,data_pull_sig.GetNbinsX()+1):
        if (h_postfit['totalb'].GetBinContent(hbin)>0):
            #print "bin",hbin,"data pull diff", data_pull_sig.GetBinContent(hbin), "sys", h_postfit['totalb'].GetBinError(hbin)
            data_pull_sig.SetBinContent(hbin, data_pull_sig.GetBinContent(hbin)/h_postfit['totalb'].GetBinError(hbin))
            data_pull_sig.SetBinError(hbin, 0)

    data_pull_sig.SetLineColor(2)
    data_pull_sig.SetFillColor(2)
    data_pull_sig.SetFillStyle(3004)
    data_pull_sig.SetMarkerColor(2)
    legend3 = TLegend(0.20,0.21,0.60,0.23,"","brNDC")
    legend3.AddEntry(data_pull    , "Background only", "f")
    legend3.SetNColumns(2)
    legend3.SetShadowColor(0)
    legend3.SetFillColor(0)
    legend3.SetLineColor(0)

    dummy3 = TH1F("dummy3","dummy3",len(binLowE)-1,array('d',binLowE))

    for i in range(1,dummy3.GetNbinsX()):
        dummy3.SetBinContent(i,1.0)

    dummy3.GetYaxis().SetTitle("#frac{(Data-Pred.)}{#sigma}")
    dummy3.SetLineColor(0)
    dummy3.SetMarkerColor(0)
    dummy3.SetLineWidth(0)
    dummy3.SetMarkerSize(0)

    if LogX is True:
        dummy3.GetXaxis().SetRangeUser(0.4,10)
    dummy3.GetYaxis().SetLabelSize(0.04)

    #if region is 'signal':
        #dummy3.GetYaxis().SetLabelSize(0.03)
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
    c.SaveAs(postfolder+"/"+region+"_"+variable+".pdf")
    c.SaveAs(postfolder+"/"+region+"_"+variable+".png")

    #### memory management
    del pull_count
    c.Close()
    f_mlfit.Close()

variables = ["m_jj"]

for var in variables:
    for year in years:
        for ych in ychannels[year]:
            plotPreFitPostFit_v2(ych, "ltau", var, indir, year)
            #break
        break
    break
