import collections

#*********************************
#                                *
#       List of channels         *
#                                *
#*********************************
sr_var = 'BDT_output_SM'
cr_var = sr_var#'countings'
hist_pre = "h_"
### List of histos to include in the root files
histos = { "SR":hist_pre + sr_var + "_SR",
           #"PR":"h_ltau_m_jj_selection_upto_bveto_lepBDTcut",
           "CRWJ":hist_pre + cr_var + "_wjets_CR",
           "CRTT":hist_pre + cr_var + "_ttbar_CR",
           "CRQCD":hist_pre + cr_var + "_QCD_CR",
}
### List of regions for which creating the datacards
channels = ["SR_muon",
            "CRWJ_muon",
            "CRTT_muon",
            #"CRQCD_muon",
            "SR_electron",
            "CRWJ_electron",
            "CRTT_electron",
            #"CRTT_emu",
            #"CRQCD_electron",
]

leptons = ['muon',
           'electron',
           #'emu'
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
VBS_SSWW_cW_BSM = ("cW_BSM")
VBS_SSWW_cHW_BSM = ("cHW_BSM")
VBS_SSWW_cW = ("cW")
VBS_SSWW_cHW = ("cHW")
VBS_SSWW_aQGC = ("aQGC")
#VBS_SSWW_FS0_25_SM = ("FS0_25_SM")
VBS_SSWW_FS0_5_SM = ("FS0_5_SM")                                                                                    
VBS_SSWW_FS0_5_BSM = ("FS0_5_BSM")                                            
VBS_SSWW_FS0_25 = ("FS0_25")
VBS_SSWW_FS0_5 = ("FS0_5")
VBS_SSWW_FS0_0 = ("FS0_0")
#VBS_SSWW_FS1_50_SM = ("FS1_50_SM")
#VBS_SSWW_FS1_10_SM = ("FS1_10_SM")
VBS_SSWW_FS1_50 = ("FS1_50")
VBS_SSWW_FS1_10 = ("FS1_10")                                                                                              
#VBS_SSWW_FM0_25_SM = ("FM0_25_SM")
#VBS_SSWW_FM0_5_SM = ("FM0_5_SM")
VBS_SSWW_FM0_25 = ("FM0_25")
VBS_SSWW_FM0_5 = ("FM0_5")
#VBS_SSWW_FM1_25_SM = ("FM1_25_SM")
VBS_SSWW_FM1_5_SM = ("FM1_5_SM")
VBS_SSWW_FM1_5_BSM = ("FM1_5_BSM")
VBS_SSWW_FM1_25 = ("FM1_25")
VBS_SSWW_FM1_5 = ("FM1_5")
VBS_SSWW_FM1_0 = ("FM1_0")
#VBS_SSWW_FM6_25_SM = ("FM6_25_SM")
#VBS_SSWW_FM6_5_SM = ("FM6_5_SM")                                                                                    
VBS_SSWW_FM6_25 = ("FM6_25")                                                                                          
VBS_SSWW_FM6_5 = ("FM6_5")                                                                                
#VBS_SSWW_FM7_50_SM = ("FM7_50_SM")                                                                                  
#VBS_SSWW_FM7_10_SM = ("FM7_10_SM")
VBS_SSWW_FM7_50 = ("FM7_50")
VBS_SSWW_FM7_10 = ("FM7_10")
#VBS_SSWW_FT0_2p5_SM = ("FT0_2p5_SM")
#VBS_SSWW_FT0_0p5_SM = ("FT0_0p5_SM")
VBS_SSWW_FT0_2p5 = ("FT0_2p5")                                                                                        
VBS_SSWW_FT0_0p5 = ("FT0_0p5")                                                                         
#VBS_SSWW_FT1_1_SM = ("FT1_1_SM")
#VBS_SSWW_FT1_0p2_SM  = ("FT1_0p2_SM")
VBS_SSWW_FT1_1 = ("FT1_1")
VBS_SSWW_FT1_0p2  = ("FT1_0p2")
#VBS_SSWW_FT2_2p5_SM = ("FT2_2p5_SM")
VBS_SSWW_FT2_0p5_SM = ("FT2_0p5_SM")
VBS_SSWW_FT2_0p5_BSM = ("FT2_0p5_BSM")
VBS_SSWW_FT2_2p5 = ("FT2_2p5")                                                                                     
VBS_SSWW_FT2_0p5 = ("FT2_0p5")
VBS_SSWW_FT2_0 = ("FT2_0")


sigpoints = [
    VBS_SSWW_SM,
    ##VBS_SSWW_aQGC,
    ##VBS_SSWW_SM_LL,
    ##VBS_SSWW_SM_TL,
    ##VBS_SSWW_SM_TT,
    ###VBS_SSWW_BSM_SM,
    ###VBS_SSWW_BSM,
    #VBS_SSWW_cHW_SM,#ls
    #VBS_SSWW_cW_SM,#ls
    #VBS_SSWW_cHW_BSM,#ls
    #VBS_SSWW_cW_BSM,#ls
    #VBS_SSWW_cHW,
    #VBS_SSWW_cW,
    ###VBS_SSWW_FS0_25_SM,
    #VBS_SSWW_FS0_5_SM,#ls
    #VBS_SSWW_FS0_5_BSM,#ls 
    ###VBS_SSWW_FS0_25,    
    #VBS_SSWW_FS0_5,
    #VBS_SSWW_FS0_0,#ls
    ###VBS_SSWW_FS1_50_SM,       
    ###VBS_SSWW_FS1_10_SM,
    ###VBS_SSWW_FS1_50,
    ###VBS_SSWW_FS1_10,           
    ###VBS_SSWW_FM0_25_SM,       
    ###VBS_SSWW_FM0_5_SM,  
    ###VBS_SSWW_FM0_25,
    ###VBS_SSWW_FM0_5, 
    ###VBS_SSWW_FM1_25_SM,       
    #VBS_SSWW_FM1_5_SM,#ls
    #VBS_SSWW_FM1_5_BSM,#ls
    ###VBS_SSWW_FM1_25,
    #VBS_SSWW_FM1_5,#ls
    #VBS_SSWW_FM1_0,
    ###VBS_SSWW_FM6_25_SM,       
    ###VBS_SSWW_FM6_5_SM,        
    ###VBS_SSWW_FM6_25,           
    ###VBS_SSWW_FM6_5,                                                                                           
    ###VBS_SSWW_FM7_50_SM,                                                                                       
    ###VBS_SSWW_FM7_10_SM,
    ###VBS_SSWW_FM7_50,
    ###VBS_SSWW_FM7_10,
    ###VBS_SSWW_FT0_2p5_SM,
    ###VBS_SSWW_FT0_0p5_SM,
    ###VBS_SSWW_FT0_2p5,          
    ###VBS_SSWW_FT0_0p5,                                                                                    
    ###VBS_SSWW_FT1_1_SM,                                                                                  
    ###VBS_SSWW_FT1_0p2_SM,                                                                                
    ###VBS_SSWW_FT1_1,
    ###VBS_SSWW_FT1_0p2,
    ###VBS_SSWW_FT2_2p5_SM,
    #VBS_SSWW_FT2_0p5_SM,#ls
    #VBS_SSWW_FT2_0p5_BSM,#ls
    ###VBS_SSWW_FT2_2p5,          
    #VBS_SSWW_FT2_0p5,
    #VBS_SSWW_FT2_0,#ls
]

