import collections

#*********************************
#                                *
#       List of channels         *
#                                *
#*********************************
### List of histos to include in the root files
histos = { #"SR":"h_jets_best_Wprime_m_selection_AND_best_topjet_isbtag_AND_best_Wpjet_isbtag_AND_best_top_m_G_120_AND_best_top_m_L_220_AND_deltaR_bestWAK4_closestAK8_L_0p4_AND_WprAK8_mSD_L_60", "CRTT":"h_jets_best_Wprime_m_selection_AND_best_topjet_isbtag_AND_best_Wpjet_isbtag_EQ_0_AND_best_top_m_G_120_AND_best_top_m_L_220_AND_deltaR_bestWAK4_closestAK8_L_0p4_AND_WprAK8_mSD_L_60", "CRWJ":"h_jets_best_Wprime_m_selection_AND_best_topjet_isbtag_EQ_0_AND_best_Wpjet_isbtag_AND_best_top_m_G_120_AND_best_top_m_L_220_AND_deltaR_bestWAK4_closestAK8_L_0p4_AND_WprAK8_mSD_L_60"
    "CR0B":"h_jets_best_Wprime_m_selection_AND_best_topjet_isbtag_EQ_0_AND_best_Wpjet_isbtag_EQ_0_AND_nbjet_pt100_EQ_0_AND_best_top_m_G_120_AND_best_top_m_L_220_AND_deltaR_bestWAK4_closestAK8_L_0p4_AND_WprAK8_mSD_L_60"
}
### List of regions for which creating the datacards
channels = ["SR_muon", "CRTT_muon", "CRWJ_muon", "SR_electron", "CRTT_electron", "CRWJ_electron"]
leptons = ['muon', 'electron']
channels = ["CR0B_muon", "CR0B_electron"]
leptons = ['muon', 'electron']
#channels = ["CR0B_muon"]
#leptons = ['muon']
#channels = ["CR0B_electron"]
#leptons = ['electron']

channels_labels = {"SR":"Signal region", "CRTT":"\ttbar Control region", "CRWJ":"wjets Control region"}
#channels_labels = {"CR0B":"0 b-jet control region"}

class rateParam(object):
    pass

rateParams = {}

DD_rate_2016 = rateParam()
DD_rate_2016.chs = channels
DD_rate_2016.bkg = "DDFitWJetsTT_MttST"
rateParams["DD_rate_2016"] = DD_rate_2016

DD_mu_rate_2017 = rateParam()
DD_mu_rate_2017.chs = channels
DD_mu_rate_2017.bkg = "DDFitWJetsTT_MttST"
rateParams["DD_mu_rate_2017"] = DD_mu_rate_2017

DD_mu_rate_2018 = rateParam()
DD_mu_rate_2018.chs = channels
DD_mu_rate_2018.bkg = "DDFitWJetsTT_MttST"
rateParams["DD_mu_rate_2018"] = DD_mu_rate_2018

DD_ele_rate_2017 = rateParam()
DD_ele_rate_2017.chs = channels
DD_ele_rate_2017.bkg = "DDFitWJetsTT_MttST"
rateParams["DD_ele_rate_2017"] = DD_ele_rate_2017

DD_ele_rate_2018 = rateParam()
DD_ele_rate_2018.chs = channels
DD_ele_rate_2018.bkg = "DDFitWJetsTT_MttST"
rateParams["DD_ele_rate_2018"] = DD_ele_rate_2018

#TT_rate = rateParam()
#TT_rate.chs = ["SR_muon", "CRTT_muon", "CRWJ_muon", "SR_electron", "CRTT_electron", "CRWJ_electron"]
#TT_rate.bkg = "TT_Mtt"
#rateParams["TT_rate"] = TT_rate

#WJ_rate = rateParam()
#WJ_rate.chs = ["SR_muon", "CRTT_muon", "CRWJ_muon", "SR_electron", "CRTT_electron", "CRWJ_electron"]
#WJ_rate.bkg = "WJets"
#rateParams["WJ_rate"] = WJ_rate

#*********************************
#                                *
#       List of backgrounds      *
#                                *
#*********************************
#processes = ["ST", "QCD", "TT_Mtt", "WJets"]
#processes = ["ST", "QCD", "DDWJetsTT_Mtt"]
processes = ["QCD", "DDFitWJetsTT_MttST"]
bkgs = []

#*********************************
#                                *
#       List of systematics      *
#                                *
#*********************************
syst = collections.OrderedDict()
syst["lumi_2016"] = ["lnN", "all", 1.025]
syst["lumi_2017"] = ["lnN", "all", 1.023]
syst["lumi_2018"] = ["lnN", "all", 1.025]
syst["qcd_rate"] = ["lnN", "QCD", 1.25]
#syst["lumi_2018"] = ["lnN", "all", 1.023]
#syst["trigger"] = ["lnN", "all", 1.02]
#syst["trigSF"] = ["shape", ["sig"]]
#syst["trigSF"] = ["lnN", ["sig",sigTTW, sigZ, "QCD", "SingleTop"]]
#syst["jes"] = ["shape", ("QCD", "TT_Mtt", "WJets", "sig")]

#syst["autoMCstat"] = ["shape", ("QCD", "ST", "TT_Mtt", "WJets", "sig")]
#syst["PF"] = ["shape", ("QCD", "ST", "TT_Mtt", "WJets", "sig")]
#syst["pu"] = ["shape", ("QCD", "ST", "TT_Mtt", "WJets", "sig")]
#syst["jes"] = ["shape", ("QCD", "ST", "TT_Mtt", "WJets", "sig")]
#syst["jer"] = ["shape", ("QCD", "ST", "TT_Mtt", "WJets", "sig")]
'''
#syst["autoMCstat"] = ["shape", ("QCD", "ST", "DDWJetsTT_Mtt", "sig")]
syst["PF"] = ["shape", ("QCD", "ST", "DDWJetsTT_Mtt", "sig")]
syst["pu"] = ["shape", ("QCD", "ST", "DDWJetsTT_Mtt", "sig")]
#syst["lep"] = ["shape", ("QCD", "ST", "DDWJetsTT_Mtt", "sig")]
#syst["trig"] = ["shape", ("QCD", "ST", "DDWJetsTT_Mtt", "sig")]
syst["jes"] = ["shape", ("QCD", "ST", "DDWJetsTT_Mtt", "sig")]
syst["jer"] = ["shape", ("QCD", "ST", "DDWJetsTT_Mtt", "sig")]
syst["btag"] = ["shape", ("QCD", "ST", "DDWJetsTT_Mtt", "sig")]
syst["mistag"] = ["shape", ("QCD", "ST", "DDWJetsTT_Mtt", "sig")]
syst["TT_Mtt"] = ["shape", ("QCD", "ST", "DDWJetsTT_Mtt", "sig")]
syst["WJets"] = ["shape", ("QCD", "ST", "DDWJetsTT_Mtt", "sig")]
'''
#syst["autoMCstat"] = ["shape", ("QCD", "ST", "DDWJetsTT_Mtt", "sig")]
syst["PF"] = ["shape", ("QCD",  "sig")]
syst["pu"] = ["shape", ("QCD",  "sig")]
syst["lep"] = ["shape", ("QCD",  "sig")]
syst["trig"] = ["shape", ("QCD",  "sig")]
syst["jes"] = ["shape", ("QCD",  "sig")]
syst["jer"] = ["shape", ("QCD",  "sig")]
syst["btag"] = ["shape", ("QCD",  "sig")]
syst["mistag"] = ["shape", ("QCD",  "sig")]
syst["pdf_total"] = ["shape", ("QCD",  "sig")]

syst["TT_Mtt"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["WJets"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["ST"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TF_mu_2016"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DD_mu_2016"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["Alt_mu_2016"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TF_mu_2017"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DD_mu_2017"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["Alt_mu_2017"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TF_mu_2018"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DD_mu_2018"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["Alt_mu_2018"] = ["shape", ("DDFitWJetsTT_MttST")]

syst["TF_ele_2016"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DD_ele_2016"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["Alt_ele_2016"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TF_ele_2017"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DD_ele_2017"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["Alt_ele_2017"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["TF_ele_2018"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["DD_ele_2018"] = ["shape", ("DDFitWJetsTT_MttST")]
syst["Alt_ele_2018"] = ["shape", ("DDFitWJetsTT_MttST")]
#syst["AltBis_2018"] = ["shape", ("DDFitWJetsTT_MttST")]

years = ["2018"]
#years = ["2016","2017","2018"]
'''
splityearjes=False
#splityearjes=True
if(splityearjes):
    for y in ys:
        #if(y=="2016"):syst["jer"+y] = ["shape", [ sigTTW]] #No QCD : low stat
        if(y=="2016"):syst["jes"+y] = ["shape", ["sig", sigZ, sigTTW, "SingleTop" ]] #No QCD : low stat
        if(y!="2016"):syst["jer"+y] = ["shape", ["sig", sigZ, sigTTW, "SingleTop"]] #No QCD : low stat
if(not splityearjes):
    syst["jes"] = ["shape", ["sig", sigTTW, sigZ, "SingleTop"]] #No QCD : low stat
    syst["jer"] = ["shape", ["sig", sigTTW, sigZ, "SingleTop"]] #No QCD : low stat
'''

#*********************************
#                                *
#         List of signals        *
#                                *
#*********************************

#*********************************************************#
#                                                         #
#                  Right-Handed samples                   #
#                                                         #
#*********************************************************#
RHvec1 = ("2000", "20", "RH")
RHvec2 = ("2200", "22", "RH")
RHvec3 = ("2400", "24", "RH")
RHvec4 = ("2600", "26", "RH")
RHvec5 = ("2800", "28", "RH")
RHvec6 = ("3000", "30", "RH")
RHvec7 = ("3200", "32", "RH")
RHvec8 = ("3400", "34", "RH")
RHvec9 = ("3600", "36", "RH")
RHvec10 = ("3800", "38", "RH")
RHvec11 = ("4000", "40", "RH")
RHvec12 = ("4200", "42", "RH")
RHvec13 = ("4400", "44", "RH")
RHvec14 = ("4600", "46", "RH")
RHvec15 = ("4800", "48", "RH")
RHvec16 = ("5000", "50", "RH")
RHvec17 = ("5200", "52", "RH")
RHvec18 = ("5400", "54", "RH")
RHvec19 = ("5600", "56", "RH")
RHvec20 = ("5800", "58", "RH")
RHvec21 = ("6000", "60", "RH")
sigpoints = [RHvec1, RHvec6, RHvec11]

RHvec1wp10 = ("2400", "240", "RH")
RHvec2wp10 = ("2800", "280", "RH")
RHvec3wp10 = ("3200", "320", "RH")
RHvec4wp10 = ("3600", "360", "RH")
RHvec5wp10 = ("4000", "400", "RH")
RHvec6wp10 = ("4400", "440", "RH")
RHvec7wp10 = ("4800", "480", "RH")
RHvec8wp10 = ("5200", "520", "RH")
RHvec9wp10 = ("5600", "560", "RH")
RHvec10wp10 = ("6000", "600", "RH")
sigspointswp10 = [RHvec1wp10, RHvec2wp10, RHvec3wp10, RHvec4wp10, RHvec5wp10, RHvec6wp10, RHvec7wp10, RHvec8wp10, RHvec9wp10, RHvec10wp10]

RHvec1wp20 = ("2400", "480", "RH")
RHvec2wp20 = ("2800", "560", "RH")
RHvec3wp20 = ("3200", "640", "RH")
RHvec4wp20 = ("3600", "720", "RH")
RHvec5wp20 = ("4000", "800", "RH")
RHvec6wp20 = ("4400", "880", "RH")
RHvec7wp20 = ("4800", "960", "RH")
RHvec8wp20 = ("5200", "1040", "RH")
RHvec9wp20 = ("5600", "1120", "RH")
RHvec10wp20 = ("6000", "1200", "RH")

sigspointswp20 = [RHvec1wp20, RHvec2wp20, RHvec3wp20, RHvec4wp20, RHvec5wp20, RHvec6wp20, RHvec7wp20, RHvec8wp20, RHvec9wp20, RHvec10wp20]

RHvec1wp30 = ("2400", "720", "RH")
RHvec2wp30 = ("2800", "840", "RH")
RHvec3wp30 = ("3200", "960", "RH")
RHvec4wp30 = ("3600", "1080", "RH")
RHvec5wp30 = ("4000", "1200", "RH")
RHvec6wp30 = ("4400", "1320", "RH")
RHvec7wp30 = ("4800", "1440", "RH")
RHvec8wp30 = ("5200", "1560", "RH")
RHvec9wp30 = ("5600", "1680", "RH")
RHvec10wp30 = ("6000", "1800", "RH")

sigspointswp30 = [RHvec1wp30, RHvec2wp30, RHvec3wp30, RHvec4wp30, RHvec5wp30, RHvec6wp30, RHvec7wp30, RHvec8wp30, RHvec9wp30, RHvec10wp30]

#*********************************************************#
#                                                         #
#                   Left-Handed samples                   #
#                                                         #
#*********************************************************#
LHvec1 = ("2000", "20", "LH")
LHvec2 = ("2200", "22", "LH")
LHvec3 = ("2400", "24", "LH")
LHvec4 = ("2600", "26", "LH")
LHvec5 = ("2800", "28", "LH")
LHvec6 = ("3000", "30", "LH")
LHvec7 = ("3200", "32", "LH")
LHvec8 = ("3400", "34", "LH")
LHvec9 = ("3600", "36", "LH")
LHvec10 = ("3800", "38", "LH")
LHvec11 = ("4000", "40", "LH")
LHvec12 = ("4200", "42", "LH")
LHvec13 = ("4400", "44", "LH")
LHvec14 = ("4600", "46", "LH")
LHvec15 = ("4800", "48", "LH")
LHvec16 = ("5000", "50", "LH")
LHvec17 = ("5200", "52", "LH")
LHvec18 = ("5400", "54", "LH")
LHvec19 = ("5600", "56", "LH")
LHvec20 = ("5800", "58", "LH")
LHvec21 = ("6000", "60", "LH")
sigpoints = [LHvec1, LHvec6, LHvec11]

LHvec1wp10 = ("2400", "240", "LH")
LHvec2wp10 = ("2800", "280", "LH")
LHvec3wp10 = ("3200", "320", "LH")
LHvec4wp10 = ("3600", "360", "LH")
LHvec5wp10 = ("4000", "400", "LH")
LHvec6wp10 = ("4400", "440", "LH")
LHvec7wp10 = ("4800", "480", "LH")
LHvec8wp10 = ("5200", "520", "LH")
LHvec9wp10 = ("5600", "560", "LH")
LHvec10wp10 = ("6000", "600", "LH")
sigspointswp10 = [LHvec1wp10, LHvec2wp10, LHvec3wp10, LHvec4wp10, LHvec5wp10, LHvec6wp10, LHvec7wp10, LHvec8wp10, LHvec9wp10, LHvec10wp10]

LHvec1wp20 = ("2400", "480", "LH")
LHvec2wp20 = ("2800", "560", "LH")
LHvec3wp20 = ("3200", "640", "LH")
LHvec4wp20 = ("3600", "720", "LH")
LHvec5wp20 = ("4000", "800", "LH")
LHvec6wp20 = ("4400", "880", "LH")
LHvec7wp20 = ("4800", "960", "LH")
LHvec8wp20 = ("5200", "1040", "LH")
LHvec9wp20 = ("5600", "1120", "LH")
LHvec10wp20 = ("6000", "1200", "LH")

sigspointswp20 = [LHvec1wp20, LHvec2wp20, LHvec3wp20, LHvec4wp20, LHvec5wp20, LHvec6wp20, LHvec7wp20, LHvec8wp20, LHvec9wp20, LHvec10wp20]

LHvec1wp30 = ("2400", "720", "LH")
LHvec2wp30 = ("2800", "840", "LH")
LHvec3wp30 = ("3200", "960", "LH")
LHvec4wp30 = ("3600", "1080", "LH")
LHvec5wp30 = ("4000", "1200", "LH")
LHvec6wp30 = ("4400", "1320", "LH")
LHvec7wp30 = ("4800", "1440", "LH")
LHvec8wp30 = ("5200", "1560", "LH")
LHvec9wp30 = ("5600", "1680", "LH")
LHvec10wp30 = ("6000", "1800", "LH")

sigspointswp30 = [LHvec1wp30, LHvec2wp30, LHvec3wp30, LHvec4wp30, LHvec5wp30, LHvec6wp30, LHvec7wp30, LHvec8wp30, LHvec9wp30, LHvec10wp30]


sigpoints = [RHvec1, RHvec6, RHvec11, RHvec16, RHvec21]

#sigpoints.extend( sigspointswp10)
#sigpoints.extend( sigspointswp20)
#sigpoints.extend( sigspointswp30)
