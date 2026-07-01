from ROOT import *
from collections import defaultdict, OrderedDict
from array import array
from tdrStyle import *
import math
import os
import optparse
#from Stat.Limits.settings import *
from Stat.Limits.variables import *
from samplesUL import *
from CMS_lumi import CMS_lumi
import copy 

setTDRStyle()
gROOT.SetBatch() # don't pop up canvases

#os.system("reset")

usage = 'python3 PreFitPostFit_v2.py'
parser = optparse.OptionParser(usage)

parser.add_option('-y', '--era', dest='era', type=str, default = 'RunII', help='Please enter desired years')
parser.add_option('--folder', dest='folder', type=str, default = 'vUL025', help='Please enter desired folder')
parser.add_option('-u', '--unblind', dest = 'unblind', default = False, action = 'store_true', help = 'unblinding SR, default not')
parser.add_option('--vars', dest='postvars', type='string', default = 'm_o1', help = 'Variables to postfit')
parser.add_option('--fitted', dest='fittedvars', type='string', default = 'm_o1,m_o1', help = 'Variables fitted in SR and CRs')
parser.add_option('--model', dest='model', type='string', default = 'sm', help = 'Variables fitted in SR and CRs')
parser.add_option('--lastbins', dest='lastbins', default = False, action='store_true', help='only last bins for DNNs')
parser.add_option('--scale', dest='scale', default = False, action='store_true', help='scale to bin width')
parser.add_option('--linscale', dest='linscale', default = False, action='store_true', help='linscale')
parser.add_option('--settmod', dest='settmod', type='string', default = 'total', help = 'Specify settmod')
parser.add_option('--eos', dest='eos', type='string', default = '', help = 'Destination of postfits')

(opt, args) = parser.parse_args()

toScale = opt.scale

if len(opt.fittedvars.split(",")) != 2:
    raise RuntimeError("--fitted must be of the type \"[srvar],[[crvar]\"!")

import importlib

setname = opt.settmod
print setname
settmod = importlib.import_module(setname)

bkg = settmod.bkg
histos = settmod.histos
years = settmod.years
leptons = settmod.leptons
sigpoints = settmod.sigpoints
lssamples_1D = settmod.lssamples_1D
syst = settmod.syst
sr_var = settmod.sr_var
cr_var = settmod.cr_var
channels = settmod.channels
srvars = opt.postvars
channels_labels = settmod.channels_labels

srvar, crvar = opt.fittedvars.split(",")

blind = (not opt.unblind)

new_dic = defaultdict(dict)
years = opt.era#.replace("RunII", "2016M,2017,2018")
indir = opt.folder

modd = ""
if opt.model == "SM":
    modd += "VBS_SSWW_"
if not opt.model.startswith("F"):
    modd += opt.model
else:
    modd += opt.model.replace("_" + opt.model.split("_")[-1], "")

infile = indir
#print "\nindir, infile", indir, infile

eosspace = opt.eos

postfolder = eosspace + "/" + modd
if blind:
    postfolder += "_TF"
else:
    postfolder += "_DF"
postfolder += "/" + srvar + "_" + crvar
if not os.path.exists(postfolder):
    print "Creating", postfolder
    os.system("mkdir -p " + postfolder)
else:
    print "Already exists", postfolder
histofolders = {}

lumi = {'UL2016M': 36.3, 'UL2017': 41.48, 'UL2018':59.83, "ULRunII":138}

sigs = []
for sigp in sigpoints:
    for sig in sigp:
        signn = sig
        if not sig.startswith("WpWp"):
            signn = "VBS_SSWW_" + signn

        sigs.append(signn)

processes = bkg    
toremove = []
for p in processes:
    isSM = False

    if p.startswith("DYJets"):
        continue

    for sigp in sigpoints:
        for sig in sigp:
            if '_SM' in sig or sig == 'SM' or sig.startswith("WpWp"):
                if 'TT_' in sig or 'TL_' in sig or 'LL_' in sig:
                    if (sig in p and not "QCD" in p) or 'SSWW_SM' in p:
                        isSM = True
                        break
                elif '_SM' in p:
                    isSM = True

                    break
                elif sig == "WpWpJJ" or sig == "WpWpJJ_QCD":
                    if p == "WpWpJJ_QCD":
                        isSM = True
                        break
            else:
                if 'TT_' in p or 'TL_' in p or 'LL_' in p or p=="VBS_SSWW_SM":
                    isSM = True
                    break
    if isSM:
        toremove.append(p)

for tor in toremove:
    processes.remove(tor)

#print "sigs:", sigs
#print "processes", processes

ychannels = {}

for year in years:
    ychannels[year] = []
    for ch in channels:
        key = ch + year
        ychannels[year].append(key)

for varr in variables:
    print varr.title

def PreFitPostFit_v2(region, channel, variable, outdir, years, infold, sb = True, isUL = True, LogX = False):
    print "region, channel, variable, outdir, years"
    print region, channel, variable, outdir, years
    
    vartitle = ""
    for possvar in variables:
        if variable == possvar.name:
            vartitle = possvar.title
    
    fitfile = infold + "histo_" + variable + "_" + region + ".root"

    print "Opening", fitfile
    f_mlfit = TFile(fitfile, 'READ')


    lyears = years.split(",")
    eras = years.split(",")
    if len(lyears) == 3:
        lyears.append("RunII")

    h_data = OrderedDict()
    h_data["UL2016M"] = OrderedDict()
    h_data["UL2017"] = OrderedDict()
    h_data["UL2018"] = OrderedDict()
    h_data["ULRunII"] = OrderedDict()

    h_prefit = OrderedDict()
    h_prefit["UL2016M"] = OrderedDict()
    h_prefit["UL2017"] = OrderedDict()
    h_prefit["UL2018"] = OrderedDict()
    h_prefit["ULRunII"] = OrderedDict()

    h_postfit = OrderedDict()
    h_postfit["UL2016M"] = OrderedDict()
    h_postfit["UL2017"] = OrderedDict()
    h_postfit["UL2018"] = OrderedDict()
    h_postfit["ULRunII"] = OrderedDict()

    histdicts = [
        h_data,
        h_prefit,
        h_postfit,
    ]

    for y in lyears:
        yul = "UL" + y
        print "HELLO yearsul", yul
        if not "RunII" in y:
            h_data[yul]["Data"] = f_mlfit.Get(region + "_" + y + "_prefit/data_obs")
        else:
            h_data[yul]["Data"] = f_mlfit.Get("prefit/data_obs")
        if toScale:
            h_data[yul]["Data"].Scale(1, "width") ###scalewidth
        #gROOT.SetStyle('Plain')
        #gStyle.SetPalette(1)
        #gStyle.SetOptStat(0)
        binLowE = []

        if channel == 'ltau':
            if "muon" in region:
                lep_tag = "#mu+"
                cmsreg = channel.replace("ltau", "#tau_{h}")
            elif "electron" in region:
                lep_tag = "e+"
                cmsreg = channel.replace("ltau", "#tau_{h}")
            else:
                lep_tag = "Combined"
                cmsreg = ""
        else:
            lep_tag = "e+#mu"
            cmsreg = ""

        cmsreg = lep_tag + cmsreg 
        genreg = region.split("_")[0]
        chlab = channels_labels[genreg]
        cmsreg += "\n"+chlab

        # Pre-Fit
        print "y", y
        h_prefit[yul] = OrderedDict()
        if not "RunII" in y:
            tothistname = region +"_" + y + "_prefit/TotalBkg"
        else:
            tothistname = "prefit/TotalBkg"
            
        print "\ntothistname", tothistname
        h_prefit[yul]['totalb'] = f_mlfit.Get(tothistname)
        if toScale:
            h_prefit[yul]['totalb'].Scale(1, "width") ###scalewidth 
        totnbins = h_prefit[yul]['totalb'].GetNbinsX()

        for i in range(1,totnbins+2):
            binLowE.append(h_prefit[yul]['totalb'].GetBinLowEdge(i))

        print "\nbinning", binLowE
        if opt.lastbins:
            firstbin = None
            lastbin = binLowE[-1]
            for edge in binLowE:
                if variable.startswith("DNN"):
                    if 0.8 - edge > 0.01:
                        continue
                    else:
                        firstbin = copy.deepcopy(edge)
                        break
                else:
                    firstbin = binLowE[-3]
            #print firstbin, lastbin
        
        h_all_prefit = h_prefit[yul]['totalb'] #TH1F("h_all_prefit", "h_all_prefit", totnbins, array('d',binLowE))
        #h_other_prefit = TH1F("h_other_prefit","h_other_prefit", totnbins, array('d',binLowE))
        #h_stack_prefit = THStack("h_stack_prefit","h_stack_prefit")
        
        h_prefit[yul]['totalb'].SetFillColor(kGray)

        # Post-Fit
        if not "RunII" in y:
            tothistname = region +"_" + y + "_postfit/TotalBkg"
            totsighistname = region +"_" + y + "_postfit/TotalSig"
            totsbhistname = region +"_" + y + "_postfit/TotalProcs"
        else:
            tothistname = "postfit/TotalBkg"
            totsighistname = "postfit/TotalSig"
            totsbhistname = "postfit/TotalProcs"

        h_postfit[yul]['totalsig'] = f_mlfit.Get(totsighistname)                     ####EDIT    total signal
        if opt.lastbins:
            h_postfit[yul]['totalsig'].GetXaxis().SetRangeUser(firstbin, lastbin)
        if toScale:
            h_postfit[yul]['totalsig'].Scale(1, "width") ###scalewidth 

        h_postfit[yul]['totalb'] = f_mlfit.Get(tothistname)                        ####EDIT    total bkgs 
        h_postfit[yul]['totalb'].SetFillColor(kGray)
        h_postfit[yul]['totalb'].SetLineColor(kGray)
        if opt.lastbins:
            h_postfit[yul]['totalb'].GetXaxis().SetRangeUser(firstbin, lastbin)
        if toScale:
            h_postfit[yul]['totalb'].Scale(1, "width") ###scalewidth 
        
        h_postfit[yul]['totalsb'] = f_mlfit.Get(totsbhistname)               ####EDIT  total s+b
        if opt.lastbins:
            h_postfit[yul]['totalsb'].GetXaxis().SetRangeUser(firstbin, lastbin)
        if toScale:
            h_postfit[yul]['totalsb'].Scale(1, "width") ###scalewidth 
        

        h_all_postfit = h_postfit[yul]['totalb'] #TH1F("h_all_postfit","h_all_postfit",totnbins, array('d',binLowE))
        h_stack_postfit = THStack("h_stack_postfit","h_stack_postfit")                    
        h_stack_postfit.Add(h_postfit[yul]['totalb'].Clone(""))

        #for i in range(1, h_postfit[yul]['totalsb'].GetNbinsX()+1):
            #error = h_postfit[yul]['totalsb'].GetBinError(i)
            #content = h_postfit[yul]['totalsb'].GetBinContent(i)


        H=1000
        W=900
        L = 0.12*W
        R = 0.08*W
        c = TCanvas("c","c",50,50,W,H)
        #c = TCanvas("c","c",600,800)
        SetOwnership(c, False)
        c.cd()
        if LogX is True:
            c.SetLogx()
        if not opt.linscale:
            c.SetLogy()

        c.SetFillColor(0)
        c.SetBorderMode(0)
        c.SetFrameFillStyle(0)
        c.SetFrameBorderMode(0)
        c.SetLeftMargin(0.12 )
        c.SetRightMargin(0.9)
        c.SetTopMargin(1)
        c.SetBottomMargin(-1)
        c.SetTickx(1)
        c.SetTicky(1)
        c.cd()

        pad1= ROOT.TPad("pad1", "pad1", 0, 0.39, 1, 1)
        pad1.SetTopMargin(0.1)
        pad1.SetBottomMargin(0.02)
        pad1.SetLeftMargin(0.12)
        pad1.SetRightMargin(0.05)
        pad1.SetBorderMode(0)
        pad1.SetTickx(1)
        pad1.SetTicky(1)
        pad1.Draw()
        pad1.cd()

        if not opt.lastbins:
            if not (blind and "SR" in region):
                maximum = max(h_stack_postfit.GetMaximum(),h_data[yul]["Data"].GetMaximum())
            else:
                maximum = h_stack_postfit.GetMaximum()
        else:
            print range(binLowE.index(firstbin)+1, binLowE.index(firstbin)+2)
            print [h_postfit[yul]['totalb'].GetBinContent(idxb) for idxb in range(binLowE.index(firstbin)+1, binLowE.index(lastbin)+2)]
            maximum = max([h_postfit[yul]['totalb'].GetBinContent(idxb) for idxb in range(binLowE.index(firstbin)+1, binLowE.index(lastbin)+2)])
        print "maximum", maximum
        #print h_stack_postfit.GetMaximum(), h_data[yul]["Data"].GetMaximum()

        if not opt.linscale:
            h_stack_postfit.SetMinimum(0.01)
            pad1.SetLogy()
            h_stack_postfit.SetMaximum(maximum*10000)
        else:
            h_stack_postfit.SetMinimum(0.0001)
            h_stack_postfit.SetMaximum(maximum*2)
        #h_other_prefit.SetLineColor(1)
        #h_other_prefit.SetFillColor(33)
        #h_other_prefit.Scale(1,"width")

        h_all_prefit.SetLineColor(2)
        h_all_prefit.SetLineWidth(2)

        h_all_postfit.SetLineColor(kAzure-4)
        h_all_postfit.SetLineWidth(2)

        ytitle = "Events"
        if toScale:
            ytitle += " / bin width"

        ysigtag = sigs[0]
        if ysigtag.startswith("Fake"):
            if "muon" in region:
                ysigtag += "Mu"
            elif "electron" in region:
                ysigtag += "Ele"
        ysigtag += "_"
        if isUL:
            ysigtag += "UL"
        if not "RunII" in y:
            ysigtag += y
        else:
            ysigtag += "2017"
        #print "color sig:", sigs, sigs[0], ysigtag
        sigcolor = ROOT.kRed
        
        #if sb is True:
        #print("h_postfit[yul]['totalsig']:", h_postfit[yul]['totalsig'])
        h_postfit[yul]['totalsig'].SetLineColor(sigcolor)
        #h_postfit[yul]['totalsig'].SetLineStyle(1)
        h_postfit[yul]['totalsig'].SetLineWidth(3)
        if opt.lastbins:
            h_postfit[yul]['totalsig'].GetXaxis().SetRangeUser(firstbin, lastbin)
        #### printing signal
        #h_postfit[yul]['totalsig'].Draw("hist same")
        h_postfit[yul]['totalsig'].SetFillColor(sigcolor)
        h_stack_postfit.Add(h_postfit[yul]['totalsig'].Clone(""))


        h_stack_postfit.Draw("hist")
        if opt.lastbins:
            h_stack_postfit.GetHistogram().GetXaxis().SetRangeUser(firstbin, lastbin)
        h_stack_postfit.GetYaxis().SetTitle(ytitle)
        h_stack_postfit.GetYaxis().SetTitleFont(42)
        
        h_stack_postfit.GetXaxis().SetLabelOffset(1.8)
        h_stack_postfit.GetYaxis().SetTitleOffset(1.25)
        h_stack_postfit.GetXaxis().SetLabelSize(0.15)
        h_stack_postfit.GetYaxis().SetLabelSize(0.04)
        h_stack_postfit.GetYaxis().SetTitleSize(0.045)
        h_stack_postfit.SetTitle("")


        h_data[yul]["Data"].SetMarkerStyle(20)
        #h_data[yul]["Data"].SetLineColor(1)
        h_data[yul]["Data"].SetMarkerSize(0.9)
        if opt.lastbins:
            h_data[yul]["Data"].GetXaxis().SetRangeUser(firstbin, lastbin)

        if not (blind and "SR" in region):
            h_data[yul]["Data"].Draw("epsamex0")


        legend = TLegend(0.37,0.58,0.94,0.87)
        legend.SetNColumns(2)
        legend.SetFillColor(0)
        legend.SetFillStyle(0)
        legend.SetTextFont(42)
        legend.SetBorderSize(0)
        legend.SetTextSize(0.034)
        legend.AddEntry(h_data[yul]["Data"], "Data", "ep")

        legend.AddEntry(h_postfit[yul]['totalb'], 'Total bkg', "f")


        ysigtag = sigs[0] + "_"
        if isUL:
            ysigtag += "UL"
        if not "RunII" in y:
            ysigtag += y
        else:
            ysigtag += "2017"

        siglabel = None 
        for plotsam in plot_list:
            if plotsam.label == ysigtag:
                siglabel = plotsam.leglabel
                break

        ###print signal
        legend.AddEntry(h_postfit[yul]['totalsig'], siglabel, "f")
        print "label sig:", sigs, sigs[0], ysigtag, siglabel

        #h_err = h_stack_postfit.GetStack().Last().Clone("h_err")
        h_err = h_postfit[yul]['totalsb'].Clone("h_err")
        ##h_err = h_all_postfit.Clone("h_err")
        #h_err = h_postfit[yul]['totalb'].Clone("h_err")
        #h_err.Add(h_postfit[yul]['totalsig'].Clone(""))
        h_err.SetLineWidth(100)
        h_err.SetFillStyle(3154)
        h_err.SetMarkerSize(0)
        h_err.SetFillColor(ROOT.kGray+2)
        if opt.lastbins:
            h_err.GetXaxis().SetRangeUser(firstbin, lastbin)
        h_err.Draw("e2same0")
        legend.AddEntry(h_err, "Stat. + Syst. Unc.", "f")

        #legend.SetShadowColor(0)
        #legend.SetFillColor(0)
        #legend.SetLineColor(0)
        legend.Draw("same")

        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = ""
        
        lumi_sqrtS = "%s fb^{-1}  (13 TeV)"%(lumi["UL"+y])
    
        iPeriod = 0
        iPos = 11
        CMS_lumi(pad1, lumi_sqrtS, iPos, str(cmsreg))

        c.cd()

        pad2= ROOT.TPad("pad2", "pad2", 0, 0.15 , 1, 0.4)
        SetOwnership(pad2, False)
        pad2.SetTopMargin(0.05)
        pad2.SetBottomMargin(0.45)
        pad2.SetLeftMargin(0.12)
        pad2.SetRightMargin(0.05)
        gStyle.SetHatchesSpacing(2)
        gStyle.SetHatchesLineWidth(2)
        c.cd()
        pad2.Draw()
        pad2.cd()

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
            ndata = h_data[yul]["Data"].GetBinContent(i)
            if (ndata > 0.0):
                e_data_hi = h_data[yul]["Data"].GetBinError(i)/ndata
                e_data_lo = h_data[yul]["Data"].GetBinError(i)/ndata
            else:
                e_data_hi = 0.0
                e_data_lo = 0.0
            n_all_pre = h_all_prefit.GetBinContent(i)
            n_all_post = h_postfit[yul]['totalb'].GetBinContent(i)

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
        g_ratio_pre.SetMarkerStyle(25)
        g_ratio_post = TGraphAsymmErrors(v_met,v_ratio_post,v_dmet,v_dmet,v_ratio_post_lo,v_ratio_post_hi)
        g_ratio_post.SetMarkerStyle(20)

        ratiosys_post = h_postfit[yul]['totalb'].Clone("")
        for hbin in range(0,ratiosys_post.GetNbinsX()+1):
            ratiosys_post.SetBinContent(hbin+1,1.0)
            if (h_postfit[yul]['totalb'].GetBinContent(hbin+1)>0):
                ratiosys_post.SetBinError(hbin+1,h_postfit[yul]['totalb'].GetBinError(hbin+1)/h_postfit[yul]['totalb'].GetBinContent(hbin+1))
            else:
                ratiosys_post.SetBinError(hbin+1,0)

        ratiosys_post.GetYaxis().SetRangeUser(-2.1, 3.1)
        ratiosys_post.GetYaxis().SetNdivisions(503)
        ratiosys_post.GetXaxis().SetLabelFont(42)
        ratiosys_post.GetYaxis().SetLabelFont(42)
        ratiosys_post.GetXaxis().SetTitleFont(42)
        ratiosys_post.GetYaxis().SetTitleFont(42)
        ratiosys_post.GetXaxis().SetTitleOffset(1.1)
        ratiosys_post.GetYaxis().SetTitleOffset(0.35)
        ratiosys_post.GetXaxis().SetLabelSize(0.1)
        ratiosys_post.GetYaxis().SetLabelSize(0.1)
        ratiosys_post.GetXaxis().SetTitleSize(0.16)
        ratiosys_post.GetYaxis().SetTitleSize(0.1)

        g_ratio_post.SetLineColor(kGreen+2)
        g_ratio_post.SetMarkerColor(kGreen+2)
        ratiosys_post.SetFillColor(kGreen-8) #SetFillColor(ROOT.kYellow)
        ratiosys_post.SetLineColor(kGreen-8) #SetLineColor(1)

        ratiosys_post.SetLineWidth(1)
        ratiosys_post.SetMarkerSize(0)
        ratiosys_post.GetYaxis().SetTitle("Data / Pred.")


        ratiosys_pre = h_all_prefit.Clone()
        for hbin in range(0,ratiosys_pre.GetNbinsX()+1):
            ratiosys_pre.SetBinContent(hbin+1,1.0)
            if (h_all_prefit.GetBinContent(hbin+1)>0):
                ratiosys_pre.SetBinError(hbin+1,h_all_prefit.GetBinError(hbin+1)/h_all_prefit.GetBinContent(hbin+1))
            else:
                ratiosys_pre.SetBinError(hbin+1,0)

        ratiosys_pre.GetYaxis().SetRangeUser(-2.1, 3.1)
        ratiosys_pre.GetYaxis().SetNdivisions(503)
        ratiosys_pre.GetXaxis().SetLabelFont(42)
        ratiosys_pre.GetYaxis().SetLabelFont(42)
        ratiosys_pre.GetXaxis().SetTitleFont(42)
        ratiosys_pre.GetYaxis().SetTitleFont(42)
        ratiosys_pre.GetXaxis().SetTitleOffset(1.1)
        ratiosys_pre.GetYaxis().SetTitleOffset(0.35)
        ratiosys_pre.GetXaxis().SetLabelSize(0.1)
        ratiosys_pre.GetYaxis().SetLabelSize(0.1)
        ratiosys_pre.GetXaxis().SetTitleSize(0.16)
        ratiosys_pre.GetYaxis().SetTitleSize(0.1)

        g_ratio_pre.SetLineColor(kOrange-3)
        g_ratio_pre.SetMarkerColor(kOrange-3)
        ratiosys_pre.SetFillColor(kOrange-9) #SetFillColor(ROOT.kYellow)
        ratiosys_pre.SetLineColor(kOrange-9) #SetLineColor(1)

        ratiosys_pre.SetLineWidth(1)
        ratiosys_pre.SetMarkerSize(0)
        ratiosys_pre.GetYaxis().SetTitle("Data / Pred.")

        if opt.lastbins:
            ratiosys_pre.GetXaxis().SetRangeUser(firstbin, lastbin)
            ratiosys_post.GetXaxis().SetRangeUser(firstbin, lastbin)

        ratiosys_pre.Draw("e2same")
        ratiosys_post.Draw("e2same")

        ratio = h_data[yul]["Data"].Clone("ratio")
        ratio.SetLineColor(ROOT.kBlack)
        ratio.SetMaximum(10)
        ratio.SetMinimum(0)
        ratio.Sumw2()
        ratio.SetStats(0)
        
        ratio.Divide(h_err)
        ratio.SetMarkerStyle(20)
        ratio.SetMarkerSize(0.9)
        ratio.GetYaxis().SetRangeUser(-2.1, 3.1)
        ratio.GetYaxis().SetNdivisions(503)
        ratio.GetXaxis().SetLabelFont(42)
        ratio.GetYaxis().SetLabelFont(42)
        ratio.GetXaxis().SetTitleFont(42)
        ratio.GetYaxis().SetTitleFont(42)
        ratio.GetXaxis().SetTitleOffset(1.1)
        ratio.GetYaxis().SetTitleOffset(0.35)
        ratio.GetXaxis().SetLabelSize(0.1)
        ratio.GetYaxis().SetLabelSize(0.1)
        ratio.GetXaxis().SetTitleSize(0.16)
        ratio.GetYaxis().SetTitleSize(0.16)
        if not (blind and "SR" in region):
            #ratio.Draw("epx0e0 same")
            ratio.SetTitle("")

        f1 = TF1("f1","1",-5000,5000);
        f1.SetLineColor(1);
        f1.SetLineStyle(2);
        f1.SetLineWidth(2);
        #f1.Draw("same")
        if not (blind and "SR" in region):
            if opt.lastbins:
                g_ratio_pre.GetXaxis().SetRangeUser(firstbin, lastbin)
                g_ratio_post.GetXaxis().SetRangeUser(firstbin, lastbin)
            
            g_ratio_pre.Draw("epsame")
            g_ratio_post.Draw("epsame")


        legend2 = TLegend(0.75,0.99,0.95,0.955)#,"","brNDC");
        legend2.SetNColumns(2)
        legend2.SetShadowColor(0);
        legend2.SetFillColor(0);
        legend2.SetLineColor(0);
        legend2.SetTextFont(42)
        legend2.SetBorderSize(0)
        legend2.SetTextSize(0.05)
        legend2.AddEntry(ratiosys_pre, "Pre-fit Unc.", "f")#ple
        legend2.AddEntry(ratiosys_post, "Post-fit Unc.", "f")#ple
        legend2.Draw("same")

        legend3 = TLegend(0.55,0.99,0.75,0.955)#,"","brNDC");
        legend3.SetNColumns(2)
        legend3.SetShadowColor(0);
        legend3.SetFillColor(0);
        legend3.SetLineColor(0);
        legend3.SetTextFont(42)
        legend3.SetBorderSize(0)
        legend3.SetTextSize(0.05)
        legend3.AddEntry(g_ratio_post, "Post-fit", "ple")
        legend3.AddEntry(g_ratio_pre, "Pre-fit", "ple")#ple
        legend3.Draw("same")

        pad3= ROOT.TPad("pad3", "pad3", 0, 0 , 1, 0.26)
        SetOwnership(pad3, False)
        pad3.SetTopMargin(0.05)
        pad3.SetBottomMargin(0.45)
        pad3.SetLeftMargin(0.12)
        pad3.SetRightMargin(0.05)
        gStyle.SetHatchesSpacing(2)
        gStyle.SetHatchesLineWidth(2)
        c.cd()
        pad3.Draw()
        pad3.cd()

        ##Compute the pulls
        pull_count = TH1F("pull_count","pull",100,-5,5)
        data_pull = h_data[yul]["Data"].Clone("pull")
        data_pull.Add(h_postfit[yul]['totalb'], -1)
        data_pull.Sumw2()
        
        addedsqrt = 0
        mean = 0
        sigma = 0
        sigmaBILL = 0
        chi2 = 0
        TH1.StatOverflows(1)

        #pull_count = TH1F("pull_count","pull",100,-5,5)

        for hbin in range(0, data_pull.GetNbinsX()+1):
            if (h_postfit[yul]['totalb'].GetBinContent(hbin)>0):
                if (math.fabs(h_data[yul]["Data"].GetBinError(hbin)*h_data[yul]["Data"].GetBinError(hbin) - h_postfit[yul]['totalb'].GetBinError(hbin)* h_postfit[yul]['totalb'].GetBinError(hbin)) < 0.001) or (h_postfit[yul]['totalb'].GetBinError(hbin) > h_data[yul]["Data"].GetBinError(hbin) ): #or (blind and "SR" in region):
                    data_pull.SetBinContent(hbin,0)
                else:
                    sigmaBILL = math.sqrt(h_data[yul]["Data"].GetBinError(hbin)*h_data[yul]["Data"].GetBinError(hbin) - h_postfit[yul]['totalb'].GetBinError(hbin)*h_postfit[yul]['totalb'].GetBinError(hbin))
                    #sigmaBILL = math.sqrt(h_data[yul]["Data"].GetBinError(hbin)*h_data[yul]["Data"].GetBinError(hbin) + h_postfit[yul]['totalb'].GetBinError(hbin)*h_postfit[yul]['totalb'].GetBinError(hbin))
                    data_pull.SetBinContent(hbin,(h_data[yul]["Data"].GetBinContent(hbin) -  h_postfit[yul]['totalb'].GetBinContent(hbin))/sigmaBILL)
                    #print ("data: ", h_data[yul]["Data"].GetBinContent(hbin)) 
                    #print (" +-, ", h_data[yul]["Data"].GetBinError(hbin))
                    #print ("MC: ", h_postfit[yul]['totalb'].GetBinContent(hbin))
                    #print (" +-, ", h_postfit[yul]['totalb'].GetBinError(hbin))
                data_pull.SetBinError(hbin,0)

            if (hbin > 2):
                pull_count.Fill(data_pull.GetBinContent(hbin))
                print " pull: ", data_pull.GetBinContent(hbin)

                if (abs(data_pull.GetBinContent(hbin)) >= 2):
                    print " ATTENZIONE "
                    print ">>>>>>>>>>>>>>"
                    print " data yield : ", h_data[yul]["Data"].GetBinContent(hbin)  
                    print " +- ", h_data[yul]["Data"].GetBinError(hbin)
                    print " BKG yield : ", h_postfit[yul]['totalb'].GetBinContent(hbin) 
                    print " +- ", h_postfit[yul]['totalb'].GetBinError(hbin)
                    print "<<<<<<<<<<<<<<"

        #print "MEAN: ", mean
        #print "CHI2: ", math.sqrt(chi2)/data_pull.GetNbinsX()
        #print "Added", sqrt(addedsqrt), "divided: ", sqrt(addedsqrt)/data_pull.GetNbinsX()
        #print "Added2", addedsqrt, "divided: ", addedsqrt/data_pull.GetNbinsX()
        data_pull.SetLineColor(kAzure-4)
        data_pull.SetFillColor(kAzure-4)
        data_pull.SetMarkerColor(kAzure-4)
        data_pull.GetYaxis().SetRangeUser(-2.5, 2.5)
        data_pull.GetYaxis().SetNdivisions(503)
        data_pull.GetXaxis().SetLabelFont(42)
        data_pull.GetYaxis().SetLabelFont(42)
        data_pull.GetXaxis().SetTitleFont(42)
        data_pull.GetYaxis().SetTitleFont(42)
        data_pull.GetXaxis().SetTitleOffset(1.1)
        data_pull.GetYaxis().SetTitleOffset(0.35)
        data_pull.GetXaxis().SetLabelSize(0.1)
        data_pull.GetYaxis().SetLabelSize(0.1)
        data_pull.GetXaxis().SetTitleSize(0.11)
        data_pull.GetYaxis().SetTitleSize(0.1)
        data_pull.GetYaxis().CenterTitle(1)
        data_pull.GetYaxis().SetTitle("#frac{(Data-Pred.)}{#sigma}")
        data_pull.GetXaxis().SetTitle(vartitle)

        #pull_count.SaveAs(postfolder + "/pull_"+region+"_"+yul+"_"+variable+".root")
        #data_pull.SaveAs(postfolder + "/test_"+region+"_"+yul+"_"+variable+".root")
        
        data_pull_sig = h_data[yul]["Data"].Clone("pull_sig")
        data_pull_sig.Sumw2()

        for hbin in range(0,data_pull_sig.GetNbinsX()+1):
            if (h_postfit[yul]['totalb'].GetBinContent(hbin)>0):
                #print "bin",hbin,"data pull diff", data_pull_sig.GetBinContent(hbin), "sys", h_postfit[yul]['totalb'].GetBinError(hbin)
                data_pull_sig.SetBinContent(hbin, data_pull_sig.GetBinContent(hbin)/h_postfit[yul]['totalb'].GetBinError(hbin))
                data_pull_sig.SetBinError(hbin, 0)

        data_pull_sig.SetLineColor(2)
        data_pull_sig.SetFillColor(2)
        data_pull_sig.SetFillStyle(3004)
        data_pull_sig.SetMarkerColor(2)
        legend4 = TLegend(0.20,0.21,0.60,0.23,"","brNDC")
        legend4.AddEntry(data_pull    , "Background only", "f")
        legend4.SetNColumns(2)
        legend4.SetShadowColor(0)
        legend4.SetFillColor(0)
        legend4.SetLineColor(0)

        if opt.lastbins:
            data_pull.GetXaxis().SetRangeUser(firstbin, lastbin)
        data_pull.Draw("hist same")
        
        #latex_chi = TLatex()
        #latex_chi.SetNDC()
        #latex_chi.SetTextSize(0.025)
        ##latex_chi.DrawLatex(0.16,0.20,"#Chi^{2} = "+str(round(addedsqrt/data_pull.GetNbinsX(),2)) + "      Mean = "+ str(round(mean,2)))
        ##latex_chi.DrawLatex(0.16,0.20,"#Chi^{2} = "+str(round(addedsqrt/data_pull.GetNbinsX(),2)) )
        ##latex_chi.DrawLatex(0.16,0.19,"Mean = "+str(round(mean,2)))
        ##latex_chi.Draw("same")
        #pad2.RedrawAxis("G sameaxis")
        #gPad.RedrawAxis()
        
        outsave = postfolder+"/try_"+variable+"_"+region+"_" + yul
        if not opt.linscale:
            outsave += "_logscale"
        else:
            outsave += "_linscale"
        if toScale:
            outsave += "_scaled"
        if opt.lastbins:
            outsave += "_lastbins"
        ### save plots and close
        if "RunII" in yul:
            c.SaveAs(outsave + ".pdf")
            c.SaveAs(outsave + ".png")

        #### memory management
        del pull_count
        del h_all_prefit
        del h_all_postfit
        c.Close()
        del c
        
    f_mlfit.Close()


plotvars = opt.postvars.split(",")

for var in plotvars:
    print "\n\nProcessing postfit for " + var + "..."
    infolder = infile + "/" + var + "/" + modd + "/"
    for chh in channels:
        ch = chh.split("_")[0]
        print "\nProcessing postfit for " + ch + "..."
        PreFitPostFit_v2(ch, "ltau", var, indir, years, infolder)
        #SoverBPlots(ch, "ltau", var, indir, years, infolder)
