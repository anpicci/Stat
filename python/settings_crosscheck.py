import collections

#*********************************
#                                *
#       List of channels         *
#                                *
#*********************************


### List of histos to include in the root files
histos = {"Merged_nofwd":"h_MT_final_incl","Merged_fwd" :"h_MT_final_incl_fwd"}

#histos = {"BDT0":"h_Mt"}

### List of regions for which creating the datacards
channels = [ "Merged_nofwd", "Merged_fwd"]

channels_labels = {"Merged":"SR_cat0_merged"}

#categories = [ "BDT1", "BDT2", "CRBDT1", "CRBDT2"]

categories = [ "Merged_nofwd", "Merged_fwd"]

class rateParam(object):
    pass

rateParams = {}

sigZ="ZJetsCRZ1"
#sigZ="ZJetsCRZ2"
#sigZ="ZJets"

sigTTW="TTW"
#sigTTW="TT"

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

#rateQCD = rateParam()
#rateQCD.chs = ["Merged_fwd", "SemiRes_fwd", "Merged_nofwd", "SemiRes_nofwd"]
#rateQCD.bkg = "QCD"
#rateParams["QCDmc"] = rateQCD



#*********************************
#                                *
#       List of backgrounds      *
#                                *
#*********************************

processes = [sigTTW, sigZ, "QCD", "SingleTop"]

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
syst["trigSF"] = ["shape", ["sig"]]
syst["topTag"] = ["lnN", ["sig",sigTTW, sigZ, "QCD", "SingleTop"]]
syst["wTag"] = ["lnN", ["sig",sigTTW, sigZ, "QCD", "SingleTop"]]
syst["prefiring"] = ["lnN", ["sig", sigTTW, sigZ, "QCD", "SingleTop"]]
syst["prefiring"] = ["lnN", ["sig"] ]
syst["pu"] = ["lnN", ["sig", sigTTW, sigZ, "QCD", "SingleTop"]]

syst["btag"] = ["lnN", ["sig", sigTTW, sigZ, "QCD", "SingleTop"]]
#syst["mistag"] = ["lnN", ["sig", sigTTW, "ZJetsCR1"]]
syst["pdf_total"] = ["lnN", ["sig", sigTTW, sigZ, "QCD", "SingleTop"]]
syst["jes"] = ["shape", ["sig", sigTTW, sigZ, "SingleTop"]] #No QCD : low stat
syst["jer"] = ["shape", ["sig", sigTTW, sigZ, "SingleTop"]] #No QCD : low stat
syst["q2QCD"] = ["shape", [sigTTW, sigZ, "QCD"]]
syst["q2ZJets"] = ["shape", [sigTTW, sigZ]]
syst["q2WJets"] = ["shape", [sigTTW, sigZ]]
syst["q2TT"] = ["shape", [sigTTW, sigZ]]
syst["q2Tprime"] = ["shape", ["sig"]]
#total
#syst["ZJetsCRZ1DDUnc"] = ["shape",[sigZ]]
##syst["ZJetsCRZ1MCUnc"] = ["shape",[sigZ]]
#syst["TTWDDUnc"] = ["shape",[sigTTW]]
#split by year
syst["ZJetsCRZ1DDUnc2018"] = ["shape",[sigZ]]
syst["ZJetsCRZ1DDUncInv2018"] = ["shape",[sigZ]]
#syst["ZJetsCRZ1MCUnc_2018"] = [["shape"],[sigZ]]
syst["ZJetsCRZ1DDUncInv2017"] = ["shape",[sigZ]]
syst["ZJetsCRZ1DDUnc2017"] = ["shape",[sigZ]]
#syst["ZJetsCRZ1MCUnc_2017"] = [["shape"],[sigZ]]
#syst["TTWDDUncInv2017"] = ["shape",[sigTTW]]
syst["ZJetsCRZ1DDUncInv2016"] = ["shape",[sigZ]]
syst["ZJetsCRZ1DDUnc2016"] = ["shape",[sigZ]]
#syst["ZJetsCRZ1MCUnc_2016"] = [["shape"],[sigZ]]
#syst["TTWDDUnc2016"] = ["shape",[sigTTW]]
##
#syst["ZJetsCRZ1DDUnc"] = [["shape"],[sigZ]]
#syst["ZJetsCRZ2DDUnc"] = [["shape"],[sigZ]]
#syst["autoMCstat"] = ["shape"]
#syst["autoMCstat"] = ["shape",["SingleTop"]]
syst["autoMCstat"] = ["shape",[sigZ,sigTTW,"SingleTop"]]






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


#sigpoints = [vec1, vec2, vec3, vec4, vec5, vec6, vec7, vec8, vec9, vec10, vec11, vec12, vec13, vec14, vec15, vec16, vec17, vec18, vec19, vec20, vec21, vec22, vec23, vec24, vec25, vec26, vec27, vec28, vec29, vec30, vec31, vec32, vec33, vec34, vec35, vec36, vec37, vec38, vec39, vec40, vec41]

sigpoints = [ vec4, vec5, vec6, vec7, vec8, vec9, vec10, vec11]
sigpoints = [ vec1, vec3, vec4, vec5, vec6, vec7, vec8, vec9, vec11]
sigpoints = [ vec2, vec6, vec10]
#sigpoints = [ vec11]

#sigpoints = [vec1]

