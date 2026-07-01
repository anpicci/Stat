import ROOT
import os 
#import json_reader as jr

path = os.path.dirname(os.path.abspath(__file__))

class sample:
    def __init__(self, color, style, fill, leglabel, label, name=""):
        self.color = color
        self.style = style
        self.fill = fill
        self.leglabel = leglabel
        self.label = label
        if name == "":
            self.name = label
        else:
            self.name = name

### color labels ###
ZZcolor = ROOT.kViolet-9
TTcolor = ROOT.kRed+2
TTdilepcolor = ROOT.kAzure+6#-9
TVXcolor = ROOT.kMagenta-9#kSpring-4
VGcolor = ROOT.kOrange-4
DYcolor = ROOT.kGreen-5
TBcolor = ROOT.kYellow-7
WJcolor = ROOT.kGreen+2
WZcolor = ROOT.kCyan-9#kPink+1#kYellow-7
WScolor = ROOT.kGreen-9#kPink+1
VBScolor = ROOT.kRed
VBSLLcolor = ROOT.kGreen+3
VBSTLcolor = ROOT.kBlue+3
VBSTTcolor = ROOT.kMagenta+3
CWcolor = ROOT.kGray+3
CHWcolor = ROOT.kAzure+10
EWVBScolor = ROOT.kRed
QCDVBScolor = ROOT.kViolet-8
WWJJcolor = ROOT.kMagenta-4
aQGCcolor = ROOT.kGreen
aTGCcolor = ROOT.kViolet
othcolor = ROOT.kMagenta-10
######### UL2016APV ##########

### ZZtoLep ###

ZZTo2L2Nu_UL2016APV = sample(ZZcolor, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_UL2016APV")
ZZTo2L2Nu_UL2016APV.year = "UL2016APV"
ZZTo2L2Nu_UL2016APV.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ZZTo2L2Nu_UL2016APV.sigma = 0.564 #pb NLO

ZZTo4L_UL2016APV = sample(ZZcolor, 1, 1001, "ZZ --> 4l", "ZZTo4L_UL2016APV") ### not sure is the right background
ZZTo4L_UL2016APV.year = "UL2016APV"
ZZTo4L_UL2016APV.dataset = "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ZZTo4L_UL2016APV.sigma = 13.74 #pb NLO

#### to be produced ####
GluGluToContinToZZTo2e2nu_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2nu", "GluGluToContinToZZTo2e2nu_UL2016APV")
GluGluToContinToZZTo2e2nu_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo2e2nu_UL2016APV.dataset = "/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
GluGluToContinToZZTo2e2nu_UL2016APV.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo4e_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4e", "GluGluToContinToZZTo4e_UL2016APV")
GluGluToContinToZZTo4e_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo4e_UL2016APV.dataset = "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo4e_UL2016APV.sigma = 0.001586 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2mu_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2mu", "GluGluToContinToZZTo2e2mu_UL2016APV")
GluGluToContinToZZTo2e2mu_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo2e2mu_UL2016APV.dataset = "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo2e2mu_UL2016APV.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2tau_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2tau", "GluGluToContinToZZTo2e2tau_UL2016APV")
GluGluToContinToZZTo2e2tau_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo2e2tau_UL2016APV.dataset = "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo2e2tau_UL2016APV.sigma = 0.003194 # * 0.001 #pb to be checked

#### in production stage ######
GluGluToContinToZZTo2mu2nu_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2nu", "GluGluToContinToZZTo2mu2nu_UL2016APV")
GluGluToContinToZZTo2mu2nu_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo2mu2nu_UL2016APV.dataset = "/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2nu_UL2016APV.sigma = 0.003194 # * 0.001 #pb to be checked

#### to be replaced with v9 when available ####
GluGluToContinToZZTo4mu_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4mu", "GluGluToContinToZZTo4mu_UL2016APV")
GluGluToContinToZZTo4mu_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo4mu_UL2016APV.dataset = "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
GluGluToContinToZZTo4mu_UL2016APV.sigma = 0.001586 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2tau_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2tau", "GluGluToContinToZZTo2mu2tau_UL2016APV")
GluGluToContinToZZTo2mu2tau_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo2mu2tau_UL2016APV.dataset = "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_UL2016APV.sigma = 0.003194 # * 0.001 #pb to be checked

#### to be produced ####
GluGluToContinToZZTo2tau2nu_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2tau2nu", "GluGluToContinToZZTo2tau2nu_UL2016APV")
GluGluToContinToZZTo2tau2nu_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo2tau2nu_UL2016APV.dataset = ""
GluGluToContinToZZTo2tau2nu_UL2016APV.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo4tau_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4tau", "GluGluToContinToZZTo4tau_UL2016APV")
GluGluToContinToZZTo4tau_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo4tau_UL2016APV.dataset = "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo4tau_UL2016APV.sigma = 0.001586 # * 0.001 #pb to be checked

ZZtoLep_UL2016APV = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_UL2016APV")
ZZtoLep_UL2016APV.year = "UL2016APV"
ZZtoLep_UL2016APV.components = [
    ZZTo2L2Nu_UL2016APV,
    ZZTo4L_UL2016APV,
    GluGluToContinToZZTo2e2nu_UL2016APV,
    GluGluToContinToZZTo4e_UL2016APV,
    GluGluToContinToZZTo2e2mu_UL2016APV,
    GluGluToContinToZZTo2e2tau_UL2016APV,
    GluGluToContinToZZTo2mu2nu_UL2016APV,
    GluGluToContinToZZTo4mu_UL2016APV,
    GluGluToContinToZZTo2mu2tau_UL2016APV,
    #GluGluToContinToZZTo2tau2nu_UL2016APV,
    GluGluToContinToZZTo4tau_UL2016APV,
]

### TT with quark ###

TT_SemiLep_UL2016APV = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_SemiLep_UL2016APV")
TT_SemiLep_UL2016APV.year = "UL2016APV"
TT_SemiLep_UL2016APV.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
TT_SemiLep_UL2016APV.sigma = 831.76 * 0.438

TT_Had_UL2016APV = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_Had_UL2016APV")
TT_Had_UL2016APV.year = "UL2016APV"
TT_Had_UL2016APV.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
TT_Had_UL2016APV.sigma = 831.76 * 0.457

TT_UL2016APV = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_UL2016APV")
TT_UL2016APV.year = "UL2016APV"
TT_UL2016APV.components = [
    TT_SemiLep_UL2016APV,
    TT_Had_UL2016APV,
]

TT_Mtt_700to1000_UL2016APV = sample(TTcolor, 1, 1001, "t#bar{t} 700 < M_{tt} < 1000 GeV", "TT_Mtt_700to1000_UL2016APV")
TT_Mtt_700to1000_UL2016APV.year = "UL2016APV"
TT_Mtt_700to1000_UL2016APV.dataset = "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM"
TT_Mtt_700to1000_UL2016APV.sigma = 66.85

TT_Mtt_1000toInf_UL2016APV = sample(TTcolor, 1, 1001, "t#bar{t} M_{tt} > 1000 GeV", "TT_Mtt_1000toInf_UL2016APV")
TT_Mtt_1000toInf_UL2016APV.year = "UL2016APV"
TT_Mtt_1000toInf_UL2016APV.dataset = "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
TT_Mtt_1000toInf_UL2016APV.sigma = 16.38

TT_Mtt_UL2016APV = sample(TTcolor, 1, 1001, "t#bar{t} M_{tt} > 700 GeV", "TT_Mtt_UL2016APV")
TT_Mtt_UL2016APV.year = "UL2016APV"
TT_Mtt_UL2016APV.components = [
    TT_Mtt_700to1000_UL2016APV,
    TT_Mtt_1000toInf_UL2016APV,
]


TTTo2L2Nu_UL2016APV = sample(TTdilepcolor, 1, 1001, "t#bar{t} dilep.", "TTTo2L2Nu_UL2016APV")
TTTo2L2Nu_UL2016APV.year = "UL2016APV"
TTTo2L2Nu_UL2016APV.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
TTTo2L2Nu_UL2016APV.sigma = 72.1 #831.76 * 0.105 #pb

TT_beff_UL2016APV = sample(TTcolor, 1, 1001, "t#bar{t} inclusive", "TT_beff_UL2016APV")
TT_beff_UL2016APV.year = "UL2016APV"
TT_beff_UL2016APV.components = [
    TT_SemiLep_UL2016APV,
    TT_Had_UL2016APV,
    TTTo2L2Nu_UL2016APV,
]

### TVX ###

TTGJets_UL2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> qq", "TTGJets_UL2016APV")
TTGJets_UL2016APV.year = "UL2016APV"
TTGJets_UL2016APV.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
TTGJets_UL2016APV.sigma = 3.697

TTZToQQ_UL2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTZToQQ_UL2016APV")
TTZToQQ_UL2016APV.year = "UL2016APV"
TTZToQQ_UL2016APV.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
TTZToQQ_UL2016APV.sigma = 0.5297

TTZToLLNuNu_UL2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> 2l2#nu", "TTZToLLNuNu_UL2016APV")
TTZToLLNuNu_UL2016APV.year = "UL2016APV"
TTZToLLNuNu_UL2016APV.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
TTZToLLNuNu_UL2016APV.sigma = 0.2529

#### to be replaced with v9 when available ####
TTWJetsToQQ_UL2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToQQ_UL2016APV")
TTWJetsToQQ_UL2016APV.year = "UL2016APV"
TTWJetsToQQ_UL2016APV.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
TTWJetsToQQ_UL2016APV.sigma = 0.4062

#### to be replaced with v9 when available ####
TTWJetsToLNu_UL2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToLNu_UL2016APV")
TTWJetsToLNu_UL2016APV.year = "UL2016APV"
TTWJetsToLNu_UL2016APV.dataset = "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
TTWJetsToLNu_UL2016APV.sigma = 0.216

tZq_ll_4f_UL2016APV = sample(TVXcolor, 1, 1001, "tZq --> ll", "tZq_ll_4f_UL2016APV")
tZq_ll_4f_UL2016APV.year = "UL2016APV"
tZq_ll_4f_UL2016APV.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
tZq_ll_4f_UL2016APV.sigma = 0.0758

TVX_UL2016APV = sample(TVXcolor, 1, 1001, "tVX", "TVX_UL2016APV")
TVX_UL2016APV.year = "UL2016APV"
TVX_UL2016APV.components = [
    TTGJets_UL2016APV,
    TTZToQQ_UL2016APV,
    TTZToLLNuNu_UL2016APV,
    TTWJetsToQQ_UL2016APV,
    TTWJetsToLNu_UL2016APV,
    tZq_ll_4f_UL2016APV,
]

### VG ###

#### to be replaced with v9 when available ####
ZG_UL2016APV = sample(VGcolor, 1, 1001, "Z #gamma", "ZG_UL2016APV")
ZG_UL2016APV.year = "UL2016APV"
ZG_UL2016APV.dataset = "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
ZG_UL2016APV.sigma = 51.1 # to check

WG_UL2016APV = sample(VGcolor, 1, 1001, "W #gamma", "WG_UL2016APV")
WG_UL2016APV.year = "UL2016APV"
WG_UL2016APV.dataset = "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WG_UL2016APV.sigma = 191.3 # to check

VG_UL2016APV = sample(VGcolor, 1, 1001, "V#gamma", "VG_UL2016APV")
VG_UL2016APV.year = "UL2016APV"
VG_UL2016APV.components = [
    ZG_UL2016APV,
    WG_UL2016APV,
]

### WrongSign ###

WWto2L2Nu_UL2016APV = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "WWto2L2Nu_UL2016APV")
WWto2L2Nu_UL2016APV.year = "UL2016APV"
WWto2L2Nu_UL2016APV.dataset = "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WWto2L2Nu_UL2016APV.sigma = 12.178

GluGluToWWToENEN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> 2e2#nu", "GluGluToWWToENEN_UL2016APV")
GluGluToWWToENEN_UL2016APV.year = "UL2016APV"
GluGluToWWToENEN_UL2016APV.dataset = "/GluGluToWWToENEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToENEN_UL2016APV.sigma = 63.87 * 1./9. * 0.001 * 2. #36.8 * 1./9. * 1.4 * 0.001 

GluGluToWWToENMN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#mu2#nu", "GluGluToWWToENMN_UL2016APV")
GluGluToWWToENMN_UL2016APV.year = "UL2016APV"
GluGluToWWToENMN_UL2016APV.dataset = "/GluGluToWWToENMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToENMN_UL2016APV.sigma = 63.87 * 1./9. * 0.001 #36.8 * 1./9. * 1.4 * 0.001 

GluGluToWWToENTN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToENTN_UL2016APV")
GluGluToWWToENTN_UL2016APV.year = "UL2016APV"
GluGluToWWToENTN_UL2016APV.dataset = "/GluGluToWWToENTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToENTN_UL2016APV.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToMNEN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNEN_UL2016APV")
GluGluToWWToMNEN_UL2016APV.year = "UL2016APV"
GluGluToWWToMNEN_UL2016APV.dataset = "/GluGluToWWToMNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToMNEN_UL2016APV.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToMNMN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNMN_UL2016APV")
GluGluToWWToMNMN_UL2016APV.year = "UL2016APV"
GluGluToWWToMNMN_UL2016APV.dataset = "/GluGluToWWToMNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToMNMN_UL2016APV.sigma = 63.87 * 1./9. * 0.001 * 2. #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToMNTN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNTN_UL2016APV")
GluGluToWWToMNTN_UL2016APV.year = "UL2016APV"
GluGluToWWToMNTN_UL2016APV.dataset = "/GluGluToWWToMNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToMNTN_UL2016APV.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToTNEN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNEN_UL2016APV")
GluGluToWWToTNEN_UL2016APV.year = "UL2016APV"
GluGluToWWToTNEN_UL2016APV.dataset = "/GluGluToWWToTNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToTNEN_UL2016APV.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToTNMN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNMN_UL2016APV")
GluGluToWWToTNMN_UL2016APV.year = "UL2016APV"
GluGluToWWToTNMN_UL2016APV.dataset = "/GluGluToWWToTNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToTNMN_UL2016APV.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToTNTN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNTN_UL2016APV")
GluGluToWWToTNTN_UL2016APV.year = "UL2016APV"
GluGluToWWToTNTN_UL2016APV.dataset = "/GluGluToWWToTNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToTNTN_UL2016APV.sigma = 63.87 * 1./9. * 0.001 * 2. #36.81 * 1./9. * 1.4 * 0.001 

ST_tW_top_UL2016APV = sample(WScolor, 1, 1001, "Single top", "ST_tW_top_UL2016APV")
ST_tW_top_UL2016APV.year = "UL2016APV"
ST_tW_top_UL2016APV.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ST_tW_top_UL2016APV.sigma =  35.85 

ST_tW_antitop_UL2016APV = sample(WScolor, 1, 1001, "Single top", "ST_tW_antitop_UL2016APV")
ST_tW_antitop_UL2016APV.year = "UL2016APV"
ST_tW_antitop_UL2016APV.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ST_tW_antitop_UL2016APV.sigma =  35.85 

GluGluHToWWTo2L2Nu_UL2016APV = sample(WScolor, 1, 1001, "Single top", "GluGluHToWWTo2L2Nu_UL2016APV")
GluGluHToWWTo2L2Nu_UL2016APV.year = "UL2016APV"
GluGluHToWWTo2L2Nu_UL2016APV.dataset = "/GluGluHToWWTo2L2Nu_M125_TuneCP5_PSw_13TeV-powheg2-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluHToWWTo2L2Nu_UL2016APV.sigma = 1.0315

#### in production stage ####
GluGluHToZZTo4L_UL2016APV = sample(WScolor, 1, 1001, "Single top", "GluGluHToZZTo4L_UL2016APV")
GluGluHToZZTo4L_UL2016APV.year = "UL2016APV"
GluGluHToZZTo4L_UL2016APV.dataset = "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluHToZZTo4L_UL2016APV.sigma = 0.0118

#### in production stage ####
GluGluHToTauTau_UL2016APV = sample(WScolor, 1, 1001, "Single top", "GluGluHToTauTau_UL2016APV")
GluGluHToTauTau_UL2016APV.year = "UL2016APV"
GluGluHToTauTau_UL2016APV.dataset = "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluHToTauTau_UL2016APV.sigma = 2.7757

VBFHToWWTo2L2Nu_UL2016APV = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToWWTo2L2Nu_UL2016APV")
VBFHToWWTo2L2Nu_UL2016APV.year = "UL2016APV"
VBFHToWWTo2L2Nu_UL2016APV.dataset = "/VBFHToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
VBFHToWWTo2L2Nu_UL2016APV.sigma = 0.0896 

#### in production stage ####
VBFHToTauTau_UL2016APV = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToTauTau_UL2016APV")
VBFHToTauTau_UL2016APV.year = "UL2016APV"
VBFHToTauTau_UL2016APV.dataset = "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
VBFHToTauTau_UL2016APV.sigma = 0.237

ttHToNonbb_UL2016APV = sample(WScolor, 1, 1001, "ttH", "ttHToNonbb_UL2016APV")
ttHToNonbb_UL2016APV.year = "UL2016APV"
ttHToNonbb_UL2016APV.dataset = "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
ttHToNonbb_UL2016APV.sigma = 0.2120 # check nowe

VHToNonbb_UL2016APV = sample(WScolor, 1, 1001, "VH", "VHToNonbb_UL2016APV")
VHToNonbb_UL2016APV.year = "UL2016APV"
VHToNonbb_UL2016APV.dataset = "/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
VHToNonbb_UL2016APV.sigma = 0.952 # check nowe

DYJetsToLL_M50_FxFx_UL2016APV = sample(DYcolor, 1, 1001, "DYJetsToLL_M50", "DYJetsToLL_M50_FxFx_UL2016APV")
DYJetsToLL_M50_FxFx_UL2016APV.year = "UL2016APV"
DYJetsToLL_M50_FxFx_UL2016APV.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
DYJetsToLL_M50_FxFx_UL2016APV.sigma = 7181.0 #6077.22 #6529.0

WrongSign_UL2016APV = sample(WScolor, 1, 1001, "OS + (Z/#gamma + jets)", "WrongSign_UL2016APV")
WrongSign_UL2016APV.year = "UL2016APV"
WrongSign_UL2016APV.components = [
    WWto2L2Nu_UL2016APV,
    GluGluToWWToENEN_UL2016APV,
    GluGluToWWToENMN_UL2016APV,
    GluGluToWWToENTN_UL2016APV,
    GluGluToWWToMNEN_UL2016APV,
    GluGluToWWToMNMN_UL2016APV,
    GluGluToWWToMNTN_UL2016APV,
    GluGluToWWToTNEN_UL2016APV,
    GluGluToWWToTNMN_UL2016APV,
    GluGluToWWToTNTN_UL2016APV,
    ST_tW_top_UL2016APV,
    ST_tW_antitop_UL2016APV,
    GluGluHToWWTo2L2Nu_UL2016APV,
    GluGluHToZZTo4L_UL2016APV,
    GluGluHToTauTau_UL2016APV,
    VBFHToWWTo2L2Nu_UL2016APV,
    VBFHToTauTau_UL2016APV,
    ttHToNonbb_UL2016APV,
    VHToNonbb_UL2016APV,
    DYJetsToLL_M50_FxFx_UL2016APV,
]


WrongSign_ML_UL2016APV = sample(WScolor, 1, 1001, "OS", "WrongSign_ML_UL2016APV")
WrongSign_ML_UL2016APV.year = "UL2016APV"
WrongSign_ML_UL2016APV.components = [
    WWto2L2Nu_UL2016APV,
    GluGluToWWToENEN_UL2016APV,
    GluGluToWWToENMN_UL2016APV,
    GluGluToWWToENTN_UL2016APV,
    GluGluToWWToMNEN_UL2016APV,
    GluGluToWWToMNMN_UL2016APV,
    GluGluToWWToMNTN_UL2016APV,
    GluGluToWWToTNEN_UL2016APV,
    GluGluToWWToTNMN_UL2016APV,
    GluGluToWWToTNTN_UL2016APV,
    ST_tW_top_UL2016APV,
    ST_tW_antitop_UL2016APV,
    GluGluHToWWTo2L2Nu_UL2016APV,
    GluGluHToZZTo4L_UL2016APV,
    GluGluHToTauTau_UL2016APV,
    VBFHToWWTo2L2Nu_UL2016APV,
    VBFHToTauTau_UL2016APV,
    ttHToNonbb_UL2016APV,
    VHToNonbb_UL2016APV,
]

### Triboson ###

#### in production stage ####
WWTo2L2Nu_DoubleScattering_UL2016APV = sample(TBcolor, 1, 1001, "WWTo2L2Nu_DoubleScattering", "WWTo2L2Nu_DoubleScattering_UL2016APV")
WWTo2L2Nu_DoubleScattering_UL2016APV.year = "UL2016APV"
WWTo2L2Nu_DoubleScattering_UL2016APV.dataset = ""
WWTo2L2Nu_DoubleScattering_UL2016APV.sigma =  0.1703#pb

WWW_4F_UL2016APV = sample(TBcolor, 1, 1001, "WWW_4F", "WWW_4F_UL2016APV")
WWW_4F_UL2016APV.year = "UL2016APV"
WWW_4F_UL2016APV.dataset = "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM"
WWW_4F_UL2016APV.sigma = 0.2086#pb

WWZ_4F_UL2016APV = sample(TBcolor, 1, 1001, "WWZ_4F", "WWZ_4F_UL2016APV")
WWZ_4F_UL2016APV.year = "UL2016APV"
WWZ_4F_UL2016APV.dataset = "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM"
WWZ_4F_UL2016APV.sigma = 0.1651#pb

WZZ_UL2016APV = sample(TBcolor, 1, 1001, "WZZ", "WZZ_UL2016APV")
WZZ_UL2016APV.year = "UL2016APV"
WZZ_UL2016APV.dataset = "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM"
WZZ_UL2016APV.sigma = 0.05565#pb

ZZZ_UL2016APV = sample(TBcolor, 1, 1001, "ZZZ", "ZZZ_UL2016APV")
ZZZ_UL2016APV.year = "UL2016APV"
ZZZ_UL2016APV.dataset = "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM"
ZZZ_UL2016APV.sigma = 0.01398#pb

WWG_UL2016APV = sample(TBcolor, 1, 1001, "WWG", "WWG_UL2016APV")
WWG_UL2016APV.year = "UL2016APV"
WWG_UL2016APV.dataset = "/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WWG_UL2016APV.sigma = 0.2147#pb

Triboson_UL2016APV = sample(TBcolor, 1, 1001, "Triboson", "Triboson_UL2016APV")
Triboson_UL2016APV.year = "UL2016APV"
Triboson_UL2016APV.components = [
    #WWTo2L2Nu_DoubleScattering_UL2016APV,
    WWW_4F_UL2016APV,
    WWZ_4F_UL2016APV,
    WZZ_UL2016APV,
    ZZZ_UL2016APV,
    WWG_UL2016APV,
]

### WJets ###

#### to be replaced with v9 when available ####
WJetsHT70to100_UL2016APV = sample(WJcolor, 1, 1001, "W + Jets 70 < HT < 100", "WJetsHT70to100_UL2016APV")
WJetsHT70to100_UL2016APV.year = "UL2016APV"
WJetsHT70to100_UL2016APV.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
WJetsHT70to100_UL2016APV.sigma = 1264. * 1.21 #pb

WJetsHT100to200_UL2016APV = sample(WJcolor, 1, 1001, "W + Jets 100 < HT < 200", "WJetsHT100to200_UL2016APV")
WJetsHT100to200_UL2016APV.year = "UL2016APV"
WJetsHT100to200_UL2016APV.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WJetsHT100to200_UL2016APV.sigma = 1345 * 1.21 #pb

WJetsHT200to400_UL2016APV = sample(WJcolor, 1, 1001, "W + Jets 200 < HT < 400", "WJetsHT200to400_UL2016APV")
WJetsHT200to400_UL2016APV.year = "UL2016APV"
WJetsHT200to400_UL2016APV.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WJetsHT200to400_UL2016APV.sigma = 359.7 * 1.21 #pb

WJetsHT400to600_UL2016APV = sample(WJcolor, 1, 1001, "W + Jets 400 < HT < 600", "WJetsHT400to600_UL2016APV")
WJetsHT400to600_UL2016APV.year = "UL2016APV"
WJetsHT400to600_UL2016APV.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WJetsHT400to600_UL2016APV.sigma = 48.91 * 1.21 #pb

WJetsHT600to800_UL2016APV = sample(WJcolor, 1, 1001, "W + Jets 600 < HT < 800", "WJetsHT600to800_UL2016APV")
WJetsHT600to800_UL2016APV.year = "UL2016APV"
WJetsHT600to800_UL2016APV.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WJetsHT600to800_UL2016APV.sigma = 12.05 * 1.21 #pb

WJetsHT800to1200_UL2016APV = sample(WJcolor, 1, 1001, "W + Jets 800 < HT < 1200", "WJetsHT800to1200_UL2016APV")
WJetsHT800to1200_UL2016APV.year = "UL2016APV"
WJetsHT800to1200_UL2016APV.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WJetsHT800to1200_UL2016APV.sigma = 5.501 * 1.21 #pb

WJetsHT1200to2500_UL2016APV = sample(WJcolor, 1, 1001, "W + Jets 800 < HT < 1200", "WJetsHT1200to2500_UL2016APV")
WJetsHT1200to2500_UL2016APV.year = "UL2016APV"
WJetsHT1200to2500_UL2016APV.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WJetsHT1200to2500_UL2016APV.sigma = 1.329 * 1.21 #pb

WJetsHT2500toInf_UL2016APV = sample(WJcolor, 1, 1001, "W + Jets HT > 2500", "WJetsHT2500toInf_UL2016APV")
WJetsHT2500toInf_UL2016APV.year = "UL2016APV"
WJetsHT2500toInf_UL2016APV.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
WJetsHT2500toInf_UL2016APV.sigma = 0.008001 * 1.21 #pb

WJets_UL2016APV = sample(WJcolor, 1, 1001, "W + Jets", "WJets_UL2016APV")
WJets_UL2016APV.year = "UL2016APV"
WJets_UL2016APV.components = [
    WJetsHT70to100_UL2016APV,
    WJetsHT100to200_UL2016APV,
    WJetsHT200to400_UL2016APV,
    WJetsHT400to600_UL2016APV,
    WJetsHT600to800_UL2016APV,
    WJetsHT800to1200_UL2016APV,
    WJetsHT1200to2500_UL2016APV,
    WJetsHT2500toInf_UL2016APV,
]

WJets_0J_UL2016APV = sample(WJcolor, 1, 1001, "W + Jets 0J", "WJets_0J_UL2016APV")
WJets_0J_UL2016APV.year = "UL2016APV"
WJets_0J_UL2016APV.dataset = "/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WJets_0J_UL2016APV.sigma = 53330.0 * 1.21 #pb

WJets_1J_UL2016APV = sample(WJcolor, 1, 1001, "W + Jets 1J", "WJets_1J_UL2016APV")
WJets_1J_UL2016APV.year = "UL2016APV"
WJets_1J_UL2016APV.dataset = "/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WJets_1J_UL2016APV.sigma = 8875.0 * 1.21 #pb

WJets_2J_UL2016APV = sample(WJcolor, 1, 1001, "W + Jets 2J", "WJets_2J_UL2016APV")
WJets_2J_UL2016APV.year = "UL2016APV"
WJets_2J_UL2016APV.dataset = "/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WJets_2J_UL2016APV.sigma = 3338.0 * 1.21 #pb

WJets_Jbin_UL2016APV = sample(WJcolor, 1, 1001, "W + Jets #jets binned", "WJets_Jbin_UL2016APV")
WJets_Jbin_UL2016APV.year = "UL2016APV"
WJets_Jbin_UL2016APV.components = [
    WJets_0J_UL2016APV,
    WJets_1J_UL2016APV,
    WJets_2J_UL2016APV,
]

### WZ ###

WZ_UL2016APV = sample(WZcolor, 1, 1001, "WZ", "WZ_UL2016APV")
WZ_UL2016APV.year = "UL2016APV"
WZ_UL2016APV.dataset = "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WZ_UL2016APV.sigma = 27.59

### DY ###

#### to be replaced with v9 when available ####
DYJetsToLL_M10to50_UL2016APV = sample(WZcolor, 1, 1001, "DY+jets (10 < M_{ll} < 50 GeV", "DYJetsToLL_M10to50_UL2016APV")
DYJetsToLL_M10to50_UL2016APV.year = "UL2016APV"
DYJetsToLL_M10to50_UL2016APV.dataset = "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
DYJetsToLL_M10to50_UL2016APV.sigma = 18610.

DYJetsToLL_M50_UL2016APV = sample(WZcolor, 1, 1001, "DYJetsToLL_M50", "DYJetsToLL_M50_UL2016APV")
DYJetsToLL_M50_UL2016APV.year = "UL2016APV"
DYJetsToLL_M50_UL2016APV.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
DYJetsToLL_M50_UL2016APV.sigma = 6077.22

DYJetsToLL_M50_UL2016APV_ext = sample(WZcolor, 1, 1001, "DYJetsToLL_M50", "DYJetsToLL_M50_UL2016APV_ext")
DYJetsToLL_M50_UL2016APV_ext.year = "UL2016APV"
DYJetsToLL_M50_UL2016APV_ext.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
DYJetsToLL_M50_UL2016APV_ext.sigma = 6077.22

DYJetsToLL_UL2016APV = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_UL2016APV")
DYJetsToLL_UL2016APV.year = "UL2016APV"
DYJetsToLL_UL2016APV.components = [
    #DYJetsToLL_M10to50_UL2016APV,
    DYJetsToLL_M50_UL2016APV,
    #DYJetsToLL_M50_UL2016APV_ext,
]

DYJetsToLL_FxFx_UL2016APV = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_FxFx_UL2016APV")
DYJetsToLL_FxFx_UL2016APV.year = "UL2016APV"
DYJetsToLL_FxFx_UL2016APV.components = [
    #DYJetsToLL_M10to50_UL2016APV,
    DYJetsToLL_M50_FxFx_UL2016APV,
]

DYJetsToLL_0J_FxFx_UL2016APV = sample(DYcolor, 1, 1001, "DYJetsToLL_0J", "DYJetsToLL_0J_FxFx_UL2016APV")
DYJetsToLL_0J_FxFx_UL2016APV.year = "UL2016APV"
DYJetsToLL_0J_FxFx_UL2016APV.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
DYJetsToLL_0J_FxFx_UL2016APV.sigma = 5993 #5129.0

DYJetsToLL_1J_FxFx_UL2016APV = sample(DYcolor, 1, 1001, "DYJetsToLL_1J", "DYJetsToLL_1J_FxFx_UL2016APV")
DYJetsToLL_1J_FxFx_UL2016APV.year = "UL2016APV"
DYJetsToLL_1J_FxFx_UL2016APV.dataset = "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
DYJetsToLL_1J_FxFx_UL2016APV.sigma = 1474 #951.5

DYJetsToLL_2J_FxFx_UL2016APV = sample(DYcolor, 1, 1001, "DYJetsToLL_2J", "DYJetsToLL_2J_FxFx_UL2016APV")
DYJetsToLL_2J_FxFx_UL2016APV.year = "UL2016APV"
DYJetsToLL_2J_FxFx_UL2016APV.dataset = "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
DYJetsToLL_2J_FxFx_UL2016APV.sigma = 111.1 #361.4

DYJetsToLL_Jbin_FxFx_UL2016APV = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_Jbin_FxFx_UL2016APV")
DYJetsToLL_Jbin_FxFx_UL2016APV.year = "UL2016APV"
DYJetsToLL_Jbin_FxFx_UL2016APV.components = [
    DYJetsToLL_0J_FxFx_UL2016APV,
    DYJetsToLL_1J_FxFx_UL2016APV,
    DYJetsToLL_2J_FxFx_UL2016APV,
]

DYJetsToTauTau_FxFx_UL2016APV = sample(DYcolor, 1, 1001, "Z/#gamma + jets --> #tau#tau", "DYJetsToTauTau_FxFx_UL2016APV")
DYJetsToTauTau_FxFx_UL2016APV.year = "UL2016APV"
DYJetsToTauTau_FxFx_UL2016APV.dataset = "/DYJetsToTauTau_TauToMuEle_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
DYJetsToTauTau_FxFx_UL2016APV.sigma = 7181.0 #6077.22 #6529.0


### WpWp EWK ###

#### to be produced ####
WpWpJJ_EWK_UL2016APV = sample(EWVBScolor, 1, 1001, "EW SSWW VBS", "WpWpJJ_EWK_UL2016APV")
WpWpJJ_EWK_UL2016APV.sigma = 0.0287
WpWpJJ_EWK_UL2016APV.year = "UL2016APV"
WpWpJJ_EWK_UL2016APV.dataset = "/WpWpJJ_EWKnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"

### WpWp QCD ###

#### to be produced ####
WpWpJJ_QCD_UL2016APV = sample(QCDVBScolor, 1, 1001, "QCD SSWW", "WpWpJJ_QCD_UL2016APV")
WpWpJJ_QCD_UL2016APV.sigma = 0.02227
WpWpJJ_QCD_UL2016APV.year = "UL2016APV"
WpWpJJ_QCD_UL2016APV.dataset = "/WpWpJJ_QCDnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"

WpWpJJ_UL2016APV = sample(WWJJcolor, 1, 1001, "EW+QCD VBS SSWW", "WpWpJJ_UL2016APV")
WpWpJJ_UL2016APV.year = "UL2016APV"
WpWpJJ_UL2016APV.components = [
    WpWpJJ_EWK_UL2016APV,
    WpWpJJ_QCD_UL2016APV,
]

### VBS SSWW polarized ###

#### in production stage ####
VBS_SSWW_LL_SM_UL2016APV = sample(VBSLLcolor, 1, 1001, "VBS SSWW LL", "VBS_SSWW_LL_SM_UL2016APV")
VBS_SSWW_LL_SM_UL2016APV.sigma = 0.002014
VBS_SSWW_LL_SM_UL2016APV.year = "UL2016APV"
VBS_SSWW_LL_SM_UL2016APV.dataset = "/VBS_SSWW_LL_polarization_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"

#### in production stage ####
VBS_SSWW_TL_SM_UL2016APV = sample(VBSTLcolor, 1, 1001, "VBS SSWW TL", "VBS_SSWW_TL_SM_UL2016APV")
VBS_SSWW_TL_SM_UL2016APV.sigma = 0.01036
VBS_SSWW_TL_SM_UL2016APV.year = "UL2016APV"
VBS_SSWW_TL_SM_UL2016APV.dataset = "/VBS_SSWW_TL_polarization_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"

#### in production stage #### v2 available
VBS_SSWW_TT_SM_UL2016APV = sample(VBSTTcolor, 1, 1001, "VBS SSWW TT", "VBS_SSWW_TT_SM_UL2016APV")
VBS_SSWW_TT_SM_UL2016APV.sigma = 0.01595
VBS_SSWW_TT_SM_UL2016APV.year = "UL2016APV"
VBS_SSWW_TT_SM_UL2016APV.dataset = "/VBS_SSWW_TT_polarization_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"

VBS_SSWW_SM_UL2016APV = sample(VBScolor, 1, 1001, "VBS SSWW (pol. sum)", "VBS_SSWW_SM_UL2016APV")
VBS_SSWW_SM_UL2016APV.year = "UL2016APV"
VBS_SSWW_SM_UL2016APV.components = [
    VBS_SSWW_LL_SM_UL2016APV,
    VBS_SSWW_TL_SM_UL2016APV,
    VBS_SSWW_TT_SM_UL2016APV,
]

VBS_SSWW_cW_BSM_UL2016APV = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (only BSM)", "VBS_SSWW_cW_BSM_UL2016APV")
VBS_SSWW_cW_BSM_UL2016APV.year = "UL2016APV"
VBS_SSWW_cW_BSM_UL2016APV.dataset = "/VBS_SSWW_cW_BSM_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
VBS_SSWW_cW_BSM_UL2016APV.sigma = 0.01388

VBS_SSWW_cW_INT_UL2016APV = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (only INT)", "VBS_SSWW_cW_INT_UL2016APV")
VBS_SSWW_cW_INT_UL2016APV.year = "UL2016APV"
VBS_SSWW_cW_INT_UL2016APV.dataset = "/VBS_SSWW_cW_INT_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
VBS_SSWW_cW_INT_UL2016APV.sigma = 0.0009987

VBS_SSWW_cW_UL2016APV = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (BSM+INT)", "VBS_SSWW_cW_UL2016APV")
VBS_SSWW_cW_UL2016APV.year = "UL2016APV"
VBS_SSWW_cW_UL2016APV.components = [
    VBS_SSWW_cW_BSM_UL2016APV,
    VBS_SSWW_cW_INT_UL2016APV,
]

VBS_SSWW_cW_SM_UL2016APV = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} + SM", "VBS_SSWW_cW_SM_UL2016APV")
VBS_SSWW_cW_SM_UL2016APV.year = "UL2016APV"
VBS_SSWW_cW_SM_UL2016APV.components = [
    VBS_SSWW_cW_BSM_UL2016APV,
    VBS_SSWW_cW_INT_UL2016APV,
    VBS_SSWW_LL_SM_UL2016APV,
    VBS_SSWW_TL_SM_UL2016APV,
    VBS_SSWW_TT_SM_UL2016APV,
]

VBS_SSWW_cHW_BSM_UL2016APV = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (only BSM)", "VBS_SSWW_cHW_BSM_UL2016APV")
VBS_SSWW_cHW_BSM_UL2016APV.year = "UL2016APV"
VBS_SSWW_cHW_BSM_UL2016APV.dataset = "/VBS_SSWW_cHW_BSM_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
VBS_SSWW_cHW_BSM_UL2016APV.sigma = 0.0001415

VBS_SSWW_cHW_INT_UL2016APV = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (only INT)", "VBS_SSWW_cHW_INT_UL2016APV")
VBS_SSWW_cHW_INT_UL2016APV.year = "UL2016APV"
VBS_SSWW_cHW_INT_UL2016APV.dataset = "/VBS_SSWW_cHW_INT_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
VBS_SSWW_cHW_INT_UL2016APV.sigma = 0.0005059

VBS_SSWW_cHW_UL2016APV = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (BSM+INT)", "VBS_SSWW_cHW_UL2016APV")
VBS_SSWW_cHW_UL2016APV.year = "UL2016APV"
VBS_SSWW_cHW_UL2016APV.components = [
    VBS_SSWW_cHW_BSM_UL2016APV,
    VBS_SSWW_cHW_INT_UL2016APV,
]

VBS_SSWW_cHW_SM_UL2016APV = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} + SM", "VBS_SSWW_cHW_SM_UL2016APV")
VBS_SSWW_cHW_SM_UL2016APV.year = "UL2016APV"
VBS_SSWW_cHW_SM_UL2016APV.components = [
    VBS_SSWW_cHW_BSM_UL2016APV,
    VBS_SSWW_cHW_INT_UL2016APV,
    VBS_SSWW_LL_SM_UL2016APV,
    VBS_SSWW_TL_SM_UL2016APV,
    VBS_SSWW_TT_SM_UL2016APV,
]

VBS_SSWW_cW_cHW_UL2016APV = sample(CWcolor, 1, 1001, "VBS SSWW int c_{W} + c_{HW})", "VBS_SSWW_cW_cHW_UL2016APV")
VBS_SSWW_cW_cHW_UL2016APV.year = "UL2016APV"
VBS_SSWW_cW_cHW_UL2016APV.dataset = "/VBS_SSWW_cW_cHW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
VBS_SSWW_cW_cHW_UL2016APV.sigma = 0.002014

VBS_SSWW_DIM6_UL2016APV = sample(ROOT.kGreen+3, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_DIM6_UL2016APV")
VBS_SSWW_DIM6_UL2016APV.year = "UL2016APV"
VBS_SSWW_DIM6_UL2016APV.components = [
    VBS_SSWW_cHW_BSM_UL2016APV,
    VBS_SSWW_cW_BSM_UL2016APV,
    VBS_SSWW_cHW_INT_UL2016APV,
    VBS_SSWW_cW_INT_UL2016APV,
    VBS_SSWW_cW_cHW_UL2016APV,
]

VBS_SSWW_DIM6_SM_UL2016APV = sample(ROOT.kGreen+2, 1, 1001, "VBS SSWW dim-6 EFT + SM", "VBS_SSWW_DIM6_SM_UL2016APV")
VBS_SSWW_DIM6_SM_UL2016APV.year = "UL2016APV"
VBS_SSWW_DIM6_SM_UL2016APV.components = [
    VBS_SSWW_LL_SM_UL2016APV,
    VBS_SSWW_TL_SM_UL2016APV,
    VBS_SSWW_TT_SM_UL2016APV,
    VBS_SSWW_cHW_BSM_UL2016APV,
    VBS_SSWW_cHW_INT_UL2016APV, 
    VBS_SSWW_cW_BSM_UL2016APV,
    VBS_SSWW_cW_INT_UL2016APV,
    VBS_SSWW_cW_cHW_UL2016APV,
]

VBS_SSWW_aQGC_UL2016APV = sample(aQGCcolor, 1, 1001, "VBS SSWW dim-8 EFT", "VBS_SSWW_aQGC_UL2016APV")
VBS_SSWW_aQGC_UL2016APV.sigma = 0.1077
VBS_SSWW_aQGC_UL2016APV.year = "UL2016APV"
VBS_SSWW_aQGC_UL2016APV.dataset = "/WWJJ_SS_WToLNu_EWK_aQGC-FT-FS-FM_TuneCP5_13TeV_madgraph-pythia8/apiccine-NanoAODv9_UL2016APV_Legnaro-00000000000000000000000000000000/USER"

VBS_SSWW_aTGC_UL2016APV = sample(aTGCcolor, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_aTGC_UL2016APV")
VBS_SSWW_aTGC_UL2016APV.sigma = 1.083
VBS_SSWW_aTGC_UL2016APV.year = "UL2016APV"
VBS_SSWW_aTGC_UL2016APV.dataset = "/WplusminusWplusminus2JTo2L2Nu2J_EWK_dim6_TuneCP5_13TeV-madgraph-pythia8/apiccine-NanoAODv9_UL2016APV_Legnaro-00000000000000000000000000000000/USER"

VBS_SSWW_aTGC_mixed_UL2016APV = sample(aTGCcolor, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_aTGC_mixed_UL2016APV")
VBS_SSWW_aTGC_mixed_UL2016APV.sigma = 1.083
VBS_SSWW_aTGC_mixed_UL2016APV.year = "UL2016APV"
VBS_SSWW_aTGC_mixed_UL2016APV.dataset = "/WplusminusWplusminus2JTo2L2Nu2J_EWK_dim6_mixed_TuneCP5_13TeV-madgraph-pythia8/apiccine-NanoAODv9_UL2016APV_Legnaro-00000000000000000000000000000000/USER"

DataMuB1_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB1_UL2016APV")
DataMuB1_UL2016APV.runP = 'B-ver1'
DataMuB1_UL2016APV.year = "UL2016APV"
DataMuB1_UL2016APV.dataset = "/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"

DataMuB2_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB2_UL2016APV")
DataMuB2_UL2016APV.runP = 'B-ver2'
DataMuB2_UL2016APV.year = "UL2016APV"
DataMuB2_UL2016APV.dataset = "/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"

DataMuC_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuC_UL2016APV")
DataMuC_UL2016APV.runP = 'C'
DataMuC_UL2016APV.year = "UL2016APV"
DataMuC_UL2016APV.dataset = "/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"

DataMuD_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuD_UL2016APV")
DataMuD_UL2016APV.runP = 'D'
DataMuD_UL2016APV.year = "UL2016APV"
DataMuD_UL2016APV.dataset = "/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"

DataMuE_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuE_UL2016APV")
DataMuE_UL2016APV.runP = 'E'
DataMuE_UL2016APV.year = "UL2016APV"
DataMuE_UL2016APV.dataset = "/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"

DataMuF_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuF_UL2016APV")
DataMuF_UL2016APV.runP = 'F'
DataMuF_UL2016APV.year = "UL2016APV"
DataMuF_UL2016APV.dataset = "/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"

DataMu_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_UL2016APV")
DataMu_UL2016APV.year = "UL2016APV"
DataMu_UL2016APV.components =  [
    #DataMuB1_UL2016APV,
    DataMuB2_UL2016APV,
    DataMuC_UL2016APV,
    DataMuD_UL2016APV,
    DataMuE_UL2016APV,
    DataMuF_UL2016APV,
] 

DataEleB1_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB1_UL2016APV")
DataEleB1_UL2016APV.runP = 'B-ver1'
DataEleB1_UL2016APV.year = "UL2016APV"
DataEleB1_UL2016APV.dataset = "/SingleElectron/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"

DataEleB2_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB2_UL2016APV")
DataEleB2_UL2016APV.runP = 'B-ver2'
DataEleB2_UL2016APV.year = "UL2016APV"
DataEleB2_UL2016APV.dataset = "/SingleElectron/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"

DataEleC_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleC_UL2016APV")
DataEleC_UL2016APV.runP = 'C'
DataEleC_UL2016APV.year = "UL2016APV"
DataEleC_UL2016APV.dataset = "/SingleElectron/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"

DataEleD_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleD_UL2016APV")
DataEleD_UL2016APV.runP = 'D'
DataEleD_UL2016APV.year = "UL2016APV"
DataEleD_UL2016APV.dataset = "/SingleElectron/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"

DataEleE_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleE_UL2016APV")
DataEleE_UL2016APV.runP = 'E'
DataEleE_UL2016APV.year = "UL2016APV"
DataEleE_UL2016APV.dataset = "/SingleElectron/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"

DataEleF_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleF_UL2016APV")
DataEleF_UL2016APV.runP = 'F'
DataEleF_UL2016APV.year = "UL2016APV"
DataEleF_UL2016APV.dataset = "/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"

DataEle_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_UL2016APV")
DataEle_UL2016APV.year = "UL2016APV"
DataEle_UL2016APV.components =  [
    #DataEleB1_UL2016APV,
    DataEleB2_UL2016APV,
    DataEleC_UL2016APV,
    DataEleD_UL2016APV,
    DataEleE_UL2016APV,
    DataEleF_UL2016APV,
] 

DataHTB1_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB1_UL2016APV")
DataHTB1_UL2016APV.runP = 'B-ver1'
DataHTB1_UL2016APV.year = "UL2016APV"
DataHTB1_UL2016APV.dataset = "/JetHT/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHTB2_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB2_UL2016APV")
DataHTB2_UL2016APV.runP = 'B-ver2'
DataHTB2_UL2016APV.year = "UL2016APV"
DataHTB2_UL2016APV.dataset = "/JetHT/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHTC_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTC_UL2016APV")
DataHTC_UL2016APV.runP = 'C'
DataHTC_UL2016APV.year = "UL2016APV"
DataHTC_UL2016APV.dataset = "/JetHT/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHTD_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTD_UL2016APV")
DataHTD_UL2016APV.runP = 'D'
DataHTD_UL2016APV.year = "UL2016APV"
DataHTD_UL2016APV.dataset = "/JetHT/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHTE_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTE_UL2016APV")
DataHTE_UL2016APV.runP = 'E'
DataHTE_UL2016APV.year = "UL2016APV"
DataHTE_UL2016APV.dataset = "/JetHT/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHTF_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTF_UL2016APV")
DataHTF_UL2016APV.runP = 'F'
DataHTF_UL2016APV.year = "UL2016APV"
DataHTF_UL2016APV.dataset = "/JetHT/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHT_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_UL2016APV")
DataHT_UL2016APV.year = "UL2016APV"
DataHT_UL2016APV.components =  [
    #DataHTB1_UL2016APV,
    DataHTB2_UL2016APV,
    DataHTC_UL2016APV,
    DataHTD_UL2016APV,
    DataHTE_UL2016APV,
    DataHTF_UL2016APV,
] 

FakeElePromptTau_UL2016APV = sample(ROOT.kGray, 1, 1001, "Nonprompt e Prompt #tau", "FakeElePromptTau_UL2016APV")
FakeElePromptTau_UL2016APV.year = "UL2016APV"
FakeElePromptTau_UL2016APV.components = [
    DataEle_UL2016APV,
    #DataHT_UL2016APV,
    WJets_UL2016APV,
    DYJetsToLL_UL2016APV
]

PromptEleFakeTau_UL2016APV = sample(ROOT.kGray+2, 1, 1001, "Prompt e Fake #tau", "PromptEleFakeTau_UL2016APV")
PromptEleFakeTau_UL2016APV.year = "UL2016APV"
PromptEleFakeTau_UL2016APV.components = [
    DataEle_UL2016APV,
    #DataHT_UL2016APV,
    WJets_UL2016APV,
    DYJetsToLL_UL2016APV
]

FakeEleFakeTau_UL2016APV = sample(ROOT.kGray+3, 1, 1001, "Nonprompt e Fake #tau", "FakeEleFakeTau_UL2016APV")
FakeEleFakeTau_UL2016APV.year = "UL2016APV"
FakeEleFakeTau_UL2016APV.components = [
    DataEle_UL2016APV,
    #DataHT_UL2016APV,
    WJets_UL2016APV,
    DYJetsToLL_UL2016APV
]

FakeEle_UL2016APV = sample(ROOT.kGray, 1, 1001, "Nonprompt leptons", "FakeEle_UL2016APV")
FakeEle_UL2016APV.year = "UL2016APV"
FakeEle_UL2016APV.components = [
    DataEle_UL2016APV,
    #DataHT_UL2016APV,
    WJets_UL2016APV,
    DYJetsToLL_FxFx_UL2016APV,
    TT_UL2016APV,
]

FakeMuPromptTau_UL2016APV = sample(ROOT.kGray, 1, 1001, "Nonprompt #mu Prompt #tau", "FakeMuPromptTau_UL2016APV")
FakeMuPromptTau_UL2016APV.year = "UL2016APV"
FakeMuPromptTau_UL2016APV.components = [
    DataMu_UL2016APV,
    #DataHT_UL2016APV,
    WJets_UL2016APV,
    DYJetsToLL_UL2016APV
]

PromptMuFakeTau_UL2016APV = sample(ROOT.kGray+2, 1, 1001, "Prompt #mu Fake #tau", "PromptMuFakeTau_UL2016APV")
PromptMuFakeTau_UL2016APV.year = "UL2016APV"
PromptMuFakeTau_UL2016APV.components = [
    DataMu_UL2016APV,
    #DataHT_UL2016APV,
    WJets_UL2016APV,
    DYJetsToLL_UL2016APV
]

FakeMuFakeTau_UL2016APV = sample(ROOT.kGray+3, 1, 1001, "Nonprompt #mu Fake #tau", "FakeMuFakeTau_UL2016APV")
FakeMuFakeTau_UL2016APV.year = "UL2016APV"
FakeMuFakeTau_UL2016APV.components = [
    DataMu_UL2016APV,
    #DataHT_UL2016APV,
    WJets_UL2016APV,
    DYJetsToLL_UL2016APV
]

FakeMu_UL2016APV = sample(ROOT.kGray, 1, 1001, "Nonprompt leptons", "FakeMu_UL2016APV")
FakeMu_UL2016APV.year = "UL2016APV"
FakeMu_UL2016APV.components = [
    DataMu_UL2016APV,
    #DataHT_UL2016APV,
    WJets_UL2016APV,
    DYJetsToLL_FxFx_UL2016APV,
    TT_UL2016APV,
]

SampleHTFake_UL2016APV = sample(ROOT.kBlack, 1, 1001, "Sample for FR", "SampleHTFake_UL2016APV")
SampleHTFake_UL2016APV.year = "UL2016APV"
SampleHTFake_UL2016APV.components = [
    #DataHTB1_UL2016APV,
    DataHTB2_UL2016APV,
    DataHTC_UL2016APV,
    DataHTD_UL2016APV,
    DataHTE_UL2016APV,
    DataHTF_UL2016APV,
    WJetsHT70to100_UL2016APV,
    WJetsHT100to200_UL2016APV,
    WJetsHT200to400_UL2016APV,
    WJetsHT400to600_UL2016APV,
    WJetsHT600to800_UL2016APV,
    WJetsHT800to1200_UL2016APV,
    WJetsHT1200to2500_UL2016APV,
    WJetsHT2500toInf_UL2016APV,
    DYJetsToLL_M10to50_UL2016APV,
    DYJetsToLL_M50_UL2016APV,
    #DYJetsToLL_M50_UL2016APV_ext,
    TT_Had_UL2016APV,
    TT_SemiLep_UL2016APV,
    ZZTo2L2Nu_UL2016APV,
    ZZTo4L_UL2016APV,
    #GluGluToContinToZZTo2e2nu_UL2016APV,
    GluGluToContinToZZTo4e_UL2016APV,
    GluGluToContinToZZTo2e2mu_UL2016APV,
    GluGluToContinToZZTo2e2tau_UL2016APV,
    #GluGluToContinToZZTo2mu2nu_UL2016APV,
    GluGluToContinToZZTo4mu_UL2016APV,
    GluGluToContinToZZTo2mu2tau_UL2016APV,
    #GluGluToContinToZZTo2tau2nu_UL2016APV,
    GluGluToContinToZZTo4tau_UL2016APV,
]

######### UL2016 ##########

### ZZtoLep ###

ZZTo2L2Nu_UL2016 = sample(ZZcolor, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_UL2016")
ZZTo2L2Nu_UL2016.year = "UL2016"
ZZTo2L2Nu_UL2016.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
ZZTo2L2Nu_UL2016.sigma = 0.9738 #pb NLO

ZZTo4L_UL2016 = sample(ZZcolor, 1, 1001, "ZZ --> 4l", "ZZTo4L_UL2016") ### not sure is the right background
ZZTo4L_UL2016.year = "UL2016"
ZZTo4L_UL2016.dataset = "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
ZZTo4L_UL2016.sigma = 13.74 #pb NLO

GluGluToContinToZZTo2e2nu_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2nu", "GluGluToContinToZZTo2e2nu_UL2016")
GluGluToContinToZZTo2e2nu_UL2016.year = "UL2016"
GluGluToContinToZZTo2e2nu_UL2016.dataset = "/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2e2nu_UL2016.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo4e_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4e", "GluGluToContinToZZTo4e_UL2016")
GluGluToContinToZZTo4e_UL2016.year = "UL2016"
GluGluToContinToZZTo4e_UL2016.dataset = "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
GluGluToContinToZZTo4e_UL2016.sigma = 0.001586 # * 0.001 #pb

GluGluToContinToZZTo2e2mu_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2mu", "GluGluToContinToZZTo2e2mu_UL2016")
GluGluToContinToZZTo2e2mu_UL2016.year = "UL2016"
GluGluToContinToZZTo2e2mu_UL2016.dataset = "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2e2mu_UL2016.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2tau_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2tau", "GluGluToContinToZZTo2e2tau_UL2016")
GluGluToContinToZZTo2e2tau_UL2016.year = "UL2016"
GluGluToContinToZZTo2e2tau_UL2016.dataset = "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2e2tau_UL2016.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2nu_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2nu", "GluGluToContinToZZTo2mu2nu_UL2016")
GluGluToContinToZZTo2mu2nu_UL2016.year = "UL2016"
GluGluToContinToZZTo2mu2nu_UL2016.dataset = "/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2mu2nu_UL2016.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo4mu_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4mu", "GluGluToContinToZZTo4mu_UL2016")
GluGluToContinToZZTo4mu_UL2016.year = "UL2016"
GluGluToContinToZZTo4mu_UL2016.dataset = "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
GluGluToContinToZZTo4mu_UL2016.sigma = 0.001586 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2tau_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2tau", "GluGluToContinToZZTo2mu2tau_UL2016")
GluGluToContinToZZTo2mu2tau_UL2016.year = "UL2016"
GluGluToContinToZZTo2mu2tau_UL2016.dataset = "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_UL2016.sigma = 0.003194 # * 0.001 #pb to be checked

#### to be produced ####
GluGluToContinToZZTo2tau2nu_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2tau2nu", "GluGluToContinToZZTo2tau2nu_UL2016")
GluGluToContinToZZTo2tau2nu_UL2016.year = "UL2016"
GluGluToContinToZZTo2tau2nu_UL2016.dataset = ""
GluGluToContinToZZTo2tau2nu_UL2016.sigma = 0.003194# * 0.001 #pb to be checked

GluGluToContinToZZTo4tau_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4tau", "GluGluToContinToZZTo4tau_UL2016")
GluGluToContinToZZTo4tau_UL2016.year = "UL2016"
GluGluToContinToZZTo4tau_UL2016.dataset = "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo4tau_UL2016.sigma = 0.001586 # * 0.001 #pb to be checked

ZZtoLep_UL2016 = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_UL2016")
ZZtoLep_UL2016.year = "UL2016"
ZZtoLep_UL2016.components = [
    ZZTo2L2Nu_UL2016,
    ZZTo4L_UL2016,
    GluGluToContinToZZTo2e2nu_UL2016,
    GluGluToContinToZZTo4e_UL2016,
    GluGluToContinToZZTo2e2mu_UL2016,
    GluGluToContinToZZTo2e2tau_UL2016,
    GluGluToContinToZZTo2mu2nu_UL2016,
    GluGluToContinToZZTo4mu_UL2016,
    GluGluToContinToZZTo2mu2tau_UL2016,
    ##GluGluToContinToZZTo2tau2nu_UL2016,
    GluGluToContinToZZTo4tau_UL2016,
]

ZZtoLep_UL2016M = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_UL2016M")
ZZtoLep_UL2016M.year = "UL2016M"
ZZtoLep_UL2016M.components = [
    ZZtoLep_UL2016APV,
    ZZtoLep_UL2016,
]

### TT with quark ###

TT_SemiLep_UL2016 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_SemiLep_UL2016")
TT_SemiLep_UL2016.year = "UL2016"
TT_SemiLep_UL2016.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TT_SemiLep_UL2016.sigma = 831.76 * 0.438 #pb to check

TT_Had_UL2016 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_Had_UL2016")
TT_Had_UL2016.year = "UL2016"
TT_Had_UL2016.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TT_Had_UL2016.sigma = 831.76 * 0.457 #pb to check

TT_UL2016 = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_UL2016")
TT_UL2016.year = "UL2016"
TT_UL2016.components = [
    TT_SemiLep_UL2016,
    TT_Had_UL2016,
]

TT_UL2016M = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_UL2016M")
TT_UL2016M.year = "UL2016M"
TT_UL2016M.components = [
    TT_UL2016APV,
    TT_UL2016,
]

TT_Mtt_700to1000_UL2016 = sample(TTcolor, 1, 1001, "t#bar{t} 700 < M_{tt} < 1000 GeV", "TT_Mtt_700to1000_UL2016")
TT_Mtt_700to1000_UL2016.year = "UL2016"
TT_Mtt_700to1000_UL2016.dataset = "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TT_Mtt_700to1000_UL2016.sigma = 66.85

TT_Mtt_1000toInf_UL2016 = sample(TTcolor, 1, 1001, "t#bar{t} M_{tt} > 1000 GeV", "TT_Mtt_1000toInf_UL2016")
TT_Mtt_1000toInf_UL2016.year = "UL2016"
TT_Mtt_1000toInf_UL2016.dataset = "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TT_Mtt_1000toInf_UL2016.sigma = 16.38

TT_Mtt_UL2016 = sample(TTcolor, 1, 1001, "t#bar{t} M_{tt} > 700 GeV", "TT_Mtt_UL2016")
TT_Mtt_UL2016.year = "UL2016"
TT_Mtt_UL2016.components = [
    TT_Mtt_700to1000_UL2016,
    TT_Mtt_1000toInf_UL2016,
]

TT_Mtt_UL2016M = sample(TTcolor, 1, 1001, "t#bar{t} M_{tt} > 700 GeV", "TT_Mtt_UL2016M")
TT_Mtt_UL2016M.year = "UL2016M"
TT_Mtt_UL2016M.components = [
    TT_Mtt_UL2016APV,
    TT_Mtt_UL2016,
]

TTTo2L2Nu_UL2016 = sample(TTdilepcolor, 1, 1001, "t#bar{t} dilep.", "TTTo2L2Nu_UL2016")
TTTo2L2Nu_UL2016.year = "UL2016"
TTTo2L2Nu_UL2016.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTTo2L2Nu_UL2016.sigma = 72.1 #831.76 * 0.105 #pb

TTTo2L2Nu_UL2016M = sample(TTdilepcolor, 1, 1001, "t#bar{t} dilep.", "TTTo2L2Nu_UL2016M")
TTTo2L2Nu_UL2016M.year = "UL2016M"
TTTo2L2Nu_UL2016M.components= [
    TTTo2L2Nu_UL2016APV,
    TTTo2L2Nu_UL2016,
]

TT_beff_UL2016 = sample(TTcolor, 1, 1001, "t#bar{t} inclusive", "TT_beff_UL2016")
TT_beff_UL2016.year = "UL2016"
TT_beff_UL2016.components = [
    TT_SemiLep_UL2016,
    TT_Had_UL2016,
    TTTo2L2Nu_UL2016,
]

### TVX ###

TTGJets_UL2016 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTGJets_UL2016")
TTGJets_UL2016.year = "UL2016"
TTGJets_UL2016.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTGJets_UL2016.sigma = 3.697

TTZToQQ_UL2016 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTZToQQ_UL2016")
TTZToQQ_UL2016.year = "UL2016"
TTZToQQ_UL2016.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTZToQQ_UL2016.sigma = 0.5297

TTZToLLNuNu_UL2016 = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> 2l2#nu", "TTZToLLNuNu_UL2016")
TTZToLLNuNu_UL2016.year = "UL2016"
TTZToLLNuNu_UL2016.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTZToLLNuNu_UL2016.sigma = 0.2529

TTWJetsToQQ_UL2016 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToQQ_UL2016")
TTWJetsToQQ_UL2016.year = "UL2016"
TTWJetsToQQ_UL2016.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTWJetsToQQ_UL2016.sigma = 0.4062

TTWJetsToLNu_UL2016 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToLNu_UL2016")
TTWJetsToLNu_UL2016.year = "UL2016"
TTWJetsToLNu_UL2016.dataset = "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
TTWJetsToLNu_UL2016.sigma = 0.216

tZq_ll_4f_UL2016 = sample(TVXcolor, 1, 1001, "tZq --> ll", "tZq_ll_4f_UL2016")
tZq_ll_4f_UL2016.year = "UL2016"
tZq_ll_4f_UL2016.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
tZq_ll_4f_UL2016.sigma = 0.0758

TVX_UL2016 = sample(TVXcolor, 1, 1001, "tVX", "TVX_UL2016")
TVX_UL2016.year = "UL2016"
TVX_UL2016.components = [
    TTGJets_UL2016,
    TTZToQQ_UL2016,
    TTZToLLNuNu_UL2016,
    TTWJetsToQQ_UL2016,
    TTWJetsToLNu_UL2016,
    tZq_ll_4f_UL2016,
]

TVX_UL2016M = sample(TVXcolor, 1, 1001, "tVX", "TVX_UL2016M")
TVX_UL2016M.year = "UL2016M"
TVX_UL2016M.components = [
    TVX_UL2016APV,
    TVX_UL2016,
]

### VG ###

ZG_UL2016 = sample(VGcolor, 1, 1001, "Z #gamma", "ZG_UL2016")
ZG_UL2016.year = "UL2016"
ZG_UL2016.dataset = "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
ZG_UL2016.sigma = 51.1 # to check

WG_UL2016 = sample(VGcolor, 1, 1001, "W #gamma", "WG_UL2016")
WG_UL2016.year = "UL2016"
WG_UL2016.dataset = "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WG_UL2016.sigma = 191.3 # to check

VG_UL2016 = sample(VGcolor, 1, 1001, "V#gamma", "VG_UL2016")
VG_UL2016.year = "UL2016"
VG_UL2016.components = [
    ZG_UL2016,
    WG_UL2016,
]

### WrongSign ###

WWto2L2Nu_UL2016 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "WWto2L2Nu_UL2016")
WWto2L2Nu_UL2016.year = "UL2016"
WWto2L2Nu_UL2016.dataset = "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WWto2L2Nu_UL2016.sigma = 12.178

GluGluToWWToENEN_UL2016 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "GluGluToWWToENEN_UL2016")
GluGluToWWToENEN_UL2016.year = "UL2016"
GluGluToWWToENEN_UL2016.dataset = "/GluGluToWWToENEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToENEN_UL2016.sigma = 63.87 * 1./9. * 0.001 * 2. #36.8 * 1./9. * 1.4 * 0.001 

GluGluToWWToENMN_UL2016 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "GluGluToWWToENMN_UL2016")
GluGluToWWToENMN_UL2016.year = "UL2016"
GluGluToWWToENMN_UL2016.dataset = "/GluGluToWWToENMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToENMN_UL2016.sigma = 63.87 * 1./9. * 0.001 #36.8 * 1./9. * 1.4 * 0.001 

GluGluToWWToENTN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToENTN_UL2016")
GluGluToWWToENTN_UL2016.year = "UL2016"
GluGluToWWToENTN_UL2016.dataset = "/GluGluToWWToENTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToENTN_UL2016.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToMNEN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNEN_UL2016")
GluGluToWWToMNEN_UL2016.year = "UL2016"
GluGluToWWToMNEN_UL2016.dataset = "/GluGluToWWToMNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToMNEN_UL2016.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToMNMN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNMN_UL2016")
GluGluToWWToMNMN_UL2016.year = "UL2016"
GluGluToWWToMNMN_UL2016.dataset = "/GluGluToWWToMNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToMNMN_UL2016.sigma = 63.87 * 1./9. * 0.001 * 2. #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToMNTN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNTN_UL2016")
GluGluToWWToMNTN_UL2016.year = "UL2016"
GluGluToWWToMNTN_UL2016.dataset = "/GluGluToWWToMNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToMNTN_UL2016.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToTNEN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNEN_UL2016")
GluGluToWWToTNEN_UL2016.year = "UL2016"
GluGluToWWToTNEN_UL2016.dataset = "/GluGluToWWToTNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToTNEN_UL2016.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToTNMN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNMN_UL2016")
GluGluToWWToTNMN_UL2016.year = "UL2016"
GluGluToWWToTNMN_UL2016.dataset = "/GluGluToWWToTNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToTNMN_UL2016.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToTNTN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNTN_UL2016")
GluGluToWWToTNTN_UL2016.year = "UL2016"
GluGluToWWToTNTN_UL2016.dataset = "/GluGluToWWToTNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToTNTN_UL2016.sigma = 63.87 * 1./9. * 0.001 * 2. #36.81 * 1./9. * 1.4 * 0.001 

ST_tW_top_UL2016 = sample(WScolor, 1, 1001, "Single top", "ST_tW_top_UL2016")
ST_tW_top_UL2016.year = "UL2016"
ST_tW_top_UL2016.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
ST_tW_top_UL2016.sigma = 35.85 

ST_tW_antitop_UL2016 = sample(WScolor, 1, 1001, "Single top", "ST_tW_antitop_UL2016")
ST_tW_antitop_UL2016.year = "UL2016"
ST_tW_antitop_UL2016.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
ST_tW_antitop_UL2016.sigma =  35.85 

GluGluHToWWTo2L2Nu_UL2016 = sample(WScolor, 1, 1001, "Single top", "GluGluHToWWTo2L2Nu_UL2016")
GluGluHToWWTo2L2Nu_UL2016.year = "UL2016"
GluGluHToWWTo2L2Nu_UL2016.dataset = "/GluGluHToWWTo2L2Nu_M125_TuneCP5_PSw_13TeV-powheg2-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluHToWWTo2L2Nu_UL2016.sigma = 1.0315

GluGluHToZZTo4L_UL2016 = sample(WScolor, 1, 1001, "Single top", "GluGluHToZZTo4L_UL2016")
GluGluHToZZTo4L_UL2016.year = "UL2016"
GluGluHToZZTo4L_UL2016.dataset = "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
GluGluHToZZTo4L_UL2016.sigma = 0.0118 # check nowe

#### to be replaced with v9 when available ####
GluGluHToTauTau_UL2016 = sample(WScolor, 1, 1001, "Single top", "GluGluHToTauTau_UL2016")
GluGluHToTauTau_UL2016.year = "UL2016"
GluGluHToTauTau_UL2016.dataset = "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"
GluGluHToTauTau_UL2016.sigma = 2.7757# check nowe

VBFHToWWTo2L2Nu_UL2016 = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToWWTo2L2Nu_UL2016")
VBFHToWWTo2L2Nu_UL2016.year = "UL2016"
VBFHToWWTo2L2Nu_UL2016.dataset = "/VBFHToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
VBFHToWWTo2L2Nu_UL2016.sigma = 0.0896 # check nowe

VBFHToTauTau_UL2016 = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToTauTau_UL2016")
VBFHToTauTau_UL2016.year = "UL2016"
VBFHToTauTau_UL2016.dataset = "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
VBFHToTauTau_UL2016.sigma = 0.237 # check nowe

ttHToNonbb_UL2016 = sample(WScolor, 1, 1001, "ttH", "ttHToNonbb_UL2016")
ttHToNonbb_UL2016.year = "UL2016"
ttHToNonbb_UL2016.dataset = "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
ttHToNonbb_UL2016.sigma = 0.2120 # check nowe

VHToNonbb_UL2016 = sample(WScolor, 1, 1001, "VH", "VHToNonbb_UL2016")
VHToNonbb_UL2016.year = "UL2016"
VHToNonbb_UL2016.dataset = "/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
VHToNonbb_UL2016.sigma = 0.952 # check nowe

DYJetsToLL_M50_FxFx_UL2016 = sample(WZcolor, 1, 1001, "DYJetsToLL_M50", "DYJetsToLL_M50_FxFx_UL2016")
DYJetsToLL_M50_FxFx_UL2016.year = "UL2016"
DYJetsToLL_M50_FxFx_UL2016.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
DYJetsToLL_M50_FxFx_UL2016.sigma = 7181.0 #6077.22 #6529.0


WrongSign_UL2016 = sample(WScolor, 1, 1001, "OS + (Z/#gamma + jets)", "WrongSign_UL2016")
WrongSign_UL2016.year = "UL2016"
WrongSign_UL2016.components = [
    WWto2L2Nu_UL2016,
    GluGluToWWToENEN_UL2016,
    GluGluToWWToENMN_UL2016,
    GluGluToWWToENTN_UL2016,
    GluGluToWWToMNEN_UL2016,
    GluGluToWWToMNMN_UL2016,
    GluGluToWWToMNTN_UL2016,
    GluGluToWWToTNEN_UL2016,
    GluGluToWWToTNMN_UL2016,
    GluGluToWWToTNTN_UL2016,
    ST_tW_top_UL2016,
    ST_tW_antitop_UL2016,
    GluGluHToWWTo2L2Nu_UL2016,
    GluGluHToZZTo4L_UL2016,
    GluGluHToTauTau_UL2016,
    VBFHToWWTo2L2Nu_UL2016,
    VBFHToTauTau_UL2016,
    ttHToNonbb_UL2016,
    VHToNonbb_UL2016,
    DYJetsToLL_M50_FxFx_UL2016,
]

WrongSign_ML_UL2016 = sample(WScolor, 1, 1001, "OS", "WrongSign_ML_UL2016")
WrongSign_ML_UL2016.year = "UL2016"
WrongSign_ML_UL2016.components = [
    WWto2L2Nu_UL2016,
    GluGluToWWToENEN_UL2016,
    GluGluToWWToENMN_UL2016,
    GluGluToWWToENTN_UL2016,
    GluGluToWWToMNEN_UL2016,
    GluGluToWWToMNMN_UL2016,
    GluGluToWWToMNTN_UL2016,
    GluGluToWWToTNEN_UL2016,
    GluGluToWWToTNMN_UL2016,
    GluGluToWWToTNTN_UL2016,
    ST_tW_top_UL2016,
    ST_tW_antitop_UL2016,
    GluGluHToWWTo2L2Nu_UL2016,
    GluGluHToZZTo4L_UL2016,
    GluGluHToTauTau_UL2016,
    VBFHToWWTo2L2Nu_UL2016,
    VBFHToTauTau_UL2016,
    ttHToNonbb_UL2016,
    VHToNonbb_UL2016,
]

WrongSign_UL2016M = sample(WScolor, 1, 1001, "OS + (Z/#gamma + jets)", "WrongSign_UL2016M")
WrongSign_UL2016M.year = "UL2016M"
WrongSign_UL2016M.components = [
    WrongSign_UL2016APV,
    WrongSign_UL2016,
]

WrongSign_ML_UL2016M = sample(WScolor, 1, 1001, "OS", "WrongSign_ML_UL2016M")
WrongSign_ML_UL2016M.year = "UL2016M"
WrongSign_ML_UL2016M.components = [
    WrongSign_ML_UL2016APV,
    WrongSign_ML_UL2016,
]

### Triboson ###

WWTo2L2Nu_DoubleScattering_UL2016 = sample(TBcolor, 1, 1001, "WWTo2L2Nu_DoubleScattering", "WWTo2L2Nu_DoubleScattering_UL2016")
WWTo2L2Nu_DoubleScattering_UL2016.year = "UL2016"
WWTo2L2Nu_DoubleScattering_UL2016.dataset = ""
WWTo2L2Nu_DoubleScattering_UL2016.sigma =  0.1703#pb

WWW_4F_UL2016 = sample(TBcolor, 1, 1001, "WWW_4F", "WWW_4F_UL2016")
WWW_4F_UL2016.year = "UL2016"
WWW_4F_UL2016.dataset = "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM"
WWW_4F_UL2016.sigma = 0.2086#pb

WWZ_4F_UL2016 = sample(TBcolor, 1, 1001, "WWZ_4F", "WWZ_4F_UL2016")
WWZ_4F_UL2016.year = "UL2016"
WWZ_4F_UL2016.dataset = "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM"
WWZ_4F_UL2016.sigma = 0.1651#pb

WZZ_UL2016 = sample(TBcolor, 1, 1001, "WZZ", "WZZ_UL2016")
WZZ_UL2016.year = "UL2016"
WZZ_UL2016.dataset = "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM"
WZZ_UL2016.sigma = 0.05565#pb

ZZZ_UL2016 = sample(TBcolor, 1, 1001, "ZZZ", "ZZZ_UL2016")
ZZZ_UL2016.year = "UL2016"
ZZZ_UL2016.dataset = "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM"
ZZZ_UL2016.sigma = 0.01398#pb

WWG_UL2016 = sample(TBcolor, 1, 1001, "WWG", "WWG_UL2016")
WWG_UL2016.year = "UL2016"
WWG_UL2016.dataset = "/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WWG_UL2016.sigma = 0.2147#pb

Triboson_UL2016 = sample(TBcolor, 1, 1001, "Triboson", "Triboson_UL2016")
Triboson_UL2016.year = "UL2016"
Triboson_UL2016.components = [
    #WWTo2L2Nu_DoubleScattering_UL2016,
    WWW_4F_UL2016,
    WWZ_4F_UL2016,
    WZZ_UL2016,
    ZZZ_UL2016,
    WWG_UL2016,
]

Triboson_UL2016M = sample(TBcolor, 1, 1001, "Triboson", "Triboson_UL2016M")
Triboson_UL2016M.year = "UL2016M"
Triboson_UL2016M.components = [
    Triboson_UL2016APV,
    Triboson_UL2016,
]

### WJets ###

WJetsHT70to100_UL2016 = sample(WJcolor, 1, 1001, "W + Jets", "WJetsHT70to100_UL2016")
WJetsHT70to100_UL2016.year = "UL2016"
WJetsHT70to100_UL2016.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WJetsHT70to100_UL2016.sigma = 1264. * 1.21 #pb

WJetsHT100to200_UL2016 = sample(WJcolor, 1, 1001, "W + Jets 100 < HT < 200", "WJetsHT100to200_UL2016")
WJetsHT100to200_UL2016.year = "UL2016"
WJetsHT100to200_UL2016.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WJetsHT100to200_UL2016.sigma = 1345 * 1.21 #pb

WJetsHT200to400_UL2016 = sample(WJcolor, 1, 1001, "W + Jets 200 < HT < 400", "WJetsHT200to400_UL2016")
WJetsHT200to400_UL2016.year = "UL2016"
WJetsHT200to400_UL2016.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WJetsHT200to400_UL2016.sigma = 359.7 * 1.21 #pb

WJetsHT400to600_UL2016 = sample(WJcolor, 1, 1001, "W + Jets 400 < HT < 600", "WJetsHT400to600_UL2016")
WJetsHT400to600_UL2016.year = "UL2016"
WJetsHT400to600_UL2016.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WJetsHT400to600_UL2016.sigma = 48.91 * 1.21 #pb

WJetsHT600to800_UL2016 = sample(WJcolor, 1, 1001, "W + Jets 600 < HT < 800", "WJetsHT600to800_UL2016")
WJetsHT600to800_UL2016.year = "UL2016"
WJetsHT600to800_UL2016.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WJetsHT600to800_UL2016.sigma = 12.05 * 1.21 #pb

WJetsHT800to1200_UL2016 = sample(WJcolor, 1, 1001, "W + Jets 800 < HT < 1200", "WJetsHT800to1200_UL2016")
WJetsHT800to1200_UL2016.year = "UL2016"
WJetsHT800to1200_UL2016.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WJetsHT800to1200_UL2016.sigma = 5.501 * 1.21 #pb

WJetsHT1200to2500_UL2016 = sample(WJcolor, 1, 1001, "W + Jets 1200 < HT < 2500", "WJetsHT1200to2500_UL2016")
WJetsHT1200to2500_UL2016.year = "UL2016"
WJetsHT1200to2500_UL2016.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WJetsHT1200to2500_UL2016.sigma = 1.329 * 1.21 #pb

WJetsHT2500toInf_UL2016 = sample(WJcolor, 1, 1001, "W + Jets HT > 2500", "WJetsHT2500toInf_UL2016")
WJetsHT2500toInf_UL2016.year = "UL2016"
WJetsHT2500toInf_UL2016.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
WJetsHT2500toInf_UL2016.sigma = 0.008001 * 1.21 #pb

WJets_UL2016 = sample(WJcolor, 1, 1001, "W + Jets", "WJets_UL2016")
WJets_UL2016.year = "UL2016"
WJets_UL2016.components = [
    WJetsHT70to100_UL2016,
    WJetsHT100to200_UL2016,
    WJetsHT200to400_UL2016,
    WJetsHT400to600_UL2016,
    WJetsHT600to800_UL2016,
    WJetsHT800to1200_UL2016,
    WJetsHT1200to2500_UL2016,
    WJetsHT2500toInf_UL2016,
]

WJets_UL2016M = sample(WJcolor, 1, 1001, "W + Jets", "WJets_UL2016M")
WJets_UL2016M.year = "UL2016M"
WJets_UL2016M.components = [
    WJets_UL2016APV,
    WJets_UL2016,
]

WJets_0J_UL2016 = sample(WJcolor, 1, 1001, "W + Jets 0J", "WJets_0J_UL2016")
WJets_0J_UL2016.year = "UL2016"
WJets_0J_UL2016.dataset = "/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WJets_0J_UL2016.sigma = 53330.0 * 1.21 #pb

WJets_1J_UL2016 = sample(WJcolor, 1, 1001, "W + Jets 1J", "WJets_1J_UL2016")
WJets_1J_UL2016.year = "UL2016"
WJets_1J_UL2016.dataset = "/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WJets_1J_UL2016.sigma = 8875.0 * 1.21 #pb

WJets_2J_UL2016 = sample(WJcolor, 1, 1001, "W + Jets 2J", "WJets_2J_UL2016")
WJets_2J_UL2016.year = "UL2016"
WJets_2J_UL2016.dataset = "/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WJets_2J_UL2016.sigma = 3338.0 * 1.21 #pb

WJets_Jbin_UL2016 = sample(WJcolor, 1, 1001, "W + Jets #jets binned", "WJets_Jbin_UL2016")
WJets_Jbin_UL2016.year = "UL2016"
WJets_Jbin_UL2016.components = [
    WJets_0J_UL2016,
    WJets_1J_UL2016,
    WJets_2J_UL2016,
]

WJets_Jbin_UL2016M = sample(WJcolor, 1, 1001, "W + Jets #jets binned", "WJets_Jbin_UL2016M")
WJets_Jbin_UL2016M.year = "UL2016M"
WJets_Jbin_UL2016M.components = [
    WJets_Jbin_UL2016APV,
    WJets_Jbin_UL2016,
]

### WZ ###

WZ_UL2016 = sample(WZcolor, 1, 1001, "WZ", "WZ_UL2016")
WZ_UL2016.year = "UL2016"
WZ_UL2016.dataset = "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WZ_UL2016.sigma = 27.59

WZ_UL2016M = sample(WZcolor, 1, 1001, "WZ", "WZ_UL2016M")
WZ_UL2016M.year = "UL2016M"
WZ_UL2016M.components = [
    WZ_UL2016APV,
    WZ_UL2016,
]

### DYJets ###

### to be replaced with v9 when available ####
DYJetsToLL_M10to50_UL2016 = sample(WZcolor, 1, 1001, "DY+jets (10 < M_{ll} < 50 GeV", "DYJetsToLL_M10to50_UL2016")
DYJetsToLL_M10to50_UL2016.year = "UL2016"
DYJetsToLL_M10to50_UL2016.dataset = "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
DYJetsToLL_M10to50_UL2016.sigma = 18610.

DYJetsToLL_M50_UL2016 = sample(WZcolor, 1, 1001, "DYJetsToLL_M50", "DYJetsToLL_M50_UL2016")
DYJetsToLL_M50_UL2016.year = "UL2016"
DYJetsToLL_M50_UL2016.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_Pilot_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
DYJetsToLL_M50_UL2016.sigma = 6077.22

DYJetsToLL_M50_UL2016_ext = sample(WZcolor, 1, 1001, "DYJetsToLL_M50", "DYJetsToLL_M50_UL2016_ext")
DYJetsToLL_M50_UL2016_ext.year = "UL2016"
DYJetsToLL_M50_UL2016_ext.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-FlatPU0to75_20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
DYJetsToLL_M50_UL2016_ext.sigma = 6077.22

DYJetsToLL_UL2016 = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_UL2016")
DYJetsToLL_UL2016.year = "UL2016"
DYJetsToLL_UL2016.components = [
    #DYJetsToLL_M10to50_UL2016,
    DYJetsToLL_M50_UL2016,
    #DYJetsToLL_M50_UL2016_ext,
]

DYJetsToLL_UL2016M = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_UL2016M")
DYJetsToLL_UL2016M.year = "UL2016M"
DYJetsToLL_UL2016M.components = [
    DYJetsToLL_UL2016APV,
    DYJetsToLL_UL2016,
]

DYJetsToLL_FxFx_UL2016 = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_FxFx_UL2016")
DYJetsToLL_FxFx_UL2016.year = "UL2016"
DYJetsToLL_FxFx_UL2016.components = [
    #DYJetsToLL_M10to50_UL2016,
    DYJetsToLL_M50_FxFx_UL2016,
]

DYJetsToLL_FxFx_UL2016M = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_FxFx_UL2016M")
DYJetsToLL_FxFx_UL2016M.year = "UL2016M"
DYJetsToLL_FxFx_UL2016M.components = [
    DYJetsToLL_FxFx_UL2016APV,
    DYJetsToLL_FxFx_UL2016,
]

DYJetsToLL_0J_FxFx_UL2016 = sample(DYcolor, 1, 1001, "DYJetsToLL_0J", "DYJetsToLL_0J_FxFx_UL2016")
DYJetsToLL_0J_FxFx_UL2016.year = "UL2016"
DYJetsToLL_0J_FxFx_UL2016.dataset = "/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
DYJetsToLL_0J_FxFx_UL2016.sigma = 5993 #5129.0

DYJetsToLL_1J_FxFx_UL2016 = sample(DYcolor, 1, 1001, "DYJetsToLL_1J", "DYJetsToLL_1J_FxFx_UL2016")
DYJetsToLL_1J_FxFx_UL2016.year = "UL2016"
DYJetsToLL_1J_FxFx_UL2016.dataset = "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
DYJetsToLL_1J_FxFx_UL2016.sigma = 1474 #951.5

DYJetsToLL_2J_FxFx_UL2016 = sample(DYcolor, 1, 1001, "DYJetsToLL_2J", "DYJetsToLL_2J_FxFx_UL2016")
DYJetsToLL_2J_FxFx_UL2016.year = "UL2016"
DYJetsToLL_2J_FxFx_UL2016.dataset = "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
DYJetsToLL_2J_FxFx_UL2016.sigma = 111.1 #361.4

DYJetsToLL_Jbin_FxFx_UL2016 = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_Jbin_FxFx_UL2016")
DYJetsToLL_Jbin_FxFx_UL2016.year = "UL2016"
DYJetsToLL_Jbin_FxFx_UL2016.components = [
    DYJetsToLL_0J_FxFx_UL2016,
    DYJetsToLL_1J_FxFx_UL2016,
    DYJetsToLL_2J_FxFx_UL2016,
]

DYJetsToLL_Jbin_FxFx_UL2016M = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_Jbin_FxFx_UL2016M")
DYJetsToLL_Jbin_FxFx_UL2016M.year = "UL2016M"
DYJetsToLL_Jbin_FxFx_UL2016M.components = [
    DYJetsToLL_Jbin_FxFx_UL2016APV,
    DYJetsToLL_Jbin_FxFx_UL2016,
]

### WpWp EWK ###

#### to be produced ####
WpWpJJ_EWK_UL2016 = sample(EWVBScolor, 1, 1001, "EW SSWW VBS", "WpWpJJ_EWK_UL2016")
WpWpJJ_EWK_UL2016.sigma = 0.0287
WpWpJJ_EWK_UL2016.year = "UL2016"
WpWpJJ_EWK_UL2016.dataset = "/WpWpJJ_EWKnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"

### WpWp QCD ###

#### to be produced ####
WpWpJJ_QCD_UL2016 = sample(QCDVBScolor, 1, 1001, "QCD SSWW", "WpWpJJ_QCD_UL2016")
WpWpJJ_QCD_UL2016.sigma = 0.02227
WpWpJJ_QCD_UL2016.year = "UL2016"
WpWpJJ_QCD_UL2016.dataset = "/WpWpJJ_QCDnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"

WpWpJJ_UL2016 = sample(WWJJcolor, 1, 1001, "EW+QCD VBS SSWW", "WpWpJJ_UL2016")
WpWpJJ_UL2016.year = "UL2016"
WpWpJJ_UL2016.components = [
    WpWpJJ_EWK_UL2016,
    WpWpJJ_QCD_UL2016,
]

WpWpJJ_EWK_UL2016M = sample(EWVBScolor, 1, 1001, "EW VBS SSWW", "WpWpJJ_EWK_UL2016M")
WpWpJJ_EWK_UL2016M.year = "UL2016M"
WpWpJJ_EWK_UL2016M.components = [
    WpWpJJ_EWK_UL2016APV,
    WpWpJJ_EWK_UL2016,
]

WpWpJJ_QCD_UL2016M = sample(QCDVBScolor, 1, 1001, "QCD SSWW", "WpWpJJ_QCD_UL2016M")
WpWpJJ_QCD_UL2016M.year = "UL2016M"
WpWpJJ_QCD_UL2016M.components = [
    WpWpJJ_QCD_UL2016APV,
    WpWpJJ_QCD_UL2016,
]

WpWpJJ_UL2016M = sample(WWJJcolor, 1, 1001, "EW+QCD SSWW", "WpWpJJ_UL2016M")
WpWpJJ_UL2016M.year = "UL2016M"
WpWpJJ_UL2016M.components = [
    WpWpJJ_UL2016APV,
    WpWpJJ_UL2016,
]

### VBS SSWW polarized ###

#### in production stage ####
VBS_SSWW_LL_SM_UL2016 = sample(VBSLLcolor, 1, 1001, "VBS SSWW LL", "VBS_SSWW_LL_SM_UL2016")
VBS_SSWW_LL_SM_UL2016.sigma = 0.002014
VBS_SSWW_LL_SM_UL2016.year = "UL2016"
VBS_SSWW_LL_SM_UL2016.dataset = "/VBS_SSWW_LL_polarization_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"

#### in production stage ####
VBS_SSWW_TL_SM_UL2016 = sample(VBSTLcolor, 1, 1001, "VBS SSWW TL", "VBS_SSWW_TL_SM_UL2016")
VBS_SSWW_TL_SM_UL2016.sigma = 0.01036
VBS_SSWW_TL_SM_UL2016.year = "UL2016"
VBS_SSWW_TL_SM_UL2016.dataset = "/VBS_SSWW_TL_polarization_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"

#### in production stage ####
VBS_SSWW_TT_SM_UL2016 = sample(VBSTTcolor, 1, 1001, "VBS SSWW TT", "VBS_SSWW_TT_SM_UL2016")
VBS_SSWW_TT_SM_UL2016.sigma = 0.01595
VBS_SSWW_TT_SM_UL2016.year = "UL2016"
VBS_SSWW_TT_SM_UL2016.dataset = "/VBS_SSWW_TT_polarization_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"

VBS_SSWW_SM_UL2016 = sample(VBScolor, 1, 1001, "VBS SSWW (pol. sum)", "VBS_SSWW_SM_UL2016")
VBS_SSWW_SM_UL2016.year = "UL2016"
VBS_SSWW_SM_UL2016.components = [
    VBS_SSWW_LL_SM_UL2016,
    VBS_SSWW_TL_SM_UL2016,
    VBS_SSWW_TT_SM_UL2016,
]

VBS_SSWW_SM_UL2016M = sample(VBScolor, 1, 1001, "VBS SSWW (pol. sum)", "VBS_SSWW_SM_UL2016M")
VBS_SSWW_SM_UL2016M.year = "UL2016M"
VBS_SSWW_SM_UL2016M.components = [
    VBS_SSWW_SM_UL2016APV,
    VBS_SSWW_SM_UL2016,
]

VBS_SSWW_LL_SM_UL2016M = sample(VBSLLcolor, 1, 1001, "VBS SSWW LL", "VBS_SSWW_LL_SM_UL2016M")
VBS_SSWW_LL_SM_UL2016M.year = "UL2016M"
VBS_SSWW_LL_SM_UL2016M.components = [
    VBS_SSWW_LL_SM_UL2016APV,
    VBS_SSWW_LL_SM_UL2016,
]

VBS_SSWW_TL_SM_UL2016M = sample(VBSTLcolor, 1, 1001, "VBS SSWW TL", "VBS_SSWW_TL_SM_UL2016M")
VBS_SSWW_TL_SM_UL2016M.year = "UL2016M"
VBS_SSWW_TL_SM_UL2016M.components = [
    VBS_SSWW_TL_SM_UL2016APV,
    VBS_SSWW_TL_SM_UL2016,
]

VBS_SSWW_TT_SM_UL2016M = sample(VBSTTcolor, 1, 1001, "VBS SSWW TT", "VBS_SSWW_TT_SM_UL2016M")
VBS_SSWW_TT_SM_UL2016M.year = "UL2016M"
VBS_SSWW_TT_SM_UL2016M.components = [
    VBS_SSWW_TT_SM_UL2016APV,
    VBS_SSWW_TT_SM_UL2016,
]

VBS_SSWW_cW_BSM_UL2016 = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (only BSM)", "VBS_SSWW_cW_BSM_UL2016")
VBS_SSWW_cW_BSM_UL2016.year = "UL2016"
VBS_SSWW_cW_BSM_UL2016.dataset = "/VBS_SSWW_cW_BSM_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
VBS_SSWW_cW_BSM_UL2016.sigma = 0.01388

VBS_SSWW_cW_INT_UL2016 = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (only INT)", "VBS_SSWW_cW_INT_UL2016")
VBS_SSWW_cW_INT_UL2016.year = "UL2016"
VBS_SSWW_cW_INT_UL2016.dataset = "/VBS_SSWW_cW_INT_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
VBS_SSWW_cW_INT_UL2016.sigma = 0.0009987

VBS_SSWW_cW_UL2016 = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (BSM+INT)", "VBS_SSWW_cW_UL2016")
VBS_SSWW_cW_UL2016.year = "UL2016"
VBS_SSWW_cW_UL2016.components = [
    VBS_SSWW_cW_BSM_UL2016,
    VBS_SSWW_cW_INT_UL2016,
]

VBS_SSWW_cW_UL2016M = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (BSM+INT)", "VBS_SSWW_cW_UL2016M")
VBS_SSWW_cW_UL2016M.year = "UL2016M"
VBS_SSWW_cW_UL2016M.components = [
    VBS_SSWW_cW_UL2016APV,
    VBS_SSWW_cW_UL2016,
]

VBS_SSWW_cW_BSM_UL2016M = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (only BSM)", "VBS_SSWW_cW_BSM_UL2016M")
VBS_SSWW_cW_BSM_UL2016M.year = "UL2016M"
VBS_SSWW_cW_BSM_UL2016M.components = [
    VBS_SSWW_cW_BSM_UL2016APV,
    VBS_SSWW_cW_BSM_UL2016,
]

VBS_SSWW_cW_SM_UL2016 = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} + SM", "VBS_SSWW_cW_SM_UL2016")
VBS_SSWW_cW_SM_UL2016.year = "UL2016"
VBS_SSWW_cW_SM_UL2016.components = [
    VBS_SSWW_cW_BSM_UL2016,
    VBS_SSWW_cW_INT_UL2016,
    VBS_SSWW_LL_SM_UL2016,
    VBS_SSWW_TL_SM_UL2016,
    VBS_SSWW_TT_SM_UL2016,
]

VBS_SSWW_cW_SM_UL2016M = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} + SM", "VBS_SSWW_cW_SM_UL2016M")
VBS_SSWW_cW_SM_UL2016M.year = "UL2016M"
VBS_SSWW_cW_SM_UL2016M.components = [
    VBS_SSWW_cW_SM_UL2016APV,
    VBS_SSWW_cW_SM_UL2016,
]

VBS_SSWW_cHW_BSM_UL2016 = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (only BSM)", "VBS_SSWW_cHW_BSM_UL2016")
VBS_SSWW_cHW_BSM_UL2016.year = "UL2016"
VBS_SSWW_cHW_BSM_UL2016.dataset = "/VBS_SSWW_cHW_BSM_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
VBS_SSWW_cHW_BSM_UL2016.sigma = 0.0001415

VBS_SSWW_cHW_INT_UL2016 = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (only INT)", "VBS_SSWW_cHW_INT_UL2016")
VBS_SSWW_cHW_INT_UL2016.year = "UL2016"
VBS_SSWW_cHW_INT_UL2016.dataset = "/VBS_SSWW_cHW_INT_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
VBS_SSWW_cHW_INT_UL2016.sigma = 0.0005059

VBS_SSWW_cHW_UL2016 = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (BSM+INT)", "VBS_SSWW_cHW_UL2016")
VBS_SSWW_cHW_UL2016.year = "UL2016"
VBS_SSWW_cHW_UL2016.components = [
    VBS_SSWW_cHW_BSM_UL2016,
    VBS_SSWW_cHW_INT_UL2016,
]

VBS_SSWW_cHW_UL2016M = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (BSM+INT)", "VBS_SSWW_cHW_UL2016M")
VBS_SSWW_cHW_UL2016M.year = "UL2016M"
VBS_SSWW_cHW_UL2016M.components = [
    VBS_SSWW_cHW_UL2016APV,
    VBS_SSWW_cHW_UL2016,
]

VBS_SSWW_cHW_BSM_UL2016M = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (only BSM)", "VBS_SSWW_cHW_BSM_UL2016M")
VBS_SSWW_cHW_BSM_UL2016M.year = "UL2016M"
VBS_SSWW_cHW_BSM_UL2016M.components = [
    VBS_SSWW_cHW_BSM_UL2016APV,
    VBS_SSWW_cHW_BSM_UL2016,
]

VBS_SSWW_cHW_SM_UL2016 = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} + SM", "VBS_SSWW_cHW_SM_UL2016")
VBS_SSWW_cHW_SM_UL2016.year = "UL2016"
VBS_SSWW_cHW_SM_UL2016.components = [
    VBS_SSWW_cHW_BSM_UL2016,
    VBS_SSWW_cHW_INT_UL2016,
    VBS_SSWW_LL_SM_UL2016,
    VBS_SSWW_TL_SM_UL2016,
    VBS_SSWW_TT_SM_UL2016,
]

VBS_SSWW_cHW_SM_UL2016M = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} + SM", "VBS_SSWW_cHW_SM_UL2016M")
VBS_SSWW_cHW_SM_UL2016M.year = "UL2016M"
VBS_SSWW_cHW_SM_UL2016M.components = [
    VBS_SSWW_cHW_SM_UL2016APV,
    VBS_SSWW_cHW_SM_UL2016,
]

VBS_SSWW_cW_cHW_UL2016 = sample(CWcolor, 1, 1001, "VBS SSWW int c_{W} + c_{HW})", "VBS_SSWW_cW_cHW_UL2016")
VBS_SSWW_cW_cHW_UL2016.year = "UL2016"
VBS_SSWW_cW_cHW_UL2016.dataset = "/VBS_SSWW_cW_cHW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
VBS_SSWW_cW_cHW_UL2016.sigma = 0.002014

VBS_SSWW_cW_cHW_UL2016M = sample(CWcolor, 1, 1001, "VBS SSWW int c_{W} + c_{HW})", "VBS_SSWW_cW_cHW_UL2016M")
VBS_SSWW_cW_cHW_UL2016M.year = "UL2016M"
VBS_SSWW_cW_cHW_UL2016M.components = [
    VBS_SSWW_cW_cHW_UL2016,
    VBS_SSWW_cW_cHW_UL2016APV,
]

VBS_SSWW_DIM6_UL2016 = sample(ROOT.kGreen+3, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_DIM6_UL2016")
VBS_SSWW_DIM6_UL2016.year = "UL2016"
VBS_SSWW_DIM6_UL2016.components = [
    VBS_SSWW_cHW_BSM_UL2016,
    VBS_SSWW_cW_BSM_UL2016,
    VBS_SSWW_cHW_INT_UL2016,
    VBS_SSWW_cW_INT_UL2016,
    VBS_SSWW_cW_cHW_UL2016,
]

VBS_SSWW_DIM6_UL2016M = sample(ROOT.kGreen+3, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_DIM6_UL2016M")
VBS_SSWW_DIM6_UL2016M.year = "UL2016M"
VBS_SSWW_DIM6_UL2016M.components = [
    VBS_SSWW_DIM6_UL2016APV,
    VBS_SSWW_DIM6_UL2016,
]

VBS_SSWW_DIM6_SM_UL2016 = sample(ROOT.kGreen+2, 1, 1001, "VBS SSWW dim-6 EFT + SM", "VBS_SSWW_DIM6_SM_UL2016")
VBS_SSWW_DIM6_SM_UL2016.year = "UL2016"
VBS_SSWW_DIM6_SM_UL2016.components = [
    VBS_SSWW_LL_SM_UL2016,
    VBS_SSWW_TL_SM_UL2016,
    VBS_SSWW_TT_SM_UL2016,
    VBS_SSWW_cHW_BSM_UL2016,
    VBS_SSWW_cHW_INT_UL2016, 
    VBS_SSWW_cW_BSM_UL2016,
    VBS_SSWW_cW_INT_UL2016,
    VBS_SSWW_cW_cHW_UL2016,
]

VBS_SSWW_DIM6_SM_UL2016M = sample(ROOT.kGreen+2, 1, 1001, "VBS SSWW dim-6 EFT + SM", "VBS_SSWW_DIM6_SM_UL2016M")
VBS_SSWW_DIM6_SM_UL2016M.year = "UL2016M"
VBS_SSWW_DIM6_SM_UL2016M.components = [
    VBS_SSWW_DIM6_SM_UL2016APV,
    VBS_SSWW_DIM6_SM_UL2016,
]

VBS_SSWW_aQGC_UL2016 = sample(aQGCcolor, 1, 1001, "VBS SSWW dim-8 EFT", "VBS_SSWW_aQGC_UL2016")
VBS_SSWW_aQGC_UL2016.sigma = 0.1077
VBS_SSWW_aQGC_UL2016.year = "UL2016"
VBS_SSWW_aQGC_UL2016.dataset = "/WWJJ_SS_WToLNu_EWK_aQGC-FT-FS-FM_TuneCP5_13TeV_madgraph-pythia8/apiccine-NanoAODv9_UL2016_Legnaro-00000000000000000000000000000000/USER"

VBS_SSWW_aTGC_UL2016 = sample(aTGCcolor, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_aTGC_UL2016")
VBS_SSWW_aTGC_UL2016.sigma = 1.083
VBS_SSWW_aTGC_UL2016.year = "UL2016"
VBS_SSWW_aTGC_UL2016.dataset = "/WplusminusWplusminus2JTo2L2Nu2J_EWK_dim6_TuneCP5_13TeV-madgraph-pythia8/apiccine-NanoAODv9_UL2016_Legnaro-00000000000000000000000000000000/USER"

VBS_SSWW_aTGC_mixed_UL2016 = sample(aTGCcolor, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_aTGC_mixed_UL2016")
VBS_SSWW_aTGC_mixed_UL2016.sigma = 1.083
VBS_SSWW_aTGC_mixed_UL2016.year = "UL2016"
VBS_SSWW_aTGC_mixed_UL2016.dataset = "/WplusminusWplusminus2JTo2L2Nu2J_EWK_dim6_mixed_TuneCP5_13TeV-madgraph-pythia8/apiccine-NanoAODv9_UL2016_Legnaro-00000000000000000000000000000000/USER"

VBS_SSWW_aQGC_UL2016M = sample(aQGCcolor, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_aQGC_UL2016M")
VBS_SSWW_aQGC_UL2016M.year = "UL2016M"
VBS_SSWW_aQGC_UL2016M.components = [
    VBS_SSWW_aQGC_UL2016APV,
    VBS_SSWW_aQGC_UL2016,
]

VBS_SSWW_aTGC_UL2016M = sample(aTGCcolor, 1, 1001, "VBS SSWW dim-8 EFT", "VBS_SSWW_aTGC_UL2016M")
VBS_SSWW_aTGC_UL2016M.year = "UL2016M"
VBS_SSWW_aTGC_UL2016M.components = [
    VBS_SSWW_aTGC_UL2016APV,
    VBS_SSWW_aTGC_UL2016,
]

VBS_SSWW_aTGC_mixed_UL2016M = sample(aTGCcolor, 1, 1001, "VBS SSWW dim-8 EFT", "VBS_SSWW_aTGC_mixed_UL2016M")
VBS_SSWW_aTGC_mixed_UL2016M.year = "UL2016M"
VBS_SSWW_aTGC_mixed_UL2016M.components = [
    VBS_SSWW_aTGC_mixed_UL2016APV,
    VBS_SSWW_aTGC_mixed_UL2016,
]

DataMuF_UL2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuF_UL2016")
DataMuF_UL2016.runP = 'F'
DataMuF_UL2016.year = "UL2016"
DataMuF_UL2016.dataset = "/SingleMuon/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataMuG_UL2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuG_UL2016")
DataMuG_UL2016.runP = 'G'
DataMuG_UL2016.year = "UL2016"
DataMuG_UL2016.dataset = "/SingleMuon/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataMuH_UL2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuH_UL2016")
DataMuH_UL2016.runP = 'H'
DataMuH_UL2016.year = "UL2016"
DataMuH_UL2016.dataset = "/SingleMuon/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataMu_UL2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_UL2016")
DataMu_UL2016.year = "UL2016"
DataMu_UL2016.components =  [
    DataMuF_UL2016,
    DataMuG_UL2016,
    DataMuH_UL2016,
]

DataMu_UL2016M = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_UL2016M")
DataMu_UL2016M.year = "UL2016M"
DataMu_UL2016M.components =  [
    DataMu_UL2016APV,
    DataMu_UL2016,
]

DataEleF_UL2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleF_UL2016")
DataEleF_UL2016.runP = 'F'
DataEleF_UL2016.year = "UL2016"
DataEleF_UL2016.dataset = "/SingleElectron/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataEleG_UL2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleG_UL2016")
DataEleG_UL2016.runP = 'G'
DataEleG_UL2016.year = "UL2016"
DataEleG_UL2016.dataset = "/SingleElectron/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataEleH_UL2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleH_UL2016")
DataEleH_UL2016.runP = 'H'
DataEleH_UL2016.year = "UL2016"
DataEleH_UL2016.dataset = "/SingleElectron/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataEle_UL2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_UL2016")
DataEle_UL2016.year = "UL2016"
DataEle_UL2016.components =  [
    DataEleF_UL2016,
    DataEleG_UL2016,
    DataEleH_UL2016,
]

DataEle_UL2016M = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_UL2016M")
DataEle_UL2016M.year = "UL2016M"
DataEle_UL2016M.components =  [
    DataEle_UL2016APV,
    DataEle_UL2016,
]

DataHTF_UL2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTF_UL2016")
DataHTF_UL2016.runP = 'F'
DataHTF_UL2016.year = "UL2016"
DataHTF_UL2016.dataset = "/JetHT/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHTG_UL2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTG_UL2016")
DataHTG_UL2016.runP = 'G'
DataHTG_UL2016.year = "UL2016"
DataHTG_UL2016.dataset = "/JetHT/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHTH_UL2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTH_UL2016")
DataHTH_UL2016.runP = 'H'
DataHTH_UL2016.year = "UL2016"
DataHTH_UL2016.dataset = "/JetHT/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHT_UL2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_UL2016")
DataHT_UL2016.year = "UL2016"
DataHT_UL2016.components =  [
    DataHTF_UL2016,
    DataHTG_UL2016,
    DataHTH_UL2016,
]

FakeElePromptTau_UL2016 = sample(ROOT.kGray, 1, 1001, "Nonprompt e Prompt #tau", "FakeElePromptTau_UL2016")
FakeElePromptTau_UL2016.year = "UL2016"
FakeElePromptTau_UL2016.components = [
    DataEle_UL2016,
    #DataHT_UL2016,
    WJets_UL2016,
    DYJetsToLL_UL2016
]

PromptEleFakeTau_UL2016 = sample(ROOT.kGray+2, 1, 1001, "Prompt e Fake #tau", "PromptEleFakeTau_UL2016")
PromptEleFakeTau_UL2016.year = "UL2016"
PromptEleFakeTau_UL2016.components = [
    DataEle_UL2016,
    #DataHT_UL2016,
    WJets_UL2016,
    DYJetsToLL_UL2016
]

FakeEleFakeTau_UL2016 = sample(ROOT.kGray+3, 1, 1001, "Nonprompt e Fake #tau", "FakeEleFakeTau_UL2016")
FakeEleFakeTau_UL2016.year = "UL2016"
FakeEleFakeTau_UL2016.components = [
    DataEle_UL2016,
    #DataHT_UL2016,
    WJets_UL2016,
    DYJetsToLL_UL2016
]

FakeEle_UL2016 = sample(ROOT.kGray, 1, 1001, "Nonprompt leptons", "FakeEle_UL2016")
FakeEle_UL2016.year = "UL2016"
FakeEle_UL2016.components = [
    DataEle_UL2016,
    #DataHT_UL2016,
    WJets_UL2016,
    DYJetsToLL_FxFx_UL2016,
    TT_UL2016,
]

FakeElePromptTau_UL2016M = sample(ROOT.kGray, 1, 1001, "Nonprompt e Prompt #tau", "FakeElePromptTau_UL2016M")
FakeElePromptTau_UL2016M.year = "UL2016M"
FakeElePromptTau_UL2016M.components = [
    FakeElePromptTau_UL2016APV,
    FakeElePromptTau_UL2016,
]

PromptEleFakeTau_UL2016M = sample(ROOT.kGray+2, 1, 1001, "Prompt e Fake #tau", "PromptEleFakeTau_UL2016M")
PromptEleFakeTau_UL2016M.year = "UL2016M"
PromptEleFakeTau_UL2016M.components = [
    PromptEleFakeTau_UL2016APV,
    PromptEleFakeTau_UL2016,
]

FakeEleFakeTau_UL2016M = sample(ROOT.kGray+3, 1, 1001, "Nonprompt e Fake #tau", "FakeEleFakeTau_UL2016M")
FakeEleFakeTau_UL2016M.year = "UL2016M"
FakeEleFakeTau_UL2016M.components = [
    FakeEleFakeTau_UL2016APV,
    FakeEleFakeTau_UL2016,
]

FakeEle_UL2016M = sample(ROOT.kGray, 1, 1001, "Nonprompt leptons", "FakeEle_UL2016M")
FakeEle_UL2016M.year = "UL2016M"
FakeEle_UL2016M.components = [
    FakeEle_UL2016APV,
    FakeEle_UL2016,
]

FakeMuPromptTau_UL2016 = sample(ROOT.kGray, 1, 1001, "Nonprompt #mu Prompt #tau", "FakeMuPromptTau_UL2016")
FakeMuPromptTau_UL2016.year = "UL2016"
FakeMuPromptTau_UL2016.components = [
    DataMu_UL2016,
    #DataHT_UL2016,
    WJets_UL2016,
    DYJetsToLL_UL2016
]

PromptMuFakeTau_UL2016 = sample(ROOT.kGray+2, 1, 1001, "Prompt #mu Fake #tau", "PromptMuFakeTau_UL2016")
PromptMuFakeTau_UL2016.year = "UL2016"
PromptMuFakeTau_UL2016.components = [
    DataMu_UL2016,
    #DataHT_UL2016,
    WJets_UL2016,
    DYJetsToLL_UL2016
]

FakeMuFakeTau_UL2016 = sample(ROOT.kGray+3, 1, 1001, "Nonprompt #mu Fake #tau", "FakeMuFakeTau_UL2016")
FakeMuFakeTau_UL2016.year = "UL2016"
FakeMuFakeTau_UL2016.components = [
    DataMu_UL2016,
    #DataHT_UL2016,
    WJets_UL2016,
    DYJetsToLL_UL2016
]

FakeMu_UL2016 = sample(ROOT.kGray, 1, 1001, "Nonprompt leptons", "FakeMu_UL2016")
FakeMu_UL2016.year = "UL2016"
FakeMu_UL2016.components = [
    DataMu_UL2016,
    #DataHT_UL2016,
    WJets_UL2016,
    DYJetsToLL_FxFx_UL2016,
    TT_UL2016,
]

FakeMu_UL2016M = sample(ROOT.kGray, 1, 1001, "Nonprompt leptons", "FakeMu_UL2016M")
FakeMu_UL2016M.year = "UL2016M"
FakeMu_UL2016M.components = [
    FakeMu_UL2016APV,
    FakeMu_UL2016,
]

FakeMuPromptTau_UL2016M = sample(ROOT.kGray, 1, 1001, "Nonprompt #mu Prompt #tau", "FakeMuPromptTau_UL2016M")
FakeMuPromptTau_UL2016M.year = "UL2016M"
FakeMuPromptTau_UL2016M.components = [
    FakeMuPromptTau_UL2016APV,
    FakeMuPromptTau_UL2016,
]

PromptMuFakeTau_UL2016M = sample(ROOT.kGray+2, 1, 1001, "Prompt #mu Fake #tau", "PromptMuFakeTau_UL2016M")
PromptMuFakeTau_UL2016M.year = "UL2016M"
PromptMuFakeTau_UL2016M.components = [
    PromptMuFakeTau_UL2016APV,
    PromptMuFakeTau_UL2016,
]

FakeMuFakeTau_UL2016M = sample(ROOT.kGray+3, 1, 1001, "Nonprompt #mu Fake #tau", "FakeMuFakeTau_UL2016M")
FakeMuFakeTau_UL2016M.year = "UL2016M"
FakeMuFakeTau_UL2016M.components = [
    FakeMuFakeTau_UL2016APV,
    FakeMuFakeTau_UL2016,
]

SampleHTFake_UL2016 = sample(ROOT.kBlack, 1, 1001, "Sample for FR", "SampleHTFake_UL2016")
SampleHTFake_UL2016.year = "UL2016"
SampleHTFake_UL2016.components = [
    DataHTF_UL2016,
    DataHTG_UL2016,
    DataHTH_UL2016,
    WJetsHT70to100_UL2016,
    WJetsHT100to200_UL2016,
    WJetsHT200to400_UL2016,
    WJetsHT400to600_UL2016,
    WJetsHT600to800_UL2016,
    WJetsHT800to1200_UL2016,
    WJetsHT1200to2500_UL2016,
    WJetsHT2500toInf_UL2016,
    DYJetsToLL_M10to50_UL2016,
    DYJetsToLL_M50_UL2016,
    #DYJetsToLL_M50_UL2016_ext,
    TT_Had_UL2016,
    TT_SemiLep_UL2016,
    ZZTo2L2Nu_UL2016,
    ZZTo4L_UL2016,
    GluGluToContinToZZTo2e2nu_UL2016,
    GluGluToContinToZZTo4e_UL2016,
    GluGluToContinToZZTo2e2mu_UL2016,
    GluGluToContinToZZTo2e2tau_UL2016,
    GluGluToContinToZZTo2mu2nu_UL2016,
    GluGluToContinToZZTo4mu_UL2016,
    GluGluToContinToZZTo2mu2tau_UL2016,
    #GluGluToContinToZZTo2tau2nu_UL2016,
    GluGluToContinToZZTo4tau_UL2016,
]

######### UL2017 ##########

### ZZtoLep ###

ZZTo2L2Nu_UL2017 = sample(ZZcolor, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_UL2017")
ZZTo2L2Nu_UL2017.year = "UL2017"
ZZTo2L2Nu_UL2017.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
ZZTo2L2Nu_UL2017.sigma = 0.9738 #pb NLO

ZZTo4L_UL2017 = sample(ZZcolor, 1, 1001, "ZZ --> 4l", "ZZTo4L_UL2017") ### not sure is the right background
ZZTo4L_UL2017.year = "UL2017"
ZZTo4L_UL2017.dataset = "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
ZZTo4L_UL2017.sigma = 13.74 #pb NLO

GluGluToContinToZZTo2e2nu_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2nu", "GluGluToContinToZZTo2e2nu_UL2017")
GluGluToContinToZZTo2e2nu_UL2017.year = "UL2017"
GluGluToContinToZZTo2e2nu_UL2017.dataset = "/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2e2nu_UL2017.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo4e_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4e", "GluGluToContinToZZTo4e_UL2017")
GluGluToContinToZZTo4e_UL2017.year = "UL2017"
GluGluToContinToZZTo4e_UL2017.dataset = "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo4e_UL2017.sigma = 0.001586 # * 0.001 #pb

GluGluToContinToZZTo2e2mu_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2mu", "GluGluToContinToZZTo2e2mu_UL2017")
GluGluToContinToZZTo2e2mu_UL2017.year = "UL2017"
GluGluToContinToZZTo2e2mu_UL2017.dataset = "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2e2mu_UL2017.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2tau_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2tau", "GluGluToContinToZZTo2e2tau_UL2017")
GluGluToContinToZZTo2e2tau_UL2017.year = "UL2017"
GluGluToContinToZZTo2e2tau_UL2017.dataset = "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2e2tau_UL2017.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2nu_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2nu", "GluGluToContinToZZTo2mu2nu_UL2017")
GluGluToContinToZZTo2mu2nu_UL2017.year = "UL2017"
GluGluToContinToZZTo2mu2nu_UL2017.dataset = "/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2nu_UL2017.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo4mu_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4mu", "GluGluToContinToZZTo4mu_UL2017")
GluGluToContinToZZTo4mu_UL2017.year = "UL2017"
GluGluToContinToZZTo4mu_UL2017.dataset = "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo4mu_UL2017.sigma = 0.001586 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2tau_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2tau", "GluGluToContinToZZTo2mu2tau_UL2017")
GluGluToContinToZZTo2mu2tau_UL2017.year = "UL2017"
GluGluToContinToZZTo2mu2tau_UL2017.dataset = "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_UL2017.sigma = 0.003194 # * 0.001 #pb to be checked

#### to be produced ####
GluGluToContinToZZTo2tau2nu_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2tau2nu", "GluGluToContinToZZTo2tau2nu_UL2017")
GluGluToContinToZZTo2tau2nu_UL2017.year = "UL2017"
GluGluToContinToZZTo2tau2nu_UL2017.dataset = ""
GluGluToContinToZZTo2tau2nu_UL2017.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo4tau_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4tau", "GluGluToContinToZZTo4tau_UL2017")
GluGluToContinToZZTo4tau_UL2017.year = "UL2017"
GluGluToContinToZZTo4tau_UL2017.dataset = "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo4tau_UL2017.sigma = 0.001586 # * 0.001 #pb to be checked

ZZtoLep_UL2017 = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_UL2017")
ZZtoLep_UL2017.year = "UL2017"
ZZtoLep_UL2017.components = [
    ZZTo2L2Nu_UL2017,
    ZZTo4L_UL2017,
    GluGluToContinToZZTo2e2nu_UL2017,
    GluGluToContinToZZTo4e_UL2017,
    GluGluToContinToZZTo2e2mu_UL2017,
    GluGluToContinToZZTo2e2tau_UL2017,
    GluGluToContinToZZTo2mu2nu_UL2017,
    GluGluToContinToZZTo4mu_UL2017,
    GluGluToContinToZZTo2mu2tau_UL2017,
    #GluGluToContinToZZTo2tau2nu_UL2017,
    GluGluToContinToZZTo4tau_UL2017,
]

### TT with quark ###

TT_SemiLep_UL2017 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_SemiLep_UL2017")
TT_SemiLep_UL2017.year = "UL2017"
TT_SemiLep_UL2017.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM"
TT_SemiLep_UL2017.sigma = 831.76 * 0.438 #pb to check

#### in production stage ####
TT_Had_UL2017 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_Had_UL2017")
TT_Had_UL2017.year = "UL2017"
TT_Had_UL2017.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TT_Had_UL2017.sigma = 831.76 * 0.457 #pb to check

TT_UL2017 = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_UL2017")
TT_UL2017.year = "UL2017"
TT_UL2017.components = [
    TT_SemiLep_UL2017,
    TT_Had_UL2017,
]

TT_Mtt_700to1000_UL2017 = sample(TTcolor, 1, 1001, "t#bar{t} 700 < M_{tt} < 1000 GeV", "TT_Mtt_700to1000_UL2017")
TT_Mtt_700to1000_UL2017.year = "UL2017"
TT_Mtt_700to1000_UL2017.dataset = "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
TT_Mtt_700to1000_UL2017.sigma = 66.85

TT_Mtt_1000toInf_UL2017 = sample(TTcolor, 1, 1001, "t#bar{t} M_{tt} > 1000 GeV", "TT_Mtt_1000toInf_UL2017")
TT_Mtt_1000toInf_UL2017.year = "UL2017"
TT_Mtt_1000toInf_UL2017.dataset = "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
TT_Mtt_1000toInf_UL2017.sigma = 16.38

TT_Mtt_UL2017 = sample(TTcolor, 1, 1001, "t#bar{t} M_{tt} > 700 GeV", "TT_Mtt_UL2017")
TT_Mtt_UL2017.year = "UL2017"
TT_Mtt_UL2017.components = [
    TT_Mtt_700to1000_UL2017,
    TT_Mtt_1000toInf_UL2017,
]

TTTo2L2Nu_UL2017 = sample(TTdilepcolor, 1, 1001, "t#bar{t} dilep.", "TTTo2L2Nu_UL2017")
TTTo2L2Nu_UL2017.year = "UL2017"
TTTo2L2Nu_UL2017.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTTo2L2Nu_UL2017.sigma = 72.1 #831.76 * 0.105 #pb

TT_beff_UL2017 = sample(TTcolor, 1, 1001, "t#bar{t} inclusive", "TT_beff_UL2017")
TT_beff_UL2017.year = "UL2017"
TT_beff_UL2017.components = [
    TT_SemiLep_UL2017,
    TT_Had_UL2017,
    TTTo2L2Nu_UL2017,
]

### TVX ###

TTGJets_UL2017 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTGJets_UL2017")
TTGJets_UL2017.year = "UL2017"
TTGJets_UL2017.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTGJets_UL2017.sigma = 3.697

TTZToQQ_UL2017 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTZToQQ_UL2017")
TTZToQQ_UL2017.year = "UL2017"
TTZToQQ_UL2017.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTZToQQ_UL2017.sigma = 0.5297

TTZToLLNuNu_UL2017 = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> 2l2#nu", "TTZToLLNuNu_UL2017")
TTZToLLNuNu_UL2017.year = "UL2017"
TTZToLLNuNu_UL2017.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTZToLLNuNu_UL2017.sigma = 0.2529

TTWJetsToQQ_UL2017 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToQQ_UL2017")
TTWJetsToQQ_UL2017.year = "UL2017"
TTWJetsToQQ_UL2017.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTWJetsToQQ_UL2017.sigma = 0.4062

TTWJetsToLNu_UL2017 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToLNu_UL2017")
TTWJetsToLNu_UL2017.year = "UL2017"
TTWJetsToLNu_UL2017.dataset = "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
TTWJetsToLNu_UL2017.sigma = 0.216

tZq_ll_4f_UL2017 = sample(TVXcolor, 1, 1001, "tZq --> ll", "tZq_ll_4f_UL2017")
tZq_ll_4f_UL2017.year = "UL2017"
tZq_ll_4f_UL2017.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
tZq_ll_4f_UL2017.sigma = 0.0758

TVX_UL2017 = sample(TVXcolor, 1, 1001, "tVX", "TVX_UL2017")
TVX_UL2017.year = "UL2017"
TVX_UL2017.components = [
    TTGJets_UL2017,
    TTZToQQ_UL2017,
    TTZToLLNuNu_UL2017,
    TTWJetsToQQ_UL2017,
    TTWJetsToLNu_UL2017,
    tZq_ll_4f_UL2017,
]

### VG ###

ZG_UL2017 = sample(VGcolor, 1, 1001, "Z #gamma", "ZG_UL2017")
ZG_UL2017.year = "UL2017"
ZG_UL2017.dataset = "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
ZG_UL2017.sigma = 51.1 # to check

WG_UL2017 = sample(VGcolor, 1, 1001, "W #gamma", "WG_UL2017")
WG_UL2017.year = "UL2017"
WG_UL2017.dataset = "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WG_UL2017.sigma = 191.3 # to check

VG_UL2017 = sample(VGcolor, 1, 1001, "V#gamma", "VG_UL2017")
VG_UL2017.year = "UL2017"
VG_UL2017.components = [
    ZG_UL2017,
    WG_UL2017,
]

### WrongSign ###

WWto2L2Nu_UL2017 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "WWto2L2Nu_UL2017")
WWto2L2Nu_UL2017.year = "UL2017"
WWto2L2Nu_UL2017.dataset = "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
WWto2L2Nu_UL2017.sigma = 12.178

GluGluToWWToENEN_UL2017 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "GluGluToWWToENEN_UL2017")
GluGluToWWToENEN_UL2017.year = "UL2017"
GluGluToWWToENEN_UL2017.dataset = "/GluGluToWWToENEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToENEN_UL2017.sigma = 63.87 * 1./9. * 0.001 * 2. # 36.8 * 1./9. * 1.4 * 0.001 

GluGluToWWToENMN_UL2017 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "GluGluToWWToENMN_UL2017")
GluGluToWWToENMN_UL2017.year = "UL2017"
GluGluToWWToENMN_UL2017.dataset = "/GluGluToWWToENMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToENMN_UL2017.sigma = 63.87 * 1./9. * 0.001 # 36.8 * 1./9. * 1.4 * 0.001 

GluGluToWWToENTN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToENTN_UL2017")
GluGluToWWToENTN_UL2017.year = "UL2017"
GluGluToWWToENTN_UL2017.dataset = "/GluGluToWWToENTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToENTN_UL2017.sigma = 63.87 * 1./9. *0.001 # 36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToMNEN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNEN_UL2017")
GluGluToWWToMNEN_UL2017.year = "UL2017"
GluGluToWWToMNEN_UL2017.dataset = "/GluGluToWWToMNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToMNEN_UL2017.sigma = 63.87 * 1./9. * 0.001 # 36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToMNMN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNMN_UL2017")
GluGluToWWToMNMN_UL2017.year = "UL2017"
GluGluToWWToMNMN_UL2017.dataset = "/GluGluToWWToMNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToMNMN_UL2017.sigma = 63.87 * 1./9. * 0.001 * 2.# 36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToMNTN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNTN_UL2017")
GluGluToWWToMNTN_UL2017.year = "UL2017"
GluGluToWWToMNTN_UL2017.dataset = "/GluGluToWWToMNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToMNTN_UL2017.sigma = 63.87 * 1./9. * 0.001 # 36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToTNEN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNEN_UL2017")
GluGluToWWToTNEN_UL2017.year = "UL2017"
GluGluToWWToTNEN_UL2017.dataset = "/GluGluToWWToTNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToTNEN_UL2017.sigma = 63.87 * 1./9. * 0.001 # 36.81 * 1./9. * 1.4 * 0.001 

#### to be replaced with v9 when available ####
GluGluToWWToTNMN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNMN_UL2017")
GluGluToWWToTNMN_UL2017.year = "UL2017"
GluGluToWWToTNMN_UL2017.dataset = "/GluGluToWWToTNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM"
GluGluToWWToTNMN_UL2017.sigma = 63.87 * 1./9. * 0.001 # 36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToTNTN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNTN_UL2017")
GluGluToWWToTNTN_UL2017.year = "UL2017"
GluGluToWWToTNTN_UL2017.dataset = "/GluGluToWWToTNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToTNTN_UL2017.sigma = 63.87 * 1./9. * 0.001 * 2.# 36.81 * 1./9. * 1.4 * 0.001 

ST_tW_top_UL2017 = sample(WScolor, 1, 1001, "Single top", "ST_tW_top_UL2017")
ST_tW_top_UL2017.year = "UL2017"
ST_tW_top_UL2017.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
ST_tW_top_UL2017.sigma = 35.85 

ST_tW_antitop_UL2017 = sample(WScolor, 1, 1001, "Single top", "ST_tW_antitop_UL2017")
ST_tW_antitop_UL2017.year = "UL2017"
ST_tW_antitop_UL2017.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
ST_tW_antitop_UL2017.sigma =  35.85 

#### to be replaced with v9 when available ####
GluGluHToWWTo2L2Nu_UL2017 = sample(WScolor, 1, 1001, "Single top", "GluGluHToWWTo2L2Nu_UL2017")
GluGluHToWWTo2L2Nu_UL2017.year = "UL2017"
GluGluHToWWTo2L2Nu_UL2017.dataset = "/GluGluHToWWTo2L2Nu_M125_TuneCP5_PSw_13TeV-powheg2-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM"
GluGluHToWWTo2L2Nu_UL2017.sigma = 1.0315

GluGluHToZZTo4L_UL2017 = sample(WScolor, 1, 1001, "Single top", "GluGluHToZZTo4L_UL2017")
GluGluHToZZTo4L_UL2017.year = "UL2017"
GluGluHToZZTo4L_UL2017.dataset = "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluHToZZTo4L_UL2017.sigma = 0.0118# check nowe

GluGluHToTauTau_UL2017 = sample(WScolor, 1, 1001, "Single top", "GluGluHToTauTau_UL2017")
GluGluHToTauTau_UL2017.year = "UL2017"
GluGluHToTauTau_UL2017.dataset = "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluHToTauTau_UL2017.sigma = 2.7757# check nowe

VBFHToWWTo2L2Nu_UL2017 = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToWWTo2L2Nu_UL2017")
VBFHToWWTo2L2Nu_UL2017.year = "UL2017"
VBFHToWWTo2L2Nu_UL2017.dataset = "/VBFHToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
VBFHToWWTo2L2Nu_UL2017.sigma = 0.0896 # check nowe

VBFHToTauTau_UL2017 = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToTauTau_UL2017")
VBFHToTauTau_UL2017.year = "UL2017"
VBFHToTauTau_UL2017.dataset = "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
VBFHToTauTau_UL2017.sigma = 0.237 # check nowe

ttHToNonbb_UL2017 = sample(WScolor, 1, 1001, "ttH", "ttHToNonbb_UL2017")
ttHToNonbb_UL2017.year = "UL2017"
ttHToNonbb_UL2017.dataset = "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
ttHToNonbb_UL2017.sigma = 0.2120 # check nowe

VHToNonbb_UL2017 = sample(WScolor, 1, 1001, "VH", "VHToNonbb_UL2017")
VHToNonbb_UL2017.year = "UL2017"
VHToNonbb_UL2017.dataset = "/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
VHToNonbb_UL2017.sigma = 0.952 # check nowe

DYJetsToLL_M50_FxFx_UL2017 = sample(WZcolor, 1, 1001, "DYJetsToLL_M50", "DYJetsToLL_M50_FxFx_UL2017")
DYJetsToLL_M50_FxFx_UL2017.year = "UL2017"
DYJetsToLL_M50_FxFx_UL2017.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
DYJetsToLL_M50_FxFx_UL2017.sigma = 7181.0 #6529.0 # #6077.22 #

WrongSign_UL2017 = sample(WScolor, 1, 1001, "OS + (Z/#gamma + jets)", "WrongSign_UL2017")
WrongSign_UL2017.year = "UL2017"
WrongSign_UL2017.components = [
    WWto2L2Nu_UL2017,
    GluGluToWWToENEN_UL2017,
    GluGluToWWToENMN_UL2017,
    GluGluToWWToENTN_UL2017,
    GluGluToWWToMNEN_UL2017,
    GluGluToWWToMNMN_UL2017,
    GluGluToWWToMNTN_UL2017,
    GluGluToWWToTNEN_UL2017,
    GluGluToWWToTNMN_UL2017,
    GluGluToWWToTNTN_UL2017,
    ST_tW_top_UL2017,
    ST_tW_antitop_UL2017,
    GluGluHToWWTo2L2Nu_UL2017,
    GluGluHToZZTo4L_UL2017,
    GluGluHToTauTau_UL2017,
    VBFHToWWTo2L2Nu_UL2017,
    VBFHToTauTau_UL2017,
    ttHToNonbb_UL2017,
    VHToNonbb_UL2017,
    DYJetsToLL_M50_FxFx_UL2017,
]

WrongSign_ML_UL2017 = sample(WScolor, 1, 1001, "OS", "WrongSign_ML_UL2017")
WrongSign_ML_UL2017.year = "UL2017"
WrongSign_ML_UL2017.components = [
    WWto2L2Nu_UL2017,
    GluGluToWWToENEN_UL2017,
    GluGluToWWToENMN_UL2017,
    GluGluToWWToENTN_UL2017,
    GluGluToWWToMNEN_UL2017,
    GluGluToWWToMNMN_UL2017,
    GluGluToWWToMNTN_UL2017,
    GluGluToWWToTNEN_UL2017,
    GluGluToWWToTNMN_UL2017,
    GluGluToWWToTNTN_UL2017,
    ST_tW_top_UL2017,
    ST_tW_antitop_UL2017,
    GluGluHToWWTo2L2Nu_UL2017,
    GluGluHToZZTo4L_UL2017,
    GluGluHToTauTau_UL2017,
    VBFHToWWTo2L2Nu_UL2017,
    VBFHToTauTau_UL2017,
    ttHToNonbb_UL2017,
    VHToNonbb_UL2017,
]

### Triboson ###

WWTo2L2Nu_DoubleScattering_UL2017 = sample(TBcolor, 1, 1001, "WWTo2L2Nu_DoubleScattering", "WWTo2L2Nu_DoubleScattering_UL2017")
WWTo2L2Nu_DoubleScattering_UL2017.year = "UL2017"
WWTo2L2Nu_DoubleScattering_UL2017.dataset = ""
WWTo2L2Nu_DoubleScattering_UL2017.sigma =  0.1703#pb

WWW_4F_UL2017 = sample(TBcolor, 1, 1001, "WWW_4F", "WWW_4F_UL2017")
WWW_4F_UL2017.year = "UL2017"
WWW_4F_UL2017.dataset = "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM"
WWW_4F_UL2017.sigma = 0.2086#pb

WWZ_4F_UL2017 = sample(TBcolor, 1, 1001, "WWZ_4F", "WWZ_4F_UL2017")
WWZ_4F_UL2017.year = "UL2017"
WWZ_4F_UL2017.dataset = "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WWZ_4F_UL2017.sigma = 0.1651#pb

WZZ_UL2017 = sample(TBcolor, 1, 1001, "WZZ", "WZZ_UL2017")
WZZ_UL2017.year = "UL2017"
WZZ_UL2017.dataset = "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM"
WZZ_UL2017.sigma = 0.05565#pb

ZZZ_UL2017 = sample(TBcolor, 1, 1001, "ZZZ", "ZZZ_UL2017")
ZZZ_UL2017.year = "UL2017"
ZZZ_UL2017.dataset = "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM"
ZZZ_UL2017.sigma = 0.01398#pb

WWG_UL2017 = sample(TBcolor, 1, 1001, "WWG", "WWG_UL2017")
WWG_UL2017.year = "UL2017"
WWG_UL2017.dataset = "/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WWG_UL2017.sigma = 0.2147#pb

Triboson_UL2017 = sample(TBcolor, 1, 1001, "Triboson", "Triboson_UL2017")
Triboson_UL2017.year = "UL2017"
Triboson_UL2017.components = [
    #WWTo2L2Nu_DoubleScattering_UL2017,
    WWW_4F_UL2017,
    WWZ_4F_UL2017,
    WZZ_UL2017,
    ZZZ_UL2017,
    WWG_UL2017,
]

### WJets ###

WJetsHT70to100_UL2017 = sample(WJcolor, 1, 1001, "W + Jets", "WJetsHT70to100_UL2017")
WJetsHT70to100_UL2017.year = "UL2017"
WJetsHT70to100_UL2017.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WJetsHT70to100_UL2017.sigma = 1264. * 1.21 #pb

WJetsHT100to200_UL2017 = sample(WJcolor, 1, 1001, "W + Jets 100 < HT < 200", "WJetsHT100to200_UL2017")
WJetsHT100to200_UL2017.year = "UL2017"
WJetsHT100to200_UL2017.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WJetsHT100to200_UL2017.sigma = 1345 * 1.21 #pb

WJetsHT200to400_UL2017 = sample(WJcolor, 1, 1001, "W + Jets 200 < HT < 400", "WJetsHT200to400_UL2017")
WJetsHT200to400_UL2017.year = "UL2017"
WJetsHT200to400_UL2017.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WJetsHT200to400_UL2017.sigma = 359.7 * 1.21 #pb

WJetsHT400to600_UL2017 = sample(WJcolor, 1, 1001, "W + Jets 400 < HT < 600", "WJetsHT400to600_UL2017")
WJetsHT400to600_UL2017.year = "UL2017"
WJetsHT400to600_UL2017.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WJetsHT400to600_UL2017.sigma = 48.91 * 1.21 #pb

WJetsHT600to800_UL2017 = sample(WJcolor, 1, 1001, "W + Jets 600 < HT < 800", "WJetsHT600to800_UL2017")
WJetsHT600to800_UL2017.year = "UL2017"
WJetsHT600to800_UL2017.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WJetsHT600to800_UL2017.sigma = 12.05 * 1.21 #pb

#### to be replaced with v9 when available ####
WJetsHT800to1200_UL2017 = sample(WJcolor, 1, 1001, "W + Jets 800 < HT < 1200", "WJetsHT800to1200_UL2017")
WJetsHT800to1200_UL2017.year = "UL2017"
WJetsHT800to1200_UL2017.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM"
WJetsHT800to1200_UL2017.sigma = 5.501 * 1.21 #pb

WJetsHT1200to2500_UL2017 = sample(WJcolor, 1, 1001, "W + Jets 1200 < HT < 2500", "WJetsHT1200to2500_UL2017")
WJetsHT1200to2500_UL2017.year = "UL2017"
WJetsHT1200to2500_UL2017.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WJetsHT1200to2500_UL2017.sigma = 1.329 * 1.21 #pb

WJetsHT2500toInf_UL2017 = sample(WJcolor, 1, 1001, "W + Jets HT > 2500", "WJetsHT2500toInf_UL2017")
WJetsHT2500toInf_UL2017.year = "UL2017"
WJetsHT2500toInf_UL2017.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
WJetsHT2500toInf_UL2017.sigma = 0.008001 * 1.21 #pb

WJets_UL2017 = sample(WJcolor, 1, 1001, "W + Jets", "WJets_UL2017")
WJets_UL2017.year = "UL2017"
WJets_UL2017.components = [
    WJetsHT70to100_UL2017,
    WJetsHT100to200_UL2017,
    WJetsHT200to400_UL2017,
    WJetsHT400to600_UL2017,
    WJetsHT600to800_UL2017,
    WJetsHT800to1200_UL2017,
    WJetsHT1200to2500_UL2017,
    WJetsHT2500toInf_UL2017,
]


WJets_0J_UL2017 = sample(WJcolor, 1, 1001, "W + Jets 0J", "WJets_0J_UL2017")
WJets_0J_UL2017.year = "UL2017"
WJets_0J_UL2017.dataset = "/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WJets_0J_UL2017.sigma = 53330.0 * 1.21 #pb

WJets_1J_UL2017 = sample(WJcolor, 1, 1001, "W + Jets 1J", "WJets_1J_UL2017")
WJets_1J_UL2017.year = "UL2017"
WJets_1J_UL2017.dataset = "/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WJets_1J_UL2017.sigma = 8875.0 * 1.21 #pb

WJets_2J_UL2017 = sample(WJcolor, 1, 1001, "W + Jets 2J", "WJets_2J_UL2017")
WJets_2J_UL2017.year = "UL2017"
WJets_2J_UL2017.dataset = "/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WJets_2J_UL2017.sigma = 3338.0 * 1.21 #pb

WJets_Jbin_UL2017 = sample(WJcolor, 1, 1001, "W + Jets #jets binned", "WJets_Jbin_UL2017")
WJets_Jbin_UL2017.year = "UL2017"
WJets_Jbin_UL2017.components = [
    WJets_0J_UL2017,
    WJets_1J_UL2017,
    WJets_2J_UL2017,
]

### WZ ###

WZ_UL2017 = sample(WZcolor, 1, 1001, "WZ", "WZ_UL2017")
WZ_UL2017.year = "UL2017"
WZ_UL2017.dataset = "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WZ_UL2017.sigma = 27.59

### DYJets ###

DYJetsToLL_M10to50_UL2017 = sample(WZcolor, 1, 1001, "DY+jets (10 < M_{ll} < 50 GeV", "DYJetsToLL_M10to50_UL2017")
DYJetsToLL_M10to50_UL2017.year = "UL2017"
DYJetsToLL_M10to50_UL2017.dataset = "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
DYJetsToLL_M10to50_UL2017.sigma = 15890. # 18610.

DYJetsToLL_M50_UL2017 = sample(WZcolor, 1, 1001, "DYJetsToLL_M50", "DYJetsToLL_M50_UL2017")
DYJetsToLL_M50_UL2017.year = "UL2017"
DYJetsToLL_M50_UL2017.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
DYJetsToLL_M50_UL2017.sigma = 6077.22

DYJetsToLL_M50_UL2017_ext = sample(WZcolor, 1, 1001, "DYJetsToLL_M50", "DYJetsToLL_M50_UL2017_ext")
DYJetsToLL_M50_UL2017_ext.year = "UL2017"
DYJetsToLL_M50_UL2017_ext.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v1/NANOAODSIM"
DYJetsToLL_M50_UL2017_ext.sigma = 6077.22

DYJetsToLL_UL2017 = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_UL2017")
DYJetsToLL_UL2017.year = "UL2017"
DYJetsToLL_UL2017.components = [
    #DYJetsToLL_M10to50_UL2017,
    DYJetsToLL_M50_UL2017,
    #DYJetsToLL_M50_UL2017_ext,
]

DYJetsToLL_FxFx_UL2017 = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_FxFx_UL2017")
DYJetsToLL_FxFx_UL2017.year = "UL2017"
DYJetsToLL_FxFx_UL2017.components = [
    #DYJetsToLL_M10to50_UL2017,
    DYJetsToLL_M50_FxFx_UL2017,
]


DYJetsToLL_0J_FxFx_UL2017 = sample(DYcolor, 1, 1001, "DYJetsToLL_0J", "DYJetsToLL_0J_FxFx_UL2017")
DYJetsToLL_0J_FxFx_UL2017.year = "UL2017"
DYJetsToLL_0J_FxFx_UL2017.dataset = "/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
DYJetsToLL_0J_FxFx_UL2017.sigma = 5993 #5129.0

DYJetsToLL_1J_FxFx_UL2017 = sample(DYcolor, 1, 1001, "DYJetsToLL_1J", "DYJetsToLL_1J_FxFx_UL2017")
DYJetsToLL_1J_FxFx_UL2017.year = "UL2017"
DYJetsToLL_1J_FxFx_UL2017.dataset = "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
DYJetsToLL_1J_FxFx_UL2017.sigma = 1474 #951.5

DYJetsToLL_2J_FxFx_UL2017 = sample(DYcolor, 1, 1001, "DYJetsToLL_2J", "DYJetsToLL_2J_FxFx_UL2017")
DYJetsToLL_2J_FxFx_UL2017.year = "UL2017"
DYJetsToLL_2J_FxFx_UL2017.dataset = "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
DYJetsToLL_2J_FxFx_UL2017.sigma = 111.1 #361.4

DYJetsToLL_Jbin_FxFx_UL2017 = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_Jbin_FxFx_UL2017")
DYJetsToLL_Jbin_FxFx_UL2017.year = "UL2017"
DYJetsToLL_Jbin_FxFx_UL2017.components = [
    DYJetsToLL_0J_FxFx_UL2017,
    DYJetsToLL_1J_FxFx_UL2017,
    DYJetsToLL_2J_FxFx_UL2017,
]

### WpWp EWK ###

#### to be produced ####
WpWpJJ_EWK_UL2017 = sample(EWVBScolor, 1, 1001, "EW SSWW VBS", "WpWpJJ_EWK_UL2017")
WpWpJJ_EWK_UL2017.sigma = 0.0287
WpWpJJ_EWK_UL2017.year = "UL2017"
WpWpJJ_EWK_UL2017.dataset = "/WpWpJJ_EWKnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"

### WpWp QCD ###

#### to be produced ####
WpWpJJ_QCD_UL2017 = sample(QCDVBScolor, 1, 1001, "QCD SSWW", "WpWpJJ_QCD_UL2017")
WpWpJJ_QCD_UL2017.sigma = 0.02227
WpWpJJ_QCD_UL2017.year = "UL2017"
WpWpJJ_QCD_UL2017.dataset = "/WpWpJJ_QCDnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"

WpWpJJ_UL2017 = sample(WWJJcolor, 1, 1001, "EW+QCD VBS SSWW", "WpWpJJ_UL2017")
WpWpJJ_UL2017.year = "UL2017"
WpWpJJ_UL2017.components = [
    WpWpJJ_EWK_UL2017,
    WpWpJJ_QCD_UL2017,
]

### VBS SSWW polarized ###

#### in production stage ####
VBS_SSWW_LL_SM_UL2017 = sample(VBSLLcolor, 1, 1001, "VBS SSWW LL", "VBS_SSWW_LL_SM_UL2017")
VBS_SSWW_LL_SM_UL2017.sigma = 0.002014
VBS_SSWW_LL_SM_UL2017.year = "UL2017"
VBS_SSWW_LL_SM_UL2017.dataset = "/VBS_SSWW_LL_polarization_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"

#### in production stage ####
VBS_SSWW_TL_SM_UL2017 = sample(VBSTLcolor, 1, 1001, "VBS SSWW TL", "VBS_SSWW_TL_SM_UL2017")
VBS_SSWW_TL_SM_UL2017.sigma = 0.01036
VBS_SSWW_TL_SM_UL2017.year = "UL2017"
VBS_SSWW_TL_SM_UL2017.dataset = "/VBS_SSWW_TL_polarization_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"

#### in production stage ####
VBS_SSWW_TT_SM_UL2017 = sample(VBSTTcolor, 1, 1001, "VBS SSWW TT", "VBS_SSWW_TT_SM_UL2017")
VBS_SSWW_TT_SM_UL2017.sigma = 0.01595
VBS_SSWW_TT_SM_UL2017.year = "UL2017"
VBS_SSWW_TT_SM_UL2017.dataset = "/VBS_SSWW_TT_polarization_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"

VBS_SSWW_SM_UL2017 = sample(VBScolor, 1, 1001, "VBS SSWW (pol. sum)", "VBS_SSWW_SM_UL2017")
VBS_SSWW_SM_UL2017.year = "UL2017"
VBS_SSWW_SM_UL2017.components = [
    VBS_SSWW_LL_SM_UL2017,
    VBS_SSWW_TL_SM_UL2017,
    VBS_SSWW_TT_SM_UL2017,
]

VBS_SSWW_cW_BSM_UL2017 = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (only BSM)", "VBS_SSWW_cW_BSM_UL2017")
VBS_SSWW_cW_BSM_UL2017.year = "UL2017"
VBS_SSWW_cW_BSM_UL2017.dataset = "/VBS_SSWW_cW_BSM_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
VBS_SSWW_cW_BSM_UL2017.sigma = 0.01388

VBS_SSWW_cW_INT_UL2017 = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (only INT)", "VBS_SSWW_cW_INT_UL2017")
VBS_SSWW_cW_INT_UL2017.year = "UL2017"
VBS_SSWW_cW_INT_UL2017.dataset = "/VBS_SSWW_cW_INT_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
VBS_SSWW_cW_INT_UL2017.sigma = 0.0009987

VBS_SSWW_cW_UL2017 = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (BSM+INT)", "VBS_SSWW_cW_UL2017")
VBS_SSWW_cW_UL2017.year = "UL2017"
VBS_SSWW_cW_UL2017.components = [
    VBS_SSWW_cW_BSM_UL2017,
    VBS_SSWW_cW_INT_UL2017,
]

VBS_SSWW_cW_SM_UL2017 = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} + SM", "VBS_SSWW_cW_SM_UL2017")
VBS_SSWW_cW_SM_UL2017.year = "UL2017"
VBS_SSWW_cW_SM_UL2017.components = [
    VBS_SSWW_cW_BSM_UL2017,
    VBS_SSWW_cW_INT_UL2017,
    VBS_SSWW_LL_SM_UL2017,
    VBS_SSWW_TL_SM_UL2017,
    VBS_SSWW_TT_SM_UL2017,
]

VBS_SSWW_cHW_BSM_UL2017 = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (only BSM)", "VBS_SSWW_cHW_BSM_UL2017")
VBS_SSWW_cHW_BSM_UL2017.year = "UL2017"
VBS_SSWW_cHW_BSM_UL2017.dataset = "/VBS_SSWW_cHW_BSM_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
VBS_SSWW_cHW_BSM_UL2017.sigma = 0.0001415

VBS_SSWW_cHW_INT_UL2017 = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (only INT)", "VBS_SSWW_cHW_INT_UL2017")
VBS_SSWW_cHW_INT_UL2017.year = "UL2017"
VBS_SSWW_cHW_INT_UL2017.dataset = "/VBS_SSWW_cHW_INT_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
VBS_SSWW_cHW_INT_UL2017.sigma = 0.0005059

VBS_SSWW_cHW_UL2017 = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (BSM+INT)", "VBS_SSWW_cHW_UL2017")
VBS_SSWW_cHW_UL2017.year = "UL2017"
VBS_SSWW_cHW_UL2017.components = [
    VBS_SSWW_cHW_BSM_UL2017,
    VBS_SSWW_cHW_INT_UL2017,
]

VBS_SSWW_cHW_SM_UL2017 = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} + SM", "VBS_SSWW_cHW_SM_UL2017")
VBS_SSWW_cHW_SM_UL2017.year = "UL2017"
VBS_SSWW_cHW_SM_UL2017.components = [
    VBS_SSWW_cHW_BSM_UL2017,
    VBS_SSWW_cHW_INT_UL2017,
    VBS_SSWW_LL_SM_UL2017,
    VBS_SSWW_TL_SM_UL2017,
    VBS_SSWW_TT_SM_UL2017,
]

VBS_SSWW_cW_cHW_UL2017 = sample(CWcolor, 1, 1001, "VBS SSWW int c_{W} + c_{HW})", "VBS_SSWW_cW_cHW_UL2017")
VBS_SSWW_cW_cHW_UL2017.year = "UL2017"
VBS_SSWW_cW_cHW_UL2017.dataset = "/VBS_SSWW_cW_cHW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
VBS_SSWW_cW_cHW_UL2017.sigma = 0.002014

VBS_SSWW_DIM6_UL2017 = sample(ROOT.kGreen+3, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_DIM6_UL2017")
VBS_SSWW_DIM6_UL2017.year = "UL2017"
VBS_SSWW_DIM6_UL2017.components = [
    VBS_SSWW_cHW_BSM_UL2017,
    VBS_SSWW_cW_BSM_UL2017,
    VBS_SSWW_cHW_INT_UL2017,
    VBS_SSWW_cW_INT_UL2017,
    VBS_SSWW_cW_cHW_UL2017,
]

VBS_SSWW_DIM6_SM_UL2017 = sample(ROOT.kGreen+2, 1, 1001, "VBS SSWW dim-6 EFT + SM", "VBS_SSWW_DIM6_SM_UL2017")
VBS_SSWW_DIM6_SM_UL2017.year = "UL2017"
VBS_SSWW_DIM6_SM_UL2017.components = [
    VBS_SSWW_LL_SM_UL2017,
    VBS_SSWW_TL_SM_UL2017,
    VBS_SSWW_TT_SM_UL2017,
    VBS_SSWW_cHW_BSM_UL2017,
    VBS_SSWW_cHW_INT_UL2017, 
    VBS_SSWW_cW_BSM_UL2017,
    VBS_SSWW_cW_INT_UL2017,
    VBS_SSWW_cW_cHW_UL2017,
]

VBS_SSWW_aQGC_UL2017 = sample(aQGCcolor, 1, 1001, "VBS SSWW dim-8 EFT", "VBS_SSWW_aQGC_UL2017")
VBS_SSWW_aQGC_UL2017.sigma = 0.1077
VBS_SSWW_aQGC_UL2017.year = "UL2017"
VBS_SSWW_aQGC_UL2017.dataset = "/WWJJ_SS_WToLNu_EWK_aQGC-FT-FS-FM_TuneCP5_13TeV_madgraph-pythia8/apiccine-NanoAODv9_UL2017_Legnaro-00000000000000000000000000000000/USER"

VBS_SSWW_aTGC_UL2017 = sample(aTGCcolor, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_aTGC_UL2017")
VBS_SSWW_aTGC_UL2017.sigma = 1.083
VBS_SSWW_aTGC_UL2017.year = "UL2017"
VBS_SSWW_aTGC_UL2017.dataset = "/WplusminusWplusminus2JTo2L2Nu2J_EWK_dim6_TuneCP5_13TeV-madgraph-pythia8/apiccine-NanoAODv9_UL2017_Legnaro-00000000000000000000000000000000/USER"

VBS_SSWW_aTGC_mixed_UL2017 = sample(aTGCcolor, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_aTGC_mixed_UL2017")
VBS_SSWW_aTGC_mixed_UL2017.sigma = 1.083
VBS_SSWW_aTGC_mixed_UL2017.year = "UL2017"
VBS_SSWW_aTGC_mixed_UL2017.dataset = "/WplusminusWplusminus2JTo2L2Nu2J_EWK_dim6_mixed_TuneCP5_13TeV-madgraph-pythia8/apiccine-NanoAODv9_UL2017_Legnaro-00000000000000000000000000000000/USER"

DataMuB_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB_UL2017")
DataMuB_UL2017.runP = 'B'
DataMuB_UL2017.year = "UL2017"
DataMuB_UL2017.dataset = "/SingleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataMuC_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuC_UL2017")
DataMuC_UL2017.runP = 'C'
DataMuC_UL2017.year = "UL2017"
DataMuC_UL2017.dataset = "/SingleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataMuD_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuD_UL2017")
DataMuD_UL2017.runP = 'D'
DataMuD_UL2017.year = "UL2017"
DataMuD_UL2017.dataset = "/SingleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataMuE_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuE_UL2017")
DataMuE_UL2017.runP = 'E'
DataMuE_UL2017.year = "UL2017"
DataMuE_UL2017.dataset = "/SingleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataMuF_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuF_UL2017")
DataMuF_UL2017.runP = 'F'
DataMuF_UL2017.year = "UL2017"
DataMuF_UL2017.dataset = "/SingleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataMu_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_UL2017")
DataMu_UL2017.year = "UL2017"
DataMu_UL2017.components =  [
    DataMuB_UL2017,
    DataMuC_UL2017,
    DataMuD_UL2017,
    DataMuE_UL2017,
    DataMuF_UL2017,
]

DataEleB_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB_UL2017")
DataEleB_UL2017.runP = 'B'
DataEleB_UL2017.year = "UL2017"
DataEleB_UL2017.dataset = "/SingleElectron/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataEleC_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleC_UL2017")
DataEleC_UL2017.runP = 'C'
DataEleC_UL2017.year = "UL2017"
DataEleC_UL2017.dataset = "/SingleElectron/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataEleD_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleD_UL2017")
DataEleD_UL2017.runP = 'D'
DataEleD_UL2017.year = "UL2017"
DataEleD_UL2017.dataset = "/SingleElectron/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataEleE_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleE_UL2017")
DataEleE_UL2017.runP = 'E'
DataEleE_UL2017.year = "UL2017"
DataEleE_UL2017.dataset = "/SingleElectron/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataEleF_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleF_UL2017")
DataEleF_UL2017.runP = 'F'
DataEleF_UL2017.year = "UL2017"
DataEleF_UL2017.dataset = "/SingleElectron/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataEle_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_UL2017")
DataEle_UL2017.year = "UL2017"
DataEle_UL2017.components =  [
    DataEleB_UL2017,
    DataEleC_UL2017,
    DataEleD_UL2017,
    DataEleE_UL2017,
    DataEleF_UL2017,
]

DataHTB_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB_UL2017")
DataHTB_UL2017.runP = 'B'
DataHTB_UL2017.year = "UL2017"
DataHTB_UL2017.dataset = "/JetHT/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHTC_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTC_UL2017")
DataHTC_UL2017.runP = 'C'
DataHTC_UL2017.year = "UL2017"
DataHTC_UL2017.dataset = "/JetHT/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHTD_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTD_UL2017")
DataHTD_UL2017.runP = 'D'
DataHTD_UL2017.year = "UL2017"
DataHTD_UL2017.dataset = "/JetHT/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHTE_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTE_UL2017")
DataHTE_UL2017.runP = 'E'
DataHTE_UL2017.year = "UL2017"
DataHTE_UL2017.dataset = "/JetHT/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHTF_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTF_UL2017")
DataHTF_UL2017.runP = 'F'
DataHTF_UL2017.year = "UL2017"
DataHTF_UL2017.dataset = "/JetHT/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHT_UL2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_UL2017")
DataHT_UL2017.year = "UL2017"
DataHT_UL2017.components =  [
    DataHTB_UL2017,
    DataHTC_UL2017,
    DataHTD_UL2017,
    DataHTE_UL2017,
    DataHTF_UL2017,
]

FakeElePromptTau_UL2017 = sample(ROOT.kGray, 1, 1001, "Nonprompt e Prompt #tau", "FakeElePromptTau_UL2017")
FakeElePromptTau_UL2017.year = "UL2017"
FakeElePromptTau_UL2017.components = [
    DataEle_UL2017,
    #DataHT_UL2017,
    WJets_UL2017,
    #DYJetsToLL_UL2017
]

PromptEleFakeTau_UL2017 = sample(ROOT.kGray+2, 1, 1001, "Prompt e Fake #tau", "PromptEleFakeTau_UL2017")
PromptEleFakeTau_UL2017.year = "UL2017"
PromptEleFakeTau_UL2017.components = [
    DataEle_UL2017,
    #DataHT_UL2017,
    WJets_UL2017,
    #DYJetsToLL_UL2017
]

FakeEleFakeTau_UL2017 = sample(ROOT.kGray+3, 1, 1001, "Nonprompt e Fake #tau", "FakeEleFakeTau_UL2017")
FakeEleFakeTau_UL2017.year = "UL2017"
FakeEleFakeTau_UL2017.components = [
    DataEle_UL2017,
    #DataHT_UL2017,
    WJets_UL2017,
    #DYJetsToLL_UL2017
]

FakeEle_UL2017 = sample(ROOT.kGray, 1, 1001, "Nonprompt leptons", "FakeEle_UL2017")
FakeEle_UL2017.year = "UL2017"
FakeEle_UL2017.components = [
    DataEle_UL2017,
    #DataHT_UL2017,
    WJets_UL2017,
    #DYJetsToLL_FxFx_UL2017,
    TT_UL2017,
]

FakeMuPromptTau_UL2017 = sample(ROOT.kGray, 1, 1001, "Nonprompt #mu Prompt #tau", "FakeMuPromptTau_UL2017")
FakeMuPromptTau_UL2017.year = "UL2017"
FakeMuPromptTau_UL2017.components = [
    DataMu_UL2017,
    #DataHT_UL2017,
    WJets_UL2017,
    DYJetsToLL_UL2017
]

PromptMuFakeTau_UL2017 = sample(ROOT.kGray+2, 1, 1001, "Prompt #mu Fake #tau", "PromptMuFakeTau_UL2017")
PromptMuFakeTau_UL2017.year = "UL2017"
PromptMuFakeTau_UL2017.components = [
    DataMu_UL2017,
    #DataHT_UL2017,
    WJets_UL2017,
    DYJetsToLL_UL2017
]

FakeMuFakeTau_UL2017 = sample(ROOT.kGray+3, 1, 1001, "Nonprompt #mu Fake #tau", "FakeMuFakeTau_UL2017")
FakeMuFakeTau_UL2017.year = "UL2017"
FakeMuFakeTau_UL2017.components = [
    DataMu_UL2017,
    #DataHT_UL2017,
    WJets_UL2017,
    DYJetsToLL_UL2017
]

FakeMu_UL2017 = sample(ROOT.kGray, 1, 1001, "Nonprompt leptons", "FakeMu_UL2017")
FakeMu_UL2017.year = "UL2017"
FakeMu_UL2017.components = [
    DataMu_UL2017,
    #DataHT_UL2017,
    WJets_UL2017,
    #DYJetsToLL_FxFx_UL2017,
    TT_UL2017,
]

SampleHTFake_UL2017 = sample(ROOT.kBlack, 1, 1001, "Sample for FR", "SampleHTFake_UL2017")
SampleHTFake_UL2017.year = "UL2017"
SampleHTFake_UL2017.components = [
    DataHTB_UL2017,
    DataHTC_UL2017,
    DataHTD_UL2017,
    DataHTE_UL2017,
    DataHTF_UL2017,
    WJetsHT70to100_UL2017,
    WJetsHT100to200_UL2017,
    WJetsHT200to400_UL2017,
    WJetsHT400to600_UL2017,
    WJetsHT600to800_UL2017,
    WJetsHT800to1200_UL2017,
    WJetsHT1200to2500_UL2017,
    WJetsHT2500toInf_UL2017,
    DYJetsToLL_M10to50_UL2017,
    DYJetsToLL_M50_UL2017,
    #DYJetsToLL_M50_UL2017_ext,
    TT_Had_UL2017,
    TT_SemiLep_UL2017,
    ZZTo2L2Nu_UL2017,
    ZZTo4L_UL2017,
    GluGluToContinToZZTo2e2nu_UL2017,
    GluGluToContinToZZTo4e_UL2017,
    GluGluToContinToZZTo2e2mu_UL2017,
    GluGluToContinToZZTo2e2tau_UL2017,
    GluGluToContinToZZTo2mu2nu_UL2017,
    GluGluToContinToZZTo4mu_UL2017,
    GluGluToContinToZZTo2mu2tau_UL2017,
    #GluGluToContinToZZTo2tau2nu_UL2017,
    GluGluToContinToZZTo4tau_UL2017,
]

######### UL2018 ##########

### ZZtoLep ###

ZZTo2L2Nu_UL2018 = sample(ZZcolor, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_UL2018")
ZZTo2L2Nu_UL2018.year = "UL2018"
ZZTo2L2Nu_UL2018.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
ZZTo2L2Nu_UL2018.sigma = 0.9738 #pb NLO

ZZTo4L_UL2018 = sample(ZZcolor, 1, 1001, "ZZ --> 4l", "ZZTo4L_UL2018") ### not sure is the right background
ZZTo4L_UL2018.year = "UL2018"
ZZTo4L_UL2018.dataset = "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
ZZTo4L_UL2018.sigma = 13.74 #pb NLO

GluGluToContinToZZTo2e2nu_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2nu", "GluGluToContinToZZTo2e2nu_UL2018")
GluGluToContinToZZTo2e2nu_UL2018.year = "UL2018"
GluGluToContinToZZTo2e2nu_UL2018.dataset = "/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2e2nu_UL2018.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo4e_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4e", "GluGluToContinToZZTo4e_UL2018")
GluGluToContinToZZTo4e_UL2018.year = "UL2018"
GluGluToContinToZZTo4e_UL2018.dataset = "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo4e_UL2018.sigma = 0.001586 # * 0.001 #pb

GluGluToContinToZZTo2e2mu_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2mu", "GluGluToContinToZZTo2e2mu_UL2018")
GluGluToContinToZZTo2e2mu_UL2018.year = "UL2018"
GluGluToContinToZZTo2e2mu_UL2018.dataset = "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2e2mu_UL2018.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2tau_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2tau", "GluGluToContinToZZTo2e2tau_UL2018")
GluGluToContinToZZTo2e2tau_UL2018.year = "UL2018"
GluGluToContinToZZTo2e2tau_UL2018.dataset = "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2e2tau_UL2018.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2nu_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2nu", "GluGluToContinToZZTo2mu2nu_UL2018")
GluGluToContinToZZTo2mu2nu_UL2018.year = "UL2018"
GluGluToContinToZZTo2mu2nu_UL2018.dataset = "/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2nu_UL2018.sigma = 0.003194 # * 0.001 #pb to be checked

#### to be replaced with v9 when available ####
GluGluToContinToZZTo4mu_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4mu", "GluGluToContinToZZTo4mu_UL2018")
GluGluToContinToZZTo4mu_UL2018.year = "UL2018"
GluGluToContinToZZTo4mu_UL2018.dataset = "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"
GluGluToContinToZZTo4mu_UL2018.sigma = 0.001586 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2tau_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2tau", "GluGluToContinToZZTo2mu2tau_UL2018")
GluGluToContinToZZTo2mu2tau_UL2018.year = "UL2018"
GluGluToContinToZZTo2mu2tau_UL2018.dataset = "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_UL2018.sigma = 0.003194 # * 0.001 #pb to be checked

#### to be produced ####
GluGluToContinToZZTo2tau2nu_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2tau2nu", "GluGluToContinToZZTo2tau2nu_UL2018")
GluGluToContinToZZTo2tau2nu_UL2018.year = "UL2018"
GluGluToContinToZZTo2tau2nu_UL2018.dataset = ""
GluGluToContinToZZTo2tau2nu_UL2018.sigma = 0.003194 # * 0.001 #pb to be checked

GluGluToContinToZZTo4tau_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4tau", "GluGluToContinToZZTo4tau_UL2018")
GluGluToContinToZZTo4tau_UL2018.year = "UL2018"
GluGluToContinToZZTo4tau_UL2018.dataset = "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo4tau_UL2018.sigma = 0.001586 # * 0.001 #pb to be checked

ZZtoLep_UL2018 = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_UL2018")
ZZtoLep_UL2018.year = "UL2018"
ZZtoLep_UL2018.components = [
    ZZTo2L2Nu_UL2018,
    ZZTo4L_UL2018,
    GluGluToContinToZZTo2e2nu_UL2018,
    GluGluToContinToZZTo4e_UL2018,
    GluGluToContinToZZTo2e2mu_UL2018,
    GluGluToContinToZZTo2e2tau_UL2018,
    GluGluToContinToZZTo2mu2nu_UL2018,
    GluGluToContinToZZTo4mu_UL2018,
    GluGluToContinToZZTo2mu2tau_UL2018,
    #GluGluToContinToZZTo2tau2nu_UL2018,
    GluGluToContinToZZTo4tau_UL2018,
]

ZZtoLep_ULRunII = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_ULRunII")
ZZtoLep_ULRunII.year = "ULRunII"
ZZtoLep_ULRunII.components = [
    ZZtoLep_UL2016APV,
    ZZtoLep_UL2016,
    ZZtoLep_UL2017,
    ZZtoLep_UL2018,
]

TT_SemiLep_UL2018 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_SemiLep_UL2018")
TT_SemiLep_UL2018.year = "UL2018"
TT_SemiLep_UL2018.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TT_SemiLep_UL2018.sigma = 831.76 * 0.438 #pb to check

TT_Had_UL2018 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_Had_UL2018")
TT_Had_UL2018.year = "UL2018"
TT_Had_UL2018.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TT_Had_UL2018.sigma = 831.76 * 0.457 #pb to check

TT_UL2018 = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_UL2018")
TT_UL2018.year = "UL2018"
TT_UL2018.components = [
    TT_SemiLep_UL2018,
    TT_Had_UL2018,
]

TT_ULRunII = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_ULRunII")
TT_ULRunII.year = "ULRunII"
TT_ULRunII.components = [
    TT_UL2016APV,
    TT_UL2016,
    TT_UL2017,
    TT_UL2018,
]

TT_Mtt_700to1000_UL2018 = sample(TTcolor, 1, 1001, "t#bar{t} 700 < M_{tt} < 1000 GeV", "TT_Mtt_700to1000_UL2018")
TT_Mtt_700to1000_UL2018.year = "UL2018"
TT_Mtt_700to1000_UL2018.dataset = "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TT_Mtt_700to1000_UL2018.sigma = 66.85

TT_Mtt_1000toInf_UL2018 = sample(TTcolor, 1, 1001, "t#bar{t} M_{tt} > 1000 GeV", "TT_Mtt_1000toInf_UL2018")
TT_Mtt_1000toInf_UL2018.year = "UL2018"
TT_Mtt_1000toInf_UL2018.dataset = "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TT_Mtt_1000toInf_UL2018.sigma = 16.38

TT_Mtt_UL2018 = sample(TTcolor, 1, 1001, "t#bar{t} M_{tt} > 700 GeV", "TT_Mtt_UL2018")
TT_Mtt_UL2018.year = "UL2018"
TT_Mtt_UL2018.components = [
    TT_Mtt_700to1000_UL2018,
    TT_Mtt_1000toInf_UL2018,
]

TT_Mtt_ULRunII = sample(TTcolor, 1, 1001, "t#bar{t} M_{tt} > 700 GeV", "TT_Mtt_ULRunII")
TT_Mtt_ULRunII.year = "ULRunII"
TT_Mtt_ULRunII.components = [
    TT_Mtt_UL2016APV,
    TT_Mtt_UL2016,
    TT_Mtt_UL2017,
    TT_Mtt_UL2018,
]


TTTo2L2Nu_UL2018 = sample(TTdilepcolor, 1, 1001, "t#bar{t} dilep.", "TTTo2L2Nu_UL2018")
TTTo2L2Nu_UL2018.year = "UL2018"
TTTo2L2Nu_UL2018.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTTo2L2Nu_UL2018.sigma = 72.1 #831.76 * 0.105 #pb

TTTo2L2Nu_ULRunII = sample(TTdilepcolor, 1, 1001, "t#bar{t} dilep.", "TTTo2L2Nu_ULRunII")
TTTo2L2Nu_ULRunII.year = "ULRunII"
TTTo2L2Nu_ULRunII.components= [
    TTTo2L2Nu_UL2016APV,
    TTTo2L2Nu_UL2016,
    TTTo2L2Nu_UL2017,
    TTTo2L2Nu_UL2018,
]

TT_beff_UL2018 = sample(TTcolor, 1, 1001, "t#bar{t} inclusive", "TT_beff_UL2018")
TT_beff_UL2018.year = "UL2018"
TT_beff_UL2018.components = [
    TT_SemiLep_UL2018,
    TT_Had_UL2018,
    TTTo2L2Nu_UL2018,
]


### TVX ###

TTGJets_UL2018 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTGJets_UL2018")
TTGJets_UL2018.year = "UL2018"
TTGJets_UL2018.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTGJets_UL2018.sigma = 3.697

TTZToQQ_UL2018 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTZToQQ_UL2018")
TTZToQQ_UL2018.year = "UL2018"
TTZToQQ_UL2018.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTZToQQ_UL2018.sigma = 0.5297

TTZToLLNuNu_UL2018 = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> 2l2#nu", "TTZToLLNuNu_UL2018")
TTZToLLNuNu_UL2018.year = "UL2018"
TTZToLLNuNu_UL2018.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTZToLLNuNu_UL2018.sigma = 0.2529

TTWJetsToQQ_UL2018 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToQQ_UL2018")
TTWJetsToQQ_UL2018.year = "UL2018"
TTWJetsToQQ_UL2018.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTWJetsToQQ_UL2018.sigma = 0.4062

#### to be replaced with v9 when available ####
TTWJetsToLNu_UL2018 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToLNu_UL2018")
TTWJetsToLNu_UL2018.year = "UL2018"
TTWJetsToLNu_UL2018.dataset = "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTWJetsToLNu_UL2018.sigma = 0.216

#### to be replaced with v9 when available ####
tZq_ll_4f_UL2018 = sample(TVXcolor, 1, 1001, "tZq --> ll", "tZq_ll_4f_UL2018")
tZq_ll_4f_UL2018.year = "UL2018"
tZq_ll_4f_UL2018.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"
tZq_ll_4f_UL2018.sigma = 0.0758

TVX_UL2018 = sample(TVXcolor, 1, 1001, "tVX", "TVX_UL2018")
TVX_UL2018.year = "UL2018"
TVX_UL2018.components = [
    TTGJets_UL2018,
    TTZToQQ_UL2018,
    TTZToLLNuNu_UL2018,
    TTWJetsToQQ_UL2018,
    TTWJetsToLNu_UL2018,
    tZq_ll_4f_UL2018,
]

TVX_ULRunII = sample(TVXcolor, 1, 1001, "tVX", "TVX_ULRunII")
TVX_ULRunII.year = "ULRunII"
TVX_ULRunII.components = [
    TVX_UL2016APV,
    TVX_UL2016,
    TVX_UL2017,
    TVX_UL2018,
]

### VG ###

ZG_UL2018 = sample(VGcolor, 1, 1001, "Z #gamma", "ZG_UL2018")
ZG_UL2018.year = "UL2018"
ZG_UL2018.dataset = "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
ZG_UL2018.sigma = 51.1 # to check

WG_UL2018 = sample(VGcolor, 1, 1001, "W #gamma", "WG_UL2018")
WG_UL2018.year = "UL2018"
WG_UL2018.dataset = "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WG_UL2018.sigma = 191.3 # to check

VG_UL2018 = sample(VGcolor, 1, 1001, "V#gamma", "VG_UL2018")
VG_UL2018.year = "UL2018"
VG_UL2018.components = [
    ZG_UL2018,
    WG_UL2018,
]

VG_UL2016M = sample(VGcolor, 1, 1001, "V#gamma", "VG_UL2016M")
VG_UL2016M.year = "UL2016M"
VG_UL2016M.components = [
    VG_UL2016APV,
    VG_UL2016,
]

VG_ULRunII = sample(VGcolor, 1, 1001, "V#gamma", "VG_ULRunII")
VG_ULRunII.year = "ULRunII"
VG_ULRunII.components = [
    VG_UL2016APV,
    VG_UL2016,
    VG_UL2017,
    VG_UL2018,
]

### WrongSign ###

WWto2L2Nu_UL2018 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "WWto2L2Nu_UL2018")
WWto2L2Nu_UL2018.year = "UL2018"
WWto2L2Nu_UL2018.dataset = "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
WWto2L2Nu_UL2018.sigma = 12.178

GluGluToWWToENEN_UL2018 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "GluGluToWWToENEN_UL2018")
GluGluToWWToENEN_UL2018.year = "UL2018"
GluGluToWWToENEN_UL2018.dataset = "/GluGluToWWToENEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToWWToENEN_UL2018.sigma = 63.87 * 1./9. * 0.001 * 2. #36.8 * 1./9. * 1.4 * 0.001 

GluGluToWWToENMN_UL2018 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "GluGluToWWToENMN_UL2018")
GluGluToWWToENMN_UL2018.year = "UL2018"
GluGluToWWToENMN_UL2018.dataset = "/GluGluToWWToENMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToWWToENMN_UL2018.sigma = 63.87 * 1./9. * 0.001 #36.8 * 1./9. * 1.4 * 0.001 

GluGluToWWToENTN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToENTN_UL2018")
GluGluToWWToENTN_UL2018.year = "UL2018"
GluGluToWWToENTN_UL2018.dataset = "/GluGluToWWToENTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
GluGluToWWToENTN_UL2018.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToMNEN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNEN_UL2018")
GluGluToWWToMNEN_UL2018.year = "UL2018"
GluGluToWWToMNEN_UL2018.dataset = "/GluGluToWWToMNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToWWToMNEN_UL2018.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToMNMN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNMN_UL2018")
GluGluToWWToMNMN_UL2018.year = "UL2018"
GluGluToWWToMNMN_UL2018.dataset = "/GluGluToWWToMNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToWWToMNMN_UL2018.sigma = 63.87 * 1./9. * 0.001 * 2. #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToMNTN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNTN_UL2018")
GluGluToWWToMNTN_UL2018.year = "UL2018"
GluGluToWWToMNTN_UL2018.dataset = "/GluGluToWWToMNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
GluGluToWWToMNTN_UL2018.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToTNEN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNEN_UL2018")
GluGluToWWToTNEN_UL2018.year = "UL2018"
GluGluToWWToTNEN_UL2018.dataset = "/GluGluToWWToTNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
GluGluToWWToTNEN_UL2018.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToTNMN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNMN_UL2018")
GluGluToWWToTNMN_UL2018.year = "UL2018"
GluGluToWWToTNMN_UL2018.dataset = "/GluGluToWWToTNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
GluGluToWWToTNMN_UL2018.sigma = 63.87 * 1./9. * 0.001 #36.81 * 1./9. * 1.4 * 0.001 

GluGluToWWToTNTN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNTN_UL2018")
GluGluToWWToTNTN_UL2018.year = "UL2018"
GluGluToWWToTNTN_UL2018.dataset = "/GluGluToWWToTNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToWWToTNTN_UL2018.sigma = 63.87 * 1./9. * 0.001 * 2. #36.81 * 1./9. * 1.4 * 0.001 

ST_tW_top_UL2018 = sample(WScolor, 1, 1001, "Single top", "ST_tW_top_UL2018")
ST_tW_top_UL2018.year = "UL2018"
ST_tW_top_UL2018.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
ST_tW_top_UL2018.sigma = 35.85 

ST_tW_antitop_UL2018 = sample(WScolor, 1, 1001, "Single top", "ST_tW_antitop_UL2018")
ST_tW_antitop_UL2018.year = "UL2018"
ST_tW_antitop_UL2018.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
ST_tW_antitop_UL2018.sigma =  35.85 

#### to be replaced with v9 when available ####
GluGluHToWWTo2L2Nu_UL2018 = sample(WScolor, 1, 1001, "Single top", "GluGluHToWWTo2L2Nu_UL2018")
GluGluHToWWTo2L2Nu_UL2018.year = "UL2018"
GluGluHToWWTo2L2Nu_UL2018.dataset = "/GluGluHToWWTo2L2Nu_M125_TuneCP5_PSw_13TeV-powheg2-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"
GluGluHToWWTo2L2Nu_UL2018.sigma = 1.0315

GluGluHToZZTo4L_UL2018 = sample(WScolor, 1, 1001, "Single top", "GluGluHToZZTo4L_UL2018")
GluGluHToZZTo4L_UL2018.year = "UL2018"
GluGluHToZZTo4L_UL2018.dataset = "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
GluGluHToZZTo4L_UL2018.sigma = 0.0118# check nowe

GluGluHToTauTau_UL2018 = sample(WScolor, 1, 1001, "Single top", "GluGluHToTauTau_UL2018")
GluGluHToTauTau_UL2018.year = "UL2018"
GluGluHToTauTau_UL2018.dataset = "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
GluGluHToTauTau_UL2018.sigma = 2.7757# check nowe

VBFHToWWTo2L2Nu_UL2018 = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToWWTo2L2Nu_UL2018")
VBFHToWWTo2L2Nu_UL2018.year = "UL2018"
VBFHToWWTo2L2Nu_UL2018.dataset = "/VBFHToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
VBFHToWWTo2L2Nu_UL2018.sigma = 0.0896 # check nowe

VBFHToTauTau_UL2018 = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToTauTau_UL2018")
VBFHToTauTau_UL2018.year = "UL2018"
VBFHToTauTau_UL2018.dataset = "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
VBFHToTauTau_UL2018.sigma = 0.237 # check nowe

ttHToNonbb_UL2018 = sample(WScolor, 1, 1001, "ttH", "ttHToNonbb_UL2018")
ttHToNonbb_UL2018.year = "UL2018"
ttHToNonbb_UL2018.dataset = "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
ttHToNonbb_UL2018.sigma = 0.2120

VHToNonbb_UL2018 = sample(WScolor, 1, 1001, "VH", "VHToNonbb_UL2018")
VHToNonbb_UL2018.year = "UL2018"
VHToNonbb_UL2018.dataset = "/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
VHToNonbb_UL2018.sigma = 0.952 # check nowe

DYJetsToLL_M50_FxFx_UL2018 = sample(WZcolor, 1, 1001, "DYJetsToLL_M50", "DYJetsToLL_M50_FxFx_UL2018")
DYJetsToLL_M50_FxFx_UL2018.year = "UL2018"
DYJetsToLL_M50_FxFx_UL2018.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
DYJetsToLL_M50_FxFx_UL2018.sigma = 7181.0 #6077.22 #6529.0

WrongSign_UL2018 = sample(WScolor, 1, 1001, "OS + (Z/#gamma + jets)", "WrongSign_UL2018")
WrongSign_UL2018.year = "UL2018"
WrongSign_UL2018.components = [
    WWto2L2Nu_UL2018,
    GluGluToWWToENEN_UL2018,
    GluGluToWWToENMN_UL2018,
    GluGluToWWToENTN_UL2018,
    GluGluToWWToMNEN_UL2018,
    GluGluToWWToMNMN_UL2018,
    GluGluToWWToMNTN_UL2018,
    GluGluToWWToTNEN_UL2018,
    GluGluToWWToTNMN_UL2018,
    GluGluToWWToTNTN_UL2018,
    ST_tW_top_UL2018,
    ST_tW_antitop_UL2018,
    GluGluHToWWTo2L2Nu_UL2018,
    GluGluHToZZTo4L_UL2018,
    GluGluHToTauTau_UL2018,
    VBFHToWWTo2L2Nu_UL2018,
    VBFHToTauTau_UL2018,
    ttHToNonbb_UL2018,
    VHToNonbb_UL2018,
    DYJetsToLL_M50_FxFx_UL2018,
]

WrongSign_ML_UL2018 = sample(WScolor, 1, 1001, "OS", "WrongSign_ML_UL2018")
WrongSign_ML_UL2018.year = "UL2018"
WrongSign_ML_UL2018.components = [
    WWto2L2Nu_UL2018,
    GluGluToWWToENEN_UL2018,
    GluGluToWWToENMN_UL2018,
    GluGluToWWToENTN_UL2018,
    GluGluToWWToMNEN_UL2018,
    GluGluToWWToMNMN_UL2018,
    GluGluToWWToMNTN_UL2018,
    GluGluToWWToTNEN_UL2018,
    GluGluToWWToTNMN_UL2018,
    GluGluToWWToTNTN_UL2018,
    ST_tW_top_UL2018,
    ST_tW_antitop_UL2018,
    GluGluHToWWTo2L2Nu_UL2018,
    GluGluHToZZTo4L_UL2018,
    GluGluHToTauTau_UL2018,
    VBFHToWWTo2L2Nu_UL2018,
    VBFHToTauTau_UL2018,
    ttHToNonbb_UL2018,
    VHToNonbb_UL2018,
]

WrongSign_ULRunII = sample(WScolor, 1, 1001, "OS + (Z/#gamma + jets)", "WrongSign_ULRunII")
WrongSign_ULRunII.year = "ULRunII"
WrongSign_ULRunII.components = [
    WrongSign_UL2016APV,
    WrongSign_UL2016,
    WrongSign_UL2017,
    WrongSign_UL2018,
]

WrongSign_ML_ULRunII = sample(WScolor, 1, 1001, "OS", "WrongSign_ML_ULRunII")
WrongSign_ML_ULRunII.year = "ULRunII"
WrongSign_ML_ULRunII.components = [
    WrongSign_ML_UL2016APV,
    WrongSign_ML_UL2016,
    WrongSign_ML_UL2017,
    WrongSign_ML_UL2018,
]

### Triboson ###

WWTo2L2Nu_DoubleScattering_UL2018 = sample(TBcolor, 1, 1001, "WWTo2L2Nu_DoubleScattering", "WWTo2L2Nu_DoubleScattering_UL2018")
WWTo2L2Nu_DoubleScattering_UL2018.year = "UL2018"
WWTo2L2Nu_DoubleScattering_UL2018.dataset = ""
WWTo2L2Nu_DoubleScattering_UL2018.sigma =  0.1703#pb

WWW_4F_UL2018 = sample(TBcolor, 1, 1001, "WWW_4F", "WWW_4F_UL2018")
WWW_4F_UL2018.year = "UL2018"
WWW_4F_UL2018.dataset = "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM"
WWW_4F_UL2018.sigma = 0.2086#pb

WWZ_4F_UL2018 = sample(TBcolor, 1, 1001, "WWZ_4F", "WWZ_4F_UL2018")
WWZ_4F_UL2018.year = "UL2018"
WWZ_4F_UL2018.dataset = "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM"
WWZ_4F_UL2018.sigma = 0.1651#pb

WZZ_UL2018 = sample(TBcolor, 1, 1001, "WZZ", "WZZ_UL2018")
WZZ_UL2018.year = "UL2018"
WZZ_UL2018.dataset = "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM"
WZZ_UL2018.sigma = 0.05565#pb

ZZZ_UL2018 = sample(TBcolor, 1, 1001, "ZZZ", "ZZZ_UL2018")
ZZZ_UL2018.year = "UL2018"
ZZZ_UL2018.dataset = "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM"
ZZZ_UL2018.sigma = 0.01398#pb

WWG_UL2018 = sample(TBcolor, 1, 1001, "WWG", "WWG_UL2018")
WWG_UL2018.year = "UL2018"
WWG_UL2018.dataset = "/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
WWG_UL2018.sigma = 0.2147#pb

Triboson_UL2018 = sample(TBcolor, 1, 1001, "Triboson", "Triboson_UL2018")
Triboson_UL2018.year = "UL2018"
Triboson_UL2018.components = [
    #WWTo2L2Nu_DoubleScattering_UL2018,
    WWW_4F_UL2018,
    WWZ_4F_UL2018,
    WZZ_UL2018,
    ZZZ_UL2018,
    WWG_UL2018,
]

Triboson_ULRunII = sample(TBcolor, 1, 1001, "Triboson", "Triboson_ULRunII")
Triboson_ULRunII.year = "ULRunII"
Triboson_ULRunII.components = [
    Triboson_UL2016APV,
    Triboson_UL2016,
    Triboson_UL2017,
    Triboson_UL2018,
]

### WJets ###

WJetsHT70to100_UL2018 = sample(WJcolor, 1, 1001, "W + Jets", "WJetsHT70to100_UL2018")
WJetsHT70to100_UL2018.year = "UL2018"
WJetsHT70to100_UL2018.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WJetsHT70to100_UL2018.sigma = 1264. * 1.21 #pb

WJetsHT100to200_UL2018 = sample(WJcolor, 1, 1001, "W + Jets 100 < HT < 200", "WJetsHT100to200_UL2018")
WJetsHT100to200_UL2018.year = "UL2018"
WJetsHT100to200_UL2018.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"
WJetsHT100to200_UL2018.sigma = 1345 * 1.21 #pb

WJetsHT200to400_UL2018 = sample(WJcolor, 1, 1001, "W + Jets 200 < HT < 400", "WJetsHT200to400_UL2018")
WJetsHT200to400_UL2018.year = "UL2018"
WJetsHT200to400_UL2018.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WJetsHT200to400_UL2018.sigma = 359.7 * 1.21 #pb

WJetsHT400to600_UL2018 = sample(WJcolor, 1, 1001, "W + Jets 200 < HT < 400", "WJetsHT400to600_UL2018")
WJetsHT400to600_UL2018.year = "UL2018"
WJetsHT400to600_UL2018.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WJetsHT400to600_UL2018.sigma = 48.91 * 1.21 #pb

WJetsHT600to800_UL2018 = sample(WJcolor, 1, 1001, "W + Jets 600 < HT < 800", "WJetsHT600to800_UL2018")
WJetsHT600to800_UL2018.year = "UL2018"
WJetsHT600to800_UL2018.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WJetsHT600to800_UL2018.sigma = 12.05 * 1.21 #pb

WJetsHT800to1200_UL2018 = sample(WJcolor, 1, 1001, "W + Jets 800 < HT < 1200", "WJetsHT800to1200_UL2018")
WJetsHT800to1200_UL2018.year = "UL2018"
WJetsHT800to1200_UL2018.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WJetsHT800to1200_UL2018.sigma = 5.501 * 1.21 #pb

WJetsHT1200to2500_UL2018 = sample(WJcolor, 1, 1001, "W + Jets 1200 < HT < 2500", "WJetsHT1200to2500_UL2018")
WJetsHT1200to2500_UL2018.year = "UL2018"
WJetsHT1200to2500_UL2018.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WJetsHT1200to2500_UL2018.sigma = 1.329 * 1.21 #pb

WJetsHT2500toInf_UL2018 = sample(WJcolor, 1, 1001, "W + Jets HT > 2500", "WJetsHT2500toInf_UL2018")
WJetsHT2500toInf_UL2018.year = "UL2018"
WJetsHT2500toInf_UL2018.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
WJetsHT2500toInf_UL2018.sigma = 0.008001 * 1.21 #pb

WJets_UL2018 = sample(WJcolor, 1, 1001, "W + Jets", "WJets_UL2018")
WJets_UL2018.year = "UL2018"
WJets_UL2018.components = [
    WJetsHT70to100_UL2018,
    WJetsHT100to200_UL2018,
    WJetsHT200to400_UL2018,
    WJetsHT400to600_UL2018,
    WJetsHT600to800_UL2018,
    WJetsHT800to1200_UL2018,
    WJetsHT1200to2500_UL2018,
    WJetsHT2500toInf_UL2018,
]

WJets_ULRunII = sample(WJcolor, 1, 1001, "W + Jets", "WJets_ULRunII")
WJets_ULRunII.year = "ULRunII"
WJets_ULRunII.components = [
    WJets_UL2016APV,
    WJets_UL2016,
    WJets_UL2017,
    WJets_UL2018,
]


WJets_0J_UL2018 = sample(WJcolor, 1, 1001, "W + Jets 0J", "WJets_0J_UL2018")
WJets_0J_UL2018.year = "UL2018"
WJets_0J_UL2018.dataset = "/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WJets_0J_UL2018.sigma = 53330.0 * 1.21 #pb

WJets_1J_UL2018 = sample(WJcolor, 1, 1001, "W + Jets 1J", "WJets_1J_UL2018")
WJets_1J_UL2018.year = "UL2018"
WJets_1J_UL2018.dataset = "/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WJets_1J_UL2018.sigma = 8875.0 * 1.21 #pb

WJets_2J_UL2018 = sample(WJcolor, 1, 1001, "W + Jets 2J", "WJets_2J_UL2018")
WJets_2J_UL2018.year = "UL2018"
WJets_2J_UL2018.dataset = "/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WJets_2J_UL2018.sigma = 3338.0 * 1.21 #pb

WJets_Jbin_UL2018 = sample(WJcolor, 1, 1001, "W + Jets #jets binned", "WJets_Jbin_UL2018")
WJets_Jbin_UL2018.year = "UL2018"
WJets_Jbin_UL2018.components = [
    WJets_0J_UL2018,
    WJets_1J_UL2018,
    WJets_2J_UL2018,
]

WJets_Jbin_ULRunII = sample(WJcolor, 1, 1001, "W + Jets #jets binned", "WJets_Jbin_ULRunII")
WJets_Jbin_ULRunII.year = "ULRunII"
WJets_Jbin_ULRunII.components = [
    WJets_Jbin_UL2016APV,
    WJets_Jbin_UL2016,
    WJets_Jbin_UL2017,
    WJets_Jbin_UL2018,
]

### WZ ###

WZ_UL2018 = sample(WZcolor, 1, 1001, "WZ", "WZ_UL2018")
WZ_UL2018.year = "UL2018"
WZ_UL2018.dataset = "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WZ_UL2018.sigma = 27.59

WZ_ULRunII = sample(WZcolor, 1, 1001, "WZ", "WZ_ULRunII")
WZ_ULRunII.year = "ULRunII"
WZ_ULRunII.components = [
    WZ_UL2016APV,
    WZ_UL2016,
    WZ_UL2017,
    WZ_UL2018,
]

### DYJets ###

DYJetsToLL_M10to50_UL2018 = sample(WZcolor, 1, 1001, "DY+jets (10 < M_{ll} < 50 GeV", "DYJetsToLL_M10to50_UL2018")
DYJetsToLL_M10to50_UL2018.year = "UL2018"
DYJetsToLL_M10to50_UL2018.dataset = "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
DYJetsToLL_M10to50_UL2018.sigma = 18610.

DYJetsToLL_M50_UL2018 = sample(WZcolor, 1, 1001, "DYJetsToLL_M50", "DYJetsToLL_M50_UL2018")
DYJetsToLL_M50_UL2018.year = "UL2018"
DYJetsToLL_M50_UL2018.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
DYJetsToLL_M50_UL2018.sigma = 6077.22

DYJetsToLL_M50_UL2018_ext = sample(WZcolor, 1, 1001, "DYJetsToLL_M50", "DYJetsToLL_M50_UL2018_ext")
DYJetsToLL_M50_UL2018_ext.year = "UL2018"
DYJetsToLL_M50_UL2018_ext.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v1/NANOAODSIM"
DYJetsToLL_M50_UL2018_ext.sigma = 6077.22

DYJetsToLL_UL2018 = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_UL2018")
DYJetsToLL_UL2018.year = "UL2018"
DYJetsToLL_UL2018.components = [
    #DYJetsToLL_M10to50_UL2018,
    DYJetsToLL_M50_UL2018,
    #DYJetsToLL_M50_UL2018_ext,
]

DYJetsToLL_ULRunII = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_ULRunII")
DYJetsToLL_ULRunII.year = "ULRunII"
DYJetsToLL_ULRunII.components = [
    DYJetsToLL_UL2016APV,
    DYJetsToLL_UL2016,
    DYJetsToLL_UL2017,
    DYJetsToLL_UL2018,
]

DYJetsToLL_FxFx_UL2018 = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_FxFx_UL2018")
DYJetsToLL_FxFx_UL2018.year = "UL2018"
DYJetsToLL_FxFx_UL2018.components = [
    #DYJetsToLL_M10to50_UL2018,
    DYJetsToLL_M50_FxFx_UL2018,
]

DYJetsToLL_FxFx_ULRunII = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_FxFx_ULRunII")
DYJetsToLL_FxFx_ULRunII.year = "ULRunII"
DYJetsToLL_FxFx_ULRunII.components = [
    DYJetsToLL_FxFx_UL2016APV,
    DYJetsToLL_FxFx_UL2016,
    DYJetsToLL_FxFx_UL2017,
    DYJetsToLL_FxFx_UL2018,
]


DYJetsToLL_0J_FxFx_UL2018 = sample(DYcolor, 1, 1001, "DYJetsToLL_0J", "DYJetsToLL_0J_FxFx_UL2018")
DYJetsToLL_0J_FxFx_UL2018.year = "UL2018"
DYJetsToLL_0J_FxFx_UL2018.dataset = "/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
DYJetsToLL_0J_FxFx_UL2018.sigma = 5993 #5129.0

DYJetsToLL_1J_FxFx_UL2018 = sample(DYcolor, 1, 1001, "DYJetsToLL_1J", "DYJetsToLL_1J_FxFx_UL2018")
DYJetsToLL_1J_FxFx_UL2018.year = "UL2018"
DYJetsToLL_1J_FxFx_UL2018.dataset = "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
DYJetsToLL_1J_FxFx_UL2018.sigma = 1474 #951.5

DYJetsToLL_2J_FxFx_UL2018 = sample(DYcolor, 1, 1001, "DYJetsToLL_2J", "DYJetsToLL_2J_FxFx_UL2018")
DYJetsToLL_2J_FxFx_UL2018.year = "UL2018"
DYJetsToLL_2J_FxFx_UL2018.dataset = "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
DYJetsToLL_2J_FxFx_UL2018.sigma = 111.1 #361.4

DYJetsToLL_Jbin_FxFx_UL2018 = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_Jbin_FxFx_UL2018")
DYJetsToLL_Jbin_FxFx_UL2018.year = "UL2018"
DYJetsToLL_Jbin_FxFx_UL2018.components = [
    DYJetsToLL_0J_FxFx_UL2018,
    DYJetsToLL_1J_FxFx_UL2018,
    DYJetsToLL_2J_FxFx_UL2018,
]

DYJetsToLL_Jbin_FxFx_ULRunII = sample(DYcolor, 1, 1001, "Z/#gamma + Jets", "DYJetsToLL_Jbin_FxFx_ULRunII")
DYJetsToLL_Jbin_FxFx_ULRunII.year = "ULRunII"
DYJetsToLL_Jbin_FxFx_ULRunII.components = [
    DYJetsToLL_Jbin_FxFx_UL2016APV,
    DYJetsToLL_Jbin_FxFx_UL2016,
    DYJetsToLL_Jbin_FxFx_UL2017,
    DYJetsToLL_Jbin_FxFx_UL2018,
]

### WpWp EWK ###
WpWpJJ_EWK_UL2018 = sample(EWVBScolor, 1, 1001, "EW SSWW VBS", "WpWpJJ_EWK_UL2018")
WpWpJJ_EWK_UL2018.sigma = 0.0287
WpWpJJ_EWK_UL2018.year = "UL2018"
WpWpJJ_EWK_UL2018.dataset = "/WpWpJJ_EWKnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"

### WpWp QCD ###
WpWpJJ_QCD_UL2018 = sample(QCDVBScolor, 1, 1001, "QCD SSWW", "WpWpJJ_QCD_UL2018")
WpWpJJ_QCD_UL2018.sigma = 0.01538
WpWpJJ_QCD_UL2018.year = "UL2018"
WpWpJJ_QCD_UL2018.dataset = "/WpWpJJ_QCDnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"

WpWpJJ_UL2018 = sample(WWJJcolor, 1, 1001, "EW+QCD VBS SSWW", "WpWpJJ_UL2018")
WpWpJJ_UL2018.year = "UL2018"
WpWpJJ_UL2018.components = [
    WpWpJJ_EWK_UL2018,
    WpWpJJ_QCD_UL2018,
]

WpWpJJ_EWK_ULRunII = sample(EWVBScolor, 1, 1001, "EW SSWW VBS", "WpWpJJ_EWK_ULRunII")
WpWpJJ_EWK_ULRunII.year = "ULRunII"
WpWpJJ_EWK_ULRunII.components = [
    WpWpJJ_EWK_UL2016APV,
    WpWpJJ_EWK_UL2016,
    WpWpJJ_EWK_UL2017,
    WpWpJJ_EWK_UL2018,
]

WpWpJJ_QCD_ULRunII = sample(QCDVBScolor, 1, 1001, "QCD SSWW", "WpWpJJ_QCD_ULRunII")
WpWpJJ_QCD_ULRunII.year = "ULRunII"
WpWpJJ_QCD_ULRunII.components = [
    WpWpJJ_QCD_UL2016APV,
    WpWpJJ_QCD_UL2016,
    WpWpJJ_QCD_UL2017,
    WpWpJJ_QCD_UL2018,
]


WpWpJJ_ULRunII = sample(WWJJcolor, 1, 1001, "EW+QCD VBS SSWW", "WpWpJJ_ULRunII")
WpWpJJ_ULRunII.year = "ULRunII"
WpWpJJ_ULRunII.components = [
    WpWpJJ_UL2016APV,
    WpWpJJ_UL2016,
    WpWpJJ_UL2017,
    WpWpJJ_UL2018,
]


### VBS SSWW polarized ###

#### in production stage ####
VBS_SSWW_LL_SM_UL2018 = sample(VBSLLcolor, 1, 1001, "VBS SSWW LL", "VBS_SSWW_LL_SM_UL2018")
VBS_SSWW_LL_SM_UL2018.sigma = 0.002014
VBS_SSWW_LL_SM_UL2018.year = "UL2018"
VBS_SSWW_LL_SM_UL2018.dataset = "/VBS_SSWW_LL_polarization_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"

#### in production stage ####
VBS_SSWW_TL_SM_UL2018 = sample(VBSTLcolor, 1, 1001, "VBS SSWW TL", "VBS_SSWW_TL_SM_UL2018")
VBS_SSWW_TL_SM_UL2018.sigma = 0.01036
VBS_SSWW_TL_SM_UL2018.year = "UL2018"
VBS_SSWW_TL_SM_UL2018.dataset = "/VBS_SSWW_TL_polarization_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

#### in production stage ####
VBS_SSWW_TT_SM_UL2018 = sample(VBSTTcolor, 1, 1001, "VBS SSWW TT", "VBS_SSWW_TT_SM_UL2018")
VBS_SSWW_TT_SM_UL2018.sigma = 0.01595
VBS_SSWW_TT_SM_UL2018.year = "UL2018"
VBS_SSWW_TT_SM_UL2018.dataset = "/VBS_SSWW_TT_polarization_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

VBS_SSWW_SM_UL2018 = sample(VBScolor, 1, 1001, "VBS SSWW (pol. sum)", "VBS_SSWW_SM_UL2018")
VBS_SSWW_SM_UL2018.year = "UL2018"
VBS_SSWW_SM_UL2018.components = [
    VBS_SSWW_LL_SM_UL2018,
    VBS_SSWW_TL_SM_UL2018,
    VBS_SSWW_TT_SM_UL2018,
]

VBS_SSWW_SM_ULRunII = sample(VBScolor, 1, 1001, "VBS SSWW (pol. sum)", "VBS_SSWW_SM_ULRunII")
VBS_SSWW_SM_ULRunII.year = "ULRunII"
VBS_SSWW_SM_ULRunII.components = [
    VBS_SSWW_SM_UL2016APV,
    VBS_SSWW_SM_UL2016,
    VBS_SSWW_SM_UL2017,
    VBS_SSWW_SM_UL2018,
]

VBS_SSWW_LL_SM_ULRunII = sample(VBSLLcolor, 1, 1001, "VBS SSWW LL", "VBS_SSWW_LL_SM_ULRunII")
VBS_SSWW_LL_SM_ULRunII.year = "ULRunII"
VBS_SSWW_LL_SM_ULRunII.components = [
    VBS_SSWW_LL_SM_UL2016APV,
    VBS_SSWW_LL_SM_UL2016,
    VBS_SSWW_LL_SM_UL2017,
    VBS_SSWW_LL_SM_UL2018,
]

VBS_SSWW_TL_SM_ULRunII = sample(VBSTLcolor, 1, 1001, "VBS SSWW TL", "VBS_SSWW_TL_SM_ULRunII")
VBS_SSWW_TL_SM_ULRunII.year = "ULRunII"
VBS_SSWW_TL_SM_ULRunII.components = [
    VBS_SSWW_TL_SM_UL2016APV,
    VBS_SSWW_TL_SM_UL2016,
    VBS_SSWW_TL_SM_UL2017,
    VBS_SSWW_TL_SM_UL2018,
]

VBS_SSWW_TT_SM_ULRunII = sample(VBSTTcolor, 1, 1001, "VBS SSWW TT", "VBS_SSWW_TT_SM_ULRunII")
VBS_SSWW_TT_SM_ULRunII.year = "ULRunII"
VBS_SSWW_TT_SM_ULRunII.components = [
    VBS_SSWW_TT_SM_UL2016APV,
    VBS_SSWW_TT_SM_UL2016,
    VBS_SSWW_TT_SM_UL2017,
    VBS_SSWW_TT_SM_UL2018,
]

VBS_SSWW_cW_BSM_UL2018 = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (only BSM)", "VBS_SSWW_cW_BSM_UL2018")
VBS_SSWW_cW_BSM_UL2018.year = "UL2018"
VBS_SSWW_cW_BSM_UL2018.dataset = "/VBS_SSWW_cW_BSM_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
VBS_SSWW_cW_BSM_UL2018.sigma = 0.01388

VBS_SSWW_cW_BSM_ULRunII = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (only BSM)", "VBS_SSWW_cW_BSM_ULRunII")
VBS_SSWW_cW_BSM_ULRunII.year = "ULRunII"
VBS_SSWW_cW_BSM_ULRunII.components = [
    VBS_SSWW_cW_BSM_UL2016,
    VBS_SSWW_cW_BSM_UL2016APV,
    VBS_SSWW_cW_BSM_UL2017,
    VBS_SSWW_cW_BSM_UL2018,
]


VBS_SSWW_cW_INT_UL2018 = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (only INT)", "VBS_SSWW_cW_INT_UL2018")
VBS_SSWW_cW_INT_UL2018.year = "UL2018"
VBS_SSWW_cW_INT_UL2018.dataset = "/VBS_SSWW_cW_INT_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
VBS_SSWW_cW_INT_UL2018.sigma = 0.0009987

VBS_SSWW_cW_UL2018 = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (BSM+INT)", "VBS_SSWW_cW_UL2018")
VBS_SSWW_cW_UL2018.year = "UL2018"
VBS_SSWW_cW_UL2018.components = [
    VBS_SSWW_cW_BSM_UL2018,
    VBS_SSWW_cW_INT_UL2018,
]

VBS_SSWW_cW_ULRunII = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} (BSM+INT)", "VBS_SSWW_cW_ULRunII")
VBS_SSWW_cW_ULRunII.year = "ULRunII"
VBS_SSWW_cW_ULRunII.components = [
    VBS_SSWW_cW_UL2016APV,
    VBS_SSWW_cW_UL2016,
    VBS_SSWW_cW_UL2017,
    VBS_SSWW_cW_UL2018,
]

VBS_SSWW_cW_SM_UL2018 = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} + SM", "VBS_SSWW_cW_SM_UL2018")
VBS_SSWW_cW_SM_UL2018.year = "UL2018"
VBS_SSWW_cW_SM_UL2018.components = [
    VBS_SSWW_cW_BSM_UL2018,
    VBS_SSWW_cW_INT_UL2018,
    VBS_SSWW_LL_SM_UL2018,
    VBS_SSWW_TL_SM_UL2018,
    VBS_SSWW_TT_SM_UL2018,
]

VBS_SSWW_cW_SM_ULRunII = sample(CWcolor, 1, 1001, "VBS SSWW c_{W} + SM", "VBS_SSWW_cW_SM_ULRunII")
VBS_SSWW_cW_SM_ULRunII.year = "ULRunII"
VBS_SSWW_cW_SM_ULRunII.components = [
    VBS_SSWW_cW_SM_UL2016APV,
    VBS_SSWW_cW_SM_UL2016,
    VBS_SSWW_cW_SM_UL2017,
    VBS_SSWW_cW_SM_UL2018,
]

VBS_SSWW_cHW_BSM_UL2018 = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (only BSM)", "VBS_SSWW_cHW_BSM_UL2018")
VBS_SSWW_cHW_BSM_UL2018.year = "UL2018"
VBS_SSWW_cHW_BSM_UL2018.dataset = "/VBS_SSWW_cHW_BSM_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
VBS_SSWW_cHW_BSM_UL2018.sigma = 0.0001415

VBS_SSWW_cHW_BSM_ULRunII = sample(CHWcolor, 1, 1001, "VBS SSWW c_{W} (only BSM)", "VBS_SSWW_cHW_BSM_ULRunII")
VBS_SSWW_cHW_BSM_ULRunII.year = "ULRunII"
VBS_SSWW_cHW_BSM_ULRunII.components = [
    VBS_SSWW_cHW_BSM_UL2016,
    VBS_SSWW_cHW_BSM_UL2016APV,
    VBS_SSWW_cHW_BSM_UL2017,
    VBS_SSWW_cHW_BSM_UL2018,
]

VBS_SSWW_cHW_INT_UL2018 = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (only INT)", "VBS_SSWW_cHW_INT_UL2018")
VBS_SSWW_cHW_INT_UL2018.year = "UL2018"
VBS_SSWW_cHW_INT_UL2018.dataset = "/VBS_SSWW_cHW_INT_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
VBS_SSWW_cHW_INT_UL2018.sigma = 0.0005059

VBS_SSWW_cHW_UL2018 = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (BSM+INT)", "VBS_SSWW_cHW_UL2018")
VBS_SSWW_cHW_UL2018.year = "UL2018"
VBS_SSWW_cHW_UL2018.components = [
    VBS_SSWW_cHW_BSM_UL2018,
    VBS_SSWW_cHW_INT_UL2018,
]

VBS_SSWW_cHW_ULRunII = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} (BSM+INT)", "VBS_SSWW_cHW_ULRunII")
VBS_SSWW_cHW_ULRunII.year = "ULRunII"
VBS_SSWW_cHW_ULRunII.components = [
    VBS_SSWW_cHW_UL2016APV,
    VBS_SSWW_cHW_UL2016,
    VBS_SSWW_cHW_UL2017,
    VBS_SSWW_cHW_UL2018,
]

VBS_SSWW_cHW_SM_UL2018 = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} + SM", "VBS_SSWW_cHW_SM_UL2018")
VBS_SSWW_cHW_SM_UL2018.year = "UL2018"
VBS_SSWW_cHW_SM_UL2018.components = [
    VBS_SSWW_cHW_BSM_UL2018,
    VBS_SSWW_cHW_INT_UL2018,
    VBS_SSWW_LL_SM_UL2018,
    VBS_SSWW_TL_SM_UL2018,
    VBS_SSWW_TT_SM_UL2018,
]

VBS_SSWW_cHW_SM_ULRunII = sample(CHWcolor, 1, 1001, "VBS SSWW c_{HW} + SM", "VBS_SSWW_cHW_SM_ULRunII")
VBS_SSWW_cHW_SM_ULRunII.year = "ULRunII"
VBS_SSWW_cHW_SM_ULRunII.components = [
    VBS_SSWW_cHW_SM_UL2016APV,
    VBS_SSWW_cHW_SM_UL2016,
    VBS_SSWW_cHW_SM_UL2017,
    VBS_SSWW_cHW_SM_UL2018,
]

VBS_SSWW_cW_cHW_UL2018 = sample(CWcolor, 1, 1001, "VBS SSWW int c_{W} + c_{HW})", "VBS_SSWW_cW_cHW_UL2018")
VBS_SSWW_cW_cHW_UL2018.year = "UL2018"
VBS_SSWW_cW_cHW_UL2018.dataset = "/VBS_SSWW_cW_cHW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
VBS_SSWW_cW_cHW_UL2018.sigma = 0.002014

VBS_SSWW_cW_cHW_ULRunII = sample(CWcolor, 1, 1001, "VBS SSWW int c_{W} + c_{HW})", "VBS_SSWW_cW_cHW_ULRunII")
VBS_SSWW_cW_cHW_ULRunII.year = "ULRunII"
VBS_SSWW_cW_cHW_ULRunII.components= [
    VBS_SSWW_cW_cHW_UL2016,
    VBS_SSWW_cW_cHW_UL2016APV,
    VBS_SSWW_cW_cHW_UL2017,
    VBS_SSWW_cW_cHW_UL2018,
]

VBS_SSWW_DIM6_UL2018 = sample(ROOT.kGreen+3, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_DIM6_UL2018")
VBS_SSWW_DIM6_UL2018.year = "UL2018"
VBS_SSWW_DIM6_UL2018.components = [
    VBS_SSWW_cHW_BSM_UL2018,
    VBS_SSWW_cW_BSM_UL2018,
    VBS_SSWW_cHW_INT_UL2018,
    VBS_SSWW_cW_INT_UL2018,
    VBS_SSWW_cW_cHW_UL2018,
]

VBS_SSWW_DIM6_ULRunII = sample(ROOT.kGreen+3, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_DIM6_ULRunII")
VBS_SSWW_DIM6_ULRunII.year = "ULRunII"
VBS_SSWW_DIM6_ULRunII.components = [
    VBS_SSWW_DIM6_UL2016APV,
    VBS_SSWW_DIM6_UL2016,
    VBS_SSWW_DIM6_UL2017,
    VBS_SSWW_DIM6_UL2018,
]

VBS_SSWW_DIM6_SM_UL2018 = sample(ROOT.kGreen+2, 1, 1001, "VBS SSWW dim-6 EFT + SM", "VBS_SSWW_DIM6_SM_UL2018")
VBS_SSWW_DIM6_SM_UL2018.year = "UL2018"
VBS_SSWW_DIM6_SM_UL2018.components = [
    VBS_SSWW_LL_SM_UL2018,
    VBS_SSWW_TL_SM_UL2018,
    VBS_SSWW_TT_SM_UL2018,
    VBS_SSWW_cHW_BSM_UL2018,
    VBS_SSWW_cHW_INT_UL2018, 
    VBS_SSWW_cW_BSM_UL2018,
    VBS_SSWW_cW_INT_UL2018,
    VBS_SSWW_cW_cHW_UL2018,
]

VBS_SSWW_DIM6_SM_ULRunII = sample(ROOT.kGreen+2, 1, 1001, "VBS SSWW dim-6 EFT + SM", "VBS_SSWW_DIM6_SM_ULRunII")
VBS_SSWW_DIM6_SM_ULRunII.year = "ULRunII"
VBS_SSWW_DIM6_SM_ULRunII.components = [
    VBS_SSWW_DIM6_SM_UL2016APV,
    VBS_SSWW_DIM6_SM_UL2016,
    VBS_SSWW_DIM6_SM_UL2017,
    VBS_SSWW_DIM6_SM_UL2018,
]

VBS_SSWW_aQGC_UL2018 = sample(aQGCcolor, 1, 1001, "VBS SSWW dim-8 EFT", "VBS_SSWW_aQGC_UL2018")
VBS_SSWW_aQGC_UL2018.sigma = 0.1077
VBS_SSWW_aQGC_UL2018.year = "UL2018"
VBS_SSWW_aQGC_UL2018.dataset = "/WWJJ_SS_WToLNu_EWK_aQGC-FT-FS-FM_TuneCP5_13TeV_madgraph-pythia8/apiccine-NanoAODv9_UL2018_Legnaro-00000000000000000000000000000000/USER"

VBS_SSWW_aTGC_UL2018 = sample(aTGCcolor, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_aTGC_UL2018")
VBS_SSWW_aTGC_UL2018.sigma = 1.083
VBS_SSWW_aTGC_UL2018.year = "UL2018"
VBS_SSWW_aTGC_UL2018.dataset = "/WplusminusWplusminus2JTo2L2Nu2J_EWK_dim6_TuneCP5_13TeV-madgraph-pythia8/apiccine-NanoAODv9_UL2018_Legnaro-00000000000000000000000000000000/USER"

VBS_SSWW_aTGC_mixed_UL2018 = sample(aTGCcolor, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_aTGC_mixed_UL2018")
VBS_SSWW_aTGC_mixed_UL2018.sigma = 1.083
VBS_SSWW_aTGC_mixed_UL2018.year = "UL2018"
VBS_SSWW_aTGC_mixed_UL2018.dataset = "/WplusminusWplusminus2JTo2L2Nu2J_EWK_dim6_mixed_TuneCP5_13TeV-madgraph-pythia8/apiccine-NanoAODv9_UL2018_Legnaro-00000000000000000000000000000000/USER"

VBS_SSWW_aQGC_ULRunII = sample(aQGCcolor, 1, 1001, "VBS SSWW dim-8 EFT", "VBS_SSWW_aQGC_ULRunII")
VBS_SSWW_aQGC_ULRunII.year = "ULRunII"
VBS_SSWW_aQGC_ULRunII.components = [
    VBS_SSWW_aQGC_UL2016APV,
    VBS_SSWW_aQGC_UL2016,
    VBS_SSWW_aQGC_UL2017,
    VBS_SSWW_aQGC_UL2018,
]

VBS_SSWW_aTGC_ULRunII = sample(aTGCcolor, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_aTGC_ULRunII")
VBS_SSWW_aTGC_ULRunII.year = "ULRunII"
VBS_SSWW_aTGC_ULRunII.components = [
    VBS_SSWW_aTGC_UL2016APV,
    VBS_SSWW_aTGC_UL2016,
    VBS_SSWW_aTGC_UL2017,
    VBS_SSWW_aTGC_UL2018,
]

VBS_SSWW_aTGC_mixed_ULRunII = sample(aTGCcolor, 1, 1001, "VBS SSWW dim-6 EFT", "VBS_SSWW_aTGC_mixed_ULRunII")
VBS_SSWW_aTGC_mixed_ULRunII.year = "ULRunII"
VBS_SSWW_aTGC_mixed_ULRunII.components = [
    VBS_SSWW_aTGC_mixed_UL2016APV,
    VBS_SSWW_aTGC_mixed_UL2016,
    VBS_SSWW_aTGC_mixed_UL2017,
    VBS_SSWW_aTGC_mixed_UL2018,
]

DataMuA_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuA_UL2018")
DataMuA_UL2018.runP = 'A'
DataMuA_UL2018.year = "UL2018"
#DataMuA_UL2018.dataset = "/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD"
DataMuA_UL2018.dataset = "/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD"

DataMuB_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB_UL2018")
DataMuB_UL2018.runP = 'B'
DataMuB_UL2018.year = "UL2018"
#DataMuB_UL2018.dataset = "/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD"
DataMuB_UL2018.dataset = "/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD"

DataMuC_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuC_UL2018")
DataMuC_UL2018.runP = 'C'
DataMuC_UL2018.year = "UL2018"
#DataMuC_UL2018.dataset = "/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD"
DataMuC_UL2018.dataset = "/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD"

DataMuD_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuD_UL2018")
DataMuD_UL2018.runP = 'D'
DataMuD_UL2018.year = "UL2018"
#DataMuD_UL2018.dataset = "/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"
DataMuD_UL2018.dataset = "/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD"

DataMu_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_UL2018")
DataMu_UL2018.year = "UL2018"
DataMu_UL2018.components =  [
    DataMuA_UL2018,
    DataMuB_UL2018,
    DataMuC_UL2018,
    DataMuD_UL2018,
]

DataMu_ULRunII = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_ULRunII")
DataMu_ULRunII.year = "ULRunII"
DataMu_ULRunII.components =  [
    DataMu_UL2016APV,
    DataMu_UL2016,
    DataMu_UL2017,
    DataMu_UL2018,
]

DataEleA_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleA_UL2018")
DataEleA_UL2018.runP = 'A'
DataEleA_UL2018.year = "UL2018"
DataEleA_UL2018.dataset = "/EGamma/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD"

DataEleB_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB_UL2018")
DataEleB_UL2018.runP = 'B'
DataEleB_UL2018.year = "UL2018"
DataEleB_UL2018.dataset = "/EGamma/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataEleC_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleC_UL2018")
DataEleC_UL2018.runP = 'C'
DataEleC_UL2018.year = "UL2018"
DataEleC_UL2018.dataset = "/EGamma/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataEleD_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleD_UL2018")
DataEleD_UL2018.runP = 'D'
DataEleD_UL2018.year = "UL2018"
DataEleD_UL2018.dataset = "/EGamma/Run2018D-UL2018_MiniAODv2_NanoAODv9-v3/NANOAOD"

DataEle_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_UL2018")
DataEle_UL2018.year = "UL2018"
DataEle_UL2018.components =  [
    DataEleA_UL2018,
    DataEleB_UL2018,
    DataEleC_UL2018,
    DataEleD_UL2018,
]

DataEle_ULRunII = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_ULRunII")
DataEle_ULRunII.year = "ULRunII"
DataEle_ULRunII.components =  [
    DataEle_UL2016APV,
    DataEle_UL2016,
    DataEle_UL2017,
    DataEle_UL2018,
]

DataHTA_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTA_UL2018")
DataHTA_UL2018.runP = 'A'
DataHTA_UL2018.year = "UL2018"
DataHTA_UL2018.dataset = "/JetHT/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD"

DataHTB_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB_UL2018")
DataHTB_UL2018.runP = 'B'
DataHTB_UL2018.year = "UL2018"
DataHTB_UL2018.dataset = "/JetHT/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"

DataHTC_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTC_UL2018")
DataHTC_UL2018.runP = 'C'
DataHTC_UL2018.year = "UL2018"
DataHTC_UL2018.dataset = "/JetHT/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"

#### to be replaced with v9 when available ####
DataHTD_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTD_UL2018")
DataHTD_UL2018.runP = 'D'
DataHTD_UL2018.year = "UL2018"
DataHTD_UL2018.dataset = "/JetHT/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"

DataHT_UL2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_UL2018")
DataHT_UL2018.year = "UL2018"
DataHT_UL2018.components =  [
    DataHTA_UL2018,
    DataHTB_UL2018,
    DataHTC_UL2018,
    DataHTD_UL2018,
]

FakeElePromptTau_UL2018 = sample(ROOT.kGray, 1, 1001, "Nonprompt e Prompt #tau", "FakeElePromptTau_UL2018")
FakeElePromptTau_UL2018.year = "UL2018"
FakeElePromptTau_UL2018.components = [
    DataEle_UL2018,
    #DataHT_UL2018,
    WJets_UL2018,
    DYJetsToLL_UL2018
]

PromptEleFakeTau_UL2018 = sample(ROOT.kGray+2, 1, 1001, "Prompt e Fake #tau", "PromptEleFakeTau_UL2018")
PromptEleFakeTau_UL2018.year = "UL2018"
PromptEleFakeTau_UL2018.components = [
    DataEle_UL2018,
    #DataHT_UL2018,
    WJets_UL2018,
    DYJetsToLL_UL2018
]

FakeEleFakeTau_UL2018 = sample(ROOT.kGray+3, 1, 1001, "Nonprompt e Fake #tau", "FakeEleFakeTau_UL2018")
FakeEleFakeTau_UL2018.year = "UL2018"
FakeEleFakeTau_UL2018.components = [
    DataEle_UL2018,
    #DataHT_UL2018,
    WJets_UL2018,
    DYJetsToLL_UL2018
]

FakeEle_UL2018 = sample(ROOT.kGray, 1, 1001, "Nonprompt leptons", "FakeEle_UL2018")
FakeEle_UL2018.year = "UL2018"
FakeEle_UL2018.components = [
    DataEle_UL2018,
    #DataHT_UL2018,
    WJets_UL2018,
    DYJetsToLL_FxFx_UL2018,
    TT_UL2018,
]

FakeEle_ULRunII = sample(ROOT.kGray, 1, 1001, "Nonprompt leptons", "FakeEle_ULRunII")
FakeEle_ULRunII.year = "ULRunII"
FakeEle_ULRunII.components = [
    FakeEle_UL2016APV,
    FakeEle_UL2016,
    FakeEle_UL2017,
    FakeEle_UL2018,
]

FakeElePromptTau_ULRunII = sample(ROOT.kGray, 1, 1001, "Nonprompt e Prompt #tau", "FakeElePromptTau_ULRunII")
FakeElePromptTau_ULRunII.year = "ULRunII"
FakeElePromptTau_ULRunII.components = [
    FakeElePromptTau_UL2016APV,
    FakeElePromptTau_UL2016,
    FakeElePromptTau_UL2017,
    FakeElePromptTau_UL2018,
]

PromptEleFakeTau_ULRunII = sample(ROOT.kGray+2, 1, 1001, "Prompt e Fake #tau", "PromptEleFakeTau_ULRunII")
PromptEleFakeTau_ULRunII.year = "ULRunII"
PromptEleFakeTau_ULRunII.components = [
    PromptEleFakeTau_UL2016APV,
    PromptEleFakeTau_UL2016,
    PromptEleFakeTau_UL2017,
    PromptEleFakeTau_UL2018,
]

FakeEleFakeTau_ULRunII = sample(ROOT.kGray+3, 1, 1001, "Nonprompt e Fake #tau", "FakeEleFakeTau_ULRunII")
FakeEleFakeTau_ULRunII.year = "ULRunII"
FakeEleFakeTau_ULRunII.components = [
    FakeEleFakeTau_UL2016APV,
    FakeEleFakeTau_UL2016,
    FakeEleFakeTau_UL2017,
    FakeEleFakeTau_UL2018,
]


FakeMuPromptTau_UL2018 = sample(ROOT.kGray, 1, 1001, "Nonprompt #mu Prompt #tau", "FakeMuPromptTau_UL2018")
FakeMuPromptTau_UL2018.year = "UL2018"
FakeMuPromptTau_UL2018.components = [
    DataMu_UL2018,
    #DataHT_UL2018,
    WJets_UL2018,
    DYJetsToLL_UL2018
]

PromptMuFakeTau_UL2018 = sample(ROOT.kGray+2, 1, 1001, "Prompt #mu Fake #tau", "PromptMuFakeTau_UL2018")
PromptMuFakeTau_UL2018.year = "UL2018"
PromptMuFakeTau_UL2018.components = [
    DataMu_UL2018,
    #DataHT_UL2018,
    WJets_UL2018,
    DYJetsToLL_UL2018
]

FakeMuFakeTau_UL2018 = sample(ROOT.kGray+3, 1, 1001, "Nonprompt #mu Fake #tau", "FakeMuFakeTau_UL2018")
FakeMuFakeTau_UL2018.year = "UL2018"
FakeMuFakeTau_UL2018.components = [
    DataMu_UL2018,
    #DataHT_UL2018,
    WJets_UL2018,
    DYJetsToLL_UL2018
]

FakeMu_UL2018 = sample(ROOT.kGray, 1, 1001, "Nonprompt leptons", "FakeMu_UL2018")
FakeMu_UL2018.year = "UL2018"
FakeMu_UL2018.components = [
    DataMu_UL2018,
    #DataHT_UL2018,
    WJets_UL2018,
    DYJetsToLL_FxFx_UL2018,
    TT_UL2018,
]

FakeMu_ULRunII = sample(ROOT.kGray, 1, 1001, "Nonprompt leptons", "FakeMu_ULRunII")
FakeMu_ULRunII.year = "ULRunII"
FakeMu_ULRunII.components = [
    FakeMu_UL2016APV,
    FakeMu_UL2016,
    FakeMu_UL2017,
    FakeMu_UL2018,
]

FakeMuPromptTau_ULRunII = sample(ROOT.kGray, 1, 1001, "Nonprompt #mu Prompt #tau", "FakeMuPromptTau_ULRunII")
FakeMuPromptTau_ULRunII.year = "ULRunII"
FakeMuPromptTau_ULRunII.components = [
    FakeMuPromptTau_UL2016APV,
    FakeMuPromptTau_UL2016,
    FakeMuPromptTau_UL2017,
    FakeMuPromptTau_UL2018,
]

PromptMuFakeTau_ULRunII = sample(ROOT.kGray+2, 1, 1001, "Prompt #mu Fake #tau", "PromptMuFakeTau_ULRunII")
PromptMuFakeTau_ULRunII.year = "ULRunII"
PromptMuFakeTau_ULRunII.components = [
    PromptMuFakeTau_UL2016APV,
    PromptMuFakeTau_UL2016,
    PromptMuFakeTau_UL2017,
    PromptMuFakeTau_UL2018,
]

FakeMuFakeTau_ULRunII = sample(ROOT.kGray+3, 1, 1001, "Nonprompt #mu Fake #tau", "FakeMuFakeTau_ULRunII")
FakeMuFakeTau_ULRunII.year = "ULRunII"
FakeMuFakeTau_ULRunII.components = [
    FakeMuFakeTau_UL2016APV,
    FakeMuFakeTau_UL2016,
    FakeMuFakeTau_UL2017,
    FakeMuFakeTau_UL2018,
]

SampleHTFake_UL2018 = sample(ROOT.kBlack, 1, 1001, "Sample for FR", "SampleHTFake_UL2018")
SampleHTFake_UL2018.year = "UL2018"
SampleHTFake_UL2018.components = [
    DataHTA_UL2018,
    DataHTB_UL2018,
    DataHTC_UL2018,
    DataHTD_UL2018,
    WJetsHT70to100_UL2018,
    WJetsHT100to200_UL2018,
    WJetsHT200to400_UL2018,
    WJetsHT400to600_UL2018,
    WJetsHT600to800_UL2018,
    WJetsHT800to1200_UL2018,
    WJetsHT1200to2500_UL2018,
    WJetsHT2500toInf_UL2018,
    DYJetsToLL_M10to50_UL2018,
    DYJetsToLL_M50_UL2018,
    #DYJetsToLL_M50_UL2018_ext,
    TT_Had_UL2018,
    TT_SemiLep_UL2018,
    ZZTo2L2Nu_UL2018,
    ZZTo4L_UL2018,
    GluGluToContinToZZTo2e2nu_UL2018,
    GluGluToContinToZZTo4e_UL2018,
    GluGluToContinToZZTo2e2mu_UL2018,
    GluGluToContinToZZTo2e2tau_UL2018,
    GluGluToContinToZZTo2mu2nu_UL2018,
    GluGluToContinToZZTo4mu_UL2018,
    GluGluToContinToZZTo2mu2tau_UL2018,
    #GluGluToContinToZZTo2tau2nu_UL2018,
    GluGluToContinToZZTo4tau_UL2018,
]

Others_UL2016APV = sample(othcolor, 1, 1001, "Other bkgs.", "Others_UL2016APV")
Others_UL2016APV.year = "UL2016APV"
Others_UL2016APV.components = [
    ZZtoLep_UL2016APV,
    Triboson_UL2016APV,
    TVX_UL2016APV,
    VG_UL2016APV,
    WZ_UL2016APV,
]

Others_UL2016 = sample(othcolor, 1, 1001, "Other bkgs.", "Others_UL2016")
Others_UL2016.year = "UL2016"
Others_UL2016.components = [
    ZZtoLep_UL2016,
    Triboson_UL2016,
    TVX_UL2016,
    VG_UL2016,
    WZ_UL2016,
]

Others_UL2016M = sample(othcolor, 1, 1001, "Other bkgs.", "Others_UL2016M")
Others_UL2016M.year = "UL2016M"
Others_UL2016M.components = [
    ZZtoLep_UL2016M,
    Triboson_UL2016M,
    TVX_UL2016M,
    VG_UL2016M,
    WZ_UL2016M,
]

Others_UL2017 = sample(othcolor, 1, 1001, "Other bkgs.", "Others_UL2017")
Others_UL2017.year = "UL2017"
Others_UL2017.components = [
    ZZtoLep_UL2017,
    Triboson_UL2017,
    TVX_UL2017,
    VG_UL2017,
    WZ_UL2017,
]

Others_UL2018 = sample(othcolor, 1, 1001, "Other bkgs.", "Others_UL2018")
Others_UL2018.year = "UL2018"
Others_UL2018.components = [
    ZZtoLep_UL2018,
    Triboson_UL2018,
    TVX_UL2018,
    VG_UL2018,
    WZ_UL2018,
]
    
Others_ULRunII = sample(othcolor, 1, 1001, "Other bkgs.", "Others_ULRunII")
Others_ULRunII.year = "ULRunII"
Others_ULRunII.components = [
    ZZtoLep_ULRunII,
    Triboson_ULRunII,
    TVX_ULRunII,
    VG_ULRunII,
    WZ_ULRunII,
]


########################################################

sample_dict={
    "ZZtoLep_UL2016APV":ZZtoLep_UL2016APV,
    "ZZTo2L2Nu_UL2016APV":ZZTo2L2Nu_UL2016APV, "ZZTo4L_UL2016APV":ZZTo4L_UL2016APV, "GluGluToContinToZZTo4e_UL2016APV":GluGluToContinToZZTo4e_UL2016APV, "GluGluToContinToZZTo2e2mu_UL2016APV":GluGluToContinToZZTo2e2mu_UL2016APV, "GluGluToContinToZZTo2e2tau_UL2016APV":GluGluToContinToZZTo2e2tau_UL2016APV,"GluGluToContinToZZTo2mu2nu_UL2016APV":GluGluToContinToZZTo2mu2nu_UL2016APV, "GluGluToContinToZZTo4mu_UL2016APV":GluGluToContinToZZTo4mu_UL2016APV, "GluGluToContinToZZTo2mu2tau_UL2016APV":GluGluToContinToZZTo2mu2tau_UL2016APV, "GluGluToContinToZZTo2tau2nu_UL2016APV":GluGluToContinToZZTo2tau2nu_UL2016APV, "GluGluToContinToZZTo4tau_UL2016APV":GluGluToContinToZZTo4tau_UL2016APV, "GluGluToContinToZZTo2e2nu_UL2016APV":GluGluToContinToZZTo2e2nu_UL2016APV,
    "TT_UL2016APV":TT_UL2016APV,
    "TT_SemiLep_UL2016APV":TT_SemiLep_UL2016APV, "TT_Had_UL2016APV":TT_Had_UL2016APV,
    "TTTo2L2Nu_UL2016APV":TTTo2L2Nu_UL2016APV,
    "TT_Mtt_UL2016APV":TT_Mtt_UL2016APV,
    "TT_Mtt_700to1000_UL2016APV":TT_Mtt_700to1000_UL2016APV,"TT_Mtt_1000toInf_UL2016APV":TT_Mtt_1000toInf_UL2016APV,
    "TT_beff_UL2016APV":TT_beff_UL2016APV,
    "TVX_UL2016APV":TVX_UL2016APV,
    "TTGJets_UL2016APV":TTGJets_UL2016APV, "TTZToQQ_UL2016APV":TTZToQQ_UL2016APV, "TTZToLLNuNu_UL2016APV":TTZToLLNuNu_UL2016APV, "TTWJetsToQQ_UL2016APV":TTWJetsToQQ_UL2016APV, "TTWJetsToLNu_UL2016APV":TTWJetsToLNu_UL2016APV, "tZq_ll_4f_UL2016APV":tZq_ll_4f_UL2016APV,
    "VG_UL2016APV":VG_UL2016APV,
    "ZG_UL2016APV":ZG_UL2016APV, "WG_UL2016APV":WG_UL2016APV,
    "WrongSign_UL2016APV":WrongSign_UL2016APV,
    "WrongSign_ML_UL2016APV":WrongSign_ML_UL2016APV,
    "WWto2L2Nu_UL2016APV":WWto2L2Nu_UL2016APV, "GluGluToWWToENEN_UL2016APV":GluGluToWWToENEN_UL2016APV, "GluGluToWWToENMN_UL2016APV":GluGluToWWToENMN_UL2016APV, "GluGluToWWToENTN_UL2016APV":GluGluToWWToENTN_UL2016APV, "GluGluToWWToMNEN_UL2016APV":GluGluToWWToMNEN_UL2016APV, "GluGluToWWToMNMN_UL2016APV":GluGluToWWToMNMN_UL2016APV, "GluGluToWWToMNTN_UL2016APV":GluGluToWWToMNTN_UL2016APV, "GluGluToWWToTNEN_UL2016APV":GluGluToWWToTNEN_UL2016APV, "GluGluToWWToTNMN_UL2016APV":GluGluToWWToTNMN_UL2016APV, "GluGluToWWToTNTN_UL2016APV":GluGluToWWToTNTN_UL2016APV, "ST_tW_top_UL2016APV":ST_tW_top_UL2016APV, "ST_tW_antitop_UL2016APV":ST_tW_antitop_UL2016APV, "GluGluHToWWTo2L2Nu_UL2016APV":GluGluHToWWTo2L2Nu_UL2016APV, "GluGluHToZZTo4L_UL2016APV":GluGluHToZZTo4L_UL2016APV, "GluGluHToTauTau_UL2016APV":GluGluHToTauTau_UL2016APV, "VBFHToWWTo2L2Nu_UL2016APV": VBFHToWWTo2L2Nu_UL2016APV, "VBFHToTauTau_UL2016APV":VBFHToTauTau_UL2016APV, "ttHToNonbb_UL2016APV":ttHToNonbb_UL2016APV, "VHToNonbb_UL2016APV":VHToNonbb_UL2016APV, 
    "Triboson_UL2016APV":Triboson_UL2016APV,
    "WWTo2L2Nu_DoubleScattering_UL2016":WWTo2L2Nu_DoubleScattering_UL2016, "WWW_4F_UL2016APV":WWW_4F_UL2016APV, "WWZ_4F_UL2016APV":WWZ_4F_UL2016APV, "WZZ_UL2016APV":WZZ_UL2016APV, "ZZZ_UL2016APV":ZZZ_UL2016APV, "ZZZ_UL2016APV":ZZZ_UL2016APV, "WWG_UL2016APV":WWG_UL2016APV,
    "WJets_UL2016APV":WJets_UL2016APV,
    "WJetsHT70to100_UL2016APV":WJetsHT70to100_UL2016APV, "WJetsHT100to200_UL2016APV":WJetsHT100to200_UL2016APV, "WJetsHT200to400_UL2016APV":WJetsHT200to400_UL2016APV, "WJetsHT400to600_UL2016APV":WJetsHT400to600_UL2016APV, "WJetsHT600to800_UL2016APV":WJetsHT600to800_UL2016APV, "WJetsHT800to1200_UL2016APV":WJetsHT800to1200_UL2016APV, "WJetsHT1200to2500_UL2016APV":WJetsHT1200to2500_UL2016APV, "WJetsHT2500toInf_UL2016APV":WJetsHT2500toInf_UL2016APV,
    "WJets_Jbin_UL2016APV":WJets_Jbin_UL2016APV,
    "WJets_0J_UL2016APV":WJets_0J_UL2016APV,"WJets_1J_UL2016APV":WJets_1J_UL2016APV,"WJets_2J_UL2016APV":WJets_2J_UL2016APV,
    "WZ_UL2016APV":WZ_UL2016APV,
    "DYJetsToLL_UL2016APV":DYJetsToLL_UL2016APV,
    "DYJetsToLL_M10to50_UL2016APV":DYJetsToLL_M10to50_UL2016APV, "DYJetsToLL_M50_UL2016APV":DYJetsToLL_M50_UL2016APV, "DYJetsToLL_M50_UL2016APV_ext":DYJetsToLL_M50_UL2016APV_ext,
    "DYJetsToLL_FxFx_UL2016APV":DYJetsToLL_FxFx_UL2016APV,
    "DYJetsToLL_M50_FxFx_UL2016APV":DYJetsToLL_M50_FxFx_UL2016APV,
    "DYJetsToLL_Jbin_FxFx_UL2016APV":DYJetsToLL_Jbin_FxFx_UL2016APV,
    "DYJetsToLL_0J_FxFx_UL2016APV":DYJetsToLL_0J_FxFx_UL2016APV,"DYJetsToLL_1J_FxFx_UL2016APV":DYJetsToLL_1J_FxFx_UL2016APV,"DYJetsToLL_2J_FxFx_UL2016APV":DYJetsToLL_2J_FxFx_UL2016APV,
    "WpWpJJ_UL2016APV":WpWpJJ_UL2016APV,"WpWpJJ_EWK_UL2016APV":WpWpJJ_EWK_UL2016APV,"WpWpJJ_QCD_UL2016APV":WpWpJJ_QCD_UL2016APV,
    "VBS_SSWW_SM_UL2016APV":VBS_SSWW_SM_UL2016APV,
    "VBS_SSWW_LL_SM_UL2016APV":VBS_SSWW_LL_SM_UL2016APV, "VBS_SSWW_TL_SM_UL2016APV":VBS_SSWW_TL_SM_UL2016APV, "VBS_SSWW_TT_SM_UL2016APV":VBS_SSWW_TT_SM_UL2016APV,
    "VBS_SSWW_cW_UL2016APV":VBS_SSWW_cW_UL2016APV,
    "VBS_SSWW_cW_SM_UL2016APV":VBS_SSWW_cW_SM_UL2016APV,
    "VBS_SSWW_cW_BSM_UL2016APV":VBS_SSWW_cW_BSM_UL2016APV, "VBS_SSWW_cW_INT_UL2016APV":VBS_SSWW_cW_INT_UL2016APV,
    "VBS_SSWW_cHW_UL2016APV":VBS_SSWW_cHW_UL2016APV,
    "VBS_SSWW_cHW_SM_UL2016APV":VBS_SSWW_cHW_SM_UL2016APV,
    "VBS_SSWW_cHW_BSM_UL2016APV":VBS_SSWW_cHW_BSM_UL2016APV, "VBS_SSWW_cHW_INT_UL2016APV":VBS_SSWW_cHW_INT_UL2016APV,
    "VBS_SSWW_cW_cHW_UL2016APV":VBS_SSWW_cW_cHW_UL2016APV,
    "VBS_SSWW_DIM6_UL2016APV":VBS_SSWW_DIM6_UL2016APV,
    "VBS_SSWW_DIM6_SM_UL2016APV":VBS_SSWW_DIM6_SM_UL2016APV,
    "VBS_SSWW_aQGC_UL2016APV":VBS_SSWW_aQGC_UL2016APV,
    "VBS_SSWW_aTGC_UL2016APV":VBS_SSWW_aTGC_UL2016APV,
    "VBS_SSWW_aTGC_mixed_UL2016APV":VBS_SSWW_aTGC_mixed_UL2016APV,

    "ZZtoLep_UL2016":ZZtoLep_UL2016,
    "ZZTo2L2Nu_UL2016":ZZTo2L2Nu_UL2016, "ZZTo4L_UL2016":ZZTo4L_UL2016, "GluGluToContinToZZTo4e_UL2016":GluGluToContinToZZTo4e_UL2016, "GluGluToContinToZZTo2e2mu_UL2016":GluGluToContinToZZTo2e2mu_UL2016, "GluGluToContinToZZTo2e2tau_UL2016":GluGluToContinToZZTo2e2tau_UL2016, "GluGluToContinToZZTo2mu2nu_UL2016":GluGluToContinToZZTo2mu2nu_UL2016, "GluGluToContinToZZTo4mu_UL2016":GluGluToContinToZZTo4mu_UL2016, "GluGluToContinToZZTo2mu2tau_UL2016":GluGluToContinToZZTo2mu2tau_UL2016, "GluGluToContinToZZTo2tau2nu_UL2016":GluGluToContinToZZTo2tau2nu_UL2016, "GluGluToContinToZZTo4tau_UL2016":GluGluToContinToZZTo4tau_UL2016, "GluGluToContinToZZTo2e2nu_UL2016":GluGluToContinToZZTo2e2nu_UL2016,
    "TT_UL2016":TT_UL2016,
    "TT_SemiLep_UL2016":TT_SemiLep_UL2016, "TT_Had_UL2016":TT_Had_UL2016,
    "TTTo2L2Nu_UL2016":TTTo2L2Nu_UL2016,
    "TT_Mtt_UL2016":TT_Mtt_UL2016,
    "TT_Mtt_700to1000_UL2016":TT_Mtt_700to1000_UL2016,"TT_Mtt_1000toInf_UL2016":TT_Mtt_1000toInf_UL2016,
    "TT_beff_UL2016":TT_beff_UL2016,
    "TVX_UL2016":TVX_UL2016,
    "TTGJets_UL2016":TTGJets_UL2016, "TTZToQQ_UL2016":TTZToQQ_UL2016, "TTZToLLNuNu_UL2016":TTZToLLNuNu_UL2016, "TTWJetsToQQ_UL2016":TTWJetsToQQ_UL2016, "TTWJetsToLNu_UL2016":TTWJetsToLNu_UL2016, "tZq_ll_4f_UL2016":tZq_ll_4f_UL2016,
    "VG_UL2016":VG_UL2016,
    "ZG_UL2016":ZG_UL2016, "WG_UL2016":WG_UL2016,
    "WrongSign_UL2016":WrongSign_UL2016,
    "WrongSign_ML_UL2016":WrongSign_ML_UL2016,
    "WWto2L2Nu_UL2016":WWto2L2Nu_UL2016, "GluGluToWWToENEN_UL2016":GluGluToWWToENEN_UL2016, "GluGluToWWToENMN_UL2016":GluGluToWWToENMN_UL2016, "GluGluToWWToENTN_UL2016":GluGluToWWToENTN_UL2016, "GluGluToWWToMNEN_UL2016":GluGluToWWToMNEN_UL2016, "GluGluToWWToMNMN_UL2016":GluGluToWWToMNMN_UL2016, "GluGluToWWToMNTN_UL2016":GluGluToWWToMNTN_UL2016, "GluGluToWWToTNEN_UL2016":GluGluToWWToTNEN_UL2016, "GluGluToWWToTNMN_UL2016":GluGluToWWToTNMN_UL2016, "GluGluToWWToTNTN_UL2016":GluGluToWWToTNTN_UL2016, "ST_tW_top_UL2016":ST_tW_top_UL2016, "ST_tW_antitop_UL2016":ST_tW_antitop_UL2016, "GluGluHToWWTo2L2Nu_UL2016":GluGluHToWWTo2L2Nu_UL2016, "GluGluHToZZTo4L_UL2016":GluGluHToZZTo4L_UL2016, "GluGluHToTauTau_UL2016":GluGluHToTauTau_UL2016, "VBFHToWWTo2L2Nu_UL2016": VBFHToWWTo2L2Nu_UL2016, "VBFHToTauTau_UL2016":VBFHToTauTau_UL2016, "ttHToNonbb_UL2016":ttHToNonbb_UL2016, "VHToNonbb_UL2016":VHToNonbb_UL2016,
    "Triboson_UL2016":Triboson_UL2016,
    "WWTo2L2Nu_DoubleScattering_UL2016":WWTo2L2Nu_DoubleScattering_UL2016, "WWW_4F_UL2016":WWW_4F_UL2016, "WWZ_4F_UL2016":WWZ_4F_UL2016, "WZZ_UL2016":WZZ_UL2016, "ZZZ_UL2016":ZZZ_UL2016, "ZZZ_UL2016":ZZZ_UL2016, "WWG_UL2016":WWG_UL2016,
    "WJets_UL2016":WJets_UL2016,
    "WJetsHT70to100_UL2016":WJetsHT70to100_UL2016, "WJetsHT100to200_UL2016":WJetsHT100to200_UL2016, "WJetsHT200to400_UL2016":WJetsHT200to400_UL2016, "WJetsHT400to600_UL2016":WJetsHT400to600_UL2016, "WJetsHT600to800_UL2016":WJetsHT600to800_UL2016, "WJetsHT800to1200_UL2016":WJetsHT800to1200_UL2016, "WJetsHT1200to2500_UL2016":WJetsHT1200to2500_UL2016, "WJetsHT2500toInf_UL2016":WJetsHT2500toInf_UL2016,
    "WJets_Jbin_UL2016":WJets_Jbin_UL2016,
    "WJets_0J_UL2016":WJets_0J_UL2016,"WJets_1J_UL2016":WJets_1J_UL2016,"WJets_2J_UL2016":WJets_2J_UL2016,
    "WZ_UL2016":WZ_UL2016,
    "DYJetsToLL_UL2016":DYJetsToLL_UL2016,
    "DYJetsToLL_M10to50_UL2016":DYJetsToLL_M10to50_UL2016, "DYJetsToLL_M50_UL2016":DYJetsToLL_M50_UL2016, "DYJetsToLL_M50_UL2016_ext":DYJetsToLL_M50_UL2016_ext,
    "DYJetsToLL_FxFx_UL2016":DYJetsToLL_FxFx_UL2016,
    "DYJetsToLL_M50_FxFx_UL2016":DYJetsToLL_M50_FxFx_UL2016,
    "DYJetsToLL_Jbin_FxFx_UL2016":DYJetsToLL_Jbin_FxFx_UL2016,
    "DYJetsToLL_0J_FxFx_UL2016":DYJetsToLL_0J_FxFx_UL2016,"DYJetsToLL_1J_FxFx_UL2016":DYJetsToLL_1J_FxFx_UL2016,"DYJetsToLL_2J_FxFx_UL2016":DYJetsToLL_2J_FxFx_UL2016,
    "WpWpJJ_UL2016":WpWpJJ_UL2016,"WpWpJJ_EWK_UL2016":WpWpJJ_EWK_UL2016,"WpWpJJ_QCD_UL2016":WpWpJJ_QCD_UL2016,
    "VBS_SSWW_SM_UL2016":VBS_SSWW_SM_UL2016,
    "VBS_SSWW_LL_SM_UL2016":VBS_SSWW_LL_SM_UL2016, "VBS_SSWW_TL_SM_UL2016":VBS_SSWW_TL_SM_UL2016, "VBS_SSWW_TT_SM_UL2016":VBS_SSWW_TT_SM_UL2016,
    "VBS_SSWW_cW_UL2016":VBS_SSWW_cW_UL2016,
    "VBS_SSWW_cW_SM_UL2016":VBS_SSWW_cW_SM_UL2016,
    "VBS_SSWW_cW_BSM_UL2016":VBS_SSWW_cW_BSM_UL2016, "VBS_SSWW_cW_INT_UL2016":VBS_SSWW_cW_INT_UL2016,
    "VBS_SSWW_cW_BSM_UL2016M":VBS_SSWW_cW_BSM_UL2016M,
    "VBS_SSWW_cW_BSM_ULRunII":VBS_SSWW_cW_BSM_ULRunII,
    "VBS_SSWW_cHW_UL2016":VBS_SSWW_cHW_UL2016,
    "VBS_SSWW_cHW_SM_UL2016":VBS_SSWW_cHW_SM_UL2016,
    "VBS_SSWW_cHW_BSM_UL2016":VBS_SSWW_cHW_BSM_UL2016, "VBS_SSWW_cHW_INT_UL2016":VBS_SSWW_cHW_INT_UL2016,
    "VBS_SSWW_cW_cHW_UL2016":VBS_SSWW_cW_cHW_UL2016,
    "VBS_SSWW_cHW_BSM_UL2016M":VBS_SSWW_cHW_BSM_UL2016M,
    "VBS_SSWW_cHW_BSM_ULRunII":VBS_SSWW_cHW_BSM_ULRunII,
    "VBS_SSWW_DIM6_UL2016":VBS_SSWW_DIM6_UL2016,
    "VBS_SSWW_DIM6_SM_UL2016":VBS_SSWW_DIM6_SM_UL2016,
    "VBS_SSWW_aQGC_UL2016":VBS_SSWW_aQGC_UL2016,
    "VBS_SSWW_aTGC_UL2016":VBS_SSWW_aTGC_UL2016,
    "VBS_SSWW_aTGC_mixed_UL2016":VBS_SSWW_aTGC_mixed_UL2016,

    "ZZtoLep_UL2016M":ZZtoLep_UL2016M,
    "TT_UL2016M":TT_UL2016M,
    "TT_Mtt_UL2016M":TT_Mtt_UL2016M,
    "TTTo2L2Nu_UL2016M":TTTo2L2Nu_UL2016M,
    "TVX_UL2016M":TVX_UL2016M,
    "VG_UL2016M":VG_UL2016M,
    "WrongSign_UL2016M":WrongSign_UL2016M,
    "WrongSign_ML_UL2016M":WrongSign_ML_UL2016M,
    "Triboson_UL2016M":Triboson_UL2016M,
    "WJets_UL2016M":WJets_UL2016M,
    "WJets_Jbin_UL2016M":WJets_Jbin_UL2016M,
    "WZ_UL2016M":WZ_UL2016M,
    "DYJetsToLL_UL2016M":DYJetsToLL_UL2016M,
    "DYJetsToLL_FxFx_UL2016M":DYJetsToLL_FxFx_UL2016M,
    "DYJetsToLL_Jbin_FxFx_UL2016M":DYJetsToLL_Jbin_FxFx_UL2016M,
    "WpWpJJ_UL2016M":WpWpJJ_UL2016M,"WpWpJJ_EWK_UL2016M":WpWpJJ_EWK_UL2016M,"WpWpJJ_QCD_UL2016M":WpWpJJ_QCD_UL2016M,
    "VBS_SSWW_SM_UL2016M":VBS_SSWW_SM_UL2016M,
    "VBS_SSWW_LL_SM_UL2016M":VBS_SSWW_LL_SM_UL2016M, "VBS_SSWW_TL_SM_UL2016M":VBS_SSWW_TL_SM_UL2016M, "VBS_SSWW_TT_SM_UL2016M":VBS_SSWW_TT_SM_UL2016M,
    "VBS_SSWW_cW_UL2016M":VBS_SSWW_cW_UL2016M,
    "VBS_SSWW_cW_SM_UL2016M":VBS_SSWW_cW_SM_UL2016M,
    "VBS_SSWW_cHW_UL2016M":VBS_SSWW_cHW_UL2016M,
    "VBS_SSWW_cHW_SM_UL2016M":VBS_SSWW_cHW_SM_UL2016M,
    "VBS_SSWW_cW_cHW_UL2016M":VBS_SSWW_cW_cHW_UL2016M,
    "VBS_SSWW_DIM6_UL2016M":VBS_SSWW_DIM6_UL2016M,
    "VBS_SSWW_DIM6_SM_UL2016M":VBS_SSWW_DIM6_SM_UL2016M,
    "VBS_SSWW_aQGC_UL2016M":VBS_SSWW_aQGC_UL2016M,
    "VBS_SSWW_aTGC_UL2016M":VBS_SSWW_aTGC_UL2016M,
    "VBS_SSWW_aTGC_mixed_UL2016M":VBS_SSWW_aTGC_mixed_UL2016M,

    "ZZtoLep_UL2017":ZZtoLep_UL2017,
    "ZZTo2L2Nu_UL2017":ZZTo2L2Nu_UL2017, "ZZTo4L_UL2017":ZZTo4L_UL2017, "GluGluToContinToZZTo4e_UL2017":GluGluToContinToZZTo4e_UL2017, "GluGluToContinToZZTo2e2mu_UL2017":GluGluToContinToZZTo2e2mu_UL2017, "GluGluToContinToZZTo2e2tau_UL2017":GluGluToContinToZZTo2e2tau_UL2017, "GluGluToContinToZZTo2mu2nu_UL2017":GluGluToContinToZZTo2mu2nu_UL2017, "GluGluToContinToZZTo4mu_UL2017":GluGluToContinToZZTo4mu_UL2017, "GluGluToContinToZZTo2mu2tau_UL2017":GluGluToContinToZZTo2mu2tau_UL2017, "GluGluToContinToZZTo2tau2nu_UL2017":GluGluToContinToZZTo2tau2nu_UL2017, "GluGluToContinToZZTo4tau_UL2017":GluGluToContinToZZTo4tau_UL2017, "GluGluToContinToZZTo2e2nu_UL2017":GluGluToContinToZZTo2e2nu_UL2017,
    "TT_UL2017":TT_UL2017,
    "TT_SemiLep_UL2017":TT_SemiLep_UL2017, "TT_Had_UL2017":TT_Had_UL2017,
    "TTTo2L2Nu_UL2017":TTTo2L2Nu_UL2017,
    "TT_Mtt_UL2017":TT_Mtt_UL2017,
    "TT_Mtt_700to1000_UL2017":TT_Mtt_700to1000_UL2017,"TT_Mtt_1000toInf_UL2017":TT_Mtt_1000toInf_UL2017,
    "TT_beff_UL2017":TT_beff_UL2017,
    "TVX_UL2017":TVX_UL2017,
    "TTGJets_UL2017":TTGJets_UL2017, "TTZToQQ_UL2017":TTZToQQ_UL2017, "TTZToLLNuNu_UL2017":TTZToLLNuNu_UL2017, "TTWJetsToQQ_UL2017":TTWJetsToQQ_UL2017, "TTWJetsToLNu_UL2017":TTWJetsToLNu_UL2017, "tZq_ll_4f_UL2017":tZq_ll_4f_UL2017,
    "VG_UL2017":VG_UL2017,
    "ZG_UL2017":ZG_UL2017, "WG_UL2017":WG_UL2017,
    "WrongSign_UL2017":WrongSign_UL2017,
    "WrongSign_ML_UL2017":WrongSign_ML_UL2017,
    "WWto2L2Nu_UL2017":WWto2L2Nu_UL2017, "GluGluToWWToENEN_UL2017":GluGluToWWToENEN_UL2017, "GluGluToWWToENMN_UL2017":GluGluToWWToENMN_UL2017, "GluGluToWWToENTN_UL2017":GluGluToWWToENTN_UL2017, "GluGluToWWToMNEN_UL2017":GluGluToWWToMNEN_UL2017, "GluGluToWWToMNMN_UL2017":GluGluToWWToMNMN_UL2017, "GluGluToWWToMNTN_UL2017":GluGluToWWToMNTN_UL2017, "GluGluToWWToTNEN_UL2017":GluGluToWWToTNEN_UL2017, "GluGluToWWToTNMN_UL2017":GluGluToWWToTNMN_UL2017, "GluGluToWWToTNTN_UL2017":GluGluToWWToTNTN_UL2017, "ST_tW_top_UL2017":ST_tW_top_UL2017, "ST_tW_antitop_UL2017":ST_tW_antitop_UL2017, "GluGluHToWWTo2L2Nu_UL2017":GluGluHToWWTo2L2Nu_UL2017, "GluGluHToZZTo4L_UL2017":GluGluHToZZTo4L_UL2017, "GluGluHToTauTau_UL2017":GluGluHToTauTau_UL2017, "VBFHToWWTo2L2Nu_UL2017": VBFHToWWTo2L2Nu_UL2017, "VBFHToTauTau_UL2017":VBFHToTauTau_UL2017, "ttHToNonbb_UL2017":ttHToNonbb_UL2017, "VHToNonbb_UL2017":VHToNonbb_UL2017,
    "Triboson_UL2017":Triboson_UL2017,
    "WWTo2L2Nu_DoubleScattering_UL2017":WWTo2L2Nu_DoubleScattering_UL2017, "WWW_4F_UL2017":WWW_4F_UL2017, "WWZ_4F_UL2017":WWZ_4F_UL2017, "WZZ_UL2017":WZZ_UL2017, "ZZZ_UL2017":ZZZ_UL2017, "ZZZ_UL2017":ZZZ_UL2017, "WWG_UL2017":WWG_UL2017,
    "WJets_UL2017":WJets_UL2017,
    "WJetsHT70to100_UL2017":WJetsHT70to100_UL2017, "WJetsHT100to200_UL2017":WJetsHT100to200_UL2017, "WJetsHT200to400_UL2017":WJetsHT200to400_UL2017, "WJetsHT400to600_UL2017":WJetsHT400to600_UL2017, "WJetsHT600to800_UL2017":WJetsHT600to800_UL2017, "WJetsHT800to1200_UL2017":WJetsHT800to1200_UL2017, "WJetsHT1200to2500_UL2017":WJetsHT1200to2500_UL2017, "WJetsHT2500toInf_UL2017":WJetsHT2500toInf_UL2017,
    "WJets_Jbin_UL2017":WJets_Jbin_UL2017,
    "WJets_0J_UL2017":WJets_0J_UL2017,"WJets_1J_UL2017":WJets_1J_UL2017,"WJets_2J_UL2017":WJets_2J_UL2017,
    "WZ_UL2017":WZ_UL2017,
    "DYJetsToLL_UL2017":DYJetsToLL_UL2017,
    "DYJetsToLL_M10to50_UL2017":DYJetsToLL_M10to50_UL2017, "DYJetsToLL_M50_UL2017":DYJetsToLL_M50_UL2017, "DYJetsToLL_M50_UL2017_ext":DYJetsToLL_M50_UL2017_ext,
    "DYJetsToLL_FxFx_UL2017":DYJetsToLL_FxFx_UL2017,
    "DYJetsToLL_M50_FxFx_UL2017":DYJetsToLL_M50_FxFx_UL2017,
    "DYJetsToLL_Jbin_FxFx_UL2017":DYJetsToLL_Jbin_FxFx_UL2017,
    "DYJetsToLL_0J_FxFx_UL2017":DYJetsToLL_0J_FxFx_UL2017,"DYJetsToLL_1J_FxFx_UL2017":DYJetsToLL_1J_FxFx_UL2017,"DYJetsToLL_2J_FxFx_UL2017":DYJetsToLL_2J_FxFx_UL2017,

    "WpWpJJ_UL2017":WpWpJJ_UL2017,"WpWpJJ_EWK_UL2017":WpWpJJ_EWK_UL2017,"WpWpJJ_QCD_UL2017":WpWpJJ_QCD_UL2017,
    "VBS_SSWW_SM_UL2017":VBS_SSWW_SM_UL2017,
    "VBS_SSWW_LL_SM_UL2017":VBS_SSWW_LL_SM_UL2017, "VBS_SSWW_TL_SM_UL2017":VBS_SSWW_TL_SM_UL2017, "VBS_SSWW_TT_SM_UL2017":VBS_SSWW_TT_SM_UL2017,
    "VBS_SSWW_cW_UL2017":VBS_SSWW_cW_UL2017,
    "VBS_SSWW_cW_SM_UL2017":VBS_SSWW_cW_SM_UL2017,
    "VBS_SSWW_cW_BSM_UL2017":VBS_SSWW_cW_BSM_UL2017, "VBS_SSWW_cW_INT_UL2017":VBS_SSWW_cW_INT_UL2017,
    "VBS_SSWW_cHW_UL2017":VBS_SSWW_cHW_UL2017,
    "VBS_SSWW_cHW_SM_UL2017":VBS_SSWW_cHW_SM_UL2017,
    "VBS_SSWW_cHW_BSM_UL2017":VBS_SSWW_cHW_BSM_UL2017, "VBS_SSWW_cHW_INT_UL2017":VBS_SSWW_cHW_INT_UL2017,
    "VBS_SSWW_cW_cHW_UL2017":VBS_SSWW_cW_cHW_UL2017,
    "VBS_SSWW_DIM6_UL2017":VBS_SSWW_DIM6_UL2017,
    "VBS_SSWW_DIM6_SM_UL2017":VBS_SSWW_DIM6_SM_UL2017,
    "VBS_SSWW_aQGC_UL2017":VBS_SSWW_aQGC_UL2017,
    "VBS_SSWW_aTGC_UL2017":VBS_SSWW_aTGC_UL2017,
    "VBS_SSWW_aTGC_mixed_UL2017":VBS_SSWW_aTGC_mixed_UL2017,

    "ZZtoLep_UL2018":ZZtoLep_UL2018,
    "ZZTo2L2Nu_UL2018":ZZTo2L2Nu_UL2018, "ZZTo4L_UL2018":ZZTo4L_UL2018, "GluGluToContinToZZTo4e_UL2018":GluGluToContinToZZTo4e_UL2018, "GluGluToContinToZZTo2e2mu_UL2018":GluGluToContinToZZTo2e2mu_UL2018, "GluGluToContinToZZTo2e2tau_UL2018":GluGluToContinToZZTo2e2tau_UL2018, "GluGluToContinToZZTo2mu2nu_UL2018":GluGluToContinToZZTo2mu2nu_UL2018, "GluGluToContinToZZTo4mu_UL2018":GluGluToContinToZZTo4mu_UL2018, "GluGluToContinToZZTo2mu2tau_UL2018":GluGluToContinToZZTo2mu2tau_UL2018, "GluGluToContinToZZTo2tau2nu_UL2018":GluGluToContinToZZTo2tau2nu_UL2018, "GluGluToContinToZZTo4tau_UL2018":GluGluToContinToZZTo4tau_UL2018, "GluGluToContinToZZTo2e2nu_UL2018":GluGluToContinToZZTo2e2nu_UL2018,
    "TT_UL2018":TT_UL2018,
    "TT_SemiLep_UL2018":TT_SemiLep_UL2018, "TT_Had_UL2018":TT_Had_UL2018,
    "TTTo2L2Nu_UL2018":TTTo2L2Nu_UL2018,
    "TT_Mtt_UL2018":TT_Mtt_UL2018,
    "TT_Mtt_700to1000_UL2018":TT_Mtt_700to1000_UL2018,"TT_Mtt_1000toInf_UL2018":TT_Mtt_1000toInf_UL2018,
    
    "TT_beff_UL2018":TT_beff_UL2018,
    "TVX_UL2018":TVX_UL2018,
    "TTGJets_UL2018":TTGJets_UL2018, "TTZToQQ_UL2018":TTZToQQ_UL2018, "TTZToLLNuNu_UL2018":TTZToLLNuNu_UL2018, "TTWJetsToQQ_UL2018":TTWJetsToQQ_UL2018, "TTWJetsToLNu_UL2018":TTWJetsToLNu_UL2018, "tZq_ll_4f_UL2018":tZq_ll_4f_UL2018,
    "VG_UL2018":VG_UL2018,
    "ZG_UL2018":ZG_UL2018, "WG_UL2018":WG_UL2018,
    "WrongSign_UL2018":WrongSign_UL2018,
    "WrongSign_ML_UL2018":WrongSign_ML_UL2018,
    "WWto2L2Nu_UL2018":WWto2L2Nu_UL2018, "GluGluToWWToENEN_UL2018":GluGluToWWToENEN_UL2018, "GluGluToWWToENMN_UL2018":GluGluToWWToENMN_UL2018, "GluGluToWWToENTN_UL2018":GluGluToWWToENTN_UL2018, "GluGluToWWToMNEN_UL2018":GluGluToWWToMNEN_UL2018, "GluGluToWWToMNMN_UL2018":GluGluToWWToMNMN_UL2018, "GluGluToWWToMNTN_UL2018":GluGluToWWToMNTN_UL2018, "GluGluToWWToTNEN_UL2018":GluGluToWWToTNEN_UL2018, "GluGluToWWToTNMN_UL2018":GluGluToWWToTNMN_UL2018, "GluGluToWWToTNTN_UL2018":GluGluToWWToTNTN_UL2018, "ST_tW_top_UL2018":ST_tW_top_UL2018, "ST_tW_antitop_UL2018":ST_tW_antitop_UL2018, "GluGluHToWWTo2L2Nu_UL2018":GluGluHToWWTo2L2Nu_UL2018, "GluGluHToZZTo4L_UL2018":GluGluHToZZTo4L_UL2018, "GluGluHToTauTau_UL2018":GluGluHToTauTau_UL2018, "VBFHToWWTo2L2Nu_UL2018": VBFHToWWTo2L2Nu_UL2018, "VBFHToTauTau_UL2018":VBFHToTauTau_UL2018, "ttHToNonbb_UL2018":ttHToNonbb_UL2018, "VHToNonbb_UL2018":VHToNonbb_UL2018,
    "Triboson_UL2018":Triboson_UL2018,
    "WWTo2L2Nu_DoubleScattering_UL2018":WWTo2L2Nu_DoubleScattering_UL2018, "WWW_4F_UL2018":WWW_4F_UL2018, "WWZ_4F_UL2018":WWZ_4F_UL2018, "WZZ_UL2018":WZZ_UL2018, "ZZZ_UL2018":ZZZ_UL2018, "ZZZ_UL2018":ZZZ_UL2018, "WWG_UL2018":WWG_UL2018,
    "WJets_UL2018":WJets_UL2018,
    "WJetsHT70to100_UL2018":WJetsHT70to100_UL2018, "WJetsHT100to200_UL2018":WJetsHT100to200_UL2018, "WJetsHT200to400_UL2018":WJetsHT200to400_UL2018, "WJetsHT400to600_UL2018":WJetsHT400to600_UL2018, "WJetsHT600to800_UL2018":WJetsHT600to800_UL2018, "WJetsHT800to1200_UL2018":WJetsHT800to1200_UL2018, "WJetsHT1200to2500_UL2018":WJetsHT1200to2500_UL2018, "WJetsHT2500toInf_UL2018":WJetsHT2500toInf_UL2018,
    "WJets_Jbin_UL2018":WJets_Jbin_UL2018,
    "WJets_0J_UL2018":WJets_0J_UL2018,"WJets_1J_UL2018":WJets_1J_UL2018,"WJets_2J_UL2018":WJets_2J_UL2018,
    "WZ_UL2018":WZ_UL2018,
    "DYJetsToLL_UL2018":DYJetsToLL_UL2018,
    "DYJetsToLL_M10to50_UL2018":DYJetsToLL_M10to50_UL2018, "DYJetsToLL_M50_UL2018":DYJetsToLL_M50_UL2018, "DYJetsToLL_M50_UL2018_ext":DYJetsToLL_M50_UL2018_ext,
    "DYJetsToLL_FxFx_UL2018":DYJetsToLL_FxFx_UL2018,
    "DYJetsToLL_M50_FxFx_UL2018":DYJetsToLL_M50_FxFx_UL2018,
    "DYJetsToLL_Jbin_FxFx_UL2018":DYJetsToLL_Jbin_FxFx_UL2018,
    "DYJetsToLL_0J_FxFx_UL2018":DYJetsToLL_0J_FxFx_UL2018,"DYJetsToLL_1J_FxFx_UL2018":DYJetsToLL_1J_FxFx_UL2018,"DYJetsToLL_2J_FxFx_UL2018":DYJetsToLL_2J_FxFx_UL2018,
    "WpWpJJ_UL2018":WpWpJJ_UL2018,"WpWpJJ_EWK_UL2018":WpWpJJ_EWK_UL2018,"WpWpJJ_QCD_UL2018":WpWpJJ_QCD_UL2018,
    "VBS_SSWW_SM_UL2018":VBS_SSWW_SM_UL2018,
    "VBS_SSWW_LL_SM_UL2018":VBS_SSWW_LL_SM_UL2018, "VBS_SSWW_TL_SM_UL2018":VBS_SSWW_TL_SM_UL2018, "VBS_SSWW_TT_SM_UL2018":VBS_SSWW_TT_SM_UL2018,
    "VBS_SSWW_cW_UL2018":VBS_SSWW_cW_UL2018,
    "VBS_SSWW_cW_BSM_UL2018":VBS_SSWW_cW_BSM_UL2018,
    "VBS_SSWW_cW_SM_UL2018":VBS_SSWW_cW_SM_UL2018, "VBS_SSWW_cW_INT_UL2018":VBS_SSWW_cW_INT_UL2018,
    "VBS_SSWW_cHW_UL2018":VBS_SSWW_cHW_UL2018,
    "VBS_SSWW_cHW_SM_UL2018":VBS_SSWW_cHW_SM_UL2018,
    "VBS_SSWW_cHW_BSM_UL2018":VBS_SSWW_cHW_BSM_UL2018, "VBS_SSWW_cHW_INT_UL2018":VBS_SSWW_cHW_INT_UL2018,
    "VBS_SSWW_cW_cHW_UL2018":VBS_SSWW_cW_cHW_UL2018,
    "VBS_SSWW_DIM6_UL2018":VBS_SSWW_DIM6_UL2018,
    "VBS_SSWW_DIM6_SM_UL2018":VBS_SSWW_DIM6_SM_UL2018,
    "VBS_SSWW_aQGC_UL2018":VBS_SSWW_aQGC_UL2018,
    "VBS_SSWW_aTGC_UL2018":VBS_SSWW_aTGC_UL2018,
    "VBS_SSWW_aTGC_mixed_UL2018":VBS_SSWW_aTGC_mixed_UL2018,

    ################### DataMu ###################
    "DataMu_UL2016APV":DataMu_UL2016APV,
    "DataMuB1_UL2016APV":DataMuB1_UL2016APV, "DataMuB2_UL2016APV":DataMuB2_UL2016APV, "DataMuC_UL2016APV":DataMuC_UL2016APV, "DataMuD_UL2016APV":DataMuD_UL2016APV, "DataMuE_UL2016APV":DataMuE_UL2016APV, "DataMuF_UL2016APV":DataMuF_UL2016APV,
    "DataMu_UL2016":DataMu_UL2016,
    "DataMu_UL2016M":DataMu_UL2016M,
    "DataMuF_UL2016":DataMuF_UL2016, "DataMuG_UL2016":DataMuG_UL2016, "DataMuH_UL2016":DataMuH_UL2016,
    "DataMu_UL2017":DataMu_UL2017,
    "DataMuB_UL2017":DataMuB_UL2017, "DataMuC_UL2017":DataMuC_UL2017, "DataMuD_UL2017":DataMuD_UL2017, "DataMuE_UL2017":DataMuE_UL2017, "DataMuF_UL2017":DataMuF_UL2017,
    "DataMu_UL2018":DataMu_UL2018,
    "DataMuA_UL2018":DataMuA_UL2018, "DataMuB_UL2018":DataMuB_UL2018, "DataMuC_UL2018":DataMuC_UL2018, "DataMuD_UL2018":DataMuD_UL2018,
    "DataMu_ULRunII":DataMu_ULRunII,
    ################### DataEle ###################
    "DataEle_UL2016APV":DataEle_UL2016APV,
    "DataEleB1_UL2016APV":DataEleB1_UL2016APV, "DataEleB2_UL2016APV":DataEleB2_UL2016APV, "DataEleC_UL2016APV":DataEleC_UL2016APV, "DataEleD_UL2016APV":DataEleD_UL2016APV, "DataEleE_UL2016APV":DataEleE_UL2016APV, "DataEleF_UL2016APV":DataEleF_UL2016APV,
    "DataEle_UL2016":DataEle_UL2016,
    "DataEle_UL2016M":DataEle_UL2016M,
    "DataEleF_UL2016":DataEleF_UL2016, "DataEleG_UL2016":DataEleG_UL2016, "DataEleH_UL2016":DataEleH_UL2016,
    "DataEle_UL2017":DataEle_UL2017,
    "DataEleB_UL2017":DataEleB_UL2017, "DataEleC_UL2017":DataEleC_UL2017, "DataEleD_UL2017":DataEleD_UL2017, "DataEleE_UL2017":DataEleE_UL2017, "DataEleF_UL2017":DataEleF_UL2017,
    "DataEle_UL2018":DataEle_UL2018,
    "DataEleA_UL2018":DataEleA_UL2018, "DataEleB_UL2018":DataEleB_UL2018, "DataEleC_UL2018":DataEleC_UL2018, "DataEleD_UL2018":DataEleD_UL2018,
    "DataEle_ULRunII":DataEle_ULRunII,
    ################### FakeMu ###################
    "FakeMu_UL2016APV":FakeMu_UL2016APV,
    "FakeMuPromptTau_UL2016APV":FakeMuPromptTau_UL2016APV,
    "PromptMuFakeTau_UL2016APV":PromptMuFakeTau_UL2016APV,
    "FakeMuFakeTau_UL2016APV":FakeMuFakeTau_UL2016APV,
    "FakeMu_UL2016":FakeMu_UL2016,
    "FakeMu_UL2016M":FakeMu_UL2016M,
    "FakeMuPromptTau_UL2016":FakeMuPromptTau_UL2016,
    "PromptMuFakeTau_UL2016":PromptMuFakeTau_UL2016,
    "FakeMuFakeTau_UL2016":FakeMuFakeTau_UL2016,
    "FakeMuPromptTau_UL2016M":FakeMuPromptTau_UL2016M,
    "PromptMuFakeTau_UL2016M":PromptMuFakeTau_UL2016M,
    "FakeMuFakeTau_UL2016M":FakeMuFakeTau_UL2016M,
    "FakeMu_UL2017":FakeMu_UL2017,
    "FakeMuPromptTau_UL2017":FakeMuPromptTau_UL2017,
    "PromptMuFakeTau_UL2017":PromptMuFakeTau_UL2017,
    "FakeMuFakeTau_UL2017":FakeMuFakeTau_UL2017,
    "FakeMu_UL2018":FakeMu_UL2018,
    "FakeMuPromptTau_UL2018":FakeMuPromptTau_UL2018,
    "PromptMuFakeTau_UL2018":PromptMuFakeTau_UL2018,
    "FakeMuFakeTau_UL2018":FakeMuFakeTau_UL2018,
    "FakeMu_ULRunII":FakeMu_ULRunII,
    "FakeMuPromptTau_ULRunII":FakeMuPromptTau_ULRunII,
    "PromptMuFakeTau_ULRunII":PromptMuFakeTau_ULRunII,
    "FakeMuFakeTau_ULRunII":FakeMuFakeTau_ULRunII,
    
    ################### FakeEle ###################
    "FakeEle_UL2016APV":FakeEle_UL2016APV,
    "FakeElePromptTau_UL2016APV":FakeElePromptTau_UL2016APV,
    "PromptEleFakeTau_UL2016APV":PromptEleFakeTau_UL2016APV,
    "FakeEleFakeTau_UL2016APV":FakeEleFakeTau_UL2016APV,
    "FakeEle_UL2016":FakeEle_UL2016,
    "FakeEle_UL2016M":FakeEle_UL2016M,
    "FakeElePromptTau_UL2016":FakeElePromptTau_UL2016,
    "PromptEleFakeTau_UL2016":PromptEleFakeTau_UL2016,
    "FakeEleFakeTau_UL2016":FakeEleFakeTau_UL2016,
    "FakeElePromptTau_UL2016M":FakeElePromptTau_UL2016M,
    "PromptEleFakeTau_UL2016M":PromptEleFakeTau_UL2016M,
    "FakeEleFakeTau_UL2016M":FakeEleFakeTau_UL2016M,
    "FakeEle_UL2017":FakeEle_UL2017,
    "FakeElePromptTau_UL2017":FakeElePromptTau_UL2017,
    "PromptEleFakeTau_UL2017":PromptEleFakeTau_UL2017,
    "FakeEleFakeTau_UL2017":FakeEleFakeTau_UL2017,
    "FakeEle_UL2018":FakeEle_UL2018,
    "FakeElePromptTau_UL2018":FakeElePromptTau_UL2018,
    "PromptEleFakeTau_UL2018":PromptEleFakeTau_UL2018,
    "FakeEleFakeTau_UL2018":FakeEleFakeTau_UL2018,
    "FakeElePromptTau_ULRunII":FakeElePromptTau_ULRunII,
    "PromptEleFakeTau_ULRunII":PromptEleFakeTau_ULRunII,
    "FakeEleFakeTau_ULRunII":FakeEleFakeTau_ULRunII,
    "FakeEle_ULRunII":FakeEle_ULRunII,
    ################### DataHT ###################
    "DataHT_UL2016APV":DataHT_UL2016APV,
    "DataHTB1_UL2016APV":DataHTB1_UL2016APV, "DataHTB2_UL2016APV":DataHTB2_UL2016APV, "DataHTC_UL2016APV":DataHTC_UL2016APV, "DataHTD_UL2016APV":DataHTD_UL2016APV, "DataHTE_UL2016APV":DataHTE_UL2016APV, "DataHTF_UL2016APV":DataHTF_UL2016APV,
    "DataHT_UL2016":DataHT_UL2016,
    "DataHTF_UL2016":DataHTF_UL2016, "DataHTG_UL2016":DataHTG_UL2016, "DataHTH_UL2016":DataHTH_UL2016,
    "DataHT_UL2017":DataHT_UL2017,
    "DataHTB_UL2017":DataHTB_UL2017, "DataHTC_UL2017":DataHTC_UL2017, "DataHTD_UL2017":DataHTD_UL2017, "DataHTE_UL2017":DataHTE_UL2017, "DataHTF_UL2017":DataHTF_UL2017,
    "DataHT_UL2018":DataHT_UL2018,
    "DataHTA_UL2018":DataHTA_UL2018, "DataHTB_UL2018":DataHTB_UL2018, "DataHTC_UL2018":DataHTC_UL2018, "DataHTD_UL2018":DataHTD_UL2018,

    ################### FakeRatio ###################
    "SampleHTFake_UL2016APV":SampleHTFake_UL2016APV,
    "SampleHTFake_UL2016":SampleHTFake_UL2016,
    "SampleHTFake_UL2017":SampleHTFake_UL2017,
    "SampleHTFake_UL2018":SampleHTFake_UL2018,

    "ZZtoLep_ULRunII":ZZtoLep_ULRunII,
    "TT_ULRunII":TT_ULRunII,
    "TT_Mtt_ULRunII":TT_Mtt_ULRunII,
    "TTTo2L2Nu_ULRunII":TTTo2L2Nu_ULRunII,
    "TVX_ULRunII":TVX_ULRunII,
    "VG_ULRunII":VG_ULRunII,
    "WrongSign_ULRunII":WrongSign_ULRunII,
    "WrongSign_ML_ULRunII":WrongSign_ML_ULRunII,
    "Triboson_ULRunII":Triboson_ULRunII,
    "WJets_ULRunII":WJets_ULRunII,
    "WJets_Jbin_ULRunII":WJets_Jbin_ULRunII,
    "WZ_ULRunII":WZ_ULRunII,
    "DYJetsToLL_ULRunII":DYJetsToLL_ULRunII,
    "DYJetsToLL_FxFx_ULRunII":DYJetsToLL_FxFx_ULRunII,
    "DYJetsToLL_Jbin_FxFx_ULRunII":DYJetsToLL_Jbin_FxFx_ULRunII,
    "WpWpJJ_ULRunII":WpWpJJ_ULRunII,"WpWpJJ_EWK_ULRunII":WpWpJJ_EWK_ULRunII,"WpWpJJ_QCD_ULRunII":WpWpJJ_QCD_ULRunII,
    "VBS_SSWW_SM_ULRunII":VBS_SSWW_SM_ULRunII,
    "VBS_SSWW_LL_SM_ULRunII":VBS_SSWW_LL_SM_ULRunII, "VBS_SSWW_TL_SM_ULRunII":VBS_SSWW_TL_SM_ULRunII, "VBS_SSWW_TT_SM_ULRunII":VBS_SSWW_TT_SM_ULRunII,
    "VBS_SSWW_cW_ULRunII":VBS_SSWW_cW_ULRunII,
    "VBS_SSWW_cW_SM_ULRunII":VBS_SSWW_cW_SM_ULRunII,
    "VBS_SSWW_cHW_ULRunII":VBS_SSWW_cHW_ULRunII,
    "VBS_SSWW_cHW_SM_ULRunII":VBS_SSWW_cHW_SM_ULRunII,
    "VBS_SSWW_cW_cHW_ULRunII":VBS_SSWW_cW_cHW_ULRunII,
    "VBS_SSWW_DIM6_ULRunII":VBS_SSWW_DIM6_ULRunII,
    "VBS_SSWW_DIM6_SM_ULRunII":VBS_SSWW_DIM6_SM_ULRunII,
    "VBS_SSWW_aQGC_ULRunII":VBS_SSWW_aQGC_ULRunII,
    "VBS_SSWW_aTGC_ULRunII":VBS_SSWW_aTGC_ULRunII,
    "VBS_SSWW_aTGC_mixed_ULRunII":VBS_SSWW_aTGC_mixed_ULRunII,

    "Others_ULRunII":Others_ULRunII,
}

crab_dict = {
    ##### UL2016APV #####
    "UL2016APV":[
        GluGluHToTauTau_UL2016APV,
        ZZtoLep_UL2016APV,
        TT_UL2016APV,
        TT_Mtt_UL2016APV,
        TTTo2L2Nu_UL2016APV,
        TVX_UL2016APV,
        VG_UL2016APV,
        WrongSign_UL2016APV,
        Triboson_UL2016APV,
        WJets_UL2016APV,
        WJets_Jbin_UL2016APV,
        WZ_UL2016APV,
        DYJetsToLL_M10to50_UL2016APV,
        DYJetsToLL_UL2016APV,
        DYJetsToLL_FxFx_UL2016APV,
        DYJetsToLL_Jbin_FxFx_UL2016APV,
        #VBS_SSWW_DIM6_SM_UL2016APV,
        VBS_SSWW_SM_UL2016APV,
        VBS_SSWW_DIM6_UL2016APV,
        VBS_SSWW_aQGC_UL2016APV,
        VBS_SSWW_aTGC_UL2016APV,
        VBS_SSWW_aTGC_mixed_UL2016APV,
        WpWpJJ_EWK_UL2016APV,
        WpWpJJ_QCD_UL2016APV,
        DataMu_UL2016APV,
        DataEle_UL2016APV,
        #DataHT_UL2016APV,
    ],

    ##### UL2016 #####
    "UL2016":[
        ZZtoLep_UL2016,
        TT_UL2016,
        TT_Mtt_UL2016,
        TTTo2L2Nu_UL2016,
        TVX_UL2016,
        VG_UL2016,
        WrongSign_UL2016,
        Triboson_UL2016,
        WJets_UL2016,
        WJets_Jbin_UL2016,
        WZ_UL2016,
        DYJetsToLL_M10to50_UL2016,
        DYJetsToLL_UL2016,
        DYJetsToLL_FxFx_UL2016,
        DYJetsToLL_Jbin_FxFx_UL2016,
        #VBS_SSWW_DIM6_SM_UL2016,
        VBS_SSWW_SM_UL2016,
        VBS_SSWW_DIM6_UL2016,
        VBS_SSWW_aQGC_UL2016,
        VBS_SSWW_aTGC_UL2016,
        VBS_SSWW_aTGC_mixed_UL2016,
        WpWpJJ_EWK_UL2016,
        WpWpJJ_QCD_UL2016,
        DataMu_UL2016,
        DataEle_UL2016,
        #DataHT_UL2016,
    ],

    ##### UL2017 #####
    "UL2017":[
        ZZtoLep_UL2017,
        TT_UL2017,
        TT_Mtt_UL2017,
        TTTo2L2Nu_UL2017,
        TVX_UL2017,
        VG_UL2017,
        WrongSign_UL2017,
        Triboson_UL2017,
        WJets_UL2017,
        WJets_Jbin_UL2017,
        WZ_UL2017,
        DYJetsToLL_M10to50_UL2017,
        DYJetsToLL_UL2017,
        DYJetsToLL_FxFx_UL2017,
        DYJetsToLL_Jbin_FxFx_UL2017,
        #VBS_SSWW_DIM6_SM_UL2017,
        VBS_SSWW_SM_UL2017,
        VBS_SSWW_DIM6_UL2017,
        VBS_SSWW_aQGC_UL2017,
        VBS_SSWW_aTGC_UL2017,
        VBS_SSWW_aTGC_mixed_UL2017,
        WpWpJJ_EWK_UL2017,
        WpWpJJ_QCD_UL2017,
        DataMu_UL2017,
        DataEle_UL2017,
        #DataHT_UL2017,
    ],

    ##### UL2018 #####
    "UL2018":[
        ZZtoLep_UL2018,
        TT_UL2018,
        TT_Mtt_UL2018,
        TTTo2L2Nu_UL2018,
        TVX_UL2018,
        VG_UL2018,
        WrongSign_UL2018,
        Triboson_UL2018,
        WJets_UL2018,
        WJets_Jbin_UL2018,
        WZ_UL2018,
        DYJetsToLL_M10to50_UL2018,
        DYJetsToLL_UL2018,
        DYJetsToLL_FxFx_UL2018,
        DYJetsToLL_Jbin_FxFx_UL2018,
        #VBS_SSWW_DIM6_SM_UL2018,
        VBS_SSWW_SM_UL2018,
        VBS_SSWW_DIM6_UL2018,
        VBS_SSWW_aQGC_UL2018,
        VBS_SSWW_aTGC_UL2018,
        VBS_SSWW_aTGC_mixed_UL2018,
        WpWpJJ_EWK_UL2018,
        WpWpJJ_QCD_UL2018,
        DataMu_UL2018,
        DataEle_UL2018,
        #DataHT_UL2018,
    ],
}

crab_dict_Fake = {
    ##### UL2016APV #####
    "UL2016APV":[
        WJets_UL2016APV,
        DYJetsToLL_M10to50_UL2016APV,
        DYJetsToLL_M50_UL2016APV,
        DYJetsToLL_M50_UL2016APV_ext,
        ZZtoLep_UL2016APV,
        TT_UL2016APV,
        DataHT_UL2016APV,
    ],

    ##### UL2016 #####
    "UL2016":[
        WJets_UL2016,
        DYJetsToLL_M10to50_UL2016,
        DYJetsToLL_M50_UL2016,
        DYJetsToLL_M50_UL2016_ext,
        ZZtoLep_UL2016,
        TT_UL2016,
        DataHT_UL2016,
    ],

    ##### UL2017 #####
    "UL2017":[
        WJets_UL2017,
        DYJetsToLL_M10to50_UL2017,
        DYJetsToLL_M50_UL2017,
        DYJetsToLL_M50_UL2017_ext,
        ZZtoLep_UL2017,
        TT_UL2017,
        DataHT_UL2017,
    ],

    ##### UL2018 #####
    "UL2018":[
        WJets_UL2018,
        DYJetsToLL_M10to50_UL2018,
        DYJetsToLL_M50_UL2018,
        DYJetsToLL_M50_UL2018_ext,
        ZZtoLep_UL2018,
        TT_UL2018,
        DataHT_UL2018,
    ],
}

condor_dict = {
    "ZZtoLep_UL2016APV":ZZtoLep_UL2016APV,
    "TT_UL2016APV":TT_UL2016APV,
    #"TT_Mtt_UL2016APV":TT_Mtt_UL2016APV,
    "TTTo2L2Nu_UL2016APV":TTTo2L2Nu_UL2016APV,
    "TVX_UL2016APV":TVX_UL2016APV,
    "VG_UL2016APV":VG_UL2016APV,
    "WrongSign_UL2016APV":WrongSign_UL2016APV,
    "Triboson_UL2016APV":Triboson_UL2016APV,
    "WJets_UL2016APV":WJets_UL2016APV,
    "WJets_Jbin_UL2016APV":WJets_Jbin_UL2016APV,
    "WZ_UL2016APV":WZ_UL2016APV,
    #"DYJetsToLL_UL2016APV":DYJetsToLL_UL2016APV,
    #"DYJetsToLL_M10to50_UL2016APV":DYJetsToLL_M10to50_UL2016APV,
    #"DYJetsToLL_FxFx_UL2016APV":DYJetsToLL_FxFx_UL2016APV,
    "DYJetsToLL_Jbin_FxFx_UL2016APV":DYJetsToLL_Jbin_FxFx_UL2016APV,
    #"WpWpJJ_EWK_UL2016APV":WpWpJJ_EWK_UL2016APV,
    #"WpWpJJ_QCD_UL2016APV":WpWpJJ_QCD_UL2016APV,
    "WpWpJJ_UL2016APV":WpWpJJ_UL2016APV,
    "VBS_SSWW_DIM6_SM_UL2016APV":VBS_SSWW_DIM6_SM_UL2016APV,
    #"VBS_SSWW_SM_UL2016APV":VBS_SSWW_SM_UL2016APV,
    "VBS_SSWW_aQGC_UL2016APV":VBS_SSWW_aQGC_UL2016APV,
    #"VBS_SSWW_aTGC_UL2016APV":VBS_SSWW_aTGC_UL2016APV,
    "VBS_SSWW_aTGC_mixed_UL2016APV":VBS_SSWW_aTGC_mixed_UL2016APV,
    "DataMu_UL2016APV":DataMu_UL2016APV,
    "DataEle_UL2016APV":DataEle_UL2016APV,
    "DataHT_UL2016APV":DataHT_UL2016APV,

    "ZZtoLep_UL2016":ZZtoLep_UL2016,
    "TT_UL2016":TT_UL2016,
    #"TT_Mtt_UL2016":TT_Mtt_UL2016,
    "TTTo2L2Nu_UL2016":TTTo2L2Nu_UL2016,
    "TVX_UL2016":TVX_UL2016,
    "VG_UL2016":VG_UL2016,
    "WrongSign_UL2016":WrongSign_UL2016,
    "Triboson_UL2016":Triboson_UL2016,
    "WJets_UL2016":WJets_UL2016,
    "WJets_Jbin_UL2016":WJets_Jbin_UL2016,
    "WZ_UL2016":WZ_UL2016,
    #"DYJetsToLL_UL2016":DYJetsToLL_UL2016,
    #"DYJetsToLL_M10to50_UL2016":DYJetsToLL_M10to50_UL2016,
    #"DYJetsToLL_FxFx_UL2016":DYJetsToLL_FxFx_UL2016,
    "DYJetsToLL_Jbin_FxFx_UL2016":DYJetsToLL_Jbin_FxFx_UL2016,
    #"WpWpJJ_EWK_UL2016":WpWpJJ_EWK_UL2016,
    #"WpWpJJ_QCD_UL2016":WpWpJJ_QCD_UL2016,
    "WpWpJJ_UL2016":WpWpJJ_UL2016,
    "VBS_SSWW_DIM6_SM_UL2016":VBS_SSWW_DIM6_SM_UL2016,
    #"VBS_SSWW_SM_UL2016":VBS_SSWW_SM_UL2016,
    "VBS_SSWW_aQGC_UL2016":VBS_SSWW_aQGC_UL2016,
    #"VBS_SSWW_aTGC_UL2016":VBS_SSWW_aTGC_UL2016,
    "VBS_SSWW_aTGC_mixed_UL2016":VBS_SSWW_aTGC_mixed_UL2016,
    "DataMu_UL2016":DataMu_UL2016,
    "DataEle_UL2016":DataEle_UL2016,
    "DataHT_UL2016":DataHT_UL2016,

    "ZZtoLep_UL2017":ZZtoLep_UL2017,
    "TT_UL2017":TT_UL2017,
    #"TT_Mtt_UL2017":TT_Mtt_UL2017,
    "TTTo2L2Nu_UL2017":TTTo2L2Nu_UL2017,
    "TVX_UL2017":TVX_UL2017,
    "VG_UL2017":VG_UL2017,
    "WrongSign_UL2017":WrongSign_UL2017,
    "Triboson_UL2017":Triboson_UL2017,
    "WJets_UL2017":WJets_UL2017,
    "WJets_Jbin_UL2017":WJets_Jbin_UL2017,
    "WZ_UL2017":WZ_UL2017,
    #"DYJetsToLL_UL2017":DYJetsToLL_UL2017,
    #"DYJetsToLL_M10to50_UL2017":DYJetsToLL_M10to50_UL2017,
    #"DYJetsToLL_FxFx_UL2017":DYJetsToLL_FxFx_UL2017,
    "DYJetsToLL_Jbin_FxFx_UL2017":DYJetsToLL_Jbin_FxFx_UL2017,
    #"WpWpJJ_EWK_UL2017":WpWpJJ_EWK_UL2017,
    #"WpWpJJ_QCD_UL2017":WpWpJJ_QCD_UL2017,
    "WpWpJJ_UL2017":WpWpJJ_UL2017,
    "VBS_SSWW_DIM6_SM_UL2017":VBS_SSWW_DIM6_SM_UL2017,
    #"VBS_SSWW_SM_UL2017":VBS_SSWW_SM_UL2017,
    "VBS_SSWW_aQGC_UL2017":VBS_SSWW_aQGC_UL2017,
    #"VBS_SSWW_aTGC_UL2017":VBS_SSWW_aTGC_UL2017,
    "VBS_SSWW_aTGC_mixed_UL2017":VBS_SSWW_aTGC_mixed_UL2017,
    "DataMu_UL2017":DataMu_UL2017,
    "DataEle_UL2017":DataEle_UL2017,
    "DataHT_UL2017":DataHT_UL2017,

    "ZZtoLep_UL2018":ZZtoLep_UL2018,
    "TT_UL2018":TT_UL2018,
    #"TT_Mtt_UL2018":TT_Mtt_UL2018,
    "TTTo2L2Nu_UL2018":TTTo2L2Nu_UL2018,
    "TVX_UL2018":TVX_UL2018,
    "VG_UL2018":VG_UL2018,
    "WrongSign_UL2018":WrongSign_UL2018,
    "Triboson_UL2018":Triboson_UL2018,
    "WJets_UL2018":WJets_UL2018,
    "WJets_Jbin_UL2018":WJets_Jbin_UL2018,
    "WZ_UL2018":WZ_UL2018,
    #"DYJetsToLL_UL2018":DYJetsToLL_UL2018,
    #"DYJetsToLL_M10to50_UL2018":DYJetsToLL_M10to50_UL2018,
    #"DYJetsToLL_FxFx_UL2018":DYJetsToLL_FxFx_UL2018,
    "DYJetsToLL_Jbin_FxFx_UL2018":DYJetsToLL_Jbin_FxFx_UL2018,
    #"WpWpJJ_EWK_UL2018":WpWpJJ_EWK_UL2018,
    #"WpWpJJ_QCD_UL2018":WpWpJJ_QCD_UL2018,
    "WpWpJJ_UL2018":WpWpJJ_UL2018,
    "VBS_SSWW_DIM6_SM_UL2018":VBS_SSWW_DIM6_SM_UL2018,
    #"VBS_SSWW_SM_UL2018":VBS_SSWW_SM_UL2018,
    "VBS_SSWW_aQGC_UL2018":VBS_SSWW_aQGC_UL2018,
    #"VBS_SSWW_aTGC_UL2018":VBS_SSWW_aTGC_UL2018,
    "VBS_SSWW_aTGC_mixed_UL2018":VBS_SSWW_aTGC_mixed_UL2018,
    "DataMu_UL2018":DataMu_UL2018,
    "DataEle_UL2018":DataEle_UL2018,
    "DataHT_UL2018":DataHT_UL2018,
}

merge_dict = {
    "ZZtoLep_UL2016APV":ZZtoLep_UL2016APV,
    "TT_UL2016APV":TT_UL2016APV,
    #"TT_Mtt_UL2016APV":TT_Mtt_UL2016APV,
    "TTTo2L2Nu_UL2016APV":TTTo2L2Nu_UL2016APV,
    "TVX_UL2016APV":TVX_UL2016APV,
    "VG_UL2016APV":VG_UL2016APV,
    "WrongSign_UL2016APV":WrongSign_UL2016APV,
    "WrongSign_ML_UL2016APV":WrongSign_ML_UL2016APV,
    "Triboson_UL2016APV":Triboson_UL2016APV,
    "WJets_UL2016APV":WJets_UL2016APV,
    "WJets_Jbin_UL2016APV":WJets_Jbin_UL2016APV,
    "WZ_UL2016APV":WZ_UL2016APV,
    #"DYJetsToLL_UL2016APV":DYJetsToLL_UL2016APV,
    #"DYJetsToLL_M10to50_UL2016APV":DYJetsToLL_M10to50_UL2016APV,
    #"DYJetsToLL_FxFx_UL2016APV":DYJetsToLL_FxFx_UL2016APV,
    "DYJetsToLL_Jbin_FxFx_UL2016APV":DYJetsToLL_Jbin_FxFx_UL2016APV,
    #"WpWpJJ_EWK_UL2016APV":WpWpJJ_EWK_UL2016APV,
    #"WpWpJJ_QCD_UL2016APV":WpWpJJ_QCD_UL2016APV,
    "WpWpJJ_UL2016APV":WpWpJJ_UL2016APV,
    "VBS_SSWW_SM_UL2016APV":VBS_SSWW_SM_UL2016APV,
    "VBS_SSWW_cW_UL2016APV":VBS_SSWW_cW_UL2016APV,
    "VBS_SSWW_cHW_UL2016APV":VBS_SSWW_cHW_UL2016APV,
    "VBS_SSWW_cW_SM_UL2016APV":VBS_SSWW_cW_SM_UL2016APV,
    "VBS_SSWW_cHW_SM_UL2016APV":VBS_SSWW_cHW_SM_UL2016APV,
    "VBS_SSWW_cW_cHW_UL2016APV":VBS_SSWW_cW_cHW_UL2016APV,
    #"VBS_SSWW_DIM6_SM_UL2016APV":VBS_SSWW_DIM6_SM_UL2016APV,
    "VBS_SSWW_aQGC_UL2016APV":VBS_SSWW_aQGC_UL2016APV,
    #"VBS_SSWW_aTGC_UL2016APV":VBS_SSWW_aTGC_UL2016APV,
    "VBS_SSWW_aTGC_mixed_UL2016APV":VBS_SSWW_aTGC_mixed_UL2016APV,
    "DataMu_UL2016APV":DataMu_UL2016APV,
    "FakeMu_UL2016APV":FakeMu_UL2016APV,
    "DataEle_UL2016APV":DataEle_UL2016APV,
    "FakeEle_UL2016APV":FakeEle_UL2016APV,
    "DataHT_UL2016APV":DataHT_UL2016APV,

    "ZZtoLep_UL2016":ZZtoLep_UL2016,
    "TT_UL2016":TT_UL2016,
    #"TT_Mtt_UL2016":TT_Mtt_UL2016,
    "TTTo2L2Nu_UL2016":TTTo2L2Nu_UL2016,
    "TVX_UL2016":TVX_UL2016,
    "VG_UL2016":VG_UL2016,
    "WrongSign_UL2016":WrongSign_UL2016,
    "WrongSign_ML_UL2016":WrongSign_ML_UL2016,
    #"VBFHToWWTo2L2Nu_UL2016":VBFHToWWTo2L2Nu_UL2016,
    "Triboson_UL2016":Triboson_UL2016,
    "WJets_UL2016":WJets_UL2016,
    "WJets_Jbin_UL2016":WJets_Jbin_UL2016,
    "WZ_UL2016":WZ_UL2016,
    #"DYJetsToLL_UL2016":DYJetsToLL_UL2016,
    #"DYJetsToLL_M10to50_UL2016":DYJetsToLL_M10to50_UL2016,
    #"DYJetsToLL_FxFx_UL2016":DYJetsToLL_FxFx_UL2016,
    "DYJetsToLL_Jbin_FxFx_UL2016":DYJetsToLL_Jbin_FxFx_UL2016,
    #"WpWpJJ_EWK_UL2016":WpWpJJ_EWK_UL2016,
    #"WpWpJJ_QCD_UL2016":WpWpJJ_QCD_UL2016,
    "WpWpJJ_UL2016":WpWpJJ_UL2016,
    "VBS_SSWW_SM_UL2016":VBS_SSWW_SM_UL2016,
    "VBS_SSWW_cW_UL2016":VBS_SSWW_cW_UL2016,
    "VBS_SSWW_cHW_UL2016":VBS_SSWW_cHW_UL2016,
    "VBS_SSWW_cW_SM_UL2016":VBS_SSWW_cW_SM_UL2016,
    "VBS_SSWW_cHW_SM_UL2016":VBS_SSWW_cHW_SM_UL2016,
    "VBS_SSWW_cW_cHW_UL2016":VBS_SSWW_cW_cHW_UL2016,
    #"VBS_SSWW_DIM6_SM_UL2016":VBS_SSWW_DIM6_SM_UL2016,
    "VBS_SSWW_aQGC_UL2016":VBS_SSWW_aQGC_UL2016,
    #"VBS_SSWW_aTGC_UL2016":VBS_SSWW_aTGC_UL2016,
    "VBS_SSWW_aTGC_mixed_UL2016":VBS_SSWW_aTGC_mixed_UL2016,
    "DataMu_UL2016":DataMu_UL2016,
    "FakeMu_UL2016":FakeMu_UL2016,
    "DataEle_UL2016":DataEle_UL2016,
    "FakeEle_UL2016":FakeEle_UL2016,
    "DataHT_UL2016":DataHT_UL2016,
    
    "WpWpJJ_EWK_UL2016M":WpWpJJ_EWK_UL2016M,
    "VBS_SSWW_SM_UL2016M":VBS_SSWW_SM_UL2016M,
    "VBS_SSWW_LL_SM_UL2016M":VBS_SSWW_LL_SM_UL2016M,
    "VBS_SSWW_TL_SM_UL2016M":VBS_SSWW_TL_SM_UL2016M,
    "VBS_SSWW_TT_SM_UL2016M":VBS_SSWW_TT_SM_UL2016M,
    "VBS_SSWW_cW_UL2016M":VBS_SSWW_cW_UL2016M,
    "VBS_SSWW_cHW_UL2016M":VBS_SSWW_cHW_UL2016M,
    "VBS_SSWW_cW_SM_UL2016M":VBS_SSWW_cW_SM_UL2016M,
    "VBS_SSWW_cHW_SM_UL2016M":VBS_SSWW_cHW_SM_UL2016M,
    "VBS_SSWW_cW_BSM_UL2016M":VBS_SSWW_cW_BSM_UL2016M,
    "VBS_SSWW_cHW_BSM_UL2016M":VBS_SSWW_cHW_BSM_UL2016M,
    "VBS_SSWW_cW_cHW_UL2016M":VBS_SSWW_cW_cHW_UL2016M,
    "VBS_SSWW_aQGC_UL2016M":VBS_SSWW_aQGC_UL2016M,
    #"VBS_SSWW_aTGC_UL2016M":VBS_SSWW_aTGC_UL2016M,
    "VBS_SSWW_aTGC_mixed_UL2016M":VBS_SSWW_aTGC_mixed_UL2016M,
    "WpWpJJ_QCD_UL2016M":WpWpJJ_QCD_UL2016M,
    "WpWpJJ_UL2016M":WpWpJJ_UL2016M,
    "ZZtoLep_UL2016M":ZZtoLep_UL2016M,
    "Triboson_UL2016M":Triboson_UL2016M,
    "TVX_UL2016M":TVX_UL2016M,
    "VG_UL2016M":VG_UL2016M,
    "WZ_UL2016M":WZ_UL2016M,
    "WrongSign_UL2016M":WrongSign_UL2016M,
    "WrongSign_ML_UL2016M":WrongSign_ML_UL2016M,
    #"DYJetsToLL_FxFx_UL2016M":DYJetsToLL_FxFx_UL2016M,
    #"DYJetsToLL_Jbin_FxFx_UL2016M":DYJetsToLL_Jbin_FxFx_UL2016M,
    "TTTo2L2Nu_UL2016M":TTTo2L2Nu_UL2016M,
    #TT_UL2016M,
    #WJets_UL2016M,
    "FakeMu_UL2016M":FakeMu_UL2016M,
    "DataMu_UL2016M":DataMu_UL2016M,
    "FakeEle_UL2016M":FakeEle_UL2016M,
    "DataEle_UL2016M":DataEle_UL2016M,

    "ZZtoLep_UL2017":ZZtoLep_UL2017,
    "TT_UL2017":TT_UL2017,
    #"TT_Mtt_UL2017":TT_Mtt_UL2017,
    "TTTo2L2Nu_UL2017":TTTo2L2Nu_UL2017,
    "TVX_UL2017":TVX_UL2017,
    "VG_UL2017":VG_UL2017,
    "WrongSign_UL2017":WrongSign_UL2017,
    "WrongSign_ML_UL2017":WrongSign_ML_UL2017,
    "Triboson_UL2017":Triboson_UL2017,
    "WJets_UL2017":WJets_UL2017,
    "WJets_Jbin_UL2017":WJets_Jbin_UL2017,
    "WZ_UL2017":WZ_UL2017,
    #"DYJetsToLL_UL2017":DYJetsToLL_UL2017,
    #"DYJetsToLL_M10to50_UL2017":DYJetsToLL_M10to50_UL2017,
    #"DYJetsToLL_FxFx_UL2017":DYJetsToLL_FxFx_UL2017,
    "DYJetsToLL_Jbin_FxFx_UL2017":DYJetsToLL_Jbin_FxFx_UL2017,
    #"WpWpJJ_EWK_UL2017":WpWpJJ_EWK_UL2017,
    #"WpWpJJ_QCD_UL2017":WpWpJJ_QCD_UL2017,
    "WpWpJJ_UL2017":WpWpJJ_UL2017,
    "VBS_SSWW_SM_UL2017":VBS_SSWW_SM_UL2017,
    "VBS_SSWW_cW_UL2017":VBS_SSWW_cW_UL2017,
    "VBS_SSWW_cHW_UL2017":VBS_SSWW_cHW_UL2017,
    "VBS_SSWW_cW_SM_UL2017":VBS_SSWW_cW_SM_UL2017,
    "VBS_SSWW_cW_BSM_UL2017":VBS_SSWW_cW_BSM_UL2017,
    "VBS_SSWW_cHW_SM_UL2017":VBS_SSWW_cHW_SM_UL2017,
    "VBS_SSWW_cW_cHW_UL2017":VBS_SSWW_cW_cHW_UL2017,
    #"VBS_SSWW_DIM6_SM_UL2017":VBS_SSWW_DIM6_SM_UL2017,
    "VBS_SSWW_aQGC_UL2017":VBS_SSWW_aQGC_UL2017,
    #"VBS_SSWW_aTGC_UL2017":VBS_SSWW_aTGC_UL2017,
    "VBS_SSWW_aTGC_mixed_UL2017":VBS_SSWW_aTGC_mixed_UL2017,
    "DataMu_UL2017":DataMu_UL2017,
    "FakeMu_UL2017":FakeMu_UL2017,
    "DataEle_UL2017":DataEle_UL2017,
    "FakeEle_UL2017":FakeEle_UL2017,
    "DataHT_UL2017":DataHT_UL2017,

    "ZZtoLep_UL2018":ZZtoLep_UL2018,
    "TT_UL2018":TT_UL2018,
    #"TT_Mtt_UL2018":TT_Mtt_UL2018,
    "TTTo2L2Nu_UL2018":TTTo2L2Nu_UL2018,
    "TVX_UL2018":TVX_UL2018,
    "VG_UL2018":VG_UL2018,
    "WrongSign_UL2018":WrongSign_UL2018,
    "WrongSign_ML_UL2018":WrongSign_ML_UL2018,
    "Triboson_UL2018":Triboson_UL2018,
    "WJets_UL2018":WJets_UL2018,
    "WJets_Jbin_UL2018":WJets_Jbin_UL2018,
    "WZ_UL2018":WZ_UL2018,
    #"DYJetsToLL_UL2018":DYJetsToLL_UL2018,
    #"DYJetsToLL_M10to50_UL2018":DYJetsToLL_M10to50_UL2018,
    #"DYJetsToLL_FxFx_UL2018":DYJetsToLL_FxFx_UL2018,
    "DYJetsToLL_Jbin_FxFx_UL2018":DYJetsToLL_Jbin_FxFx_UL2018,
    #"WpWpJJ_EWK_UL2018":WpWpJJ_EWK_UL2018,
    #"WpWpJJ_QCD_UL2018":WpWpJJ_QCD_UL2018,
    "WpWpJJ_UL2018":WpWpJJ_UL2018,
    "VBS_SSWW_SM_UL2018":VBS_SSWW_SM_UL2018,
    "VBS_SSWW_cW_UL2018":VBS_SSWW_cW_UL2018,
    "VBS_SSWW_cHW_UL2018":VBS_SSWW_cHW_UL2018,
    "VBS_SSWW_cW_SM_UL2018":VBS_SSWW_cW_SM_UL2018,
    "VBS_SSWW_cHW_SM_UL2018":VBS_SSWW_cHW_SM_UL2018,
    "VBS_SSWW_cW_cHW_UL2018":VBS_SSWW_cW_cHW_UL2018,
    #"VBS_SSWW_DIM6_SM_UL2018":VBS_SSWW_DIM6_SM_UL2018,
    "VBS_SSWW_aQGC_UL2018":VBS_SSWW_aQGC_UL2018,
    #"VBS_SSWW_aTGC_UL2018":VBS_SSWW_aTGC_UL2018,
    "VBS_SSWW_aTGC_mixed_UL2018":VBS_SSWW_aTGC_mixed_UL2018,
    "DataMu_UL2018":DataMu_UL2018,
    "FakeMu_UL2018":FakeMu_UL2018,
    "DataEle_UL2018":DataEle_UL2018,
    "FakeEle_UL2018":FakeEle_UL2018,
    "DataHT_UL2018":DataHT_UL2018,

    "VBS_SSWW_SM_ULRunII":VBS_SSWW_SM_ULRunII,
    "VBS_SSWW_LL_SM_ULRunII":VBS_SSWW_LL_SM_ULRunII,
    "VBS_SSWW_TL_SM_ULRunII":VBS_SSWW_TL_SM_ULRunII,
    "VBS_SSWW_TT_SM_ULRunII":VBS_SSWW_TT_SM_ULRunII,
    "VBS_SSWW_cW_ULRunII":VBS_SSWW_cW_ULRunII,
    "VBS_SSWW_cHW_ULRunII":VBS_SSWW_cHW_ULRunII,
    "VBS_SSWW_cW_SM_ULRunII":VBS_SSWW_cW_SM_ULRunII,
    "VBS_SSWW_cHW_SM_ULRunII":VBS_SSWW_cHW_SM_ULRunII,
    "VBS_SSWW_cW_BSM_ULRunII":VBS_SSWW_cW_BSM_ULRunII,
    "VBS_SSWW_cHW_BSM_ULRunII":VBS_SSWW_cHW_BSM_ULRunII,
    "VBS_SSWW_cW_cHW_ULRunII":VBS_SSWW_cW_cHW_ULRunII,
    "VBS_SSWW_aQGC_ULRunII":VBS_SSWW_aQGC_ULRunII,
    #"VBS_SSWW_aTGC_ULRunII":VBS_SSWW_aTGC_ULRunII,
    "VBS_SSWW_aTGC_mixed_ULRunII":VBS_SSWW_aTGC_mixed_ULRunII,
    "WpWpJJ_EWK_ULRunII":WpWpJJ_EWK_ULRunII,
    "WpWpJJ_QCD_ULRunII":WpWpJJ_QCD_ULRunII,
    "WpWpJJ_ULRunII":WpWpJJ_ULRunII,
    "ZZtoLep_ULRunII":ZZtoLep_ULRunII,
    "Triboson_ULRunII":Triboson_ULRunII,
    "TVX_ULRunII":TVX_ULRunII,
    "VG_ULRunII":VG_ULRunII,
    "WZ_ULRunII":WZ_ULRunII,
    "WrongSign_ULRunII":WrongSign_ULRunII,
    "WrongSign_ML_ULRunII":WrongSign_ML_ULRunII,
    #"DYJetsToLL_FxFx_ULRunII":DYJetsToLL_FxFx_ULRunII,
    #"DYJetsToLL_Jbin_FxFx_ULRunII":DYJetsToLL_Jbin_FxFx_ULRunII,
    "TTTo2L2Nu_ULRunII":TTTo2L2Nu_ULRunII,
    #TT_ULRunII,
    #WJets_ULRunII,
    "FakeMu_ULRunII":FakeMu_ULRunII,
    "DataMu_ULRunII":DataMu_ULRunII,
    "FakeEle_ULRunII":FakeEle_ULRunII,
    "DataEle_ULRunII":DataEle_ULRunII,
    "Others_ULRunII":Others_ULRunII,
}

merge_list = merge_dict.values()
condor_list = condor_dict.values()

plot_list = [
    WpWpJJ_EWK_UL2016APV,
    VBS_SSWW_SM_UL2016APV,
    #VBS_SSWW_LL_SM_UL2016APV,
    #VBS_SSWW_TL_SM_UL2016APV,
    #VBS_SSWW_TT_SM_UL2016APV,
    VBS_SSWW_cW_UL2016APV,
    VBS_SSWW_cHW_UL2016APV,
    VBS_SSWW_cW_SM_UL2016APV,
    VBS_SSWW_cHW_SM_UL2016APV,
    VBS_SSWW_cW_BSM_UL2016APV,
    VBS_SSWW_cHW_BSM_UL2016APV,
    VBS_SSWW_cW_cHW_UL2016APV,
    #VBS_SSWW_DIM6_UL2016APV,
    VBS_SSWW_aQGC_UL2016APV,
    VBS_SSWW_aTGC_UL2016APV,
    #VBS_SSWW_aTGC_mixed_UL2016APV,
    WpWpJJ_QCD_UL2016APV,
    WpWpJJ_UL2016APV,
    ZZtoLep_UL2016APV,
    Triboson_UL2016APV,
    TVX_UL2016APV,
    VG_UL2016APV,
    WZ_UL2016APV,
    Others_UL2016APV,
    WrongSign_UL2016APV,
    ##DYJetsToLL_UL2016APV,
    #DYJetsToLL_FxFx_UL2016APV,
    ##DYJetsToLL_Jbin_FxFx_UL2016APV,
    TTTo2L2Nu_UL2016APV,
    #TT_UL2016APV,
    #WJets_UL2016APV,
    FakeMu_UL2016APV,
    #FakeMuPromptTau_UL2016APV,
    #PromptMuFakeTau_UL2016APV,
    #FakeMuFakeTau_UL2016APV,
    DataMu_UL2016APV,
    FakeEle_UL2016APV,
    #FakeElePromptTau_UL2016APV,
    #PromptEleFakeTau_UL2016APV,
    #FakeEleFakeTau_UL2016APV,
    DataEle_UL2016APV,

    WpWpJJ_EWK_UL2016,
    VBS_SSWW_SM_UL2016,
    #VBS_SSWW_LL_SM_UL2016,
    #VBS_SSWW_TL_SM_UL2016,
    #VBS_SSWW_TT_SM_UL2016,
    VBS_SSWW_cW_UL2016,
    VBS_SSWW_cHW_UL2016,
    VBS_SSWW_cW_SM_UL2016,
    VBS_SSWW_cHW_SM_UL2016,
    VBS_SSWW_cW_BSM_UL2016,
    VBS_SSWW_cHW_BSM_UL2016,
    VBS_SSWW_cW_cHW_UL2016,
    VBS_SSWW_aQGC_UL2016,
    VBS_SSWW_aTGC_UL2016,
    #VBS_SSWW_aTGC_mixed_UL2016,
    #VBS_SSWW_DIM6_UL2016,
    WpWpJJ_QCD_UL2016,
    WpWpJJ_UL2016,
    ZZtoLep_UL2016,
    Triboson_UL2016,
    TVX_UL2016,
    VG_UL2016,
    WZ_UL2016,
    Others_UL2016,
    WrongSign_UL2016,
    #DYJetsToLL_FxFx_UL2016,
    ##DYJetsToLL_Jbin_FxFx_UL2016,
    ##DYJetsToLL_UL2016,
    TTTo2L2Nu_UL2016,
    #TT_UL2016,
    #WJets_UL2016,
    FakeMu_UL2016,
    #FakeMuPromptTau_UL2016,
    #PromptMuFakeTau_UL2016,
    #FakeMuFakeTau_UL2016,
    DataMu_UL2016,
    FakeEle_UL2016,
    #FakeElePromptTau_UL2016,
    #PromptEleFakeTau_UL2016,
    #FakeEleFakeTau_UL2016,
    DataEle_UL2016,

    WpWpJJ_EWK_UL2016M,
    VBS_SSWW_SM_UL2016M,
    #VBS_SSWW_LL_SM_UL2016M,
    #VBS_SSWW_TL_SM_UL2016M,
    #VBS_SSWW_TT_SM_UL2016M,
    VBS_SSWW_cW_UL2016M,
    VBS_SSWW_cHW_UL2016M,
    VBS_SSWW_cW_SM_UL2016M,
    VBS_SSWW_cHW_SM_UL2016M,
    VBS_SSWW_cW_BSM_UL2016M,
    VBS_SSWW_cHW_BSM_UL2016M,
    VBS_SSWW_cW_cHW_UL2016M,
    VBS_SSWW_aQGC_UL2016M,
    VBS_SSWW_aTGC_UL2016M,
    #VBS_SSWW_aTGC_mixed_UL2016M,
    #VBS_SSWW_DIM6_UL2016M,
    WpWpJJ_QCD_UL2016M,
    WpWpJJ_UL2016M,
    ZZtoLep_UL2016M,
    Triboson_UL2016M,
    TVX_UL2016M,
    VG_UL2016M,
    WZ_UL2016M,
    Others_UL2016M,
    WrongSign_UL2016M,
    #DYJetsToLL_FxFx_UL2016M,
    ##DYJetsToLL_Jbin_FxFx_UL2016M,
    ##DYJetsToLL_UL2016M,
    TTTo2L2Nu_UL2016M,
    #TT_UL2016M,
    #WJets_UL2016M,
    FakeMu_UL2016M,
    #FakeMuPromptTau_UL2016M,
    #PromptMuFakeTau_UL2016M,
    #FakeMuFakeTau_UL2016M,
    DataMu_UL2016M,
    FakeEle_UL2016M,
    #FakeElePromptTau_UL2016M,
    #PromptEleFakeTau_UL2016M,
    #FakeEleFakeTau_UL2016M,
    DataEle_UL2016M,

    WpWpJJ_EWK_UL2017,
    VBS_SSWW_SM_UL2017,
    #VBS_SSWW_LL_SM_UL2017,
    #VBS_SSWW_TL_SM_UL2017,
    #VBS_SSWW_TT_SM_UL2017,
    VBS_SSWW_cW_UL2017,
    VBS_SSWW_cHW_UL2017,
    VBS_SSWW_cW_SM_UL2017,
    VBS_SSWW_cHW_SM_UL2017,
    VBS_SSWW_cW_BSM_UL2017,
    VBS_SSWW_cHW_BSM_UL2017,
    VBS_SSWW_cW_cHW_UL2017,
    VBS_SSWW_aQGC_UL2017,
    VBS_SSWW_aTGC_UL2017,
    #VBS_SSWW_aTGC_mixed_UL2017,
    #VBS_SSWW_DIM6_UL2017,
    WpWpJJ_QCD_UL2017,
    WpWpJJ_UL2017,
    ZZtoLep_UL2017,
    Triboson_UL2017,
    TVX_UL2017,
    VG_UL2017,
    WZ_UL2017,
    Others_UL2017,
    WrongSign_UL2017,
    #DYJetsToLL_FxFx_UL2017,
    ##DYJetsToLL_Jbin_FxFx_UL2017,
    ##DYJetsToLL_UL2017,
    TTTo2L2Nu_UL2017,
    #TT_UL2017,
    #WJets_UL2017,
    FakeMu_UL2017,
    #FakeMuPromptTau_UL2017,
    #PromptMuFakeTau_UL2017,
    #FakeMuFakeTau_UL2017,
    DataMu_UL2017,
    FakeEle_UL2017,
    #FakeElePromptTau_UL2017,
    #PromptEleFakeTau_UL2017,
    #FakeEleFakeTau_UL2017,
    DataEle_UL2017,

    WpWpJJ_EWK_UL2018,
    VBS_SSWW_SM_UL2018,
    #VBS_SSWW_LL_SM_UL2018,
    #VBS_SSWW_TL_SM_UL2018,
    #VBS_SSWW_TT_SM_UL2018,
    VBS_SSWW_cW_UL2018,
    VBS_SSWW_cHW_UL2018,
    VBS_SSWW_cW_SM_UL2018,
    VBS_SSWW_cHW_SM_UL2018,
    VBS_SSWW_cW_BSM_UL2018,
    VBS_SSWW_cHW_BSM_UL2018,
    VBS_SSWW_cW_cHW_UL2018,
    VBS_SSWW_aQGC_UL2018,
    VBS_SSWW_aTGC_UL2018,
    #VBS_SSWW_aTGC_mixed_UL2018,
    #VBS_SSWW_DIM6_UL2018,
    WpWpJJ_QCD_UL2018,
    WpWpJJ_UL2018,
    ZZtoLep_UL2018,
    Triboson_UL2018,
    TVX_UL2018,
    VG_UL2018,
    WZ_UL2018,
    Others_UL2018,
    WrongSign_UL2018,
    #DYJetsToLL_FxFx_UL2018,
    ##DYJetsToLL_Jbin_FxFx_UL2018,
    ##DYJetsToLL_UL2018,
    TTTo2L2Nu_UL2018,
    ##WWto2L2Nu_UL2018,
    ##GluGluToWWToENEN_UL2018,
    ##GluGluToWWToENMN_UL2018,
    ##GluGluToWWToENTN_UL2018,
    ##GluGluToWWToMNEN_UL2018,
    ##GluGluToWWToMNMN_UL2018,
    ##GluGluToWWToMNTN_UL2018,
    ##GluGluToWWToTNEN_UL2018,
    ##GluGluToWWToTNMN_UL2018,
    ##GluGluToWWToTNTN_UL2018,
    ##ST_tW_top_UL2018,
    ##ST_tW_antitop_UL2018,
    ##GluGluHToWWTo2L2Nu_UL2018,
    ##GluGluHToZZTo4L_UL2018,
    ##GluGluHToTauTau_UL2018,
    ##VBFHToWWTo2L2Nu_UL2018,
    ##VBFHToTauTau_UL2018,
    ##ttHToNonbb_UL2018,
    ##VHToNonbb_UL2018,
    #TT_UL2018,
    #WJets_UL2018,
    FakeMu_UL2018,
    #FakeMuPromptTau_UL2018,
    #PromptMuFakeTau_UL2018,
    #FakeMuFakeTau_UL2018,
    DataMu_UL2018,
    FakeEle_UL2018,
    #FakeElePromptTau_UL2018,
    #PromptEleFakeTau_UL2018,
    #FakeEleFakeTau_UL2018,
    DataEle_UL2018,
    
    WpWpJJ_EWK_ULRunII,
    #VBS_SSWW_SM_ULRunII,
    #VBS_SSWW_LL_SM_ULRunII,
    #VBS_SSWW_TL_SM_ULRunII,
    #VBS_SSWW_TT_SM_ULRunII,
    VBS_SSWW_cW_ULRunII,
    #VBS_SSWW_cHW_ULRunII,
    #VBS_SSWW_cW_SM_ULRunII,
    #VBS_SSWW_cHW_SM_ULRunII,
    #VBS_SSWW_cW_BSM_ULRunII,
    #VBS_SSWW_cHW_BSM_ULRunII,
    #VBS_SSWW_cW_cHW_ULRunII,
    ##VBS_SSWW_DIM6_ULRunII,
    VBS_SSWW_aQGC_ULRunII,
    #VBS_SSWW_aTGC_ULRunII,
    ##VBS_SSWW_aTGC_mixed_ULRunII,
    WpWpJJ_QCD_ULRunII,
    WpWpJJ_ULRunII,
    ZZtoLep_ULRunII,
    Triboson_ULRunII,
    TVX_ULRunII,
    VG_ULRunII,
    WZ_ULRunII,
    Others_ULRunII,
    WrongSign_ULRunII,
    ##DYJetsToLL_FxFx_ULRunII,
    ##DYJetsToLL_Jbin_FxFx_ULRunII,
    ##DYJetsToLL_ULRunII,
    TTTo2L2Nu_ULRunII,
    #TT_ULRunII,
    #WJets_ULRunII,
    FakeMu_ULRunII,
    #FakeMuPromptTau_ULRunII,
    #PromptMuFakeTau_ULRunII,
    #FakeMuFakeTau_ULRunII,
    DataMu_ULRunII,
    FakeEle_ULRunII,
    #FakeElePromptTau_ULRunII,
    #PromptEleFakeTau_ULRunII,
    #FakeEleFakeTau_ULRunII,
    DataEle_ULRunII,
]

stack_list = [
    WpWpJJ_EWK_UL2016APV,
    ##VBS_SSWW_SM_UL2016APV,
    #VBS_SSWW_LL_SM_UL2016APV,
    #VBS_SSWW_TL_SM_UL2016APV,
    #VBS_SSWW_TT_SM_UL2016APV,
    VBS_SSWW_cW_UL2016APV,
    ##VBS_SSWW_cHW_UL2016APV,
    ##VBS_SSWW_cW_SM_UL2016APV,
    ##VBS_SSWW_cHW_SM_UL2016APV,
    ##VBS_SSWW_cW_BSM_UL2016APV,
    ##VBS_SSWW_cHW_BSM_UL2016APV,
    ##VBS_SSWW_DIM6_UL2016APV,
    ##VBS_SSWW_aQGC_UL2016APV,
    WpWpJJ_QCD_UL2016APV,
    #WpWpJJ_UL2016APV,
    ZZtoLep_UL2016APV,
    Triboson_UL2016APV,
    TVX_UL2016APV,
    VG_UL2016APV,
    WZ_UL2016APV,
    WrongSign_UL2016APV,
    #DYJetsToLL_UL2016APV,
    #DYJetsToLL_FxFx_UL2016APV,
    #DYJetsToLL_Jbin_FxFx_UL2016APV,
    TTTo2L2Nu_UL2016APV,
    #TT_UL2016APV,
    #WJets_UL2016APV,
    FakeMu_UL2016APV,
    #FakeMuPromptTau_UL2016APV,
    #PromptMuFakeTau_UL2016APV,
    #FakeMuFakeTau_UL2016APV,
    DataMu_UL2016APV,
    FakeEle_UL2016APV,
    #FakeElePromptTau_UL2016APV,
    #PromptEleFakeTau_UL2016APV,
    #FakeEleFakeTau_UL2016APV,
    DataEle_UL2016APV,

    WpWpJJ_EWK_UL2016,
    ##VBS_SSWW_SM_UL2016,
    #VBS_SSWW_LL_SM_UL2016,
    #VBS_SSWW_TL_SM_UL2016,
    #VBS_SSWW_TT_SM_UL2016,
    VBS_SSWW_cW_UL2016,
    ##VBS_SSWW_cHW_UL2016,
    ##VBS_SSWW_cW_SM_UL2016,
    ##VBS_SSWW_cHW_SM_UL2016,
    ##VBS_SSWW_cW_BSM_UL2016,
    ##VBS_SSWW_cHW_BSM_UL2016,
    ##VBS_SSWW_aQGC_UL2016,
    ##VBS_SSWW_DIM6_UL2016,
    WpWpJJ_QCD_UL2016,
    #WpWpJJ_UL2016,
    ZZtoLep_UL2016,
    Triboson_UL2016,
    TVX_UL2016,
    VG_UL2016,
    WZ_UL2016,
    WrongSign_UL2016,
    #DYJetsToLL_FxFx_UL2016,
    #DYJetsToLL_Jbin_FxFx_UL2016,
    #DYJetsToLL_UL2016,
    TTTo2L2Nu_UL2016,
    #TT_UL2016,
    #WJets_UL2016,
    FakeMu_UL2016,
    #FakeMuPromptTau_UL2016,
    #PromptMuFakeTau_UL2016,
    #FakeMuFakeTau_UL2016,
    DataMu_UL2016,
    FakeEle_UL2016,
    #FakeElePromptTau_UL2016,
    #PromptEleFakeTau_UL2016,
    #FakeEleFakeTau_UL2016,
    DataEle_UL2016,

    WpWpJJ_EWK_UL2016M,
    ##VBS_SSWW_SM_UL2016M,
    #VBS_SSWW_LL_SM_UL2016M,
    #VBS_SSWW_TL_SM_UL2016M,
    #VBS_SSWW_TT_SM_UL2016M,
    VBS_SSWW_cW_UL2016M,
    ##VBS_SSWW_cHW_UL2016M,
    ##VBS_SSWW_cW_SM_UL2016M,
    ##VBS_SSWW_cHW_SM_UL2016M,
    ##VBS_SSWW_cW_BSM_UL2016M,
    ##VBS_SSWW_cHW_BSM_UL2016M,
    ##VBS_SSWW_aQGC_UL2016M,
    ##VBS_SSWW_DIM6_UL2016M,
    WpWpJJ_QCD_UL2016M,
    #WpWpJJ_UL2016M,
    ZZtoLep_UL2016M,
    Triboson_UL2016M,
    TVX_UL2016M,
    VG_UL2016M,
    WZ_UL2016M,
    WrongSign_UL2016M,
    #DYJetsToLL_FxFx_UL2016M,
    #DYJetsToLL_Jbin_FxFx_UL2016M,
    #DYJetsToLL_UL2016M,
    TTTo2L2Nu_UL2016M,
    #TT_UL2016M,
    #WJets_UL2016M,
    FakeMu_UL2016M,
    #FakeMuPromptTau_UL2016M,
    #PromptMuFakeTau_UL2016M,
    #FakeMuFakeTau_UL2016M,
    DataMu_UL2016M,
    FakeEle_UL2016M,
    #FakeElePromptTau_UL2016M,
    #PromptEleFakeTau_UL2016M,
    #FakeEleFakeTau_UL2016M,
    DataEle_UL2016M,

    WpWpJJ_EWK_UL2017,
    ##VBS_SSWW_SM_UL2017,
    #VBS_SSWW_LL_SM_UL2017,
    #VBS_SSWW_TL_SM_UL2017,
    #VBS_SSWW_TT_SM_UL2017,
    VBS_SSWW_cW_UL2017,
    ##VBS_SSWW_cHW_UL2017,
    ##VBS_SSWW_cW_SM_UL2017,
    ##VBS_SSWW_cHW_SM_UL2017,
    ##VBS_SSWW_cW_BSM_UL2017,
    ##VBS_SSWW_cHW_BSM_UL2017,
    ##VBS_SSWW_aQGC_UL2017,
    ##VBS_SSWW_DIM6_UL2017,
    WpWpJJ_QCD_UL2017,
    #WpWpJJ_UL2017,
    ZZtoLep_UL2017,
    Triboson_UL2017,
    TVX_UL2017,
    VG_UL2017,
    WZ_UL2017,
    WrongSign_UL2017,
    #DYJetsToLL_FxFx_UL2017,
    #DYJetsToLL_Jbin_FxFx_UL2017,
    #DYJetsToLL_UL2017,
    TTTo2L2Nu_UL2017,
    #TT_UL2017,
    #WJets_UL2017,
    FakeMu_UL2017,
    #FakeMuPromptTau_UL2017,
    #PromptMuFakeTau_UL2017,
    #FakeMuFakeTau_UL2017,
    DataMu_UL2017,
    FakeEle_UL2017,
    #FakeElePromptTau_UL2017,
    #PromptEleFakeTau_UL2017,
    #FakeEleFakeTau_UL2017,
    DataEle_UL2017,

    WpWpJJ_EWK_UL2018,
    ##VBS_SSWW_SM_UL2018,
    #VBS_SSWW_LL_SM_UL2018,
    #VBS_SSWW_TL_SM_UL2018,
    #VBS_SSWW_TT_SM_UL2018,
    VBS_SSWW_cW_UL2018,
    ##VBS_SSWW_cHW_UL2018,
    ##VBS_SSWW_cW_SM_UL2018,
    ##VBS_SSWW_cHW_SM_UL2018,
    ##VBS_SSWW_cW_BSM_UL2018,
    ##VBS_SSWW_cHW_BSM_UL2018,
    ##VBS_SSWW_aQGC_UL2018,
    ##VBS_SSWW_DIM6_UL2018,
    WpWpJJ_QCD_UL2018,
    #WpWpJJ_UL2018,
    ZZtoLep_UL2018,
    Triboson_UL2018,
    TVX_UL2018,
    VG_UL2018,
    WZ_UL2018,
    WrongSign_UL2018,
    #DYJetsToLL_FxFx_UL2018,
    #DYJetsToLL_Jbin_FxFx_UL2018,
    #DYJetsToLL_UL2018,
    TTTo2L2Nu_UL2018,
    ##WWto2L2Nu_UL2018,
    ##GluGluToWWToENEN_UL2018,
    ##GluGluToWWToENMN_UL2018,
    ##GluGluToWWToENTN_UL2018,
    ##GluGluToWWToMNEN_UL2018,
    ##GluGluToWWToMNMN_UL2018,
    ##GluGluToWWToMNTN_UL2018,
    ##GluGluToWWToTNEN_UL2018,
    ##GluGluToWWToTNMN_UL2018,
    ##GluGluToWWToTNTN_UL2018,
    ##ST_tW_top_UL2018,
    ##ST_tW_antitop_UL2018,
    ##GluGluHToWWTo2L2Nu_UL2018,
    ##GluGluHToZZTo4L_UL2018,
    ##GluGluHToTauTau_UL2018,
    ##VBFHToWWTo2L2Nu_UL2018,
    ##VBFHToTauTau_UL2018,
    ##ttHToNonbb_UL2018,
    ##VHToNonbb_UL2018,
    #TT_UL2018,
    #WJets_UL2018,
    FakeMu_UL2018,
    #FakeMuPromptTau_UL2018,
    #PromptMuFakeTau_UL2018,
    #FakeMuFakeTau_UL2018,
    DataMu_UL2018,
    FakeEle_UL2018,
    #FakeElePromptTau_UL2018,
    #PromptEleFakeTau_UL2018,
    #FakeEleFakeTau_UL2018,
    DataEle_UL2018,
    
    WpWpJJ_EWK_ULRunII,
    ##VBS_SSWW_SM_ULRunII,
    #VBS_SSWW_LL_SM_ULRunII,
    #VBS_SSWW_TL_SM_ULRunII,
    #VBS_SSWW_TT_SM_ULRunII,
    VBS_SSWW_cW_ULRunII,
    ##VBS_SSWW_cHW_ULRunII,
    ##VBS_SSWW_cW_SM_ULRunII,
    ##VBS_SSWW_cHW_SM_ULRunII,
    ##VBS_SSWW_cW_BSM_ULRunII,
    ##VBS_SSWW_cHW_BSM_ULRunII,
    ##VBS_SSWW_DIM6_ULRunII,
    ##VBS_SSWW_aQGC_ULRunII,
    WpWpJJ_QCD_ULRunII,
    #WpWpJJ_ULRunII,
    ZZtoLep_ULRunII,
    Triboson_ULRunII,
    TVX_ULRunII,
    VG_ULRunII,
    WZ_ULRunII,
    Others_ULRunII,
    WrongSign_ULRunII,
    #DYJetsToLL_FxFx_ULRunII,
    #DYJetsToLL_Jbin_FxFx_ULRunII,
    #DYJetsToLL_ULRunII,
    TTTo2L2Nu_ULRunII,
    TT_ULRunII,
    #WJets_ULRunII,
    FakeMu_ULRunII,
    #FakeMuPromptTau_ULRunII,
    #PromptMuFakeTau_ULRunII,
    #FakeMuFakeTau_ULRunII,
    DataMu_ULRunII,
    FakeEle_ULRunII,
    #FakeElePromptTau_ULRunII,
    #PromptEleFakeTau_ULRunII,
    #FakeEleFakeTau_ULRunII,
    DataEle_ULRunII,
]

