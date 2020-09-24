import collections

#*********************************
#                                *
#       List of channels         *
#                                *
#*********************************


nores=False
#nores=True

onlyfwd=False
#onlyfwd=True

noresnofwd=False
#noresnofwd=True

### List of histos to include in the root files
histos = {"Merged_nofwd":"h_MT_final","Merged_fwd" :"h_MT_final_fwd", "SemiRes_nofwd": "h_MT_final_reco_0lep_1bjet", "SemiRes_fwd":"h_MT_final_reco_0lep_1bjet_fwd"}
if(nores):
    histos = {"Merged_nofwd":"h_MT_final","Merged_fwd" :"h_MT_final_fwd"}#, "SemiRes_nofwd": "h_MT_final_reco_0lep_1bjet", "SemiRes_fwd":"h_MT_final_reco_0lep_1bjet_fwd"}
if(onlyfwd):
    histos = {"Merged_fwd" :"h_MT_final_fwd",  "SemiRes_fwd":"h_MT_final_reco_0lep_1bjet_fwd"}
if(noresnofwd):
    histos = {"Merged_nofwd":"h_MT_final","Merged_fwd" :"h_MT_final_fwd", "SemiRes_fwd":"h_MT_final_reco_0lep_1bjet_fwd"}
#histos = {"BDT0":"h_Mt"}

### List of regions for which creating the datacards
channels = [ "Merged_nofwd", "Merged_fwd", "SemiRes_nofwd", "SemiRes_fwd"]

if(nores):
    channels = [ "Merged_nofwd", "Merged_fwd"]#, "SemiRes_nofwd", "SemiRes_fwd"]
if(onlyfwd):
    channels = ["Merged_fwd", "SemiRes_fwd"]
if(noresnofwd):
    channels = [ "Merged_nofwd", "Merged_fwd", "SemiRes_fwd"]

channels_labels = {"Merged":"SR_cat0_merged", "SemiRes":"CR0lep1B_reco_cat0_merged"}
if(nores):
    channels_labels = {"Merged":"SR_cat0_merged"}#, "SemiRes":"CR0lep1B_reco_cat0_merged"}
if(onlyfwd):
    channels_labels = {"Merged":"SR_cat0_merged", "SemiRes":"CR0lep1B_reco_cat0_merged"}
if(noresnofwd):
    channels_labels = {"Merged":"SR_cat0_merged", "SemiRes":"CR0lep1B_reco_cat0_merged"}

#categories = [ "BDT1", "BDT2", "CRBDT1", "CRBDT2"]

categories = [ "Merged_nofwd", "Merged_fwd", "SemiRes_nofwd", "SemiRes_fwd"]
if(nores):
    categories = [ "Merged_nofwd", "Merged_fwd"]#, "SemiRes_nofwd", "SemiRes_fwd"]
if(onlyfwd):
    categories = [ "Merged_fwd", "SemiRes_fwd"]
if(noresnofwd):
    categories = [ "Merged_nofwd", "Merged_fwd", "SemiRes_fwd"]

class rateParam(object):
    pass

rateParams = {}

sigZ="ZJetsCRZ1"
#sigZ="ZJetsCRZ2"
#sigZ="ZJets"

sigTTW="TTW"
#sigTTW="TT"
commonrp=True
#commonrp=False
if(commonrp):
    rateZJets = rateParam()
    rateZJets.chs = ["Merged_nofwd", "SemiRes_nofwd"]
    rateZJets.bkg = sigZ
    rateParams["ZJets"] = rateZJets

    rateZJetsFwd = rateParam()
    rateZJetsFwd.chs = ["Merged_fwd", "SemiRes_fwd"]
    rateZJetsFwd.bkg = sigZ
    rateParams["ZJets_fwd"] = rateZJetsFwd

    
    rateTT = rateParam()
    rateTT.chs = ["Merged_nofwd", "SemiRes_nofwd"]
    rateTT.bkg = sigTTW
    rateParams["TT"] = rateTT

    rateTTFwd = rateParam()
    rateTTFwd.chs = ["Merged_fwd", "SemiRes_fwd"]
    rateTTFwd.bkg = sigTTW
    rateParams["TT_fwd"] = rateTTFwd
else:
    rateZJets16 = rateParam()
    rateZJets16.chs = ["Merged_nofwd", "SemiRes_nofwd"]
    rateZJets16.bkg = sigZ
    rateParams["ZJets2016"] = rateZJets16
    
    rateZJetsFwd16 = rateParam()
    rateZJetsFwd16.chs = ["Merged_fwd", "SemiRes_fwd"]
    rateZJetsFwd16.bkg = sigZ
    rateParams["ZJets_fwd2016"] = rateZJetsFwd16

    rateTT16 = rateParam()
    rateTT16.chs = ["Merged_nofwd", "SemiRes_nofwd"]
    rateTT16.bkg = sigTTW
    rateParams["TT2016"] = rateTT16

    rateTTFwd16 = rateParam()
    rateTTFwd16.chs = ["Merged_fwd", "SemiRes_fwd"]
    rateTTFwd16.bkg = sigTTW
    rateParams["TT_fwd2016"] = rateTTFwd16

##
    rateZJets17 = rateParam()
    rateZJets17.chs = ["Merged_nofwd", "SemiRes_nofwd"]
    rateZJets17.bkg = sigZ
    rateParams["ZJets2017"] = rateZJets17
    
    rateZJetsFwd17 = rateParam()
    rateZJetsFwd17.chs = ["Merged_fwd", "SemiRes_fwd"]
    rateZJetsFwd17.bkg = sigZ
    rateParams["ZJets_fwd2017"] = rateZJetsFwd17

    rateTT17 = rateParam()
    rateTT17.chs = ["Merged_nofwd", "SemiRes_nofwd"]
    rateTT17.bkg = sigTTW
    rateParams["TT2017"] = rateTT17

    rateTTFwd17 = rateParam()
    rateTTFwd17.chs = ["Merged_fwd", "SemiRes_fwd"]
    rateTTFwd17.bkg = sigTTW
    rateParams["TT_fwd2017"] = rateTTFwd17

##
    rateZJets18 = rateParam()
    rateZJets18.chs = ["Merged_nofwd", "SemiRes_nofwd"]
    rateZJets18.bkg = sigZ
    rateParams["ZJets2018"] = rateZJets18
    
    rateZJetsFwd18 = rateParam()
    rateZJetsFwd18.chs = ["Merged_fwd", "SemiRes_fwd"]
    rateZJetsFwd18.bkg = sigZ
    rateParams["ZJets_fwd2018"] = rateZJetsFwd18

    rateTT18 = rateParam()
    rateTT18.chs = ["Merged_nofwd", "SemiRes_nofwd"]
    rateTT18.bkg = sigTTW
    rateParams["TT2018"] = rateTT18

    rateTTFwd18 = rateParam()
    rateTTFwd18.chs = ["Merged_fwd", "SemiRes_fwd"]
    rateTTFwd18.bkg = sigTTW
    rateParams["TT_fwd2018"] = rateTTFwd18


#rateParams = {}

#rateQCD = rateParam()
#rateQCD.chs = ["Merged_fwd", "SemiRes_fwd", "Merged_nofwd", "SemiRes_nofwd"]
#rateQCD.bkg = "QCD"
#rateParams["QCDmc"] = rateQCD



#*********************************
#                                *
#       List of backgrounds      *
#                                *
#*********************************

processes = [sigTTW, sigZ]#, "QCD", "SingleTop"]
processes = [sigTTW, sigZ, "QCD", "SingleTop"]

bkgs = ["TTW_cat0_merged", "ZJetsCRZ1_cat0_merged"]#, "QCD_cat0_merged", "SingleTop_cat0_merged"]
bkgs = ["TTW_cat0_merged", "ZJetsCRZ1_cat0_merged", "QCD_cat0_merged", "SingleTop_cat0_merged"]


#*********************************
#                                *
#       List of systematics      *
#                                *
#*********************************

syst = collections.OrderedDict()
syst["lumi_2016"] = ["lnN", "all", 1.025]
syst["lumi_2017"] = ["lnN", "all", 1.023]
syst["lumi_2018"] = ["lnN", "all", 1.025]
#syst["lumi_2018"] = ["lnN", "all", 1.023]
#syst["trigger"] = ["lnN", "all", 1.02]
#syst["mcstat"] = ["shape", ("QCD", sigTTW, "WJets", sigZ, "sig")]
#syst["trigSF"] = ["shape", ["sig"]]
syst["trigSF"] = ["lnN", ["sig",sigTTW, sigZ, "QCD", "SingleTop"]]
syst["topTag"] = ["lnN", ["sig",sigTTW, sigZ, "QCD", "SingleTop"]]
syst["wTag"] = ["lnN", ["sig",sigTTW, sigZ, "QCD", "SingleTop"]]
syst["prefiring"] = ["lnN", ["sig", sigTTW, sigZ, "QCD", "SingleTop"]]
#syst["prefiring"] = ["lnN", ["sig"] ]
syst["pu"] = ["lnN", ["sig", sigTTW, sigZ, "QCD", "SingleTop"]]

syst["btag"] = ["lnN", ["sig", sigTTW, sigZ, "QCD", "SingleTop"]]
#syst["mistag"] = ["lnN", ["sig", sigTTW, "ZJetsCR1"]]
syst["pdf_total"] = ["lnN", ["sig", sigTTW, sigZ, "QCD", "SingleTop"]]

ys=["2016","2017","2018"]

splityearjes=False
#splityearjes=True
if(splityearjes):
    for y in ys:
        #if(y=="2016"):syst["jes"+y] = ["shape", [ sigTTW]] #No QCD : low stat
        #if(y=="2016"):syst["jer"+y] = ["shape", [ sigTTW]] #No QCD : low stat
        if(y=="2016"):syst["jes"+y] = ["shape", ["sig",sigZ, sigTTW, "SingleTop" ]] #No QCD : low stat
        if(y=="2016"):syst["jer"+y] = ["shape", ["sig",sigZ, sigTTW, "SingleTop" ]] #No QCD : low stat
        if(y!="2016"):syst["jes"+y] = ["shape", ["sig", sigZ, sigTTW, "SingleTop"]] #No QCD : low stat
        if(y!="2016"):syst["jer"+y] = ["shape", ["sig", sigZ, sigTTW, "SingleTop"]] #No QCD : low stat
if(not splityearjes):
    syst["jes"] = ["shape", ["sig", sigTTW, sigZ, "SingleTop"]] #No QCD : low stat
    syst["jer"] = ["shape", ["sig", sigTTW, sigZ, "SingleTop"]] #No QCD : low stat


#syst["symjes"] = ["shape", ["sig", sigTTW, sigZ, "SingleTop"]] #No QCD : low stat
#syst["symjer"] = ["shape", ["sig", sigTTW, sigZ, "SingleTop"]] #No QCD : low stat
syst["q2QCD"] = ["shape", [sigTTW, sigZ, "QCD"]]
syst["q2ZJets"] = ["shape", [sigTTW, sigZ]]
syst["q2WJets"] = ["shape", [sigTTW, sigZ]]
syst["q2TT"] = ["shape", [sigTTW, sigZ]]
syst["q2SingleTop"] = ["shape", ["SingleTop",sigTTW, sigZ]]
syst["q2Tprime"] = ["shape", ["sig"]]
#total
#syst["ZJetsCRZ1DDUnc"] = ["shape",[sigZ]]
##syst["ZJetsCRZ1MCUnc"] = ["shape",[sigZ]]
#syst["TTWDDUnc"] = ["shape",[sigTTW]]
#split by year


#syst["TTWMCUnc2018"] = ["shape",[sigTTW]]
doseparate=False
#doseparate=True
doseparatetwo=False
#doseparatetwo=True
ys=["2016","2017","2018"]
for y in ys:
    rs=[""]
    if doseparate:
        rs=["Merged_fwd","Merged_nofwd","SemiRes_fwd","SemiRes_nofwd"] 
    if doseparatetwo:
        rs=["Merged","SemiRes"] 
    for r in rs: 
        syst["ZJetsCRZ1DDUnc"+r+y] = ["shape",[sigZ]]
        syst["ZJetsCRZ1DDUncInv"+r+y] = ["shape",[sigZ]]
        #syst["ZJetsCRZ1MCUnc2018"] = [["shape"],[sigZ]]
        
        syst["TTWDDUnc"+r+y] = ["shape",[sigTTW]]
        syst["TTWDDUncInv"+r+y] = ["shape",[sigTTW]]
        #syst["TTWMCUnc2018"] = ["shape",[sigTTW]]


#
#    syst["ZJetsCRZ1DDUnc2018"] = ["shape",[sigZ]]
#    syst["ZJetsCRZ1DDUncInv2018"] = ["shape",[sigZ]]
#    #syst["ZJetsCRZ1MCUnc2018"] = [["shape"],[sigZ]]
#    
#    syst["TTWDDUnc2018"] = ["shape",[sigTTW]]
#    syst["TTWDDUncInvDemiRes_nofwd2018"] = ["shape",[sigTTW]]
#    #syst["TTWMCUnc2018"] = ["shape",[sigTTW]]
#
#    syst["ZJetsCRZ1DDUnc2018"] = ["shape",[sigZ]]
#    syst["ZJetsCRZ1DDUncInv2018"] = ["shape",[sigZ]]
#    #syst["ZJetsCRZ1MCUnc2018"] = [["shape"],[sigZ]]
#    
#    syst["TTWDDUnc2018"] = ["shape",[sigTTW]]
#    syst["TTWDDUncInvDemiRes_nofwd2018"] = ["shape",[sigTTW]]
#    #syst["TTWMCUnc2018"] = ["shape",[sigTTW]]
#
#    syst["ZJetsCRZ1DDUnc2018"] = ["shape",[sigZ]]
#    syst["ZJetsCRZ1DDUncInv2018"] = ["shape",[sigZ]]
#    #syst["ZJetsCRZ1MCUnc2018"] = [["shape"],[sigZ]]
#    
#    syst["TTWDDUnc2018"] = ["shape",[sigTTW]]
#    syst["TTWDDUncInvDemiRes_nofwd2018"] = ["shape",[sigTTW]]
#    #syst["TTWMCUnc2018"] = ["shape",[sigTTW]]
#
#    syst["ZJetsCRZ1DDUncInv2017"] = ["shape",[sigZ]]
#    syst["ZJetsCRZ1DDUnc2017"] = ["shape",[sigZ]]
#    #syst["ZJetsCRZ1MCUnc2017"] = [["shape"],[sigZ]]
#
#    syst["TTWDDUnc2017"] = ["shape",[sigTTW]]
#    syst["TTWDDUncInv2017"] = ["shape",[sigTTW]]
#    #syst["TTWMCUnc2017"] = ["shape",[sigTTW]]
#    
#    syst["ZJetsCRZ1DDUncInv2016"] = ["shape",[sigZ]]
#    syst["ZJetsCRZ1DDUnc2016"] = ["shape",[sigZ]]
#    #syst["ZJetsCRZ1MCUnc2016"] = [["shape"],[sigZ]]
#
#    syst["TTWDDUnc2016"] = ["shape",[sigTTW]]
#    syst["TTWDDUncInv2016"] = ["shape",[sigTTW]]
#    #syst["TTWMCUnc2016"] = ["shape",[sigTTW]]


#syst["TTWDDUnc2016"] = ["shape",[sigTTW]]
##
#syst["ZJetsCRZ1DDUnc"] = [["shape"],[sigZ]]
#syst["ZJetsCRZ2DDUnc"] = [["shape"],[sigZ]]
#syst["autoMCstat"] = ["shape"]
#syst["autoMCstat"] = ["shape",["SingleTop"]]
#syst["autoMCstat"] = ["shape",[sigZ,sigTTW,"SingleTop","QCD"]]
syst["autoMCstat"] = ["shape",["sig",sigZ,sigTTW,"SingleTop","QCD"]]
#syst["autoMCstat"] = ["shape"]






#*********************************
#                                *
#         List of signals        *
#                                *
#*********************************



vec1 = ("700")
vec2 = ("800")
vec3 = ("900")
vec4 = ("1000")
vec5 = ("1100")
vec6 = ("1200")
vec7 = ("1300")
vec8 = ("1400")
vec9 = ("1500")
vec10 = ("1600")
vec11 = ("1700")
vec12 = ("1800")

vec1wp10= ("800Wp10")
vec2wp10= ("1000Wp10")
vec3wp10= ("1200Wp10")
vec4wp10= ("1400Wp10")
vec5wp10= ("1600Wp10")

sigspointswp10 = [vec1wp10,vec2wp10,vec3wp10,vec4wp10,vec5wp10]

vec1wp20= ("800Wp20")
vec2wp20= ("1000Wp20")
vec3wp20= ("1200Wp20")
vec4wp20= ("1400Wp20")
vec5wp20= ("1600Wp20")

sigspointswp20 = [vec1wp20,vec2wp20,vec3wp20,vec4wp20,vec5wp20]

vec1wp30= ("800Wp30")
vec2wp30= ("1000Wp30")
vec3wp30= ("1200Wp30")
vec4wp30= ("1400Wp30")
vec5wp30= ("1600Wp30")

sigspointswp30 = [vec1wp30,vec2wp30,vec3wp30,vec4wp30,vec5wp30]


#sigpoints = [vec1, vec2, vec3, vec4, vec5, vec6, vec7, vec8, vec9, vec10, vec11, vec12, vec13, vec14, vec15, vec16, vec17, vec18, vec19, vec20, vec21, vec22, vec23, vec24, vec25, vec26, vec27, vec28, vec29, vec30, vec31, vec32, vec33, vec34, vec35, vec36, vec37, vec38, vec39, vec40, vec41]

sigpoints = [ vec4, vec5, vec6, vec7, vec8, vec9, vec10, vec11]
sigpoints = [ vec1, vec2, vec3, vec4, vec5, vec6, vec7, vec8, vec9, vec10, vec11]
#vec2, Missing 2017 sample
#sigpoints=[]
sigpoints.extend( sigspointswp10)
sigpoints.extend( sigspointswp20)
sigpoints.extend( sigspointswp30)

#sigpoints = [ vec1, vec2, vec3, vec4]

#sigpoints = [ vec1, vec4, vec5, vec6, vec7, vec8, vec9, vec11]
#sigpoints = [ vec11]

#sigpoints = [vec1]

