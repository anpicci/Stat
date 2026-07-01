import ROOT as r
from array import array
from tdrStyle import *
setTDRStyle()
import os
from math import sqrt
import numpy as np
from collections import defaultdict

def plot_ratio(process,category, model_file, outdir, lumi, year):

    highest = {}
    highest2 = {}

    if 'mono' in category:
        bgtypes = ['']
        tag = ''
    else:
        bgtypes = ['qcd_' ,'ewk_']
        tag = "withphoton_"

    assert(os.path.exists(model_file))
    for bgtype in bgtypes:
        f = r.TFile(model_file,'READ')

        replacements = {
                        "TYPE" : bgtype,
                        "CAT" : category,
                        "TAG" : tag,
                        "PROC" : process,
                        "YEAR" : year
                        }
        print(replacements)
        if (process=='zmm'):
            dirname = "Z_constraints_{TYPE}{TAG}category_{CAT}"
            base    = "{TYPE}zmm_weights_"+category
            label = "R_{Z(#mu#mu)}"
            addsys  = sqrt(0.02**2 + 0.02**2 + 0.02**2)

        if (process=='zee'):
            dirname = "Z_constraints_{TYPE}{TAG}category_{CAT}"
            base    = "{TYPE}zee_weights_"+category
            label   = "R_{Z(ee)}"
            addsys  = sqrt(0.05**2 + 0.02**2 + 0.01**2)

        if (process=='photon'):
            dirname = "Z_constraints_{TYPE}{TAG}category_{CAT}"
            base    = "{TYPE}photon_weights_{CAT}"
            label   = "R_{#gamma}"
            addsys  = 0.01

        if (process=='w_weights'):
            dirname = "Z_constraints_{TYPE}{TAG}category_{CAT}"
            base    = "{TYPE}w_weights_"+category
            label   = "R_{Z/W}"
            addsys  = 0

        if (process=='wen'):
            dirname = "W_constraints_{TYPE}category_"+category
            base    = "{TYPE}wen_weights_"+category
            label   = "R_{W(e#nu)}"
            addsys  = sqrt(0.025**2 + 0.01**2 + 0.01**2)

        if (process=='wmn'):
            dirname = "W_constraints_{TYPE}category_{CAT}"
            base    = "{TYPE}wmn_weights_{CAT}"
            label   = "R_{W(#mu#nu)}"
            addsys  = sqrt(0.01**2 + 0.01**2 + 0.01**2)
        dirname = dirname.format(**replacements)
        base = base.format(**replacements)
        print(dirname+"/"+base)
        ratio = f.Get(dirname+"/"+base)
        up_final = ratio.Clone("ratio")
        up_ewk = ratio.Clone("ratio")
        down_final = ratio.Clone("ratio")

        for b in range(ratio.GetNbinsX()+1):
            up_final.SetBinContent(b,0.0)
            up_ewk.SetBinContent(b,0.0)
            down_final.SetBinContent(b,0.0)
            highest[b] = 0
            highest2[b] = 0

        f.cd(dirname)
        # Unertainties are stored in to dictionaries
        # unc_up/dn[type][bin number] = value
        unc_dict = defaultdict(lambda:defaultdict(int))
        for b in range(ratio.GetNbinsX()+1):
            for key in r.gDirectory.GetListOfKeys():
                name = key.GetName()

                # Skip unrelated stuff
                if not (key.GetClassName(),"TH1"):
                    continue
                if not (process in name):
                    continue
                if not ('Up' in name):
                    continue
                up = f.Get(dirname+"/"+name)
                diff = up.GetBinContent(b) - ratio.GetBinContent(b)

                if (any([x in name for x in ['stat_error']])):
                    unc_dict['stat'][b] = np.hypot(unc_dict['stat'][b], diff)
                elif (any([x in name for x in ['trig','prefiring','veto','eff','jes','jer','photon_scale']])):
                    unc_dict['exp'][b] = np.hypot(unc_dict['exp'][b], diff)
                elif (any([x in name for x in ['cross', 'pdf', 'qcd']])):
                    unc_dict['qcd'][b] = np.hypot(unc_dict['qcd'][b], diff)
                elif (any([x in name for x in ['ewk', 'sudakov', 'nnlo']])):
                    unc_dict['ewk'][b] = np.hypot(unc_dict['ewk'][b], diff)
                else:
                    raise IOError("Unrecognized variation: " + name)

        gStyle.SetOptStat(0)

        c = r.TCanvas("c","c",600,600)
        c.SetTopMargin(0.06)
        c.cd()
        c.SetRightMargin(0.04)
        c.SetTopMargin(0.07)
        c.SetLeftMargin(0.12)

        # Construct the bands
        band_ewkqcdunc    = ratio.Clone("ratio")
        band_ewkunc   = ratio.Clone("ratio2")
        band_fullunc   = ratio.Clone("ratio3")
        for b in range(ratio.GetNbinsX()+1):
            band_ewkunc.SetBinError(b, sqrt(
                                            unc_dict['ewk'][b]**2 + 
                                            unc_dict['stat'][b]**2
                                            ))
            band_ewkqcdunc.SetBinError(b, sqrt(
                                               unc_dict['ewk'][b]**2 + 
                                               unc_dict['qcd'][b]**2 + 
                                               unc_dict['stat'][b]**2
                                               ))
            band_fullunc.SetBinError(b, sqrt(
                                             unc_dict['ewk'][b]**2 + 
                                             unc_dict['qcd'][b]**2 + 
                                             unc_dict['stat'][b]**2 +
                                             unc_dict['exp'][b]**2 + 
                                             (addsys*band_ewkqcdunc.GetBinContent(b))**2
                                             ))
        
        band_ewkunc.SetFillColor(33);
        band_fullunc.SetFillColor(r.kBlue+1);

        if process == "photon" or process == "w_weights":
            band_ewkqcdunc.SetFillColor(r.kAzure+1);
        else:
            band_ewkqcdunc.SetFillColor(33);

        band_fullunc.GetYaxis().SetTitle(label)
        band_fullunc.GetYaxis().CenterTitle()
        band_fullunc.GetYaxis().SetTitleSize(0.4*c.GetLeftMargin())
        band_fullunc.GetXaxis().SetTitle("U [GeV]"  if "mono" in category else  "M_{jj} [GeV]")
        band_fullunc.GetXaxis().SetTitleSize(0.4*c.GetBottomMargin())
        band_fullunc.SetMaximum(2.0*ratio.GetMaximum())
        band_fullunc.SetMinimum(0.5*ratio.GetMinimum())
        band_fullunc.GetYaxis().SetTitleOffset(1.15)

        ratio.SetMarkerStyle(20)
        ratio.SetLineColor(1)
        ratio.SetLineWidth(2)

        band_fullunc.Draw("e2")
        band_ewkqcdunc.Draw("e2same")
        band_ewkunc.Draw("e2same")
        ratio.Draw("same")

        legend = r.TLegend(.45,.75,.82,.92)
        legend.AddEntry(ratio,"Transfer Factor (Stat Uncert)" , "p")
        if process == "photon" or process == "w_weights":
            legend.AddEntry(band_ewkunc ,"Stat + Syst. (EWK)" , "f")
            legend.AddEntry(band_ewkqcdunc  ,"Stat + Syst. (EWK+QCD)" , "f")
            legend.AddEntry(band_fullunc ,"Stat + Syst. (EWK+QCD+Exp)" , "f")
        else:
            band_fullunc.SetFillColor(33)
            legend.AddEntry(band_fullunc ,"Stat + Syst. (Exp)" , "f")


        legend.SetShadowColor(0);
        legend.SetFillColor(0);
        legend.SetLineColor(0);

        legend.Draw("same")

        latex2 = r.TLatex()
        latex2.SetNDC()
        latex2.SetTextSize(0.035)
        latex2.SetTextAlign(31) # align right
        latex2.DrawLatex(0.87, 0.95, "{LUMI:.1f} fb^{{-1}} (13 TeV)".format(LUMI=lumi))

        latex3 = r.TLatex()
        latex3.SetNDC()
        latex3.SetTextSize(0.75*c.GetTopMargin())
        latex3.SetTextFont(62)
        latex3.SetTextAlign(11) # align right
        latex3.DrawLatex(0.22, 0.85, "CMS");
        latex3.SetTextSize(0.5*c.GetTopMargin())
        latex3.SetTextFont(52)
        latex3.SetTextAlign(11)

        if "monojet" in category:
            latex3.DrawLatex(0.22, 0.8, "Monojet");
        elif "loose" in category:
            latex3.DrawLatex(0.22, 0.8, "Mono-V");
            latex3.DrawLatex(0.22, 0.75, "(low-purity)");
        elif "tight" in category:
            latex3.DrawLatex(0.22, 0.8, "Mono-V");
            latex3.DrawLatex(0.22, 0.75, "(high-purity)");

        r.gPad.RedrawAxis()
        if not os.path.exists(outdir):
            os.makedirs(outdir)

        for extension in ["png","pdf","C"]:
            c.SaveAs(outdir+"/rfactor_{CAT}_{TYPE}{PROC}_{YEAR}.{EXT}".format(EXT=extension,**replacements))
        f.Close()
        c.Close()
