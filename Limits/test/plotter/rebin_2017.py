from ROOT import *
from collections import defaultdict
from array import array
from tdrStyle import *
import math
import os
import sys
import copy



_fileIN = ROOT.TFile.Open(str(sys.argv[1])+".root", "READ")
region = str(sys.argv[2])

dir = "postfit/" 
dirPref = "prefit/"

if region == "SR": 
    dir2016 = region+"_Y2016combined_signal_region_postfit/"
    dir2016Pref = region+"_Y2016combined_signal_region_prefit/"
    dir2017 = region+"_Y2017combined_signal_region_postfit/"
    dir2017Pref = region+"_Y2017combined_signal_region_prefit/"
    dir2018 = region+"_Y2018combined_signal_region_postfit/"
    dir2018Pref = region+"_Y2018combined_signal_region_prefit/"
elif region == "DYcr":
    dir2016 = region+"_Y2016_DYcr_postfit/"
    dir2016Pref = region+"_Y2016_DYcr_prefit/"
    dir2017 = region+"_Y2017_DYcr_postfit/"
    dir2017Pref = region+"_Y2017_DYcr_prefit/"
    dir2018 = region+"_Y2018_DYcr_postfit/"
    dir2018Pref = region+"_Y2018_DYcr_prefit/"
elif region == "TOPcr":
    dir2016 = region+"_Y2016_TOPcr_postfit/"
    dir2016Pref = region+"_Y2016_TOPcr_prefit/"
    dir2017 = region+"_Y2017_TOPcr_postfit/"
    dir2017Pref = region+"_Y2017_TOPcr_prefit/"
    dir2018 = region+"_Y2018_TOPcr_postfit/"
    dir2018Pref = region+"_Y2018_TOPcr_prefit/"

print(dir2016)
print(dir2017)
print(dir2018)

###########################
#######     2016 prefit 
#print(dir2016Pref+"TTtW")
#print(dir2016Pref+"DY")
#print(dir2016Pref+"Other")

h_top_pre_16 = ROOT.TH1F(_fileIN.Get(dir2016Pref+"TTtW"))
h_dy_pre_16 = ROOT.TH1F(_fileIN.Get(dir2016Pref+"DY"))
h_other_pre_16 = ROOT.TH1F(_fileIN.Get(dir2016Pref+"Other"))

h_TotalSig_pre_16 = ROOT.TH1F(_fileIN.Get(dir2016Pref+"TotalSig"))

h_TotalBkg_pre_16 = ROOT.TH1F(_fileIN.Get(dir2016Pref+"TotalBkg"))
h_data_obs_16 = ROOT.TH1F(_fileIN.Get(dir2016Pref+"data_obs"))
#######     2016 postfit 
h_TotalBkg_16 = ROOT.TH1F(_fileIN.Get(dir2016+"TotalBkg"))
h_TotalProcs_16 = ROOT.TH1F(_fileIN.Get(dir2016+"TotalProcs"))

h_top_16 = ROOT.TH1F(_fileIN.Get(dir2016+"TTtW"))
h_dy_16 = ROOT.TH1F(_fileIN.Get(dir2016+"DY"))
h_other_16 = ROOT.TH1F(_fileIN.Get(dir2016+"Other"))
############################
#######     2017 prefit 
#print(dir2017Pref+"TTtW")
#print(dir2017Pref+"DY")
#print(dir2017Pref+"Other")

h_top_pre_17 = ROOT.TH1F(_fileIN.Get(dir2017Pref+"TTtW"))
if region != "TOPcr":
    h_dy_pre_17 = ROOT.TH1F(_fileIN.Get(dir2017Pref+"DY"))
else:
    h_dy_pre_17 = ROOT.TH1F(_fileIN.Get(dir2016Pref+"DY"))
h_other_pre_17 = ROOT.TH1F(_fileIN.Get(dir2017Pref+"Other"))

h_TotalSig_pre_17 = ROOT.TH1F(_fileIN.Get(dir2017Pref+"TotalSig"))

h_TotalBkg_pre_17 = ROOT.TH1F(_fileIN.Get(dir2017Pref+"TotalBkg"))
h_data_obs_17 = ROOT.TH1F(_fileIN.Get(dir2017Pref+"data_obs"))
#######     2017 postfit 
h_TotalBkg_17 = ROOT.TH1F(_fileIN.Get(dir2017+"TotalBkg"))
h_TotalProcs_17 = ROOT.TH1F(_fileIN.Get(dir2017+"TotalProcs"))

h_top_17 = ROOT.TH1F(_fileIN.Get(dir2017+"TTtW"))
if region != "TOPcr":
    h_dy_17 = ROOT.TH1F(_fileIN.Get(dir2017+"DY"))
else:
    h_dy_17 = ROOT.TH1F(_fileIN.Get(dir2016+"DY"))
h_other_17 = ROOT.TH1F(_fileIN.Get(dir2017+"Other"))
############################
#######     2018 prefit 
h_top_pre_18 = ROOT.TH1F(_fileIN.Get(dir2018Pref+"TTtW"))
h_dy_pre_18 = ROOT.TH1F(_fileIN.Get(dir2018Pref+"DY"))
h_other_pre_18 = ROOT.TH1F(_fileIN.Get(dir2018Pref+"Other"))

h_TotalSig_pre_18 = ROOT.TH1F(_fileIN.Get(dir2018Pref+"TotalSig"))

h_TotalBkg_pre_18 = ROOT.TH1F(_fileIN.Get(dir2018Pref+"TotalBkg"))
h_data_obs_18 = ROOT.TH1F(_fileIN.Get(dir2018Pref+"data_obs"))
#######     2018 postfit 
h_TotalBkg_18 = ROOT.TH1F(_fileIN.Get(dir2018+"TotalBkg"))
h_TotalProcs_18 = ROOT.TH1F(_fileIN.Get(dir2018+"TotalProcs"))

h_top_18 = ROOT.TH1F(_fileIN.Get(dir2018+"TTtW"))
h_dy_18 = ROOT.TH1F(_fileIN.Get(dir2018+"DY"))
h_other_18 = ROOT.TH1F(_fileIN.Get(dir2018+"Other"))


#### filling the new file with its folder structure:
_fout = ROOT.TFile.Open(str(sys.argv[1])+"_PLOT_"+region+"_2017.root", "RECREATE")
_fout.mkdir(region+"_prefit")
_fout.mkdir(region+"_postfit")


bin = array("d", [0.,0.2,0.4,0.6,0.8,1.,1.4,2.,3.5,10.])
print(bin)
nbin = len(bin) - 1 

############################### 
## fill the PREFIT folder ####
##############################
_fout.cd(region+"_prefit")

h_pre_top = TH1F("TTtW","TTtW",nbin,bin)
h_pre_dy = TH1F("DY","DY",nbin,bin)
h_pre_other = TH1F("Other","Other",nbin,bin)

h_pre_bkg = TH1F("TotalBkg","TotalBkg",nbin,bin)
h_data_obs = TH1F("data_obs","data_obs",nbin,bin)


for i in range(1,10):
    h_pre_top.SetBinContent(i,h_top_pre_17.GetBinContent(i))  
    h_pre_top.SetBinError(i,h_top_pre_17.GetBinError(i))
    ###
    h_pre_dy.SetBinContent(i,h_dy_pre_17.GetBinContent(i))  
    h_pre_dy.SetBinError(i,h_dy_pre_17.GetBinError(i))
    ###
    h_pre_other.SetBinContent(i,h_other_pre_17.GetBinContent(i))  
    h_pre_other.SetBinError(i,h_other_pre_17.GetBinError(i))
    ###
    h_pre_bkg.SetBinContent(i,h_TotalBkg_pre_17.GetBinContent(i))  
    h_pre_bkg.SetBinError(i,h_TotalBkg_pre_17.GetBinError(i))
    ###
    h_data_obs.SetBinContent(i,h_data_obs_17.GetBinContent(i))  
    h_data_obs.SetBinError(i,h_data_obs_17.GetBinError(i))

    #print("summ ", h_pre_top.GetBinContent(i)+h_pre_dy.GetBinContent(i)+h_pre_other.GetBinContent(i) )
    #print("total pre ", h_pre_bkg.GetBinContent(i))
    #print("======")

###############################
## fill the POSTFIT folder ####
##############################
_fout.cd(region+"_postfit")

h_top = TH1F("TTtW","TTtW",nbin,bin)
h_dy = TH1F("DY","DY",nbin,bin)
h_other = TH1F("Other","Other",nbin,bin)

h_bkg = TH1F("TotalBkg","TotalBkg",nbin,bin)
h_procs = TH1F("TotalProcs","TotalProcs",nbin,bin)
h_pre_sig = TH1F("TotalSig","TotalSig",nbin,bin)



for i in range(1,10):
    h_top.SetBinContent(i,h_top_17.GetBinContent(i))  
    h_top.SetBinError(i,h_top_17.GetBinError(i))
    ###
    h_dy.SetBinContent(i,h_dy_17.GetBinContent(i))  
    h_dy.SetBinError(i,h_dy_17.GetBinError(i))
    ###
    h_other.SetBinContent(i,h_other_17.GetBinContent(i))  
    h_other.SetBinError(i,h_other_17.GetBinError(i))
    ###
    h_bkg.SetBinContent(i,h_TotalBkg_17.GetBinContent(i))  
    h_bkg.SetBinError(i,h_TotalBkg_17.GetBinError(i))
    #print("error: ", h_TotalBkg_17.GetBinError(i) )
    ###
    h_procs.SetBinContent(i,h_TotalProcs_17.GetBinContent(i))  
    h_procs.SetBinError(i,h_TotalProcs_17.GetBinError(i))

    ### N.B this is actually a pre-fit histo, but it is insterted here because we would like to use pre-fit signal in plots,
    ### , and here is where the plotter reads them.
    h_pre_sig.SetBinContent(i,h_TotalSig_pre_17.GetBinContent(i))  
    h_pre_sig.SetBinError(i,h_TotalSig_pre_17.GetBinError(i))

    #print("summ ", h_top.GetBinContent(i)+h_dy.GetBinContent(i)+h_other.GetBinContent(i) )
    #print("total post ", h_bkg.GetBinContent(i))
    #print("======")





_fileIN.Close()
_fout.Write()
_fout.Close()
