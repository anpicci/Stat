import collections

def cutToTag(cut):
    newstring = cut.replace("-", "neg").replace(">=","_GE_").replace(">","_G_").replace(" ","").replace("&&","_AND_").replace("||","_OR_").replace("<=","_LE_").replace("<","_L_").replace(".","p").replace("(","").replace(")","").replace("==","_EQ_").replace("!=","_NEQ_").replace("=","_EQ_").replace("*","_AND_").replace("+","_OR_")
    return newstring

#*********************************
#                                *
#       List of channels         *
#                                *
#*********************************
hist_pre = "h_"

setfile = open("/afs/cern.ch/work/a/apiccine/CMSSW_10_2_13/src/Stat/Limits/python/metasett.txt", "r")
setlist = [line.replace("\n", "") for line in setfile.readlines()]
sr_var, cr_var = setlist[0].split(",")
intfolder = setlist[1]
cut = setlist[4]

print sr_var, cr_var, intfolder

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

if cut != "not":
    cuttag = "_AND_" + cutToTag(cut)
    for kh, vh in histos.items():
        histos[kh] = vh + cuttag

if cuttag != "":
    for k, v in histos.items():
        histos[k] = v + cuttag

### List of regions for which creating the datacards
channels = ["SR_muon",
            "CRTT_muon",
            "CRWS_muon",
            ##"CRQCD_muon",
            ##"CRWJ_muon",
            "CRF_muon",
            ##"CRDY_muon",
            "SR_electron",
            "CRTT_electron",
            "CRWS_electron",
            ##"CRQCD_electron",
            ##"CRWJ_electron",
            "CRF_electron",
            ##"CRDY_electron",
]

leptons = [
    #'inclusive',
    'muon',
    'electron',
    #'emu'
]

channels_labels = {"SR":"Signal Region", 
                   "CRWS":"Opposite Sign CR",
                   "CRTT":"t#bar{t} CR",
                   "CRF":"Fake leptons CR",
}

#*********************************
#                                *
#       List of backgrounds      *
#                                *
#*********************************
#processes = ["ST", "QCD", "TT_Mtt", "WJets"]
#processes = ["ST", "QCD", "DDWJetsTT_Mtt"]

bkg = [
    #"WpWpJJ_QCD",
    "VBS_SSWW_SM",
    "VBS_SSWW_LL_SM",
    "VBS_SSWW_TL_SM",
    "VBS_SSWW_TT_SM",
    "ZZtoLep",
    triboson_sample,
    "TVX",
    "VG",
    "WZ",
    "WrongSign",
    dyjets_sample,
    "TTTo2L2Nu",
    "Fake",
]

class rateParam(object):
    pass

rateParams = {}

'''
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
'''
'''
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
'''

FakeMu_rate_2016M = rateParam()
FakeMu_rate_2016M.chs = [
    "SR_muon",
    #"CRTT_muon",                                                    
    "CRF_muon",
    ##"CRDY_muon",
    #"CRWS_muon",
]
FakeMu_rate_2016M.bkg = "Fake"
rateParams["FRest_muon_2016M"] = FakeMu_rate_2016M


FakeEle_rate_2016M = rateParam()
FakeEle_rate_2016M.chs = [
    "SR_electron",
    #"CRTT_electron",
    "CRF_electron",
    ##"CRDY_electron",
    #"CRWS_electron",
]
FakeEle_rate_2016M.bkg = "Fake"
rateParams["FRest_electron_2016M"] = FakeEle_rate_2016M

'''
WSele_rate_2016M = rateParam()
WSele_rate_2016M.chs = [
    "SR_electron",
    #"CRTT_electron",
    #"CRF_electron",
    #"CRDY_electron",
    "CRWS_electron",
]
WSele_rate_2016M.bkg = "WrongSign"
rateParams["WSest_electron_2016M"] = WSele_rate_2016M

WSmu_rate_2016M = rateParam()
WSmu_rate_2016M.chs = [
    "SR_muon",
    #"CRTT_muon",
    #"CRF_muon",
    #"CRDY_muon",
    "CRWS_muon",
]
WSmu_rate_2016M.bkg = "WrongSign"
rateParams["WSest_muon_2016M"] = WSmu_rate_2016M
'''

TTbarele_rate_2016M = rateParam()
TTbarele_rate_2016M.chs = [
    "SR_electron",
    "CRTT_electron",
    #"CRF_electron",
    #"CRDY_electron",
    #"CRWS_electron",
]
TTbarele_rate_2016M.bkg = "TTTo2L2Nu"
rateParams["TTest_electron_2016M"] = TTbarele_rate_2016M

TTbarmu_rate_2016M = rateParam()
TTbarmu_rate_2016M.chs = [
    "SR_muon",
    "CRTT_muon",
    #"CRF_muon",
    #"CRDY_muon",
    #"CRWS_muon",
]
TTbarmu_rate_2016M.bkg = "TTTo2L2Nu"
rateParams["TTest_muon_2016M"] = TTbarmu_rate_2016M


DYele_rate_2016M = rateParam()
DYele_rate_2016M.chs = [
    "SR_electron",
    #"CRTT_electron",
    #"CRF_electron",
    #"CRDY_electron",
    "CRWS_electron",
]
DYele_rate_2016M.bkg = dyjets_sample
rateParams["DYest_electron_2016M"] = DYele_rate_2016M

DYmu_rate_2016M = rateParam()
DYmu_rate_2016M.chs = [
    "SR_muon",
    #"CRTT_muon",
    #"CRF_muon",
    #"CRDY_muon",
    "CRWS_muon",
]
DYmu_rate_2016M.bkg = dyjets_sample
rateParams["DYest_muon_2016M"] = DYmu_rate_2016M

FakeMu_rate_2017 = rateParam()
FakeMu_rate_2017.chs = [
    "SR_muon",
    #"CRTT_muon",                                                    
    "CRF_muon",
    ##"CRDY_muon",
    #"CRWS_muon",
]
FakeMu_rate_2017.bkg = "Fake"
rateParams["FRest_muon_2017"] = FakeMu_rate_2017

FakeEle_rate_2017 = rateParam()
FakeEle_rate_2017.chs = [
    "SR_electron",
    #"CRTT_electron",
    "CRF_electron",
    ##"CRDY_electron",
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
    ##"CRDY_muon",
    #"CRWS_muon",
]
FakeMu_rate_2018.bkg = "Fake"
rateParams["FRest_muon_2018"] = FakeMu_rate_2018


FakeEle_rate_2018 = rateParam()
FakeEle_rate_2018.chs = [
    "SR_electron",
    #"CRTT_electron",
    "CRF_electron",
    ##"CRDY_electron",
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

#syst["lumi_2016APV"] = ["lnN", "all", 1.01]
#syst["lumi_2016"] = ["lnN", "all", 1.01]
#syst["lumi_2017"] = ["lnN", "all", 1.02]
#syst["lumi_2018"] = ["lnN", "all", 1.015]
#syst["lumi_161718_2016APV"] = ["lnN", "all", 1.006]
#syst["lumi_161718_2016"] = ["lnN", "all", 1.006]
#syst["lumi_161718_2017"] = ["lnN", "all", 1.009]
#syst["lumi_161718_2018"] = ["lnN", "all", 1.02]
#syst["lumi_1718_2017"] = ["lnN", "all", 1.006]
#syst["lumi_1718_2018"] = ["lnN", "all", 1.002]


syst["lumi_2016M"] = ["lnN", "all", 1.012]
syst["lumi_2017"] = ["lnN", "all", 1.023]
syst["lumi_2018"] = ["lnN", "all", 1.025]

syst["FR_sys_muon_2016M"] = ["lnN", "Fake", 1.3]
syst["FR_sys_electron_2016M"] = ["lnN", "Fake", 1.3]
syst["FR_sys_muon_2017"] = ["lnN", "Fake", 1.3]
syst["FR_sys_electron_2017"] = ["lnN", "Fake", 1.3]
syst["FR_sys_muon_2018"] = ["lnN", "Fake", 1.3]
syst["FR_sys_electron_2018"] = ["lnN", "Fake", 1.3]

### ReReco
#syst["autoMCstat"] = ["shape", ("VG", "WpWpJJ_QCD", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig")]

### UltraLegacy

syst["autoMCstat"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "uncorr"]
syst["PF"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "corr"]
syst["pu"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "corr"]
syst["lep"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "uncorr"]
syst["btag"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "corr"]
syst["tau_vsjet"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "uncorr"]
syst["tau_vsele"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "uncorr"]
syst["tau_vsmu"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "uncorr"]
syst["pdf_total"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "corr"]
syst["QCDScale"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "corr"]
syst["ISR"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "corr"]
syst["FSR"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "corr"]
syst["jes"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "corr"]
syst["jer"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "uncorr"]
syst["TES"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "corr"]
syst["FES"] = ["shape", ("VG", "TVX", dyjets_sample, "TTTo2L2Nu", "WZ", triboson_sample, "WrongSign", "ZZtoLep", "sig"), "corr"]

'''
syst["trig"] = ["shape", ("QCD",  "sig")]
syst["btag"] = ["shape", ("QCD",  "sig")]
syst["mistag"] = ["shape", ("QCD",  "sig")]
'''

years = setlist[3].split(",")
print("years:", years)
'''
= [
    "2016M", 
    "2017",
    "2018",
]
'''
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

if setlist[2].endswith("SM"):
    sigs = [setlist[2]]
    lssamples_1D = {
        setlist[2]:{    
            'sm': "VBS_SSWW_" + sigs[0],#"VBS_SSWW_SM",
            'sm_lin_quad_cW': "VBS_SSWW_" + sigs[0],#"VBS_SSWW_cW_SM",
            'quad_cW': "VBS_SSWW_" + sigs[0],#"VBS_SSWW_cW_BSM",
        },
    }

elif setlist[2].startswith("c"):
    sigs = [
        "SM",
        setlist[2] + "_SM",
        setlist[2] + "_BSM",
    ]
    lssamples_1D = {
        setlist[2]:{    
            'sm': "VBS_SSWW_" + sigs[0],#"VBS_SSWW_SM",
            'sm_lin_quad_cW': "VBS_SSWW_" + sigs[1],#"VBS_SSWW_cW_SM",
            'quad_cW': "VBS_SSWW_" + sigs[2],#"VBS_SSWW_cW_BSM",
        },
    }

elif setlist[2].startswith("F"):
    sigs = [
        setlist[2].replace(setlist[2].split("_")[-1],"") + "0",
        setlist[2] + "_SM",
        setlist[2] + "_BSM",
    ]
    lssamples_1D = {
        setlist[2]:{    
            'sm': "VBS_SSWW_" + sigs[0],#"VBS_SSWW_SM",
            'sm_lin_quad_cW': "VBS_SSWW_" + sigs[1],#"VBS_SSWW_cW_SM",
            'quad_cW': "VBS_SSWW_" + sigs[2],#"VBS_SSWW_cW_BSM",
        },
    }

elif setlist[2].startswith("WpWp"):
    sigs = [setlist[2]]
    lssamples_1D = {
        setlist[2]:{    
            'sm': sigs[0],
            'sm_lin_quad_cW': sigs[0],
            'quad_cW': sigs[0],
        },
    }

else:
    raise RuntimeError("Warning! Please insert valid model!")



sigpoints = [sigs]


print sigpoints, lssamples_1D
