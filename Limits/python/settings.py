import collections

#*********************************
#                                *
#       List of channels         *
#                                *
#*********************************
sr_var = 'BDT_output'
cr_var = 'BDT_output' # 'countings' # 
### List of histos to include in the root files
histos = { "SR":"h_htau_" + sr_var + "_SR",
           #"PR":"h_htau_m_jj_selection_upto_bveto_lepBDTcut",
           "CRWJ":"h_htau_" + cr_var + "_wjets_CR",
           "CRTT":"h_htau_" + cr_var + "_ttbar_CR",
           "CRQCD":"h_htau_" + cr_var + "_QCD_CR",
}
### List of regions for which creating the datacards
channels = ["SR_muon",
            "CRWJ_muon",
            "CRTT_muon",
            "CRQCD_muon",
            "SR_electron",
            "CRWJ_electron",
            "CRTT_electron",
            "CRQCD_electron",
]

leptons = ['muon',
           'electron',
]

channels_labels = {"SR":"Pre-signal region", 
                   "CRWJ":"Fake Leptons Control region",
                   "CRTT":"ttbar Control region",
                   "CRQCD":"QCD Control region",
}

#*********************************
#                                *
#       List of backgrounds      *
#                                *
#*********************************
#processes = ["ST", "QCD", "TT_Mtt", "WJets"]
#processes = ["ST", "QCD", "DDWJetsTT_Mtt"]
bkg = ["Fake",
       "ZZtoLep",
       "OtherWS",
       "WZ",
       "TTTo2L2Nu",
       "TVX",
       "WpWpJJ_QCD",
       "VG",
       "VBS_SSWW_SM",
       "VBS_SSWW_LL_SM",
       "VBS_SSWW_TL_SM",
       "VBS_SSWW_TT_SM",
]

lssamples_1D = ['sm',
               'sm_lin_quad_cW',
               'sm_lin_quad_cHW',
               'quad_cW',
               'quad_cHW',
]

class rateParam(object):
    pass

rateParams = {}

FakeMu_rate_2017 = rateParam()
FakeMu_rate_2017.chs = [#"SR_muon",
                        "CRWJ_muon",
                        "CRTT_muon",
                        "CRQCD_muon",
]
FakeMu_rate_2017.bkg = "Fake"
rateParams["FRest_muon_2017"] = FakeMu_rate_2017


FakeEle_rate_2017 = rateParam()
FakeEle_rate_2017.chs = [#"SR_electron",
                         "CRWJ_electron",
                         "CRTT_electron",
                         "CRQCD_electron",
]
FakeEle_rate_2017.bkg = "Fake"
rateParams["FRest_electron_2017"] = FakeEle_rate_2017

'''
TTDiLep_ele_2017 = rateParam()
TTDiLep_ele_2017.chs = [#"SR_electron",
                        #"CRWJ_electron",
                         "CRTT_electron",
]
TTDiLep_ele_2017.bkg = "TTTo2L2Nu"
rateParams["TTDiLep_electron_2017"] = TTDiLep_ele_2017

TTDiLep_mu_2017 = rateParam()
TTDiLep_mu_2017.chs = [#"SR_muon",
                       #"CRWJ_muon",
                       "CRTT_muon",
]
TTDiLep_mu_2017.bkg = "TTTo2L2Nu"
rateParams["TTDiLep_muon_2017"] = TTDiLep_mu_2017
'''

#*********************************
#                                *
#       List of systematics      *
#                                *
#*********************************
syst = collections.OrderedDict()
syst["lumi_2016"] = ["lnN", "all", 1.025]
syst["lumi_2017"] = ["lnN", "all", 1.023]
syst["lumi_2018"] = ["lnN", "all", 1.025]
syst["FR_sys_muon"] = ["lnN", "Fake", 1.15]
syst["FR_sys_electron"] = ["lnN", "Fake", 1.22]
#syst["lumi_2018"] = ["lnN", "all", 1.023]
#syst["trigger"] = ["lnN", "all", 1.02]
#syst["trigSF"] = ["shape", ["sig"]]
#syst["trigSF"] = ["lnN", ["sig",sigTTW, sigZ, "QCD", "SingleTop"]]
#syst["jes"] = ["shape", ("QCD", "TT_Mtt", "WJets", "sig")]

syst["autoMCstat"] = ["shape", ("VG", "WpWpJJ_QCD", "TVX", "TTTo2L2Nu", "WZ", "OtherWS", "ZZtoLep", "sig")]
#syst["PF"] = ["shape", ("QCD", "ST", "TT_Mtt", "WJets", "sig")]
#syst["pu"] = ["shape", ("QCD", "ST", "TT_Mtt", "WJets", "sig")]
#syst["jes"] = ["shape", ("QCD", "ST", "TT_Mtt", "WJets", "sig")]
#syst["jer"] = ["shape", ("QCD", "ST", "TT_Mtt", "WJets", "sig")]

'''
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
'''
#syst["AltBis_2018"] = ["shape", ("DDFitWJetsTT_MttST")]

years = ["2017"]
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

VBS_SSWW_SM = ("SM")
VBS_SSWW_SM_LL = ("LL_SM")
VBS_SSWW_SM_TL = ("TL_SM")
VBS_SSWW_SM_TT = ("TT_SM")
VBS_SSWW_BSM_SM = ("BSM_SM")
VBS_SSWW_BSM = ("BSM_INT")
VBS_SSWW_cW_SM = ("cW_SM")
VBS_SSWW_cHW_SM = ("cHW_SM")
VBS_SSWW_cW = ("cW")
VBS_SSWW_cHW = ("cHW")
sigpoints = [
    VBS_SSWW_SM,
    #VBS_SSWW_SM_LL,
    #VBS_SSWW_SM_TL,
    #VBS_SSWW_SM_TT,
    #VBS_SSWW_BSM_SM,
    #VBS_SSWW_BSM,
    #VBS_SSWW_cHW_SM,
    #VBS_SSWW_cW_SM,
    #VBS_SSWW_cHW,
    #VBS_SSWW_cW,
]

