import collections

#*********************************
#                                *
#       List of channels         *
#                                *
#*********************************
#sr_var = 'm_jj'
#sr_var = 'm_o1'
sr_var = 'm_1T'
#sr_var = 'BDT_output_SM_opt'
#sr_var = 'DNN_output_SM_opt'
#sr_var = 'BDT_SM_xgb_UL008_no'
#sr_var = 'BDT_cW_xgb_UL008_no'
#sr_var = 'BDT_cHW_xgb_UL008_no'
#cr_var = 'm_jj'
#cr_var = 'm_o1'
#cr_var = 'm_1T'
#cr_var = 'BDT_output_SM_opt'
#cr_var = 'DNN_output_SM_opt'
#cr_var = 'BDT_SM_xgb_UL008_no'
#cr_var = 'BDT_dim6_xgb_UL008_no'
cr_var = 'countings'
hist_pre = "h_"

#dyjets_sample = "DYJetsToLL"
dyjets_sample = "DYJetsToLL_FxFx"
#triboson_sample = "Other"
triboson_sample = "Triboson"

### List of histos to include in the root files
histos = { "SR":hist_pre + sr_var + "_SR",
           #"PR":"h_ltau_m_jj_selection_upto_bveto_lepBDTcut",
           "CRTT":hist_pre + cr_var + "_ttbar_CR",
           ## ReReco ##
           #"CRWS":hist_pre + cr_var + "_wrongsing_CR",
           ## UltraLegacy ##
           "CRWS":hist_pre + cr_var + "_OS_CR_bvetoL",
           "CRF":hist_pre + cr_var + "_fakes_CR",
           #"CRQCD":hist_pre + cr_var + "_QCD_CR",
           #"CRWJ":hist_pre + cr_var + "_wjets_CR",
           #"CRDY":hist_pre + cr_var + "_DY_CR",
}

cuttag = ""#_AND_taggerScore_G_0p9"

if cuttag != "":
    for k, v in histos.items():
        histos[k] = v + cuttag

### List of regions for which creating the datacards
channels = ["SR_muon",
            "CRTT_muon",
            "CRWS_muon",
            #"CRQCD_muon",
            #"CRWJ_muon",
            "CRF_muon",
            #"CRDY_muon",
            "SR_electron",
            "CRTT_electron",
            "CRWS_electron",
            #"CRQCD_electron",
            #"CRWJ_electron",
            "CRF_electron",
            #"CRDY_electron",
]

leptons = [
    #'inclusive',
    'muon',
    'electron',
    #'emu'
]

channels_labels = {"SR":"Pre-signal region", 
                   #"CRWJ":"Fake Leptons Control region",
                   "CRTT":"ttbar Control region",
                   #"CRQCD":"QCD Control region",
}

#*********************************
#                                *
#       List of backgrounds      *
#                                *
#*********************************
#processes = ["ST", "QCD", "TT_Mtt", "WJets"]
#processes = ["ST", "QCD", "DDWJetsTT_Mtt"]

bkg = [
    "Fake",
    "ZZtoLep",
    "WrongSign",
    "WZ",
    "TTTo2L2Nu",
    triboson_sample,
    "TVX",
    dyjets_sample,
    #"WpWpJJ_QCD",
    "VG",
    "VBS_SSWW_SM",
    "VBS_SSWW_LL_SM",
    "VBS_SSWW_TL_SM",
    "VBS_SSWW_TT_SM",
]

lssamples_1D = {
    'cW':{    
        'sm': "VBS_SSWW_SM",
        'sm_lin_quad_cW': "VBS_SSWW_cW_SM",
        'quad_cW': "VBS_SSWW_cW_BSM",
    },
    'cHW':{    
        'sm': "VBS_SSWW_SM",
        'sm_lin_quad_cHW': "VBS_SSWW_cHW_SM",
        'quad_cHW': "VBS_SSWW_cHW_BSM",
    },
    'FS0_25':{    
        'sm': "VBS_SSWW_FS0_0",
        'sm_lin_quad_cS0': "VBS_SSWW_FS0_25_SM",
        'quad_cS0': "VBS_SSWW_FS0_25_BSM",
    },
    'FS0_5':{    
        'sm': "VBS_SSWW_FS0_0",
        'sm_lin_quad_cS0': "VBS_SSWW_FS0_5_SM",
        'quad_cS0': "VBS_SSWW_FS0_5_BSM",
    },
    'FS1_50':{    
        'sm': "VBS_SSWW_FS1_0",
        'sm_lin_quad_cS1': "VBS_SSWW_FS1_50_SM",
        'quad_cS1': "VBS_SSWW_FS1_50_BSM",
    },
    'FS1_10':{    
        'sm': "VBS_SSWW_FS1_0",
        'sm_lin_quad_cS1': "VBS_SSWW_FS1_10_SM",
        'quad_cS1': "VBS_SSWW_FS1_10_BSM",
    },
    'FM0_25':{    
        'sm': "VBS_SSWW_FM0_0",
        'sm_lin_quad_cM0': "VBS_SSWW_FM0_25_SM",
        'quad_cM0': "VBS_SSWW_FM0_25_BSM",
    },
    'FM0_5':{    
        'sm': "VBS_SSWW_FM0_0",
        'sm_lin_quad_cM0': "VBS_SSWW_FM0_5_SM",
        'quad_cM0': "VBS_SSWW_FM0_5_BSM",
    },
    'FM1_25':{    
        'sm': "VBS_SSWW_FM1_0",
        'sm_lin_quad_cM1': "VBS_SSWW_FM1_25_SM",
        'quad_cM1': "VBS_SSWW_FM1_25_BSM",
    },
    'FM1_5':{    
        'sm': "VBS_SSWW_FM1_0",
        'sm_lin_quad_cM1': "VBS_SSWW_FM1_5_SM",
        'quad_cM1': "VBS_SSWW_FM1_5_BSM",
    },
    'FM6_25':{    
        'sm': "VBS_SSWW_FM6_0",
        'sm_lin_quad_cM6': "VBS_SSWW_FM6_25_SM",
        'quad_cM6': "VBS_SSWW_FM6_25_BSM",
    },
    'FM6_5':{    
        'sm': "VBS_SSWW_FM6_0",
        'sm_lin_quad_cM6': "VBS_SSWW_FM6_5_SM",
        'quad_cM6': "VBS_SSWW_FM6_5_BSM",
    },
    'FM7_50':{    
        'sm': "VBS_SSWW_FM7_0",
        'sm_lin_quad_cM7': "VBS_SSWW_FM7_50_SM",
        'quad_cM7': "VBS_SSWW_FM7_50_BSM",
    },
    'FM7_10':{    
        'sm': "VBS_SSWW_FM7_0",
        'sm_lin_quad_cM7': "VBS_SSWW_FM7_10_SM",
        'quad_cM7': "VBS_SSWW_FM7_10_BSM",
    },
    'FT0_2p5':{    
        'sm': "VBS_SSWW_FT0_0",
        'sm_lin_quad_cT0': "VBS_SSWW_FT0_2p5_SM",
        'quad_cT0': "VBS_SSWW_FT0_2p5_BSM",
    },
    'FT0_0p5':{    
        'sm': "VBS_SSWW_FT0_0",
        'sm_lin_quad_cT0': "VBS_SSWW_FT0_0p5_SM",
        'quad_cT0': "VBS_SSWW_FT0_0p5_BSM",
    },
    'FT1_1':{    
        'sm': "VBS_SSWW_FT1_0",
        'sm_lin_quad_cT1': "VBS_SSWW_FT1_1_SM",
        'quad_cT1': "VBS_SSWW_FT1_1_BSM",
    },
    'FT1_0p2':{    
        'sm': "VBS_SSWW_FT1_0",
        'sm_lin_quad_cT1': "VBS_SSWW_FT1_0p2_SM",
        'quad_cT1': "VBS_SSWW_FT1_0p2_BSM",
    },
    'FT2_2p5':{    
        'sm': "VBS_SSWW_FT2_0",
        'sm_lin_quad_cT2': "VBS_SSWW_FT2_2p5_SM",
        'quad_cT2': "VBS_SSWW_FT2_2p5_BSM",
    },
    'FT2_0p5':{    
        'sm': "VBS_SSWW_FT2_0",
        'sm_lin_quad_cT2': "VBS_SSWW_FT2_0p5_SM",
        'quad_cT2': "VBS_SSWW_FT2_0p5_BSM",
    },

}

class rateParam(object):
    pass

rateParams = {}

FakeMu_rate_2016APV = rateParam()
FakeMu_rate_2016APV.chs = [
    "SR_muon",
    #"CRTT_muon",                                                    
    "CRF_muon",
    #"CRDY_muon",
    #"CRWS_muon",
]
FakeMu_rate_2016APV.bkg = "Fake"
rateParams["FRest_muon_2016APV"] = FakeMu_rate_2016APV


FakeEle_rate_2016APV = rateParam()
FakeEle_rate_2016APV.chs = [
    "SR_electron",
    #"CRTT_electron",
    "CRF_electron",
    #"CRDY_electron",
    #"CRWS_electron",
]
FakeEle_rate_2016APV.bkg = "Fake"
rateParams["FRest_electron_2016APV"] = FakeEle_rate_2016APV

'''
WSele_rate_2016APV = rateParam()
WSele_rate_2016APV.chs = [
    "SR_electron",
    "CRTT_electron",
    "CRF_electron",
    #"CRDY_electron",
    "CRWS_electron",
]
WSele_rate_2016APV.bkg = "WrongSign"
rateParams["WSest_electron_2016APV"] = WSele_rate_2016APV

WSmu_rate_2016APV = rateParam()
WSmu_rate_2016APV.chs = [
    "SR_muon",
    "CRTT_muon",
    "CRF_muon",
    #"CRDY_muon",
    "CRWS_muon",
]
WSmu_rate_2016APV.bkg = "WrongSign"
rateParams["WSest_muon_2016APV"] = WSmu_rate_2016APV
'''

TTbarele_rate_2016APV = rateParam()
TTbarele_rate_2016APV.chs = [
    "SR_electron",
    "CRTT_electron",
    #"CRF_electron",
    #"CRDY_electron",
    #"CRWS_electron",
]
TTbarele_rate_2016APV.bkg = "TTTo2L2Nu"
rateParams["TTest_electron_2016APV"] = TTbarele_rate_2016APV

TTbarmu_rate_2016APV = rateParam()
TTbarmu_rate_2016APV.chs = [
    "SR_muon",
    "CRTT_muon",
    #"CRF_muon",
    #"CRDY_muon",
    #"CRWS_muon",
]
TTbarmu_rate_2016APV.bkg = "TTTo2L2Nu"
rateParams["TTest_muon_2016APV"] = TTbarmu_rate_2016APV


DYele_rate_2016APV = rateParam()
DYele_rate_2016APV.chs = [
    "SR_electron",
    #"CRTT_electron",
    #"CRF_electron",
    #"CRDY_electron",
    "CRWS_electron",
]
DYele_rate_2016APV.bkg = dyjets_sample
rateParams["DYest_electron_2016APV"] = DYele_rate_2016APV

DYmu_rate_2016APV = rateParam()
DYmu_rate_2016APV.chs = [
    "SR_muon",
    #"CRTT_muon",
    #"CRF_muon",
    #"CRDY_muon",
    "CRWS_muon",
]
DYmu_rate_2016APV.bkg = dyjets_sample
rateParams["DYest_muon_2016APV"] = DYmu_rate_2016APV


FakeMu_rate_2016 = rateParam()
FakeMu_rate_2016.chs = [
    "SR_muon",
    #"CRTT_muon",                                                    
    "CRF_muon",
    #"CRDY_muon",
    #"CRWS_muon",
]
FakeMu_rate_2016.bkg = "Fake"
rateParams["FRest_muon_2016"] = FakeMu_rate_2016


FakeEle_rate_2016 = rateParam()
FakeEle_rate_2016.chs = [
    "SR_electron",
    #"CRTT_electron",
    "CRF_electron",
    #"CRDY_electron",
    #"CRWS_electron",
]
FakeEle_rate_2016.bkg = "Fake"
rateParams["FRest_electron_2016"] = FakeEle_rate_2016

'''
WSele_rate_2016 = rateParam()
WSele_rate_2016.chs = [
    "SR_electron",
    "CRTT_electron",
    "CRF_electron",
    #"CRDY_electron",
    "CRWS_electron",
]
WSele_rate_2016.bkg = "WrongSign"
rateParams["WSest_electron_2016"] = WSele_rate_2016

WSmu_rate_2016 = rateParam()
WSmu_rate_2016.chs = [
    "SR_muon",
    "CRTT_muon",
    "CRF_muon",
    #"CRDY_muon",
    "CRWS_muon",
]
WSmu_rate_2016.bkg = "WrongSign"
rateParams["WSest_muon_2016"] = WSmu_rate_2016
'''

TTbarele_rate_2016 = rateParam()
TTbarele_rate_2016.chs = [
    "SR_electron",
    "CRTT_electron",
    #"CRF_electron",
    #"CRDY_electron",
    #"CRWS_electron",
]
TTbarele_rate_2016.bkg = "TTTo2L2Nu"
rateParams["TTest_electron_2016"] = TTbarele_rate_2016

TTbarmu_rate_2016 = rateParam()
TTbarmu_rate_2016.chs = [
    "SR_muon",
    "CRTT_muon",
    #"CRF_muon",
    #"CRDY_muon",
    #"CRWS_muon",
]
TTbarmu_rate_2016.bkg = "TTTo2L2Nu"
rateParams["TTest_muon_2016"] = TTbarmu_rate_2016


DYele_rate_2016 = rateParam()
DYele_rate_2016.chs = [
    "SR_electron",
    #"CRTT_electron",
    #"CRF_electron",
    #"CRDY_electron",
    "CRWS_electron",
]
DYele_rate_2016.bkg = dyjets_sample
rateParams["DYest_electron_2016"] = DYele_rate_2016

DYmu_rate_2016 = rateParam()
DYmu_rate_2016.chs = [
    "SR_muon",
    #"CRTT_muon",
    #"CRF_muon",
    #"CRDY_muon",
    "CRWS_muon",
]
DYmu_rate_2016.bkg = dyjets_sample
rateParams["DYest_muon_2016"] = DYmu_rate_2016

FakeMu_rate_2017 = rateParam()
FakeMu_rate_2017.chs = [
    "SR_muon",
    #"CRTT_muon",                                                    
    "CRF_muon",
    #"CRDY_muon",
    #"CRWS_muon",
]
FakeMu_rate_2017.bkg = "Fake"
rateParams["FRest_muon_2017"] = FakeMu_rate_2017


FakeEle_rate_2017 = rateParam()
FakeEle_rate_2017.chs = [
    "SR_electron",
    #"CRTT_electron",
    "CRF_electron",
    #"CRDY_electron",
    #"CRWS_electron",
]
FakeEle_rate_2017.bkg = "Fake"
rateParams["FRest_electron_2017"] = FakeEle_rate_2017

'''
WSele_rate_2017 = rateParam()
WSele_rate_2017.chs = [
    "SR_electron",
    #"CRTT_electron",
    #"CRF_electron",
    #"CRDY_electron",
    "CRWS_electron",
]
WSele_rate_2017.bkg = "WrongSign"
rateParams["WSest_electron_2017"] = WSele_rate_2017

WSmu_rate_2017 = rateParam()
WSmu_rate_2017.chs = [
    "SR_muon",
    #"CRTT_muon",
    #"CRF_muon",
    #"CRDY_muon",
    "CRWS_muon",
]
WSmu_rate_2017.bkg = "WrongSign"
rateParams["WSest_muon_2017"] = WSmu_rate_2017
'''

TTbarele_rate_2017 = rateParam()
TTbarele_rate_2017.chs = [
    "SR_electron",
    "CRTT_electron",
    #"CRF_electron",
    #"CRDY_electron",
    #"CRWS_electron",
]
TTbarele_rate_2017.bkg = "TTTo2L2Nu"
rateParams["TTest_electron_2017"] = TTbarele_rate_2017

TTbarmu_rate_2017 = rateParam()
TTbarmu_rate_2017.chs = [
    "SR_muon",
    "CRTT_muon",
    #"CRF_muon",
    #"CRDY_muon",
    #"CRWS_muon",
]
TTbarmu_rate_2017.bkg = "TTTo2L2Nu"
rateParams["TTest_muon_2017"] = TTbarmu_rate_2017

DYele_rate_2017 = rateParam()
DYele_rate_2017.chs = [
    "SR_electron",
    #"CRTT_electron",
    #"CRF_electron",
    #"CRDY_electron",
    "CRWS_electron",
]
DYele_rate_2017.bkg = dyjets_sample
rateParams["DYest_electron_2017"] = DYele_rate_2017

DYmu_rate_2017 = rateParam()
DYmu_rate_2017.chs = [
    "SR_muon",
    #"CRTT_muon",
    #"CRF_muon",
    #"CRDY_muon",
    "CRWS_muon",
]
DYmu_rate_2017.bkg = dyjets_sample
rateParams["DYest_muon_2017"] = DYmu_rate_2017


FakeMu_rate_2018 = rateParam()
FakeMu_rate_2018.chs = [
    "SR_muon",
    #"CRTT_muon",
    "CRF_muon",
    #"CRDY_muon",
    #"CRWS_muon",
]
FakeMu_rate_2018.bkg = "Fake"
rateParams["FRest_muon_2018"] = FakeMu_rate_2018


FakeEle_rate_2018 = rateParam()
FakeEle_rate_2018.chs = [
    "SR_electron",
    #"CRTT_electron",
    "CRF_electron",
    #"CRDY_electron",
    #"CRWS_electron",
]
FakeEle_rate_2018.bkg = "Fake"
rateParams["FRest_electron_2018"] = FakeEle_rate_2018

'''
WSele_rate_2018 = rateParam()
WSele_rate_2018.chs = [
    "SR_electron",
    "CRTT_electron",
    "CRF_electron",
    #"CRDY_electron",
    "CRWS_electron",
]
WSele_rate_2018.bkg = "WrongSign"
rateParams["WSest_electron_2018"] = WSele_rate_2018

WSmu_rate_2018 = rateParam()
WSmu_rate_2018.chs = [
    "SR_muon",
    "CRTT_muon",
    "CRF_muon",
    #"CRDY_muon",
    "CRWS_muon",
]
WSmu_rate_2018.bkg = "WrongSign"
rateParams["WSest_muon_2018"] = WSmu_rate_2018
'''

TTbarele_rate_2018 = rateParam()
TTbarele_rate_2018.chs = [
    "SR_electron",
    "CRTT_electron",
    #"CRF_electron",
    #"CRDY_electron",
    #"CRWS_electron",
]
TTbarele_rate_2018.bkg = "TTTo2L2Nu"
rateParams["TTest_electron_2018"] = TTbarele_rate_2018

TTbarmu_rate_2018 = rateParam()
TTbarmu_rate_2018.chs = [
    "SR_muon",
    "CRTT_muon",
    #"CRF_muon",
    #"CRDY_muon",
    #"CRWS_muon",
]
TTbarmu_rate_2018.bkg = "TTTo2L2Nu"
rateParams["TTest_muon_2018"] = TTbarmu_rate_2018


DYele_rate_2018 = rateParam()
DYele_rate_2018.chs = [
    "SR_electron",
    #"CRTT_electron",
    #"CRF_electron",
    #"CRDY_electron",
    "CRWS_electron",
]
DYele_rate_2018.bkg = dyjets_sample
rateParams["DYest_electron_2018"] = DYele_rate_2018

DYmu_rate_2018 = rateParam()
DYmu_rate_2018.chs = [
    "SR_muon",
    #"CRTT_muon",
    #"CRF_muon",
    #"CRDY_muon",
    "CRWS_muon",
]
DYmu_rate_2018.bkg = dyjets_sample
rateParams["DYest_muon_2018"] = DYmu_rate_2018

#*********************************
#                                *
#       List of systematics      *
#                                *
#*********************************
syst = collections.OrderedDict()

syst["lumi_2016APV"] = ["lnN", "all", 1.025]
syst["lumi_2016"] = ["lnN", "all", 1.025]
syst["lumi_2017"] = ["lnN", "all", 1.023]
syst["lumi_2018"] = ["lnN", "all", 1.025]
syst["FR_sys_muon_2017"] = ["lnN", "Fake", 1.3]
syst["FR_sys_electron_2017"] = ["lnN", "Fake", 1.3]

#syst["trigger"] = ["lnN", "all", 1.02]
#syst["trigSF"] = ["shape", ["sig"]]
#syst["trigSF"] = ["lnN", ["sig",sigTTW, sigZ, "QCD", "SingleTop"]]
#syst["jes"] = ["shape", ("QCD", "TT_Mtt", "WJets", "sig")]

### ReReco
#syst["autoMCstat"] = ["shape", ("VG", "WpWpJJ_QCD", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]

### UltraLegacy
syst["autoMCstat"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["PF"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["pu"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["lep"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["btag"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["tau_vsjet_"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["tau_vsele_"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["tau_vsmu_"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["pdf_total"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["QCDScale"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["ISR"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["FSR"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["jes"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["jer"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["TES"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]
syst["FES"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]

'''
syst["trig"] = ["shape", ("QCD",  "sig")]
syst["btag"] = ["shape", ("QCD",  "sig")]
syst["mistag"] = ["shape", ("QCD",  "sig")]
'''

#years = ["2017"]
#years = ["2018"]
years = ["2017", "2018"]
#years = ["2016APV","2016","2017","2018"]

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
VBS_SSWW_cW_BSM = ("cW_BSM")
VBS_SSWW_cHW_BSM = ("cHW_BSM")
VBS_SSWW_cW = ("cW")
VBS_SSWW_cHW = ("cHW")
VBS_SSWW_aQGC = ("aQGC")
VBS_SSWW_FS0_25_SM = ("FS0_25_SM")
VBS_SSWW_FS0_5_SM = ("FS0_5_SM")                                                                                    
VBS_SSWW_FS0_5_BSM = ("FS0_5_BSM")                                            
VBS_SSWW_FS0_25_BSM = ("FS0_25_BSM")
VBS_SSWW_FS0_5 = ("FS0_5")
VBS_SSWW_FS0_0 = ("FS0_0")
#VBS_SSWW_FS1_50_SM = ("FS1_50_SM")
VBS_SSWW_FS1_10_SM = ("FS1_10_SM")
VBS_SSWW_FS1_10_BSM = ("FS1_50_BSM")
VBS_SSWW_FS1_10 = ("FS1_10")                           
VBS_SSWW_FS1_0 = ("FS1_0")
VBS_SSWW_FM0_25_SM = ("FM0_25_SM")
#VBS_SSWW_FM0_5_SM = ("FM0_5_SM")
VBS_SSWW_FM0_25_BSM = ("FM0_25_BSM")
VBS_SSWW_FM0_5 = ("FM0_5")
VBS_SSWW_FM0_0 = ("FM0_0")
VBS_SSWW_FM1_25_SM = ("FM1_25_SM")
VBS_SSWW_FM1_5_SM = ("FM1_5_SM")
VBS_SSWW_FM1_5_BSM = ("FM1_5_BSM")
VBS_SSWW_FM1_25_BSM = ("FM1_25_BSM")
VBS_SSWW_FM1_5 = ("FM1_5")
VBS_SSWW_FM1_0 = ("FM1_0")
VBS_SSWW_FM6_25_SM = ("FM6_25_SM")
#VBS_SSWW_FM6_5_SM = ("FM6_5_SM")                                                                                    
VBS_SSWW_FM6_25 = ("FM6_25")                                                                                          
VBS_SSWW_FM6_25_BSM = ("FM6_25_BSM")                                                                                          
VBS_SSWW_FM6_5 = ("FM6_5")                                                                                
VBS_SSWW_FM6_0 = ("FM6_0")
#VBS_SSWW_FM7_50_SM = ("FM7_50_SM")                                                                                  
VBS_SSWW_FM7_10_SM = ("FM7_10_SM")
VBS_SSWW_FM7_50 = ("FM7_50")
VBS_SSWW_FM7_0 = ("FM7_0")
VBS_SSWW_FM7_10_BSM = ("FM7_10_BSM")
VBS_SSWW_FT0_2p5_SM = ("FT0_2p5_SM")
VBS_SSWW_FT0_2p5_BSM = ("FT0_2p5_SBM")
#VBS_SSWW_FT0_0p5_SM = ("FT0_0p5_SM")
VBS_SSWW_FT0_2p5 = ("FT0_2p5")                                                                                        
VBS_SSWW_FT0_0p5 = ("FT0_0p5")                                                                         
VBS_SSWW_FT0_0 = ("FT0_0")
VBS_SSWW_FT1_1_SM = ("FT1_1_SM")
VBS_SSWW_FT1_1_BSM = ("FT1_1_BSM")
#VBS_SSWW_FT1_0p2_SM  = ("FT1_0p2_SM")
VBS_SSWW_FT1_1 = ("FT1_1")
VBS_SSWW_FT1_0p2  = ("FT1_0p2")
VBS_SSWW_FT1_0  = ("FT1_0")
VBS_SSWW_FT2_2p5_SM = ("FT2_2p5_SM")
VBS_SSWW_FT2_2p5_BSM = ("FT2_2p5_BSM")
VBS_SSWW_FT2_0p5_SM = ("FT2_0p5_SM")
VBS_SSWW_FT2_0p5_BSM = ("FT2_0p5_BSM")
VBS_SSWW_FT2_2p5 = ("FT2_2p5")                                                                                     
VBS_SSWW_FT2_0p5 = ("FT2_0p5")
VBS_SSWW_FT2_0 = ("FT2_0")


sigpoints = [
    [
    VBS_SSWW_SM,#ls+BDTSM
    #VBS_SSWW_aQGC],
    #VBS_SSWW_SM_LL,
    #VBS_SSWW_SM_TL,
    #VBS_SSWW_SM_TT,
    ##VBS_SSWW_BSM_SM,
    ##VBS_SSWW_BSM,
    #VBS_SSWW_cHW_SM,#ls
    #VBS_SSWW_cW,
    #VBS_SSWW_cW_SM,#ls
    #VBS_SSWW_cHW_BSM,#ls
    #VBS_SSWW_cW_BSM,#ls
    ]
    #VBS_SSWW_cHW,
    #VBS_SSWW_cW,
    #VBS_SSWW_FS0_25_SM,#ls
    ##VBS_SSWW_FS0_5_SM,
    ##VBS_SSWW_FS0_5_BSM, 
    #VBS_SSWW_FS0_25_BSM,#ls
    #VBS_SSWW_FS0_5,
    #VBS_SSWW_FS0_0,#ls
    ##VBS_SSWW_FS1_50_SM,
    #VBS_SSWW_FS1_10_SM,#ls
    ##VBS_SSWW_FS1_50,
    #VBS_SSWW_FS1_10_BSM,#ls
    ###VBS_SSWW_FS1_10,           
    #VBS_SSWW_FS1_0,#ls
    #VBS_SSWW_FM0_25_SM,#ls
    ###VBS_SSWW_FM0_5_SM,  
    #VBS_SSWW_FM0_25_BSM,#ls
    ###VBS_SSWW_FM0_5, 
    #VBS_SSWW_FM0_0,#ls 
    #VBS_SSWW_FM1_25_SM,#ls
    ##VBS_SSWW_FM1_5_SM,
    ##VBS_SSWW_FM1_5_BSM,
    #VBS_SSWW_FM1_25_BSM,#ls
    ##VBS_SSWW_FM1_5,
    #VBS_SSWW_FM1_0,#ls
    #VBS_SSWW_FM6_25_SM,#ls
    ##VBS_SSWW_FM6_5_SM,      
    #VBS_SSWW_FM6_25_BSM,#ls  
    ##VBS_SSWW_FM6_5,                                                                                           
    #VBS_SSWW_FM6_0,#ls
    ##VBS_SSWW_FM7_50_SM,                                                                                       
    #VBS_SSWW_FM7_10_SM,#ls
    #VBS_SSWW_FM7_10_BSM,#ls
    ##VBS_SSWW_FM7_50,
    ##VBS_SSWW_FM7_10,
    #VBS_SSWW_FM7_0,#ls
    #VBS_SSWW_FT0_2p5_SM,#ls
    #VBS_SSWW_FT0_2p5_BSM,#ls
    ##VBS_SSWW_FT0_0p5_SM,
    ##VBS_SSWW_FT0_2p5,          
    ##VBS_SSWW_FT0_0p5,                                                                                    
    #VBS_SSWW_FT0_0,#ls
    #[VBS_SSWW_FT1_1_SM,#ls
    #VBS_SSWW_FT1_1_BSM,#ls
    ##VBS_SSWW_FT1_0p2_SM,                                                                                
    ##VBS_SSWW_FT1_1,
    #VBS_SSWW_FT1_0,#ls
     #]
    ##VBS_SSWW_FT1_0p2,
    #VBS_SSWW_FT2_2p5_SM,#ls
    #VBS_SSWW_FT2_2p5_BSM,#ls
    #VBS_SSWW_FT2_0p5_SM,
    #VBS_SSWW_FT2_0p5_BSM,
    ###VBS_SSWW_FT2_2p5,          
    #VBS_SSWW_FT2_0p5,
    #VBS_SSWW_FT2_0,#ls
]

