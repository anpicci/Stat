import ROOT
import os 
#import json_reader as jr

path = os.path.dirname(os.path.abspath(__file__))

class sample:
    def __init__(self, color, style, fill, leglabel, label):
        self.color = color
        self.style = style
        self.fill = fill
        self.leglabel = leglabel
        self.label = label

tag_2016 = 'RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8'
tag_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8'
tag1_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_v2_102X_mc2017_realistic_v8'
tag2_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8'
tag3_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8'
tag_2018 = 'RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21'

###################################################################################################################################################################
############################################################                                           ############################################################
############################################################                    2016                   ############################################################
############################################################                                           ############################################################
###################################################################################################################################################################
################################ TTbar ################################
TT_incl_2016 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_incl_2016")
TT_incl_2016.sigma = 831.76 #pb
TT_incl_2016.year = 2016
TT_incl_2016.dataset = "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+tag_2016+"-v2/NANOAODSIM"

TT_Mtt700to1000_2016 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt700to1000_2016")
TT_Mtt700to1000_2016.sigma = 80.5 #pb
TT_Mtt700to1000_2016.year = 2016
TT_Mtt700to1000_2016.dataset = "/TT_Mtt-700to1000_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#TT_Mtt700to1000_2016.files = jr.json_reader(path+"/TT_Mtt700to1000_2016.json")

TT_Mtt1000toInf_2016 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt1000toInf_2016")
TT_Mtt1000toInf_2016.sigma = 21.3 #pb
TT_Mtt1000toInf_2016.year = 2016
TT_Mtt1000toInf_2016.dataset = "/TT_Mtt-1000toInf_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#TT_Mtt1000toInf_2016.files = jr.json_reader(path+"/TT_Mtt1000toInf_2016.json")

TT_Mtt_2016 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt_2016")
TT_Mtt_2016.year = 2016
TT_Mtt_2016.components = [TT_incl_2016, TT_Mtt700to1000_2016, TT_Mtt1000toInf_2016]

'''
TT_DiLep_2016 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_DiLep_2016")
TT_DiLep_2016.sigma = 831.76 #pb
TT_DiLep_2016.year = 2016
TT_DiLep_2016.dataset = "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+tag_2016+"-v1/NANOAODSIM"
# /TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM
'''

################################ WJets ################################
WJetsHT70to100_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT70to100_2016")
WJetsHT70to100_2016.sigma = 1353.0 * 1.21 #pb
WJetsHT70to100_2016.year = 2016
WJetsHT70to100_2016.dataset = "/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
WJetsHT100to200_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT100to200_2016")
WJetsHT100to200_2016.sigma = 1345 * 1.21 #pb
WJetsHT100to200_2016.year = 2016
WJetsHT100to200_2016.dataset = "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
WJetsHT200to400_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT200to400_2016")
WJetsHT200to400_2016.sigma = 359.7 * 1.21 #pb
WJetsHT200to400_2016.year = 2016
WJetsHT200to400_2016.dataset = "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#WJetsHT200to400_2016.files = jr.json_reader(path+"/WJets_HT200To400_2016.json")
WJetsHT400to600_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT400to600_2016")
WJetsHT400to600_2016.sigma = 48.91 * 1.21 #pb
WJetsHT400to600_2016.year = 2016
WJetsHT400to600_2016.dataset = "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#WJetsHT400to600_2016.files = jr.json_reader(path+"/WJets_HT400To600_2016.json")
WJetsHT600to800_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT600to800_2016")
WJetsHT600to800_2016.sigma = 12.05 * 1.21 #pb
WJetsHT600to800_2016.year = 2016
WJetsHT600to800_2016.dataset = "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#WJetsHT600to800_2016.files = jr.json_reader(path+"/WJets_HT600To800_2016.json")
WJetsHT800to1200_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT800to1200_2016")
WJetsHT800to1200_2016.sigma = 5.501 * 1.21 #pb
WJetsHT800to1200_2016.year = 2016
WJetsHT800to1200_2016.dataset = "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#WJetsHT800to1200_2016.files = jr.json_reader(path+"/WJets_HT800To1200_2016.json")
WJetsHT1200to2500_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT1200to2500_2016")
WJetsHT1200to2500_2016.sigma = 1.329 * 1.21 #pb
WJetsHT1200to2500_2016.year = 2016
WJetsHT1200to2500_2016.dataset = "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#WJetsHT1200to2500_2016.files = jr.json_reader(path+"/WJets_HT1200To2500_2016.json")
WJetsHT2500toInf_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT2500toInf_2016")
WJetsHT2500toInf_2016.sigma = 0.03216 * 1.21 #pb
WJetsHT2500toInf_2016.year = 2016
WJetsHT2500toInf_2016.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#WJetsHT2500toInf_2016.files = jr.json_reader(path+"/WJets_HT2500ToInf_2016.json")

WJets_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets_2016")
WJets_2016.year = 2016
WJets_2016.components = [WJetsHT70to100_2016, WJetsHT100to200_2016, WJetsHT200to400_2016, WJetsHT400to600_2016, WJetsHT600to800_2016, WJetsHT800to1200_2016, WJetsHT1200to2500_2016, WJetsHT2500toInf_2016]
#WJets_2016.components = [WJetsHT100to200_2016, WJetsHT200to400_2016, WJetsHT400to600_2016, WJetsHT600to800_2016, WJetsHT800to1200_2016, WJetsHT1200to2500_2016, WJetsHT2500toInf_2016]

################################ WZ ################################
WZ_2016 = sample(ROOT.kYellow, 1, 1001, "WZ", "WZ_2016")
WZ_2016.sigma = 47.13
WZ_2016.year = 2016
WZ_2016.dataset = "/WZ_TuneCUETP8M1_13TeV-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

################################ DrellYan ################################
DY1JetsToLL_2016 = sample(ROOT.kAzure+6, 1, 1001, "DY + 1 Jet", "DY1JetsToLL_2016")
DY1JetsToLL_2016.sigma = 1012.0
DY1JetsToLL_2016.year = 2016
DY1JetsToLL_2016.dataset = "/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

DY2JetsToLL_2016 = sample(ROOT.kAzure+6, 1, 1001, "DY + 2 Jets", "DY2JetsToLL_2016")
DY2JetsToLL_2016.sigma = 330.4
DY2JetsToLL_2016.year = 2016
DY2JetsToLL_2016.dataset = "/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

DY3JetsToLL_2016 = sample(ROOT.kAzure+6, 1, 1001, "DY + 3 Jets", "DY3JetsToLL_2016")
DY3JetsToLL_2016.sigma = 101.8
DY3JetsToLL_2016.year = 2016
DY3JetsToLL_2016.dataset = "/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

DY4JetsToLL_2016 = sample(ROOT.kAzure+6, 1, 1001, "DY + 4+ Jets", "DY4JetsToLL_2016")
DY4JetsToLL_2016.sigma = 54.80
DY4JetsToLL_2016.year = 2016
DY4JetsToLL_2016.dataset = "/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

DYJetsToLL_2016 = sample(ROOT.kAzure+6, 1, 1001, "DY + Jets", "DYJetsToLL_2016")
DYJetsToLL_2016.year = 2016
DYJetsToLL_2016.components = [DY1JetsToLL_2016, DY2JetsToLL_2016, DY3JetsToLL_2016, DY4JetsToLL_2016]

################################ ssWW EWK ################################
WpWpJJ_EWK_2016 = sample(ROOT.kRed, 1, 1001, "EW ssWW", "WpWpJJ_EWK_2016")
WpWpJJ_EWK_2016.sigma = 0.01927
WpWpJJ_EWK_2016.year = 2016
WpWpJJ_EWK_2016.dataset = "/WpWpJJ_EWK_TuneCUETP8M1_13TeV-powheg-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

WpWpJJ_QCD_2016 = sample(ROOT.kBlue, 1, 1001, "QCD ssWW", "WpWpJJ_QCD_2016")
WpWpJJ_QCD_2016.sigma = 0.02612
WpWpJJ_QCD_2016.year = 2016
WpWpJJ_QCD_2016.dataset = "/WpWpJJ_QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

###################################################################################################################################################################
############################################################                                           ############################################################
############################################################                    2017                   ############################################################
############################################################                                           ############################################################
###################################################################################################################################################################

################################ QCD ################################
QCDHT_100to200_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_100to200_2017")
QCDHT_100to200_2017.year = 2017
QCDHT_100to200_2017.dataset = "/QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
QCDHT_100to200_2017.sigma = 23700000.0 #pb                                                     

QCDHT_200to300_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_200to300_2017")
QCDHT_200to300_2017.year = 2017
QCDHT_200to300_2017.dataset = "/QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8/" + tag2_2017 + "-v1/NANOAODSIM"
QCDHT_200to300_2017.sigma = 1547000.0 #pb                                                     

QCDHT_300to500_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_300to500_2017")
QCDHT_300to500_2017.year = 2017
QCDHT_300to500_2017.dataset = "/QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8/" + tag2_2017 + "-v1/NANOAODSIM"
QCDHT_300to500_2017.sigma = 322600.0 #pb                                                    

QCDHT_500to700_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_500to700_2017")
QCDHT_500to700_2017.year = 2017
QCDHT_500to700_2017.dataset = "/QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
QCDHT_500to700_2017.sigma = 29980.0 #pb                                                     

QCDHT_700to1000_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_700to1000_2017")
QCDHT_700to1000_2017.year = 2017
QCDHT_700to1000_2017.dataset = "/QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/" + tag2_2017 + "-v1/NANOAODSIM"
QCDHT_700to1000_2017.sigma = 6334.0 #pb                                                     

QCDHT_1000to1500_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1000to1500_2017")
QCDHT_1000to1500_2017.year = 2017
QCDHT_1000to1500_2017.dataset = "/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/" + tag2_2017 + "-v1/NANOAODSIM"
QCDHT_1000to1500_2017.sigma = 1088.0 #pb                                                     

QCDHT_1500to2000_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1500to2000_2017")
QCDHT_1500to2000_2017.year = 2017
QCDHT_1500to2000_2017.dataset = "/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
QCDHT_1500to2000_2017.sigma = 99.11 #pb                                                     

QCDHT_2000toInf_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_2000toInf_2017")
QCDHT_2000toInf_2017.year = 2017
QCDHT_2000toInf_2017.dataset = "/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
QCDHT_2000toInf_2017.sigma = 20.23 #pb                                                     

QCD_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2017")
QCD_2017.year = 2017
QCD_2017.components = [QCDHT_100to200_2017, QCDHT_200to300_2017, QCDHT_300to500_2017, QCDHT_500to700_2017, QCDHT_700to1000_2017, QCDHT_1000to1500_2017, QCDHT_1500to2000_2017, QCDHT_2000toInf_2017]

################################ ZZ ################################
ZZTo2L2Nu_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "ZZTo2L2Nu_2017")
ZZTo2L2Nu_2017.year = 2017
ZZTo2L2Nu_2017.dataset = "/ZZTo2L2Nu_13TeV_powheg_pythia8/" + tag_2017 + "-v1/NANOAODSIM"
ZZTo2L2Nu_2017.sigma = 0.5644 #pb                                                     

ZZJJTo4L_EWK_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "ZZJJTo4L_EWK_2017")
ZZJJTo4L_EWK_2017.year = 2017
ZZJJTo4L_EWK_2017.dataset = "/ZZJJTo4L_EWK_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
ZZJJTo4L_EWK_2017.sigma = 0.0004536 #pb

ZZJJTo4L_QCD_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "ZZJJTo4L_QCD_2017")
ZZJJTo4L_QCD_2017.year = 2017
ZZJJTo4L_QCD_2017.dataset = "/ZZJJTo4L_QCD_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
ZZJJTo4L_QCD_2017.sigma = 0.008348 #pb

GluGluToContinToZZTo2e2nu_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2e2nu_2017")
GluGluToContinToZZTo2e2nu_2017.year = 2017
GluGluToContinToZZTo2e2nu_2017.dataset = "/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2e2nu_2017.sigma = 14.93 #pb

GluGluToContinToZZTo2e2mu_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2e2mu_2017")
GluGluToContinToZZTo2e2mu_2017.year = 2017
GluGluToContinToZZTo2e2mu_2017.dataset = "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2e2mu_2017.sigma = 3.185 #pb

GluGluToContinToZZTo2e2tau_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2e2tau_2017")
GluGluToContinToZZTo2e2tau_2017.year = 2017
GluGluToContinToZZTo2e2tau_2017.dataset = "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2e2tau_2017.sigma = 3.185 #pb

GluGluToContinToZZTo2mu2nu_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2mu2nu_2017")
GluGluToContinToZZTo2mu2nu_2017.year = 2017
GluGluToContinToZZTo2mu2nu_2017.dataset = "/GluGluToContinToZZTo2mu2nu_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2mu2nu_2017.sigma = 14.93 #pb

GluGluToContinToZZTo2mu2tau_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2mu2tau_2017")
GluGluToContinToZZTo2mu2tau_2017.year = 2017
GluGluToContinToZZTo2mu2tau_2017.dataset = "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_2017.sigma = 3.185 #pb

GluGluToContinToZZTo4e_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo4e_2017")
GluGluToContinToZZTo4e_2017.year = 2017
GluGluToContinToZZTo4e_2017.dataset = "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo4e_2017.sigma = 1.404 #pb

GluGluToContinToZZTo4mu_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo4mu_2017")
GluGluToContinToZZTo4mu_2017.year = 2017
GluGluToContinToZZTo4mu_2017.dataset = "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo4mu_2017.sigma = 1.404 #pb

GluGluToContinToZZTo4tau_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo4tau_2017")
GluGluToContinToZZTo4tau_2017.year = 2017
GluGluToContinToZZTo4tau_2017.dataset = "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/" + tag_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo4tau_2017.sigma = 1.404 #pb

GluGluToContinToZZTo4L_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo4L_2017")
GluGluToContinToZZTo4L_2017.year = 2017
GluGluToContinToZZTo4L_2017.dataset = "/GluGluToContinToZZTo4L_13TeV_TuneCP5_madgraphMLM_pythia8/" + tag_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo4L_2017.sigma = 0.7882 #pb

ZZtoLep_2017 = sample(ROOT.kViolet-9, 1, 1001, "ZZ", "ZZtoLep_2017")
ZZtoLep_2017.year = 2017
ZZtoLep_2017.components = [ZZTo2L2Nu_2017, ZZJJTo4L_EWK_2017, ZZJJTo4L_QCD_2017, GluGluToContinToZZTo2e2nu_2017, GluGluToContinToZZTo2e2mu_2017, GluGluToContinToZZTo2e2tau_2017, GluGluToContinToZZTo2mu2nu_2017, GluGluToContinToZZTo2mu2tau_2017, GluGluToContinToZZTo4e_2017, GluGluToContinToZZTo4mu_2017, GluGluToContinToZZTo4tau_2017]

################################ TTbar ################################
TT_Mtt700to1000_2017 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_Mtt700to1000_2017")
TT_Mtt700to1000_2017.sigma = 80.5 #pb
TT_Mtt700to1000_2017.year = 2017
TT_Mtt700to1000_2017.dataset = "/TT_Mtt-700to1000_TuneCP5_PSweights_13TeV-powheg-pythia8/"+tag_2017+"-extv1/NANOAODSIM"
#TT_Mtt700to1000_2017.files = jr.json_reader(path+"/TT_Mtt700to1000_2017.json")

TT_Mtt1000toInf_2017 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_Mtt1000toInf_2017")
TT_Mtt1000toInf_2017.sigma = 21.3 #pb
TT_Mtt1000toInf_2017.year = 2017
TT_Mtt1000toInf_2017.dataset = "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#TT_Mtt1000toInf_2017.files = jr.json_reader(path+"/TT_Mtt1000toInf_2017.json")

TT_Mtt_2017 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_Mtt_2017")
TT_Mtt_2017.year = 2017
TT_Mtt_2017.components = [TT_Mtt700to1000_2017, TT_Mtt1000toInf_2017]

'''
TT_DiLep_2017 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t} DiLep", "TT_DiLep_2017")
TT_DiLep_2017.sigma =  88.287 #pb
TT_DiLep_2017.year = 2017
TT_DiLep_2017.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/"+tag2_2017+"-v1/NANOAODSIM"
'''

TT_SemiLep_2017 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t} SemiLep", "TT_SemiLep2017")
TT_SemiLep_2017.sigma = 365.3
TT_SemiLep_2017.year = 2017
TT_SemiLep_2017.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/"+tag2_2017+"-v1/NANOAODSIM"

TT_Had_2017 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t} had", "TT_Had_2017")
TT_Had_2017.sigma =  377.96 #pb
TT_Had_2017.year = 2017
TT_Had_2017.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/"+tag2_2017+"-v2/NANOAODSIM"

TT_2017 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t} FH+SL", "TT_2017")
TT_2017.year = 2017
TT_2017.components = [TT_SemiLep_2017, TT_Had_2017]#TT_DiLep_2017,

###############################  NEW  ################################
###############################  TVX  ################################
TTGJets_2017 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}#gamma + jets", "TTGJets_2017")
TTGJets_2017.sigma = 4.078
TTGJets_2017.year = 2017
TTGJets_2017.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+tag3_2017+"_ext1-v1/NANOAODSIM"

TTZToQQ_2017 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}Z->q#bar{q}", "TTZToQQ_2017")
TTZToQQ_2017.sigma = 0.5104
TTZToQQ_2017.year = 2017
TTZToQQ_2017.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/"+tag_2017+"_ext1-v1/NANOAODSIM"

TTZToLLNuNu_2017 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}Z to #ell#ell#nu#nu ", "TTZToLLNuNu_2017")
TTZToLLNuNu_2017.sigma = 0.2432
TTZToLLNuNu_2017.year = 2017
TTZToLLNuNu_2017.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/"+tag3_2017+"-v1/NANOAODSIM"

TTWJetsToQQ_2017 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}W + jets to qq ", "TTWJetsToQQ_2017")
TTWJetsToQQ_2017.sigma = 0.4316
TTWJetsToQQ_2017.year = 2017
TTWJetsToQQ_2017.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+tag_2017+"-v1/NANOAODSIM"

TTWJetsToLNu_2017 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}W+jets to #ell#nu ", "TTWJetsToLNu_2017")
TTWJetsToLNu_2017.sigma = 0.2149
TTWJetsToLNu_2017.year = 2017
TTWJetsToLNu_2017.dataset = "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+tag3_2017+"-v1/NANOAODSIM"

tZq_ll_4f_2017 = sample(ROOT.kRed-2, 1, 1001, "tZq to #ell#ell ", "tZq_ll_4f_2017")
tZq_ll_4f_2017.sigma = 0.07358
tZq_ll_4f_2017.year = 2017
tZq_ll_4f_2017.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/"+tag2_2017+"-v1/NANOAODSIM"

TVX_2017 = sample(ROOT.kCyan-7, 1, 1001, "tVX", "TVX_2017")
TVX_2017.year = 2017
TVX_2017.components = [TTGJets_2017, TTZToQQ_2017, TTZToLLNuNu_2017, TTWJetsToQQ_2017, TTWJetsToLNu_2017, tZq_ll_4f_2017]

###############################  NEW     ################################
###############################  VGamma  ################################

ZG_2017 = sample(ROOT.kSpring+7, 1, 1001, "Z #gamma", "ZG_2017")
ZG_2017.sigma = 0.1097
ZG_2017.year = 2017
ZG_2017.dataset = "/LLAJJ_EWK_MLL-50_MJJ-120_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"_ext1-v1/NANOAODSIM"

WG_2017 = sample(ROOT.kSpring+7, 1, 1001, "W #gamma", "WG_2017")
WG_2017.sigma = 0.5439
WG_2017.year = 2017
WG_2017.dataset = "/LNuAJJ_EWK_MJJ-120_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

VG_2017 = sample(ROOT.kSpring+7, 1, 1001, "V#gamma", "VG_2017")
VG_2017.year = 2017
VG_2017.components = [ZG_2017, WG_2017]



###############################      NEW    ################################
###############################  Wrong Sign ################################

WWto2L2Nu_2017 = sample(ROOT.kAzure-9, 1, 1001, "WWto2L2Nu", "WWto2L2Nu_2017")
WWto2L2Nu_2017.sigma = 11.08
WWto2L2Nu_2017.year = 2017
WWto2L2Nu_2017.dataset = "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToENuENu_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToENuENu", "GluGluToWWToENuENu_2017")
GluGluToWWToENuENu_2017.sigma = 45.62
GluGluToWWToENuENu_2017.year = 2017
GluGluToWWToENuENu_2017.dataset = "/GluGluToWWToENEN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToENuMNu2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToENuENu", "GluGluToWWToENuMNu2017")
GluGluToWWToENuMNu2017.sigma = 45.62
GluGluToWWToENuMNu2017.year = 2017
GluGluToWWToENuMNu2017.dataset = "/GluGluToWWToENMN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToENuTNu2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToENuENu", "GluGluToWWToENuTNu2017")
GluGluToWWToENuTNu2017.sigma = 45.62
GluGluToWWToENuTNu2017.year = 2017
GluGluToWWToENuTNu2017.dataset = "/GluGluToWWToENTN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToMNuENu_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToMNuENu", "GluGluToWWToMNuENu_2017")
GluGluToWWToMNuENu_2017.sigma = 45.62
GluGluToWWToMNuENu_2017.year = 2017
GluGluToWWToMNuENu_2017.dataset = "/GluGluToWWToMNEN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToMNuMNu2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToMNuENu", "GluGluToWWToMNuMNu2017")
GluGluToWWToMNuMNu2017.sigma = 45.62
GluGluToWWToMNuMNu2017.year = 2017
GluGluToWWToMNuMNu2017.dataset = "/GluGluToWWToMNMN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToMNuTNu2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToMNuENu", "GluGluToWWToMNuTNu2017")
GluGluToWWToMNuTNu2017.sigma = 45.62
GluGluToWWToMNuTNu2017.year = 2017
GluGluToWWToMNuTNu2017.dataset = "/GluGluToWWToMNTN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToTNuENu_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToTNuENu", "GluGluToWWToTNuENu_2017")
GluGluToWWToTNuENu_2017.sigma = 45.62
GluGluToWWToTNuENu_2017.year = 2017
GluGluToWWToTNuENu_2017.dataset = "/GluGluToWWToTNEN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToTNuMNu2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToTNuENu", "GluGluToWWToTNuMNu2017")
GluGluToWWToTNuMNu2017.sigma = 45.62
GluGluToWWToTNuMNu2017.year = 2017
GluGluToWWToTNuMNu2017.dataset = "/GluGluToWWToTNMN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToTNuTNu2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToTNuENu", "GluGluToWWToTNuTNu2017")
GluGluToWWToTNuTNu2017.sigma = 45.62
GluGluToWWToTNuTNu2017.year = 2017
GluGluToWWToTNuTNu2017.dataset = "/GluGluToWWToTNTN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

TTTo2L2Nu_2017 = sample(ROOT.kAzure-9, 1, 1001, "t#bar{t} DiLep", "TTTo2L2Nu_2017")
TTTo2L2Nu_2017.sigma =  88.287 #pb
TTTo2L2Nu_2017.year = 2017
TTTo2L2Nu_2017.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/"+tag2_2017+"-v1/NANOAODSIM"

STtW_top_2017 = sample(ROOT.kAzure-9, 1, 1001, "single t", "STtW_top_2017")
STtW_top_2017.sigma =  34.91#pb
STtW_top_2017.year = 2017
STtW_top_2017.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v1/NANOAODSIM"

STtW_antitop_2017 = sample(ROOT.kAzure-9, 1, 1001, "single t", "STtW_antitop_2017")
STtW_antitop_2017.sigma =  34.97#pb
STtW_antitop_2017.year = 2017
STtW_antitop_2017.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluHToWWTo2L2Nu_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluHToWWTo2L2Nu", "GluGluHToWWTo2L2Nu_2017")
GluGluHToWWTo2L2Nu_2017.sigma =  28.87#pb
GluGluHToWWTo2L2Nu_2017.year = 2017
GluGluHToWWTo2L2Nu_2017.dataset = "/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluHToZZTo2L2Q_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluHToZZTo2L2Q", "GluGluHToZZTo2L2Q_2017")
GluGluHToZZTo2L2Q_2017.sigma =  28.87#pb
GluGluHToZZTo2L2Q_2017.year = 2017
GluGluHToZZTo2L2Q_2017.dataset = "/GluGluHToZZTo2L2Q_M125_13TeV_powheg2_JHUGenV7011_pythia8/"+tag3_2017+"-v1/NANOAODSIM"

GluGluHToZZTo4L_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluHToZZTo4L", "GluGluHToZZTo4L_2017")
GluGluHToZZTo4L_2017.sigma =  28.87#pb
GluGluHToZZTo4L_2017.year = 2017
GluGluHToZZTo4L_2017.dataset = "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/"+tag_2017+"_ext3-v1/NANOAODSIM"

GluGluHToTauTau_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluHToTauTau", "GluGluHToTauTau_2017")
GluGluHToTauTau_2017.sigma =  30.52#pb
GluGluHToTauTau_2017.year = 2017
GluGluHToTauTau_2017.dataset = "/GluGluHToTauTau_M125_13TeV_powheg_pythia8/"+tag2_2017+"-v1/NANOAODSIM"

VBFHToWWTo2L2Nu_2017 = sample(ROOT.kAzure-9, 1, 1001, "VBFHToWWTo2L2Nu", "VBFHToWWTo2L2Nu_2017")
VBFHToWWTo2L2Nu_2017.sigma =  3.879#pb
VBFHToWWTo2L2Nu_2017.year = 2017
VBFHToWWTo2L2Nu_2017.dataset = "/VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/"+tag_2017+"-v1/NANOAODSIM"

VBFHToTauTau_2017 = sample(ROOT.kAzure-9, 1, 1001, "VBFHToTauTau", "VBFHToTauTau_2017")
VBFHToTauTau_2017.sigma =  3.879#pb
VBFHToTauTau_2017.year = 2017
VBFHToTauTau_2017.dataset = "/VBFHToTauTau_M125_13TeV_amcatnloFXFX_pythia8/"+tag_2017+"-v1/NANOAODSIM"

ttHToNonbb_2017 = sample(ROOT.kAzure-9, 1, 1001, "ttHToNonbb", "ttHToNonbb_2017")
ttHToNonbb_2017.sigma =  0.5269#pb
ttHToNonbb_2017.year = 2017
ttHToNonbb_2017.dataset = "/ttHToNonbb_M125_TuneCP5_PSweights_13TeV-powheg-pythia8/"+tag_2017+"-v1/NANOAODSIM"

VHToNonbb_2017 = sample(ROOT.kAzure-9, 1, 1001, "VHToNonbb", "VHToNonbb_2017")
VHToNonbb_2017.sigma =  2.127#pb
VHToNonbb_2017.year = 2017
VHToNonbb_2017.dataset = "/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/"+tag_2017+"-v1/NANOAODSIM"

WrongSign_2017 = sample(ROOT.kAzure-9, 1, 1001, "Leptonic t#bar{t} + WS", "WrongSign_2017")
WrongSign_2017.year = 2017
WrongSign_2017.components = [WWto2L2Nu_2017, GluGluToWWToENuENu_2017, GluGluToWWToENuMNu2017, 
                            GluGluToWWToENuTNu2017, GluGluToWWToMNuENu_2017, GluGluToWWToMNuMNu2017, 
                            GluGluToWWToMNuTNu2017, GluGluToWWToTNuENu_2017, GluGluToWWToTNuMNu2017, 
                            GluGluToWWToTNuTNu2017, STtW_top_2017, GluGluHToWWTo2L2Nu_2017, 
                            GluGluHToZZTo2L2Q_2017, GluGluHToZZTo4L_2017, GluGluHToTauTau_2017, 
                            VBFHToWWTo2L2Nu_2017, VBFHToTauTau_2017, ttHToNonbb_2017, VHToNonbb_2017]


###############################      NEW    ################################
###############################     Other   ################################


WWTo2L2Nu_DoubleScattering_2017 = sample(ROOT.kOrange-4, 1, 1001, "WWTo2L2Nu_DoubleScattering", "WWTo2L2Nu_DoubleScattering_2017")
WWTo2L2Nu_DoubleScattering_2017.sigma =  0.1703#pb
WWTo2L2Nu_DoubleScattering_2017.year = 2017
WWTo2L2Nu_DoubleScattering_2017.dataset = "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/"+tag_2017+"-v1/NANOAODSIM"

WWW_4F_2017 = sample(ROOT.kOrange-4, 1, 1001, "WWW_4F", "WWW_4F_2017")
WWW_4F_2017.sigma =  0.2086#pb
WWW_4F_2017.year = 2017
WWW_4F_2017.dataset = "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/"+tag3_2017+"-v1/NANOAODSIM"

WWZTo3L1Nu2Q_2017 = sample(ROOT.kOrange-4, 1, 1001, "WWZTo3L1Nu2Q", "WWZTo3L1Nu2Q_2017")
WWZTo3L1Nu2Q_2017.sigma =  0.008039#pb
WWZTo3L1Nu2Q_2017.year = 2017
WWZTo3L1Nu2Q_2017.dataset = "/WWZTo3L1Nu2Q_4f_TuneCP5_13TeV_amcatnlo_pythia8/"+tag_2017+"-v1/NANOAODSIM"


WZZ_2017 = sample(ROOT.kOrange-4, 1, 1001, "WZZ", "WZZ_2017")
WZZ_2017.sigma =  0.05565#pb
WZZ_2017.year = 2017
WZZ_2017.dataset = "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/"+tag3_2017+"-v1/NANOAODSIM"


ZZZ_2017 = sample(ROOT.kOrange-4, 1, 1001, "ZZZ", "ZZZ_2017")
ZZZ_2017.sigma =  0.013989#pb
ZZZ_2017.year = 2017
ZZZ_2017.dataset = "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/"+tag3_2017+"-v1/NANOAODSIM"

WWG_2017 = sample(ROOT.kOrange-4, 1, 1001, "WWG", "WWG_2017")
WWG_2017.sigma =  0.2147#pb
WWG_2017.year = 2017
WWG_2017.dataset = "/WWG_TuneCP5_13TeV-amcatnlo-pythia8/"+tag3_2017+"-v1/NANOAODSIM"

Other_2017 = sample(ROOT.kOrange-4, 1, 1001, "Other", "Other_2017")
Other_2017.year = 2017
Other_2017.components = [WWTo2L2Nu_DoubleScattering_2017, WWW_4F_2017, WWZTo3L1Nu2Q_2017, WZZ_2017, ZZZ_2017, WWG_2017]

OtherWS_2017 = sample(ROOT.kOrange-4, 1, 1001, "Other + Wrong Sign", "OtherWS_2017")
OtherWS_2017.year = 2017
OtherWS_2017.components = [WWTo2L2Nu_DoubleScattering_2017, WWW_4F_2017, WWZTo3L1Nu2Q_2017, WZZ_2017, ZZZ_2017, WWG_2017,
                           WWto2L2Nu_2017, GluGluToWWToENuENu_2017, GluGluToWWToENuMNu2017, 
                           GluGluToWWToENuTNu2017, GluGluToWWToMNuENu_2017, GluGluToWWToMNuMNu2017, 
                           GluGluToWWToMNuTNu2017, GluGluToWWToTNuENu_2017, GluGluToWWToTNuMNu2017, 
                           GluGluToWWToTNuTNu2017, STtW_top_2017, GluGluHToWWTo2L2Nu_2017, 
                           GluGluHToZZTo2L2Q_2017, GluGluHToZZTo4L_2017, GluGluHToTauTau_2017, 
                           VBFHToWWTo2L2Nu_2017, VBFHToTauTau_2017, ttHToNonbb_2017, VHToNonbb_2017]
################################ WJets ################################
WJetsHT70to100_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT70to100_2017")
WJetsHT70to100_2017.sigma = 1353 * 1.21 #pb
WJetsHT70to100_2017.year = 2017
WJetsHT70to100_2017.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

WJetsHT100to200_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT100to200_2017")
WJetsHT100to200_2017.sigma = 1345 * 1.21 #pb
WJetsHT100to200_2017.year = 2017
WJetsHT100to200_2017.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

WJetsHT200to400_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT200to400_2017")
WJetsHT200to400_2017.sigma = 359.7 * 1.21 #pb
WJetsHT200to400_2017.year = 2017
WJetsHT200to400_2017.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT200to400_2017.files = jr.json_reader(path+"/WJets_HT200To400_2017.json")

WJetsHT400to600_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT400to600_2017")
WJetsHT400to600_2017.sigma = 48.91 * 1.21 #pb
WJetsHT400to600_2017.year = 2017
WJetsHT400to600_2017.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT400to600_2017.files = jr.json_reader(path+"/WJets_HT400To600_2017.json")

WJetsHT600to800_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT600to800_2017")
WJetsHT600to800_2017.sigma = 12.05 * 1.21 #pb
WJetsHT600to800_2017.year = 2017
WJetsHT600to800_2017.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT600to800_2017.files = jr.json_reader(path+"/WJets_HT600To800_2017.json")

WJetsHT800to1200_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT800to1200_2017")
WJetsHT800to1200_2017.sigma = 5.501 * 1.21 #pb
WJetsHT800to1200_2017.year = 2017
WJetsHT800to1200_2017.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT800to1200_2017.files = jr.json_reader(path+"/WJets_HT800To1200_2017.json")

WJetsHT1200to2500_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT1200to2500_2017")
WJetsHT1200to2500_2017.sigma = 1.329 * 1.21 #pb
WJetsHT1200to2500_2017.year = 2017
WJetsHT1200to2500_2017.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT1200to2500_2017.files = jr.json_reader(path+"/WJets_HT1200To2500_2017.json")

WJetsHT2500toInf_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT2500toInf_2017")
WJetsHT2500toInf_2017.sigma = 0.03216 * 1.21 #pb
WJetsHT2500toInf_2017.year = 2017
WJetsHT2500toInf_2017.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT2500toInf_2017.files = jr.json_reader(path+"/WJets_HT2500ToInf_2017.json")

WJets_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets_2017")
WJets_2017.year = 2017
WJets_2017.components = [WJetsHT70to100_2017, WJetsHT100to200_2017, WJetsHT200to400_2017, WJetsHT400to600_2017, WJetsHT600to800_2017, WJetsHT800to1200_2017, WJetsHT1200to2500_2017, WJetsHT2500toInf_2017]

WJetsHT70to100_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT70to100_Fake_2017")
WJetsHT70to100_Fake_2017.sigma = 1353 * 1.21 #pb
WJetsHT70to100_Fake_2017.year = 2017
WJetsHT70to100_Fake_2017.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

WJetsHT100to200_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT100to200_Fake_2017")
WJetsHT100to200_Fake_2017.sigma = 1345 * 1.21 #pb
WJetsHT100to200_Fake_2017.year = 2017
WJetsHT100to200_Fake_2017.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

WJetsHT200to400_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT200to400_Fake_2017")
WJetsHT200to400_Fake_2017.sigma = 359.7 * 1.21 #pb
WJetsHT200to400_Fake_2017.year = 2017
WJetsHT200to400_Fake_2017.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT200to400_Fake_2017.files = jr.json_reader(path+"/WJets_HT200To400_2017.json")

WJetsHT400to600_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT400to600_Fake_2017")
WJetsHT400to600_Fake_2017.sigma = 48.91 * 1.21 #pb
WJetsHT400to600_Fake_2017.year = 2017
WJetsHT400to600_Fake_2017.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT400to600_Fake_2017.files = jr.json_reader(path+"/WJets_HT400To600_2017.json")

WJetsHT600to800_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT600to800_Fake_2017")
WJetsHT600to800_Fake_2017.sigma = 12.05 * 1.21 #pb
WJetsHT600to800_Fake_2017.year = 2017
WJetsHT600to800_Fake_2017.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT600to800_Fake_2017.files = jr.json_reader(path+"/WJets_HT600To800_2017.json")

WJetsHT800to1200_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT800to1200_Fake_2017")
WJetsHT800to1200_Fake_2017.sigma = 5.501 * 1.21 #pb
WJetsHT800to1200_Fake_2017.year = 2017
WJetsHT800to1200_Fake_2017.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT800to1200_Fake_2017.files = jr.json_reader(path+"/WJets_HT800To1200_2017.json")

WJetsHT1200to2500_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT1200to2500_Fake_2017")
WJetsHT1200to2500_Fake_2017.sigma = 1.329 * 1.21 #pb
WJetsHT1200to2500_Fake_2017.year = 2017
WJetsHT1200to2500_Fake_2017.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT1200to2500_Fake_2017.files = jr.json_reader(path+"/WJets_HT1200To2500_2017.json")

WJetsHT2500toInf_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT2500toInf_Fake_2017")
WJetsHT2500toInf_Fake_2017.sigma = 0.03216 * 1.21 #pb
WJetsHT2500toInf_Fake_2017.year = 2017
WJetsHT2500toInf_Fake_2017.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT2500toInf_Fake_2017.files = jr.json_reader(path+"/WJets_HT2500ToInf_2017.json")

WJets_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets_Fake_2017")
WJets_Fake_2017.year = 2017
WJets_Fake_2017.components = [WJetsHT70to100_Fake_2017, WJetsHT100to200_Fake_2017, WJetsHT200to400_Fake_2017, WJetsHT400to600_Fake_2017, WJetsHT600to800_Fake_2017, WJetsHT800to1200_Fake_2017, WJetsHT1200to2500_Fake_2017, WJetsHT2500toInf_Fake_2017]


################################ WZ ################################
WZ_2017 = sample(ROOT.kYellow-7, 1, 1001, "WZ", "WZ_2017")
WZ_2017.sigma = 47.13
WZ_2017.year = 2017
WZ_2017.dataset = "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_PU2017_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"

################################ DrellYan ################################
DY1JetsToLL_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 1 Jet", "DY1JetsToLL_2017")
DY1JetsToLL_2017.sigma = 1012.0
DY1JetsToLL_2017.year = 2017
DY1JetsToLL_2017.dataset = "/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag2_2017 + "-v1/NANOAODSIM"

DY2JetsToLL_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 2 Jets", "DY2JetsToLL_2017")
DY2JetsToLL_2017.sigma = 330.4
DY2JetsToLL_2017.year = 2017
DY2JetsToLL_2017.dataset = "/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag2_2017 + "_ext1-v1/NANOAODSIM"

DY3JetsToLL_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 3 Jets", "DY3JetsToLL_2017")
DY3JetsToLL_2017.sigma = 101.8
DY3JetsToLL_2017.year = 2017
DY3JetsToLL_2017.dataset = "/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

DY4JetsToLL_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 4+ Jets", "DY4JetsToLL_2017")
DY4JetsToLL_2017.sigma = 54.80
DY4JetsToLL_2017.year = 2017
DY4JetsToLL_2017.dataset = "/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag1_2017 + "-v1/NANOAODSIM"

DYJetsToLLM5to50_2017 = sample(ROOT.kCyan, 1, 1001, "DY M5to50", "DYJetsToLLM5to50_2017")
DYJetsToLLM5to50_2017.sigma = 81880.0
DYJetsToLLM5to50_2017.year = 2017
DYJetsToLLM5to50_2017.dataset = "/DYJetsToLL_M-5to50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

DYJetsToLLM50_2017 = sample(ROOT.kCyan, 1, 1001, "DY M50", "DYJetsToLLM50_2017")
DYJetsToLLM50_2017.sigma = 6529.0
DYJetsToLLM50_2017.year = 2017
DYJetsToLLM50_2017.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/" + tag2_2017 + "_ext1-v1/NANOAODSIM"

DYJetsToLL_2017 = sample(ROOT.kCyan, 1, 1001, "DY + Jets", "DYJetsToLL_2017")
DYJetsToLL_2017.year = 2017
DYJetsToLL_2017.components = [DY1JetsToLL_2017, DY2JetsToLL_2017, DY3JetsToLL_2017, DY4JetsToLL_2017, DYJetsToLLM5to50_2017]

DY1JetsToLL_Fake_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 1 Jet", "DY1JetsToLL_Fake_2017")
DY1JetsToLL_Fake_2017.sigma = 1012.0
DY1JetsToLL_Fake_2017.year = 2017
DY1JetsToLL_Fake_2017.dataset = "/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag2_2017 + "-v1/NANOAODSIM"

DY2JetsToLL_Fake_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 2 Jets", "DY2JetsToLL_Fake_2017")
DY2JetsToLL_Fake_2017.sigma = 330.4
DY2JetsToLL_Fake_2017.year = 2017
DY2JetsToLL_Fake_2017.dataset = "/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag2_2017 + "_ext1-v1/NANOAODSIM"

DY3JetsToLL_Fake_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 3 Jets", "DY3JetsToLL_Fake_2017")
DY3JetsToLL_Fake_2017.sigma = 101.8
DY3JetsToLL_Fake_2017.year = 2017
DY3JetsToLL_Fake_2017.dataset = "/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

DY4JetsToLL_Fake_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 4+ Jets", "DY4JetsToLL_Fake_2017")
DY4JetsToLL_Fake_2017.sigma = 54.80
DY4JetsToLL_Fake_2017.year = 2017
DY4JetsToLL_Fake_2017.dataset = "/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag1_2017 + "-v1/NANOAODSIM"

DYJetsToLL_Fake_2017 = sample(ROOT.kCyan, 1, 1001, "DY + Jets", "DYJetsToLL_Fake_2017")
DYJetsToLL_Fake_2017.year = 2017
DYJetsToLL_Fake_2017.components = [DY1JetsToLL_Fake_2017, DY2JetsToLL_Fake_2017, DY3JetsToLL_Fake_2017, DY4JetsToLL_Fake_2017]

DYJetsToLL_Old_2017 = sample(ROOT.kCyan, 1, 1001, "DY + Jets", "DYJetsToLL_2017")
DYJetsToLL_Old_2017.year = 2017
DYJetsToLL_Old_2017.components = [DY1JetsToLL_2017, DY2JetsToLL_2017, DY3JetsToLL_2017, DY4JetsToLL_2017]

DYJetsM_2017 = sample(ROOT.kCyan, 1, 1001, "DY + Jets (M)", "DYJetsM_2017")
DYJetsM_2017.year = 2017
DYJetsM_2017.components = [DYJetsToLLM5to50_2017, DYJetsToLLM50_2017]

################################ ssWW EWK ################################
WpWpJJ_EWK_2017 = sample(ROOT.kRed, 1, 1001, "EW ssWW", "WpWpJJ_EWK_2017")
WpWpJJ_EWK_2017.sigma = 0.02064
WpWpJJ_EWK_2017.year = 2017
WpWpJJ_EWK_2017.dataset = "/WpWpJJ_EWK_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

WpWpJJ_QCD_2017 = sample(ROOT.kPink+1, 1, 1001, "QCD ssWW", "WpWpJJ_QCD_2017")
WpWpJJ_QCD_2017.sigma = 0.01538
WpWpJJ_QCD_2017.year = 2017
WpWpJJ_QCD_2017.dataset = "/WpWpJJ_QCD_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_LL_SM_2017 = sample(ROOT.kBlack, 1, 1001, "VBS ssWW LL", "VBS_SSWW_LL_SM_2017")
VBS_SSWW_LL_SM_2017.sigma = 0.002014
VBS_SSWW_LL_SM_2017.year = 2017
VBS_SSWW_LL_SM_2017.dataset = "/VBS_SSWW_LL_polarization_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_TL_SM_2017 = sample(ROOT.kBlack, 1, 1001, "VBS ssWW TL", "VBS_SSWW_TL_SM_2017")
VBS_SSWW_TL_SM_2017.sigma = 0.01036
VBS_SSWW_TL_SM_2017.year = 2017
VBS_SSWW_TL_SM_2017.dataset = "/VBS_SSWW_TL_polarization_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_TT_SM_2017 = sample(ROOT.kBlack, 1, 1001, "VBS ssWW TT", "VBS_SSWW_TT_SM_2017")
VBS_SSWW_TT_SM_2017.sigma = 0.01595
VBS_SSWW_TT_SM_2017.year = 2017
VBS_SSWW_TT_SM_2017.dataset = "/VBS_SSWW_TT_polarization_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_SM_2017 = sample(ROOT.kRed+2, 1, 1001, "VBS ssWW", "VBS_SSWW_SM_2017")
VBS_SSWW_SM_2017.year = 2017
VBS_SSWW_SM_2017.components = [VBS_SSWW_LL_SM_2017, VBS_SSWW_TL_SM_2017, VBS_SSWW_TT_SM_2017]

VBS_SSWW_cHW_BSM_2017 = sample(ROOT.kGreen+3, 1, 1001, "VBS ssWW c_{HW} (only BSM)", "VBS_SSWW_cHW_BSM_2017")
VBS_SSWW_cHW_BSM_2017.sigma = 0.002014
VBS_SSWW_cHW_BSM_2017.year = 2017
VBS_SSWW_cHW_BSM_2017.dataset = "/VBS_SSWW_cHW_BSM_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_cHW_INT_2017 = sample(ROOT.kGreen+3, 1, 1001, "VBS ssWW c_{HW} (only INT)", "VBS_SSWW_cHW_INT_2017")
VBS_SSWW_cHW_INT_2017.sigma = 0.002014
VBS_SSWW_cHW_INT_2017.year = 2017
VBS_SSWW_cHW_INT_2017.dataset = "/VBS_SSWW_cHW_INT_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_cHW_2017 = sample(ROOT.kMagenta+2, 1, 1001, "VBS ssWW c_{HW} (BSM+INT)", "VBS_SSWW_cHW_2017")
VBS_SSWW_cHW_2017.year = 2017
VBS_SSWW_cHW_2017.components = [VBS_SSWW_cHW_BSM_2017]#, VBS_SSWW_cHW_INT_2017]

VBS_SSWW_cW_BSM_2017 = sample(ROOT.kMagenta+3, 1, 1001, "VBS ssWW c_{W} (only BSM)", "VBS_SSWW_cW_BSM_2017")
VBS_SSWW_cW_BSM_2017.sigma = 0.002014
VBS_SSWW_cW_BSM_2017.year = 2017
VBS_SSWW_cW_BSM_2017.dataset = "/VBS_SSWW_cW_BSM_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_cW_INT_2017 = sample(ROOT.kMagenta+3, 1, 1001, "VBS ssWW c_{W} (only INT)", "VBS_SSWW_cW_INT_2017")
VBS_SSWW_cW_INT_2017.sigma = 0.002014
VBS_SSWW_cW_INT_2017.year = 2017
VBS_SSWW_cW_INT_2017.dataset = "/VBS_SSWW_cW_INT_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_cW_2017 = sample(ROOT.kMagenta+1, 1, 1001, "VBS ssWW c_{W} (BSM+INT)", "VBS_SSWW_cW_2017")
VBS_SSWW_cW_2017.year = 2017
VBS_SSWW_cW_2017.components = [VBS_SSWW_cW_BSM_2017]#, VBS_SSWW_cW_INT_2017]

VBS_SSWW_cW_cHW_2017 = sample(ROOT.kAzure+3, 1, 1001, "VBS ssWW c_{HW}+c_{W}", "VBS_SSWW_cW_cHW_2017")
VBS_SSWW_cW_cHW_2017.sigma = 0.002014
VBS_SSWW_cW_cHW_2017.year = 2017
VBS_SSWW_cW_cHW_2017.dataset = "/VBS_SSWW_cW_cHW_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_BSM_INT_2017 = sample(ROOT.kGreen+3, 1, 1001, "VBS ssWW (BSM)", "VBS_SSWW_BSM_INT_2017")
VBS_SSWW_BSM_INT_2017.year = 2017
VBS_SSWW_BSM_INT_2017.components = [VBS_SSWW_cHW_BSM_2017, VBS_SSWW_cW_BSM_2017, VBS_SSWW_cW_cHW_2017]

VBS_SSWW_BSM_SM_2017 = sample(ROOT.kGreen+2, 1, 1001, "VBS ssWW (BSM+SM+INT)", "VBS_SSWW_BSM_SM_2017")
VBS_SSWW_BSM_SM_2017.year = 2017
VBS_SSWW_BSM_SM_2017.components = [VBS_SSWW_cHW_BSM_2017, VBS_SSWW_cHW_INT_2017, VBS_SSWW_cW_BSM_2017, VBS_SSWW_cW_INT_2017, VBS_SSWW_cW_cHW_2017, VBS_SSWW_LL_SM_2017, VBS_SSWW_TL_SM_2017, VBS_SSWW_TT_SM_2017]

DHiggsToWW_2017 = sample(ROOT.kAzure, 1, 1001, "m_{H} = 200 m_{X} = 150 m_{Z'} = 2e3", "DHiggsToWW_2017")
DHiggsToWW_2017.sigma = 0.0002014
DHiggsToWW_2017.year = 2017
DHiggsToWW_2017.dataset = "/DarkHiggs_MonoHs_HsToWWTo2l2nu_mhs_200_mx_150_mZp_2000_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v2/NANOAODSIM"

###################################################################################################################################################################
############################################################                                           ############################################################
############################################################                    2018                   ############################################################
############################################################                                           ############################################################
###################################################################################################################################################################

################################ TTbar ################################
TT_Mtt700to1000_2018 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_Mtt700to1000_2018")
TT_Mtt700to1000_2018.sigma = 80.5 #pb
TT_Mtt700to1000_2018.year = 2018
TT_Mtt700to1000_2018.dataset = "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#TT_Mtt700to1000_2018.files = jr.json_reader(path+"/TT_Mtt700to1000_2018.json")

TT_Mtt1000toInf_2018 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_Mtt1000toInf_2018")
TT_Mtt1000toInf_2018.sigma = 21.3 #pb
TT_Mtt1000toInf_2018.year = 2018
TT_Mtt1000toInf_2018.dataset = "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#TT_Mtt1000toInf_2018.files = jr.json_reader(path+"/TT_Mtt1000toInf_2018.json")

TT_Mtt_2018 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_Mtt_2018")
TT_Mtt_2018.year = 2018
TT_Mtt_2018.components = [TT_Mtt700to1000_2018, TT_Mtt1000toInf_2018]

TT_Mtt_2018 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt_2018")
TT_Mtt_2018.year = 2018
TT_Mtt_2018.components = [TT_Mtt700to1000_2018, TT_Mtt1000toInf_2018]

TT_DiLep_2018 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_DiLep_2018")
TT_DiLep_2018.sigma =  88.287 #pb
TT_DiLep_2018.year = 2018
TT_DiLep_2018.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/NANOAODSIM"

TT_SemiLep_2018 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_SemiLep_2018")
TT_SemiLep_2018.sigma = 365.3 #pb
TT_SemiLep_2018.year = 2018
TT_SemiLep_2018.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

TT_Had_2018 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t} had", "TT_Had_2018")
TT_Had_2018.sigma =  377.96 #pb
TT_Had_2018.year = 2018
TT_Had_2018.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/NANOAODSIM"

TT_2018 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_2018")
TT_2018.year = 2018
TT_2018.components = [TT_DiLep_2018, TT_SemiLep_2018, TT_Had_2018]

################################ WJets ################################
WJetsHT70to100_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT70to100_2018")
WJetsHT70to100_2018.sigma = 1353 * 1.21 #pb
WJetsHT70to100_2018.year = 2018
WJetsHT70to100_2018.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

WJetsHT100to200_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT100to200_2018")
WJetsHT100to200_2018.sigma = 1345 * 1.21 #pb
WJetsHT100to200_2018.year = 2018
WJetsHT100to200_2018.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

WJetsHT200to400_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT200to400_2018")
WJetsHT200to400_2018.sigma = 359.7 * 1.21 #pb
WJetsHT200to400_2018.year = 2018
WJetsHT200to400_2018.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT200to400_2018.files = jr.json_reader(path+"/WJets_HT200To400_2018.json")

WJetsHT400to600_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT400to600_2018")
WJetsHT400to600_2018.sigma = 48.91 * 1.21 #pb
WJetsHT400to600_2018.year = 2018
WJetsHT400to600_2018.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT400to600_2018.files = jr.json_reader(path+"/WJets_HT400To600_2018.json")

WJetsHT600to800_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT600to800_2018")
WJetsHT600to800_2018.sigma = 12.05 * 1.21 #pb
WJetsHT600to800_2018.year = 2018
WJetsHT600to800_2018.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT600to800_2018.files = jr.json_reader(path+"/WJets_HT600To800_2018.json")

WJetsHT800to1200_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT800to1200_2018")
WJetsHT800to1200_2018.sigma = 5.501 * 1.21 #pb
WJetsHT800to1200_2018.year = 2018
WJetsHT800to1200_2018.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT800to1200_2018.files = jr.json_reader(path+"/WJets_HT800To1200_2018.json")

WJetsHT1200to2500_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT1200to2500_2018")
WJetsHT1200to2500_2018.sigma = 1.329 * 1.21 #pb
WJetsHT1200to2500_2018.year = 2018
WJetsHT1200to2500_2018.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT1200to2500_2018.files = jr.json_reader(path+"/WJets_HT1200To2500_2018.json")

WJetsHT2500toInf_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT2500toInf_2018")
WJetsHT2500toInf_2018.sigma = 0.03216 * 1.2 #pb
WJetsHT2500toInf_2018.year = 2018
WJetsHT2500toInf_2018.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT2500toInf_2018.files = jr.json_reader(path+"/WJets_HT2500ToInf_2018.json")

WJets_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets_2018")
WJets_2018.year = 2018
WJets_2018.components = [WJetsHT70to100_2018, WJetsHT100to200_2018, WJetsHT200to400_2018, WJetsHT400to600_2018, WJetsHT600to800_2018, WJetsHT800to1200_2018, WJetsHT1200to2500_2018, WJetsHT2500toInf_2018]

################################ WZ ################################
WZ_2018 = sample(ROOT.kYellow-7, 1, 1001, "WZ", "WZ_2018")
WZ_2018.sigma = 47.13
WZ_2018.year = 2018
WZ_2018.dataset = "/WZ_TuneCP5_13TeV-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

################################ DrellYan ################################
DY1JetsToLL_2018 = sample(ROOT.kAzure+6, 1, 1001, "DY + 1 Jet", "DY1JetsToLL_2018")
DY1JetsToLL_2018.sigma = 1012.0
DY1JetsToLL_2018.year = 2018
DY1JetsToLL_2018.dataset = "/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

DY2JetsToLL_2018 = sample(ROOT.kAzure+6, 1, 1001, "DY + 2 Jets", "DY2JetsToLL_2018")
DY2JetsToLL_2018.sigma = 330.4
DY2JetsToLL_2018.year = 2018
DY2JetsToLL_2018.dataset = "/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

DY3JetsToLL_2018 = sample(ROOT.kAzure+6, 1, 1001, "DY + 3 Jets", "DY3JetsToLL_2018")
DY3JetsToLL_2018.sigma = 101.8
DY3JetsToLL_2018.year = 2018
DY3JetsToLL_2018.dataset = "/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

DY4JetsToLL_2018 = sample(ROOT.kAzure+6, 1, 1001, "DY + 4+ Jets", "DY4JetsToLL_2018")
DY4JetsToLL_2018.sigma = 54.80
DY4JetsToLL_2018.year = 2018
DY4JetsToLL_2018.dataset = "/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

DYJetsToLL_2018 = sample(ROOT.kAzure+6, 1, 1001, "DY + Jets", "DYJetsToLL_2018")
DYJetsToLL_2018.year = 2018
DYJetsToLL_2018.components = [DY1JetsToLL_2018, DY2JetsToLL_2018, DY3JetsToLL_2018, DY4JetsToLL_2018]

################################ ssWW EWK ################################
WpWpJJ_EWK_2018 = sample(ROOT.kBlue, 1, 1001, "EW ssWW", "WpWpJJ_EWK_2018")
WpWpJJ_EWK_2018.sigma = 0.02064
WpWpJJ_EWK_2018.year = 2018
WpWpJJ_EWK_2018.dataset = "/WpWpJJ_EWK_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

WpWpJJ_QCD_2018 = sample(ROOT.kBlue, 1, 1001, "QCD ssWW", "WpWpJJ_QCD_2018")
WpWpJJ_QCD_2018.sigma = 0.01538
WpWpJJ_QCD_2018.year = 2018
WpWpJJ_QCD_2018.dataset = "/WpWpJJ_QCD_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"


####################################################### Data #####################################################################################
#tag_data = 'Nano25Oct2019'
tag_data = '02Apr2020'

DataMuB_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB_2016")
DataMuB_2016.runP = 'B'
DataMuB_2016.year = 2016
DataMuB_2016.dataset = '/SingleMuon/Run2016B-'+tag_data + '_ver2-v1/NANOAOD'
DataMuC_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuC_2016")
DataMuC_2016.runP = 'C'
DataMuC_2016.year = 2016
DataMuC_2016.dataset = '/SingleMuon/Run2016C-'+tag_data + '-v1/NANOAOD'
DataMuD_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuD_2016")
DataMuD_2016.runP = 'D'
DataMuD_2016.year = 2016
DataMuD_2016.dataset = '/SingleMuon/Run2016D-'+tag_data + '-v1/NANOAOD'
DataMuE_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuE_2016")
DataMuE_2016.runP = 'E'
DataMuE_2016.year = 2016
DataMuE_2016.dataset = '/SingleMuon/Run2016E-'+tag_data + '-v1/NANOAOD'
DataMuF_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuF_2016")
DataMuF_2016.runP = 'F'
DataMuF_2016.year = 2016
DataMuF_2016.dataset = '/SingleMuon/Run2016F-'+tag_data + '-v1/NANOAOD'
DataMuG_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuG_2016")
DataMuG_2016.runP = 'G'
DataMuG_2016.year = 2016
DataMuG_2016.dataset = '/SingleMuon/Run2016G-'+tag_data + '-v1/NANOAOD'
DataMuH_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuH_2016")
DataMuH_2016.runP = 'H'
DataMuH_2016.year = 2016
DataMuH_2016.dataset = '/SingleMuon/Run2016H-'+tag_data + '-v1/NANOAOD'
DataMu_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_2016")
DataMu_2016.year = 2016
DataMu_2016.components = [DataMuB_2016, DataMuC_2016, DataMuD_2016, DataMuE_2016, DataMuF_2016, DataMuG_2016, DataMuH_2016]

DataEleB_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB_2016")
DataEleB_2016.runP = 'B'
DataEleB_2016.year = 2016
DataEleB_2016.dataset = '/SingleElectron/Run2016B-'+tag_data + '_ver2-v1/NANOAOD'
DataEleC_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleC_2016")
DataEleC_2016.runP = 'C'
DataEleC_2016.year = 2016
DataEleC_2016.dataset = '/SingleElectron/Run2016C-'+tag_data + '-v1/NANOAOD'
DataEleD_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleD_2016")
DataEleD_2016.runP = 'D'
DataEleD_2016.year = 2016
DataEleD_2016.dataset = '/SingleElectron/Run2016D-'+tag_data + '-v1/NANOAOD'
DataEleE_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleE_2016")
DataEleE_2016.runP = 'E'
DataEleE_2016.year = 2016
DataEleE_2016.dataset = '/SingleElectron/Run2016E-'+tag_data + '-v1/NANOAOD'
DataEleF_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleF_2016")
DataEleF_2016.runP = 'F'
DataEleF_2016.year = 2016
DataEleF_2016.dataset = '/SingleElectron/Run2016F-'+tag_data + '-v1/NANOAOD'
DataEleG_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleG_2016")
DataEleG_2016.runP = 'G'
DataEleG_2016.year = 2016
DataEleG_2016.dataset = '/SingleElectron/Run2016G-'+tag_data + '-v1/NANOAOD'
DataEleH_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleH_2016")
DataEleH_2016.runP = 'H'
DataEleH_2016.year = 2016
DataEleH_2016.dataset = '/SingleElectron/Run2016H-'+tag_data + '-v1/NANOAOD'
DataEle_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_2016")
DataEle_2016.year = 2016
DataEle_2016.components = [DataEleB_2016, DataEleC_2016, DataEleD_2016, DataEleE_2016, DataEleF_2016, DataEleG_2016, DataEleH_2016]

DataHTB_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB_2016")
DataHTB_2016.runP = 'B'
DataHTB_2016.year = 2016
DataHTB_2016.dataset = '/JetHT/Run2016B-'+tag_data + '_ver2-v1/NANOAOD'
DataHTC_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTC_2016")
DataHTC_2016.runP = 'C'
DataHTC_2016.year = 2016
DataHTC_2016.dataset = '/JetHT/Run2016C-'+tag_data + '-v1/NANOAOD'
DataHTD_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTD_2016")
DataHTD_2016.runP = 'D'
DataHTD_2016.year = 2016
DataHTD_2016.dataset = '/JetHT/Run2016D-'+tag_data + '-v1/NANOAOD'
DataHTE_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTE_2016")
DataHTE_2016.runP = 'E'
DataHTE_2016.year = 2016
DataHTE_2016.dataset = '/JetHT/Run2016E-'+tag_data + '-v1/NANOAOD'
DataHTF_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTF_2016")
DataHTF_2016.runP = 'F'
DataHTF_2016.year = 2016
DataHTF_2016.dataset = '/JetHT/Run2016F-'+tag_data + '-v1/NANOAOD'
DataHTG_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTG_2016")
DataHTG_2016.runP = 'G'
DataHTG_2016.year = 2016
DataHTG_2016.dataset = '/JetHT/Run2016G-'+tag_data + '-v1/NANOAOD'
DataHTH_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTH_2016")
DataHTH_2016.runP = 'H'
DataHTH_2016.year = 2016
DataHTH_2016.dataset = '/JetHT/Run2016H-'+tag_data + '-v1/NANOAOD'
DataHT_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_2016")
DataHT_2016.year = 2016
DataHT_2016.components = [DataHTB_2016, DataHTC_2016, DataHTD_2016, DataHTE_2016, DataHTF_2016, DataHTG_2016, DataHTH_2016]

DataTauB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTauB_2017")
DataTauB_2017.runP = 'B'
DataTauB_2017.year = 2017
DataTauB_2017.dataset = '/Tau/Run2017B-'+tag_data + '-v1/NANOAOD'
DataTauC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTauC_2017")
DataTauC_2017.runP = 'C'
DataTauC_2017.year = 2017
DataTauC_2017.dataset = '/Tau/Run2017C-'+tag_data + '-v1/NANOAOD'
DataTauD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTauD_2017")
DataTauD_2017.runP = 'D'
DataTauD_2017.year = 2017
DataTauD_2017.dataset = '/Tau/Run2017D-'+tag_data + '-v1/NANOAOD'
DataTauE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTauE_2017")
DataTauE_2017.runP = 'E'
DataTauE_2017.year = 2017
DataTauE_2017.dataset = '/Tau/Run2017E-'+tag_data + '-v1/NANOAOD'
DataTauF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTauF_2017")
DataTauF_2017.runP = 'F'
DataTauF_2017.year = 2017
DataTauF_2017.dataset = '/Tau/Run2017F-'+tag_data + '-v1/NANOAOD'
DataTau_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTau_2017")
DataTau_2017.year = 2017
DataTau_2017.components = [DataTauB_2017, DataTauC_2017, DataTauD_2017, DataTauE_2017, DataTauF_2017]
DataTauFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTauFake_2017")
DataTauFake_2017.year = 2017
DataTauFake_2017.components = [DataTauB_2017, DataTauC_2017, DataTauD_2017, DataTauE_2017, DataTauF_2017]

DataMuB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB_2017")
DataMuB_2017.runP = 'B'
DataMuB_2017.year = 2017
DataMuB_2017.dataset = '/SingleMuon/Run2017B-'+tag_data + '-v1/NANOAOD'
DataMuC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuC_2017")
DataMuC_2017.runP = 'C'
DataMuC_2017.year = 2017
DataMuC_2017.dataset = '/SingleMuon/Run2017C-'+tag_data + '-v1/NANOAOD'
DataMuD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuD_2017")
DataMuD_2017.runP = 'D'
DataMuD_2017.year = 2017
DataMuD_2017.dataset = '/SingleMuon/Run2017D-'+tag_data + '-v1/NANOAOD'
DataMuE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuE_2017")
DataMuE_2017.runP = 'E'
DataMuE_2017.year = 2017
DataMuE_2017.dataset = '/SingleMuon/Run2017E-'+tag_data + '-v1/NANOAOD'
DataMuF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuF_2017")
DataMuF_2017.runP = 'F'
DataMuF_2017.year = 2017
DataMuF_2017.dataset = '/SingleMuon/Run2017F-'+tag_data + '-v1/NANOAOD'
DataMu_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_2017")
DataMu_2017.year = 2017
DataMu_2017.components = [DataMuB_2017, DataMuC_2017, DataMuD_2017, DataMuE_2017, DataMuF_2017]
DataMuFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuFake_2017")
DataMuFake_2017.year = 2017
DataMuFake_2017.components = [DataMuC_2017, DataMuD_2017, DataMuE_2017, DataMuF_2017]

DataEleB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB_2017")
DataEleB_2017.runP = 'B'
DataEleB_2017.year = 2017
DataEleB_2017.dataset = '/SingleElectron/Run2017B-'+tag_data + '-v1/NANOAOD'
DataEleC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleC_2017")
DataEleC_2017.runP = 'C'
DataEleC_2017.year = 2017
DataEleC_2017.dataset = '/SingleElectron/Run2017C-'+tag_data + '-v1/NANOAOD'
DataEleD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleD_2017")
DataEleD_2017.runP = 'D'
DataEleD_2017.year = 2017
DataEleD_2017.dataset = '/SingleElectron/Run2017D-'+tag_data + '-v1/NANOAOD'
DataEleE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleE_2017")
DataEleE_2017.runP = 'E'
DataEleE_2017.year = 2017
DataEleE_2017.dataset = '/SingleElectron/Run2017E-'+tag_data + '-v1/NANOAOD'
DataEleF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleF_2017")
DataEleF_2017.runP = 'F'
DataEleF_2017.year = 2017
DataEleF_2017.dataset = '/SingleElectron/Run2017F-'+tag_data + '-v1/NANOAOD'
DataEle_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_2017")
DataEle_2017.year = 2017
DataEle_2017.components = [DataEleB_2017, DataEleC_2017, DataEleD_2017, DataEleE_2017, DataEleF_2017]

DataEleFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleFake_2017")
DataEleFake_2017.year = 2017
DataEleFake_2017.components = [DataEleC_2017, DataEleD_2017, DataEleE_2017, DataEleF_2017]


SampleEleFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleFake_2017")
SampleEleFake_2017.year = 2017
SampleEleFake_2017.components = [DataEleC_2017, DataEleD_2017, DataEleE_2017, DataEleF_2017, WJetsHT70to100_2017, WJetsHT100to200_2017, WJetsHT200to400_2017, WJetsHT400to600_2017, WJetsHT600to800_2017, WJetsHT800to1200_2017, WJetsHT1200to2500_2017, WJetsHT2500toInf_2017, DY1JetsToLL_2017, DY2JetsToLL_2017, DY3JetsToLL_2017, DY4JetsToLL_2017, DYJetsToLLM5to50_2017]
SampleMuFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleFake_2017")
SampleMuFake_2017.year = 2017
SampleMuFake_2017.components = [DataMuC_2017, DataMuD_2017, DataMuE_2017, DataMuF_2017, WJetsHT70to100_2017, WJetsHT100to200_2017, WJetsHT200to400_2017, WJetsHT400to600_2017, WJetsHT600to800_2017, WJetsHT800to1200_2017, WJetsHT1200to2500_2017, WJetsHT2500toInf_2017, DY1JetsToLL_2017, DY2JetsToLL_2017, DY3JetsToLL_2017, DY4JetsToLL_2017, DYJetsToLLM5to50_2017]


MCFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "MCFake_2017")
MCFake_2017.year = 2017
MCFake_2017.components = [WJetsHT70to100_2017, WJetsHT100to200_2017, WJetsHT200to400_2017, WJetsHT400to600_2017, WJetsHT600to800_2017, WJetsHT800to1200_2017, WJetsHT1200to2500_2017, WJetsHT2500toInf_2017, DY1JetsToLL_2017, DY2JetsToLL_2017, DY3JetsToLL_2017, DY4JetsToLL_2017, DYJetsToLLM5to50_2017]

DataHTB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB_2017")
DataHTB_2017.runP = 'B'
DataHTB_2017.year = 2017
DataHTB_2017.dataset = '/JetHT/Run2017B-'+tag_data + '-v1/NANOAOD'
DataHTC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTC_2017")
DataHTC_2017.runP = 'C'
DataHTC_2017.year = 2017
DataHTC_2017.dataset = '/JetHT/Run2017C-'+tag_data + '-v1/NANOAOD'
DataHTD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTD_2017")
DataHTD_2017.runP = 'D'
DataHTD_2017.year = 2017
DataHTD_2017.dataset = '/JetHT/Run2017D-'+tag_data + '-v1/NANOAOD'
DataHTE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTE_2017")
DataHTE_2017.runP = 'E'
DataHTE_2017.year = 2017
DataHTE_2017.dataset = '/JetHT/Run2017E-'+tag_data + '-v1/NANOAOD'
DataHTF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTF_2017")
DataHTF_2017.runP = 'F'
DataHTF_2017.year = 2017
DataHTF_2017.dataset = '/JetHT/Run2017F-'+tag_data + '-v1/NANOAOD'
DataHT_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_2017")
DataHT_2017.year = 2017
DataHT_2017.components = [DataHTB_2017, DataHTC_2017, DataHTD_2017, DataHTE_2017, DataHTF_2017]
DataHTnoB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_2017")
DataHTnoB_2017.year = 2017
DataHTnoB_2017.components = [DataHTC_2017, DataHTD_2017, DataHTE_2017, DataHTF_2017]

SampleHTFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "SampleHTFake_2017")
SampleHTFake_2017.year = 2017
SampleHTFake_2017.components = [DataHTB_2017, DataHTC_2017, DataHTD_2017, DataHTE_2017, DataHTF_2017, WJetsHT70to100_2017, WJetsHT100to200_2017, WJetsHT200to400_2017, WJetsHT400to600_2017, WJetsHT600to800_2017, WJetsHT800to1200_2017, WJetsHT1200to2500_2017, WJetsHT2500toInf_2017, DY1JetsToLL_2017, DY2JetsToLL_2017, DY3JetsToLL_2017, DY4JetsToLL_2017, DYJetsToLLM5to50_2017]

FakeElePromptTau_2017 = sample(ROOT.kGray+1, 1, 1001, "Fake e Prompt #tau", "FakeElePromptTau_2017")
FakeElePromptTau_2017.year = 2017
FakeElePromptTau_2017.components = [DataEle_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

PromptEleFakeTau_2017 = sample(ROOT.kGray+2, 1, 1001, "Prompt e Fake #tau", "PromptEleFakeTau_2017")
PromptEleFakeTau_2017.year = 2017
PromptEleFakeTau_2017.components = [DataEle_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

FakeEleFakeTau_2017 = sample(ROOT.kGray+3, 1, 1001, "Fake e Fake #tau", "FakeEleFakeTau_2017")
FakeEleFakeTau_2017.year = 2017
FakeEleFakeTau_2017.components = [DataEle_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

FakeEle_2017 = sample(ROOT.kGray, 1, 1001, "Fake Leptons", "FakeEle_2017")
FakeEle_2017.year = 2017
FakeEle_2017.components = [DataEle_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

FakeMuPromptTau_2017 = sample(ROOT.kGray+1, 1, 1001, "Fake #mu Prompt #tau", "FakeMuPromptTau_2017")
FakeMuPromptTau_2017.year = 2017
FakeMuPromptTau_2017.components = [DataMu_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

PromptMuFakeTau_2017 = sample(ROOT.kGray+2, 1, 1001, "Prompt #mu Fake #tau", "PromptMuFakeTau_2017")
PromptMuFakeTau_2017.year = 2017
PromptMuFakeTau_2017.components = [DataMu_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

FakeMuFakeTau_2017 = sample(ROOT.kGray+3, 1, 1001, "Fake #mu Fake #tau", "FakeMuFakeTau_2017")
FakeMuFakeTau_2017.year = 2017
FakeMuFakeTau_2017.components = [DataMu_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

FakeMu_2017 = sample(ROOT.kGray, 1, 1001, "Fake Leptons", "FakeMu_2017")
FakeMu_2017.year = 2017
FakeMu_2017.components = [DataMu_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

DataMETB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETB_2017")
DataMETB_2017.runP = 'B'
DataMETB_2017.year = 2017
DataMETB_2017.dataset = '/MET/Run2017B-'+tag_data + '-v1/NANOAOD'
DataMETC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETC_2017")
DataMETC_2017.runP = 'C'
DataMETC_2017.year = 2017
DataMETC_2017.dataset = '/MET/Run2017C-'+tag_data + '-v1/NANOAOD'
DataMETD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETD_2017")
DataMETD_2017.runP = 'D'
DataMETD_2017.year = 2017
DataMETD_2017.dataset = '/MET/Run2017D-'+tag_data + '-v1/NANOAOD'
DataMETE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETE_2017")
DataMETE_2017.runP = 'E'
DataMETE_2017.year = 2017
DataMETE_2017.dataset = '/MET/Run2017E-'+tag_data + '-v1/NANOAOD'
DataMETF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETF_2017")
DataMETF_2017.runP = 'F'
DataMETF_2017.year = 2017
DataMETF_2017.dataset = '/MET/Run2017F-'+tag_data + '-v1/NANOAOD'
DataMET_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMET_2017")
DataMET_2017.year = 2017
DataMET_2017.components = [DataMETB_2017, DataMETC_2017, DataMETD_2017, DataMETE_2017, DataMETF_2017]

DataMuA_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuA_2018")
DataMuA_2018.runP = 'A'
DataMuA_2018.year = 2018
DataMuA_2018.dataset = '/SingleMuon/Run2018A-'+tag_data + '-v1/NANOAOD'
DataMuB_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB_2018")
DataMuB_2018.runP = 'B'
DataMuB_2018.year = 2018
DataMuB_2018.dataset = '/SingleMuon/Run2018B-'+tag_data + '-v1/NANOAOD'
DataMuC_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuC_2018")
DataMuC_2018.runP = 'C'
DataMuC_2018.year = 2018
DataMuC_2018.dataset = '/SingleMuon/Run2018C-'+tag_data + '-v1/NANOAOD'
DataMuD_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuD_2018")
DataMuD_2018.runP = 'D'
DataMuD_2018.year = 2018
DataMuD_2018.dataset = '/SingleMuon/Run2018D-'+tag_data + '-v1/NANOAOD'
DataMu_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_2018")
DataMu_2018.year = 2018
DataMu_2018.components = [DataMuA_2018, DataMuB_2018, DataMuC_2018, DataMuD_2018]

DataEleA_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleA_2018")
DataEleA_2018.runP = 'A'
DataEleA_2018.year = 2018
DataEleA_2018.dataset = '/EGamma/Run2018A-'+tag_data + '-v1/NANOAOD'
DataEleB_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB_2018")
DataEleB_2018.runP = 'B'
DataEleB_2018.year = 2018
DataEleB_2018.dataset = '/EGamma/Run2018B-'+tag_data + '-v1/NANOAOD'
DataEleC_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleC_2018")
DataEleC_2018.runP = 'C'
DataEleC_2018.year = 2018
DataEleC_2018.dataset = '/EGamma/Run2018C-'+tag_data + '-v1/NANOAOD'
DataEleD_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleD_2018")
DataEleD_2018.runP = 'D'
DataEleD_2018.year = 2018
DataEleD_2018.dataset = '/EGamma/Run2018D-'+tag_data + '-v1/NANOAOD'
DataEle_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_2018")
DataEle_2018.year = 2018
DataEle_2018.components = [DataEleA_2018, DataEleB_2018, DataEleC_2018, DataEleD_2018]

DataHTA_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTA_2018")
DataHTA_2018.runP = 'A'
DataHTA_2018.year = 2018
DataHTA_2018.dataset = '/JetHT/Run2018A-'+tag_data + '-v2/NANOAOD'
DataHTB_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB_2018")
DataHTB_2018.runP = 'B'
DataHTB_2018.year = 2018
DataHTB_2018.dataset = '/JetHT/Run2018B-'+tag_data + '-v2/NANOAOD'
DataHTC_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTC_2018")
DataHTC_2018.runP = 'C'
DataHTC_2018.year = 2018
DataHTC_2018.dataset = '/JetHT/Run2018C-'+tag_data + '-v2/NANOAOD'
DataHTD_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTD_2018")
DataHTD_2018.runP = 'D'
DataHTD_2018.year = 2018
DataHTD_2018.dataset = '/JetHT/Run2018D-'+tag_data + '_v2/NANOAOD'
DataHT_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_2018")
DataHT_2018.year = 2018
DataHT_2018.components = [DataHTA_2018, DataHTB_2018, DataHTC_2018, DataHTD_2018]


sample_dict={
    'WpWpJJ_EWK_2017':WpWpJJ_EWK_2017,
    'WpWpJJ_QCD_2017':WpWpJJ_QCD_2017,
    'VBS_SSWW_SM_2017':VBS_SSWW_SM_2017, 'VBS_SSWW_LL_SM_2017':VBS_SSWW_LL_SM_2017, 'VBS_SSWW_TL_SM_2017':VBS_SSWW_TL_SM_2017, 'VBS_SSWW_TT_SM_2017':VBS_SSWW_TT_SM_2017,
    'VBS_SSWW_cHW_2017':VBS_SSWW_cHW_2017, 'VBS_SSWW_cHW_BSM_2017':VBS_SSWW_cHW_BSM_2017, 'VBS_SSWW_cHW_INT_2017':VBS_SSWW_cHW_INT_2017,
    'VBS_SSWW_cW_2017':VBS_SSWW_cW_2017, 'VBS_SSWW_cW_BSM_2017':VBS_SSWW_cW_BSM_2017, 'VBS_SSWW_cW_INT_2017':VBS_SSWW_cW_INT_2017,
    'VBS_SSWW_cW_cHW_2017':VBS_SSWW_cW_cHW_2017,
    'VBS_SSWW_BSM_INT_2017':VBS_SSWW_BSM_INT_2017,
    'VBS_SSWW_BSM_SM_2017':VBS_SSWW_BSM_SM_2017,
    'DHiggsToWW_2017':DHiggsToWW_2017,
    ### fake contributions form here...
    'QCD_2017':QCD_2017, 'QCDHT_100to200_2017':QCDHT_100to200_2017, 'QCDHT_200to300_2017':QCDHT_200to300_2017, 'QCDHT_300to500_2017':QCDHT_300to500_2017, 'QCDHT_500to700_2017':QCDHT_500to700_2017, 'QCDHT_700to1000_2017':QCDHT_700to1000_2017, 'QCDHT_1000to1500_2017':QCDHT_1000to1500_2017, 'QCDHT_1500to2000_2017':QCDHT_1500to2000_2017, 'QCDHT_2000toInf_2017':QCDHT_2000toInf_2017,
    'ZZtoLep_2017':ZZtoLep_2017, 'ZZTo2L2Nu_2017':ZZTo2L2Nu_2017, 'ZZJJTo4L_EWK_2017':ZZJJTo4L_EWK_2017, 'ZZJJTo4L_QCD_2017':ZZJJTo4L_QCD_2017, 'GluGluToContinToZZTo2e2nu_2017':GluGluToContinToZZTo2e2nu_2017, 'GluGluToContinToZZTo2e2mu_2017':GluGluToContinToZZTo2e2mu_2017, 'GluGluToContinToZZTo2e2tau_2017':GluGluToContinToZZTo2e2tau_2017, 'GluGluToContinToZZTo2mu2nu_2017':GluGluToContinToZZTo2mu2nu_2017, 'GluGluToContinToZZTo2mu2tau_2017':GluGluToContinToZZTo2mu2tau_2017, 'GluGluToContinToZZTo4e_2017':GluGluToContinToZZTo4e_2017, 'GluGluToContinToZZTo4mu_2017':GluGluToContinToZZTo4mu_2017, 'GluGluToContinToZZTo4tau_2017':GluGluToContinToZZTo4tau_2017,
    'GluGluToContinToZZTo4L_2017':GluGluToContinToZZTo4L_2017,
    'TT_2017':TT_2017, 'TT_SemiLep2017':TT_SemiLep_2017, 'TT_Had_2017':TT_Had_2017,#'TT_DiLep_2017':TT_DiLep_2017, 
    'WJets_2017':WJets_2017, 'WJets_Fake_2017':WJets_Fake_2017, 'WJetsHT70to100_2017':WJetsHT70to100_2017, 'WJetsHT100to200_2017':WJetsHT100to200_2017, 'WJetsHT200to400_2017':WJetsHT200to400_2017, 'WJetsHT400to600_2017':WJetsHT400to600_2017, 'WJetsHT600to800_2017':WJetsHT600to800_2017, 'WJetsHT800to1200_2017':WJetsHT800to1200_2017, 'WJetsHT1200to2500_2017':WJetsHT1200to2500_2017, 'WJetsHT2500toInf_2017':WJetsHT2500toInf_2017,
    'WJets_Fake_2017':WJets_Fake_2017, 'WJetsHT70to100_Fake_2017':WJetsHT70to100_Fake_2017, 'WJetsHT100to200_Fake_2017':WJetsHT100to200_Fake_2017, 'WJetsHT200to400_Fake_2017':WJetsHT200to400_Fake_2017, 'WJetsHT400to600_Fake_2017':WJetsHT400to600_Fake_2017, 'WJetsHT600to800_Fake_2017':WJetsHT600to800_Fake_2017, 'WJetsHT800to1200_Fake_2017':WJetsHT800to1200_Fake_2017, 'WJetsHT1200to2500_Fake_2017':WJetsHT1200to2500_Fake_2017, 'WJetsHT2500toInf_Fake_2017':WJetsHT2500toInf_Fake_2017,
    'DYJetsToLL_2017':DYJetsToLL_2017, 'DY1JetsToLL_2017':DY1JetsToLL_2017, 'DY2JetsToLL_2017':DY2JetsToLL_2017, 'DY3JetsToLL_2017':DY3JetsToLL_2017, 'DY4JetsToLL_2017':DY4JetsToLL_2017, 'DYJetsToLLM5to50_2017':DYJetsToLLM5to50_2017,
    'DYJetsToLL_Fake_2017':DYJetsToLL_Fake_2017, 'DY1JetsToLL_Fake_2017':DY1JetsToLL_Fake_2017, 'DY2JetsToLL_Fake_2017':DY2JetsToLL_Fake_2017, 'DY3JetsToLL_Fake_2017':DY3JetsToLL_Fake_2017, 'DY4JetsToLL_Fake_2017':DY4JetsToLL_Fake_2017,
    #'DYJetsM_2017':DYJetsM_2017, 'DYJetsToLLM5to50_2017':DYJetsToLLM5to50_2017, 'DYJetsToLLM50_2017':DYJetsToLLM50_2017,
    # to here
    'VG_2017':VG_2017, 'ZG_2017':ZG_2017, 'WG_2017':WG_2017,
    'TVX_2017':TVX_2017, 'TTGJets_2017':TTGJets_2017, 'TTZToQQ_2017':TTZToQQ_2017, 'TTZToLLNuNu_2017':TTZToLLNuNu_2017, 'TTWJetsToQQ_2017':TTWJetsToQQ_2017, 'TTWJetsToLNu_2017':TTWJetsToLNu_2017, 'tZq_ll_4f_2017':tZq_ll_4f_2017,
    'WrongSign_2017': WrongSign_2017, 'WWto2L2Nu_2017':WWto2L2Nu_2017, 'GluGluToWWToENuENu_2017':GluGluToWWToENuENu_2017, 'GluGluToWWToENuMNu2017':GluGluToWWToENuMNu2017, 'GluGluToWWToENuTNu2017':GluGluToWWToENuTNu2017, 'GluGluToWWToMNuENu_2017':GluGluToWWToMNuENu_2017, 'GluGluToWWToMNuMNu2017':GluGluToWWToMNuMNu2017, 'GluGluToWWToMNuTNu2017':GluGluToWWToMNuTNu2017, 'GluGluToWWToTNuENu_2017':GluGluToWWToTNuENu_2017, 'GluGluToWWToTNuMNu2017':GluGluToWWToTNuMNu2017, 'GluGluToWWToTNuTNu2017':GluGluToWWToTNuTNu2017, 'STtW_top_2017':STtW_top_2017, 'GluGluHToWWTo2L2Nu_2017':GluGluHToWWTo2L2Nu_2017, 'GluGluHToZZTo2L2Q_2017':GluGluHToZZTo2L2Q_2017, 'GluGluHToZZTo4L_2017':GluGluHToZZTo4L_2017, 'GluGluHToTauTau_2017':GluGluHToTauTau_2017, 'VBFHToWWTo2L2Nu_2017':VBFHToWWTo2L2Nu_2017, 'VBFHToTauTau_2017':VBFHToTauTau_2017, 'ttHToNonbb_2017':ttHToNonbb_2017, 'VHToNonbb_2017':VHToNonbb_2017,
    'OtherWS_2017':OtherWS_2017,
    'Other_2017':Other_2017, 'WWTo2L2Nu_DoubleScattering_2017':WWTo2L2Nu_DoubleScattering_2017, 'WWW_4F_2017':WWW_4F_2017, 'WWZTo3L1Nu2Q_2017':WWZTo3L1Nu2Q_2017, 'WZZ_2017':WZZ_2017, 'ZZZ_2017':ZZZ_2017, 'WWG_2017':WWG_2017,
    'TTTo2L2Nu_2017':TTTo2L2Nu_2017,
    'WZ_2017':WZ_2017,
    'FakeMu_2017':FakeMu_2017,
    'DataMu_2017':DataMu_2017, 'DataMuB_2017':DataMuB_2017, 'DataMuC_2017':DataMuC_2017, 'DataMuD_2017':DataMuD_2017, 'DataMuE_2017':DataMuE_2017, 'DataMuF_2017':DataMuF_2017, 'DataMuFake_2017': DataMuFake_2017,
    'FakeEle_2017':FakeEle_2017,
    'FakeMuPromptTau_2017':FakeMuPromptTau_2017, 'PromptMuFakeTau_2017':PromptMuFakeTau_2017, 'FakeMuFakeTau_2017':FakeMuFakeTau_2017,
    'DataEle_2017':DataEle_2017, 'DataEleB_2017':DataEleB_2017, 'DataEleC_2017':DataEleC_2017, 'DataEleD_2017':DataEleD_2017, 'DataEleE_2017':DataEleE_2017, 'DataEleF_2017':DataEleF_2017, 'DataEleFake_2017': DataEleFake_2017, 'MCFake_2017': MCFake_2017,
    'FakeElePromptTau_2017':FakeElePromptTau_2017, 'PromptEleFakeTau_2017':PromptEleFakeTau_2017, 'FakeEleFakeTau_2017':FakeEleFakeTau_2017,
    'DataTau_2017':DataTau_2017, 'DataTauB_2017':DataTauB_2017, 'DataTauC_2017':DataTauC_2017, 'DataTauD_2017':DataTauD_2017, 'DataTauE_2017':DataTauE_2017, 'DataTauF_2017':DataTauF_2017, 'DataTauFake_2017': DataTauFake_2017,
    'DataHT_2017':DataHT_2017, 'DataHTnoB_2017':DataHTnoB_2017, 'DataHTB_2017':DataHTB_2017, 'DataHTC_2017':DataHTC_2017, 'DataHTD_2017':DataHTD_2017, 'DataHTE_2017':DataHTE_2017, 'DataHTF_2017':DataHTF_2017,
    'DataMET_2017':DataMET_2017, 'DataMETB_2017':DataMETB_2017, 'DataMETC_2017':DataMETC_2017, 'DataMETD_2017':DataMETD_2017, 'DataMETE_2017':DataMETE_2017, 'DataMETF_2017':DataMETF_2017,

    'SampleEleFake_2017': SampleEleFake_2017, 'SampleMuFake_2017': SampleMuFake_2017, 'SampleHTFake_2017': SampleHTFake_2017,

}

class_dict={
    'WpWpJJ_EWK_2017':WpWpJJ_EWK_2017,
    'WpWpJJ_QCD_2017':WpWpJJ_QCD_2017,
    'VBS_SSWW_SM_2017':VBS_SSWW_SM_2017,
    'VBS_SSWW_cHW_2017':VBS_SSWW_cHW_2017,
    'VBS_SSWW_cW_2017':VBS_SSWW_cW_2017,
    #'VBS_SSWW_cW_cHW_2017':VBS_SSWW_cW_cHW_2017,
    'VBS_SSWW_BSM_INT_2017':VBS_SSWW_BSM_INT_2017,
    'VBS_SSWW_BSM_SM_2017':VBS_SSWW_BSM_SM_2017,
    ### fake contributions from here...
    #'QCD_2017':QCD_2017,
    'ZZtoLep_2017':ZZtoLep_2017,
    #'TT_2017':TT_2017,
    'WJets_2017':WJets_2017,
    #'WJets_Fake_2017':WJets_Fake_2017,
    #'DYJetsToLL_2017':DYJetsToLL_2017,
    #'DYJetsToLL_Fake_2017':DYJetsToLL_Fake_2017,
    #'DYJetsM_2017':DYJetsM_2017,
    # to here
    'VG_2017':VG_2017,
    'TVX_2017':TVX_2017,
    #'WrongSign_2017': WrongSign_2017,
    #'Other_2017':Other_2017,
    'OtherWS_2017':OtherWS_2017,
    'TTTo2L2Nu_2017':TTTo2L2Nu_2017,
    'WZ_2017':WZ_2017,
    'DataMu_2017':DataMu_2017,
    'DataEle_2017':DataEle_2017,
    #'DataHT_2017':DataHT_2017,
    #'DataMET_2017':DataMET_2017,
    #'FakeEle_2017': FakeEle_2017,
    #'FakeMu_2017': FakeMu_2017,
}

class_list=[
    #WpWpJJ_EWK_2017,
    #VBS_SSWW_LL_SM_2017,
    #VBS_SSWW_TL_SM_2017,
    #VBS_SSWW_TT_SM_2017,
    VBS_SSWW_SM_2017,
    #VBS_SSWW_cHW_2017,
    #VBS_SSWW_cW_2017,
    #VBS_SSWW_cW_cHW_2017,
    VBS_SSWW_BSM_INT_2017,
    VBS_SSWW_BSM_SM_2017,
    VG_2017,
    WpWpJJ_QCD_2017,
    TVX_2017,
    TTTo2L2Nu_2017,
    WZ_2017,
    OtherWS_2017,
    ZZtoLep_2017,
    #ZZTo2L2Nu_2017,
    #ZZJJTo4L_EWK_2017,
    #ZZJJTo4L_QCD_2017,
    #GluGluToContinToZZTo2e2nu_2017,
    #GluGluToContinToZZTo2e2mu_2017,
    #GluGluToContinToZZTo2e2tau_2017,
    #GluGluToContinToZZTo2mu2nu_2017,
    #GluGluToContinToZZTo2mu2tau_2017,
    #GluGluToContinToZZTo4e_2017,
    #GluGluToContinToZZTo4mu_2017,
    #Other_2017,
    #WrongSign_2017, 
    #DYJetsToLL_2017,
    #DYJetsToLL_Fake_2017,
    #DYJetsM_2017,
    #TT_2017,
    #QCD_2017,
    #WJets_2017,
    ##WJets_Fake_2017,
    FakeMu_2017,
    FakeMuPromptTau_2017,
    PromptMuFakeTau_2017,
    FakeMuFakeTau_2017,
    DataMu_2017,
    FakeEle_2017,
    FakeEleFakeTau_2017,
    FakeElePromptTau_2017,
    PromptEleFakeTau_2017,
    DataEle_2017,
    #DataHT_2017,
    ]

'''
sample_dict = {
    #2016
    #'TT_Mtt_2016':TT_Mtt_2016, 'TT_Mtt700to1000_2016':TT_Mtt700to1000_2016, 'TT_Mtt1000toInf_2016':TT_Mtt1000toInf_2016, 'TT_incl_2016':TT_incl_2016, 'TT_DiLep_2016':TT_DiLep_2016,
    #'WJets_2016':WJets_2016, 'WJetsHT70to100_2016':WJetsHT70to100_2016, 'WJetsHT100to200_2016':WJetsHT100to200_2016, 'WJetsHT200to400_2016':WJetsHT200to400_2016, 'WJetsHT400to600_2016':WJetsHT400to600_2016, 'WJetsHT600to800_2016':WJetsHT600to800_2016, 'WJetsHT800to1200_2016':WJetsHT800to1200_2016, 'WJetsHT1200to2500_2016':WJetsHT1200to2500_2016, 'WJetsHT2500toInf_2016':WJetsHT2500toInf_2016,
    #'WZ_2016':WZ_2016,
    #'DYJetsToLL_2016':DYJetsToLL_2016, 'DY1JetsToLL_2016':DY1JetsToLL_2016, 'DY2JetsToLL_2016':DY2JetsToLL_2016, 'DY3JetsToLL_2016':DY3JetsToLL_2016, 'DY4JetsToLL_2016':DY4JetsToLL_2016, 
    #'WpWpJJ_EWK_2016':WpWpJJ_EWK_2016,
    #'WpWpJJ_QCD_2016':WpWpJJ_QCD_2016,
    #'DataMu_2016':DataMu_2016, 'DataMuB_2016':DataMuB_2016,  'DataMuC_2016':DataMuC_2016, 'DataMuD_2016':DataMuD_2016, 'DataMuE_2016':DataMuE_2016, 'DataMuF_2016':DataMuF_2016, 'DataMuG_2016':DataMuG_2016, 'DataMuH_2016':DataMuH_2016,
    #'DataEle_2016':DataEle_2016, 'DataEleB_2016':DataEleB_2016, 'DataEleC_2016':DataEleC_2016, 'DataEleD_2016':DataEleD_2016, 'DataEleE_2016':DataEleE_2016, 'DataEleF_2016':DataEleF_2016, 'DataEleG_2016':DataEleG_2016, 'DataEleH_2016':DataEleH_2016,
    #'DataHT_2016':DataHT_2016, 'DataHTB_2016':DataHTB_2016, 'DataHTC_2016':DataHTC_2016, 'DataHTD_2016':DataHTD_2016, 'DataHTE_2016':DataHTE_2016, 'DataHTF_2016':DataHTF_2016, 'DataHTG_2016':DataHTG_2016, 'DataHTH_2016':DataHTH_2016,
    #2017
    #'TT_Mtt_2017':TT_Mtt_2017, 'TT_Mtt700to1000_2017':TT_Mtt700to1000_2017, 'TT_Mtt1000toInf_2017':TT_Mtt1000toInf_2017,
    'TT_2017':TT_2017, 'TT_DiLep_2017':TT_DiLep_2017, 'TT_SemiLep2017':TT_SemiLep_2017, 'TT_Had_2017':TT_Had_2017,
    'WJets_2017':WJets_2017, 'WJetsHT70to100_2017':WJetsHT70to100_2017, 'WJetsHT100to200_2017':WJetsHT100to200_2017, 'WJetsHT200to400_2017':WJetsHT200to400_2017, 'WJetsHT400to600_2017':WJetsHT400to600_2017, 'WJetsHT600to800_2017':WJetsHT600to800_2017, 'WJetsHT800to1200_2017':WJetsHT800to1200_2017, 'WJetsHT1200to2500_2017':WJetsHT1200to2500_2017, 'WJetsHT2500toInf_2017':WJetsHT2500toInf_2017,
    'WZ_2017':WZ_2017,
    'DYJetsToLL_2017':DYJetsToLL_2017, 'DY1JetsToLL_2017':DY1JetsToLL_2017, 'DY2JetsToLL_2017':DY2JetsToLL_2017, 'DY3JetsToLL_2017':DY3JetsToLL_2017, 'DY4JetsToLL_2017':DY4JetsToLL_2017, 
    'WpWpJJ_EWK_2017':WpWpJJ_EWK_2017,
    'WpWpJJ_QCD_2017':WpWpJJ_QCD_2017,
    'DataMu_2017':DataMu_2017, 'DataMuB_2017':DataMuB_2017, 'DataMuC_2017':DataMuC_2017, 'DataMuD_2017':DataMuD_2017, 'DataMuE_2017':DataMuE_2017, 'DataMuF_2017':DataMuF_2017,
    'DataEle_2017':DataEle_2017, 'DataEleB_2017':DataEleB_2017, 'DataEleC_2017':DataEleC_2017, 'DataEleD_2017':DataEleD_2017, 'DataEleE_2017':DataEleE_2017, 'DataEleF_2017':DataEleF_2017,
    'DataHT_2017':DataHT_2017, 'DataHTB_2017':DataHTB_2017, 'DataHTC_2017':DataHTC_2017, 'DataHTD_2017':DataHTD_2017, 'DataHTE_2017':DataHTE_2017, 'DataHTF_2017':DataHTF_2017,

    #2018
    #'TT_Mtt_2018':TT_Mtt_2018, 'TT_Mtt700to1000_2018':TT_Mtt700to1000_2018, 'TT_Mtt1000toInf_2018':TT_Mtt1000toInf_2018,
    #'TT_2018':TT_2018, 'TT_DiLep_2018':TT_DiLep_2018, 'TT_SemiLep_2018':TT_SemiLep_2018, 'TT_Had_2018':TT_Had_2018,
    #'WJets_2018':WJets_2018, 'WJetsHT70to100_2018':WJetsHT70to100_2018, 'WJetsHT100to200_2018':WJetsHT100to200_2018, 'WJetsHT200to400_2018':WJetsHT200to400_2018, 'WJetsHT400to600_2018':WJetsHT400to600_2018, 'WJetsHT600to800_2018':WJetsHT600to800_2018, 'WJetsHT800to1200_2018':WJetsHT800to1200_2018, 'WJetsHT1200to2500_2018':WJetsHT1200to2500_2018, 'WJetsHT2500toInf_2018':WJetsHT2500toInf_2018,
    #'WZ_2018':WZ_2018,
    #'DYJetsToLL_2018':DYJetsToLL_2018, 'DY1JetsToLL_2018':DY1JetsToLL_2018, 'DY2JetsToLL_2018':DY2JetsToLL_2018, 'DY3JetsToLL_2018':DY3JetsToLL_2018, 'DY4JetsToLL_2018':DY4JetsToLL_2018, 
    #'WpWpJJ_EWK_2018':WpWpJJ_EWK_2018,
    #'WpWpJJ_QCD_2018':WpWpJJ_QCD_2018,
    #'DataMu_2018':DataMu_2018, 'DataMuA_2018':DataMuA_2018, 'DataMuB_2018':DataMuB_2018, 'DataMuC_2018':DataMuC_2018, 'DataMuD_2018':DataMuD_2018,
    #'DataEle_2018':DataEle_2018, 'DataEleA_2018':DataEleA_2018, 'DataEleB_2018':DataEleB_2018, 'DataEleC_2018':DataEleC_2018, 'DataEleD_2018':DataEleD_2018,
    #'DataHT_2018':DataHT_2018,'DataHTA_2018':DataHTA_2018,  'DataHTB_2018':DataHTB_2018, 'DataHTC_2018':DataHTC_2018, 'DataHTD_2018':DataHTD_2018,
    }
'''
