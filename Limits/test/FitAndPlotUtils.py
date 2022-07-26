import os
import ROOT
from Stat.Limits.variables import *
#from Stat.Limits.settings import syst, systgroups
import importlib
import sys
import optparse

LineWrite = lambda fname, s : fname.write(s + "\n") 

colors = ["920", "632", "416", "600", "400", "616", "432", "800", "820", "840", "860", "880", "900"]



def WriteSett(srvar, crvar, folder, model, cut, year = "2016M,2017,2018"):
    settname = open("../python/settings_" + model + "_" + srvar + "_" + crvar + ".py", "w")
    LineWrite(settname, "import collections")
    LineWrite(settname, "import copy")
    LineWrite(settname, "def cutToTag(cut):")
    LineWrite(settname, "\tnewstring = cut.replace('-', 'neg').replace('>=','_GE_').replace('>','_G_').replace(' ','').replace('&&','_AND_').replace('||','_OR_').replace('<=','_LE_').replace('<','_L_').replace('.','p').replace('(','').replace(')','').replace('==','_EQ_').replace('!=','_NEQ_').replace('=','_EQ_').replace('*','_AND_').replace('+','_OR_')")
    LineWrite(settname, "\treturn newstring")
    LineWrite(settname, "#*********************************")
    LineWrite(settname, "#                                *")
    LineWrite(settname, "#       List of channels         *")
    LineWrite(settname, "#                                *")
    LineWrite(settname, "#*********************************")
    LineWrite(settname, "hist_pre = 'h_'")
    LineWrite(settname, "")
    LineWrite(settname, "setfile = open('/afs/cern.ch/work/a/apiccine/CMSSW_10_2_13/src/Stat/Limits/python/metasett_" + model + "_" + srvar + "_" + crvar + ".txt', 'r')")
    LineWrite(settname, "setlist = [line.replace('\\n', '') for line in setfile.readlines()]")
    LineWrite(settname, "sr_var, cr_var = setlist[0].split(',')")
    LineWrite(settname, "intfolder = setlist[1]")
    LineWrite(settname, "model = setlist[2]")
    LineWrite(settname, "cut = setlist[4]")
    LineWrite(settname, "")
    LineWrite(settname, "print sr_var, cr_var, intfolder, cut")
    LineWrite(settname, "")
    LineWrite(settname, "shapesyst = ''")
    LineWrite(settname, "if model.startswith('c') or model.startswith('F'):")
    LineWrite(settname, "\tshapesyst = 'shape'")
    LineWrite(settname, "else:")
    LineWrite(settname, "\tshapesyst = 'shape'")
    LineWrite(settname, "")
    if "UL" in folder:
        LineWrite(settname, "dyjets_sample = 'DYJetsToLL_FxFx'")
        LineWrite(settname, "triboson_sample = 'Triboson'")
    else:
        LineWrite(settname, "dyjets_sample = 'DYJetsToLL'")
        LineWrite(settname, "triboson_sample = 'Other'")
    LineWrite(settname, "")
    LineWrite(settname, "### List of histos to include in the root files")
    LineWrite(settname, "histos = {")
    LineWrite(settname, "\t'SR':hist_pre + sr_var + '_SR',")
    LineWrite(settname, "\t'CRTT':hist_pre + cr_var + '_ttbar_CR',")
    LineWrite(settname, "\t'CRWS':hist_pre + cr_var + '_OS_CR_bvetoL',")
    LineWrite(settname, "\t'CRF':hist_pre + cr_var + '_fakes_CR',")                                                                                        
    LineWrite(settname, "}")
    LineWrite(settname, "")
    LineWrite(settname, "if cut != 'not':")
    LineWrite(settname, "\tcuttag = '_AND_' + cutToTag(cut)")
    LineWrite(settname, "\tfor kh, vh in histos.items():")
    LineWrite(settname, "\t\thistos[kh] = vh + cuttag")
    LineWrite(settname, "else:")
    LineWrite(settname, "\tcuttag = ''")
    LineWrite(settname, "")
    LineWrite(settname, "### List of regions for which creating the datacards")
    LineWrite(settname, "channels = [")
    LineWrite(settname, "\t'SR_muon',")
    LineWrite(settname, "\t'CRTT_muon',")
    LineWrite(settname, "\t'CRWS_muon',")
    LineWrite(settname, "\t'CRF_muon',")
    LineWrite(settname, "\t'SR_electron',")
    LineWrite(settname, "\t'CRTT_electron',")
    LineWrite(settname, "\t'CRWS_electron',")
    LineWrite(settname, "\t'CRF_electron',")
    LineWrite(settname, "]")
    LineWrite(settname, "")
    LineWrite(settname, "leptons = [")
    LineWrite(settname, "\t\'muon\',")
    LineWrite(settname, "\t\'electron\',")
    LineWrite(settname, "]")
    LineWrite(settname, "")
    LineWrite(settname, "channels_labels = {")
    LineWrite(settname, "\t'SR':'Signal Region',")
    LineWrite(settname, "\t'CRWS':'Opposite Sign CR',")
    LineWrite(settname, "\t'CRTT':'t#bar{t} CR',")
    LineWrite(settname, "\t'CRF':'Fake leptons CR',")
    LineWrite(settname, "}")
    LineWrite(settname, "")
    LineWrite(settname, "#*********************************")
    LineWrite(settname, "#                                *")
    LineWrite(settname, "#       List of backgrounds      *")
    LineWrite(settname, "#                                *")
    LineWrite(settname, "#*********************************")
    LineWrite(settname, "")
    LineWrite(settname, "bkg = [")
    LineWrite(settname, "\t'WpWpJJ_QCD',")
    LineWrite(settname, "\t'VBS_SSWW_SM',")
    LineWrite(settname, "\t'VBS_SSWW_LL_SM',")
    LineWrite(settname, "\t'VBS_SSWW_TL_SM',")
    LineWrite(settname, "\t'VBS_SSWW_TT_SM',")
    LineWrite(settname, "\t'ZZtoLep',")
    LineWrite(settname, "\ttriboson_sample,")
    LineWrite(settname, "\t'TVX',")
    LineWrite(settname, "\t'VG',")
    LineWrite(settname, "\t'WZ',")
    LineWrite(settname, "\t'WrongSign',")
    LineWrite(settname, "\tdyjets_sample,")
    LineWrite(settname, "\t'TTTo2L2Nu',")
    LineWrite(settname, "\t'Fake',")
    LineWrite(settname, "]")
    LineWrite(settname, "")

    LineWrite(settname, "class rateParam(object):")
    LineWrite(settname, "\tpass")
    LineWrite(settname, "rateParams = collections.OrderedDict()")
    LineWrite(settname, "")

    LineWrite(settname, "FakeMu_rate_2016M = rateParam()")
    LineWrite(settname, "FakeMu_rate_2016M.chs = [")
    LineWrite(settname, "\t'SR_muon',")
    LineWrite(settname, "\t'CRF_muon',")
    LineWrite(settname, "]")
    LineWrite(settname, "FakeMu_rate_2016M.bkg = 'Fake'")
    LineWrite(settname, "")
    LineWrite(settname, "FakeEle_rate_2016M = rateParam()")
    LineWrite(settname, "FakeEle_rate_2016M.chs = [")
    LineWrite(settname, "\t'SR_electron',")
    LineWrite(settname, "\t'CRF_electron',")
    LineWrite(settname, "]")
    LineWrite(settname, "FakeEle_rate_2016M.bkg = 'Fake'")
    LineWrite(settname, "")

    LineWrite(settname, "TTbarmu_rate_2016M = rateParam()")
    LineWrite(settname, "TTbarmu_rate_2016M.chs = [")
    LineWrite(settname, "\t'SR_muon',")
    LineWrite(settname, "\t'CRTT_muon',")
    LineWrite(settname, "]")
    LineWrite(settname, "TTbarmu_rate_2016M.bkg = 'TTTo2L2Nu'")
    LineWrite(settname, "")
    LineWrite(settname, "TTbarele_rate_2016M = rateParam()")
    LineWrite(settname, "TTbarele_rate_2016M.chs = [")
    LineWrite(settname, "\t'SR_electron',")
    LineWrite(settname, "\t'CRTT_electron',")
    LineWrite(settname, "]")
    LineWrite(settname, "TTbarele_rate_2016M.bkg = 'TTTo2L2Nu'")
    LineWrite(settname, "")

    LineWrite(settname, "DYmu_rate_2016M = rateParam()")
    LineWrite(settname, "DYmu_rate_2016M.chs = [")
    LineWrite(settname, "\t'SR_muon',")
    LineWrite(settname, "\t'CRWS_muon',")
    LineWrite(settname, "]")
    LineWrite(settname, "DYmu_rate_2016M.bkg = dyjets_sample")
    LineWrite(settname, "")
    LineWrite(settname, "DYele_rate_2016M = rateParam()")
    LineWrite(settname, "DYele_rate_2016M.chs = [")
    LineWrite(settname, "\t'SR_electron',")
    LineWrite(settname, "\t'CRWS_electron',")
    LineWrite(settname, "]")
    LineWrite(settname, "DYele_rate_2016M.bkg = dyjets_sample")
    LineWrite(settname, "")

    LineWrite(settname, "FakeMu_rate_2017 = rateParam()")
    LineWrite(settname, "FakeMu_rate_2017.chs = [")
    LineWrite(settname, "\t'SR_muon',")
    LineWrite(settname, "\t'CRF_muon',")
    LineWrite(settname, "]")
    LineWrite(settname, "FakeMu_rate_2017.bkg = 'Fake'")
    LineWrite(settname, "")
    LineWrite(settname, "FakeEle_rate_2017 = rateParam()")
    LineWrite(settname, "FakeEle_rate_2017.chs = [")
    LineWrite(settname, "\t'SR_electron',")
    LineWrite(settname, "\t'CRF_electron',")
    LineWrite(settname, "]")
    LineWrite(settname, "FakeEle_rate_2017.bkg = 'Fake'")
    LineWrite(settname, "")

    LineWrite(settname, "TTbarmu_rate_2017 = rateParam()")
    LineWrite(settname, "TTbarmu_rate_2017.chs = [")
    LineWrite(settname, "\t'SR_muon',")
    LineWrite(settname, "\t'CRTT_muon',")
    LineWrite(settname, "]")
    LineWrite(settname, "TTbarmu_rate_2017.bkg = 'TTTo2L2Nu'")
    LineWrite(settname, "")
    LineWrite(settname, "TTbarele_rate_2017 = rateParam()")
    LineWrite(settname, "TTbarele_rate_2017.chs = [")
    LineWrite(settname, "\t'SR_electron',")
    LineWrite(settname, "\t'CRTT_electron',")
    LineWrite(settname, "]")
    LineWrite(settname, "TTbarele_rate_2017.bkg = 'TTTo2L2Nu'")
    LineWrite(settname, "")

    LineWrite(settname, "DYmu_rate_2017 = rateParam()")
    LineWrite(settname, "DYmu_rate_2017.chs = [")
    LineWrite(settname, "\t'SR_muon',")
    LineWrite(settname, "\t'CRWS_muon',")
    LineWrite(settname, "]")
    LineWrite(settname, "DYmu_rate_2017.bkg = dyjets_sample")
    LineWrite(settname, "")
    LineWrite(settname, "DYele_rate_2017 = rateParam()")
    LineWrite(settname, "DYele_rate_2017.chs = [")
    LineWrite(settname, "\t'SR_electron',")
    LineWrite(settname, "\t'CRWS_electron',")
    LineWrite(settname, "]")
    LineWrite(settname, "DYele_rate_2017.bkg = dyjets_sample")
    LineWrite(settname, "")

    LineWrite(settname, "FakeMu_rate_2018 = rateParam()")
    LineWrite(settname, "FakeMu_rate_2018.chs = [")
    LineWrite(settname, "\t'SR_muon',")
    LineWrite(settname, "\t'CRF_muon',")
    LineWrite(settname, "]")
    LineWrite(settname, "FakeMu_rate_2018.bkg = 'Fake'")
    LineWrite(settname, "")
    LineWrite(settname, "FakeEle_rate_2018 = rateParam()")
    LineWrite(settname, "FakeEle_rate_2018.chs = [")
    LineWrite(settname, "\t'SR_electron',")
    LineWrite(settname, "\t'CRF_electron',")
    LineWrite(settname, "]")
    LineWrite(settname, "FakeEle_rate_2018.bkg = 'Fake'")
    LineWrite(settname, "")

    LineWrite(settname, "TTbarmu_rate_2018 = rateParam()")
    LineWrite(settname, "TTbarmu_rate_2018.chs = [")
    LineWrite(settname, "\t'SR_muon',")
    LineWrite(settname, "\t'CRTT_muon',")
    LineWrite(settname, "]")
    LineWrite(settname, "TTbarmu_rate_2018.bkg = 'TTTo2L2Nu'")
    LineWrite(settname, "")
    LineWrite(settname, "TTbarele_rate_2018 = rateParam()")
    LineWrite(settname, "TTbarele_rate_2018.chs = [")
    LineWrite(settname, "\t'SR_electron',")
    LineWrite(settname, "\t'CRTT_electron',")
    LineWrite(settname, "]")
    LineWrite(settname, "TTbarele_rate_2018.bkg = 'TTTo2L2Nu'")
    LineWrite(settname, "")

    LineWrite(settname, "DYmu_rate_2018 = rateParam()")
    LineWrite(settname, "DYmu_rate_2018.chs = [")
    LineWrite(settname, "\t'SR_muon',")
    LineWrite(settname, "\t'CRWS_muon',")
    LineWrite(settname, "]")
    LineWrite(settname, "DYmu_rate_2018.bkg = dyjets_sample")
    LineWrite(settname, "")
    LineWrite(settname, "DYele_rate_2018 = rateParam()")
    LineWrite(settname, "DYele_rate_2018.chs = [")
    LineWrite(settname, "\t'SR_electron',")
    LineWrite(settname, "\t'CRWS_electron',")
    LineWrite(settname, "]")
    LineWrite(settname, "DYele_rate_2018.bkg = dyjets_sample")
    LineWrite(settname, "")

    LineWrite(settname, "rateParams['FRest_muon_2016M'] = FakeMu_rate_2016M")
    LineWrite(settname, "rateParams['FRest_electron_2016M'] = FakeEle_rate_2016M")
    LineWrite(settname, "rateParams['FRest_muon_2017'] = FakeMu_rate_2017")
    LineWrite(settname, "rateParams['FRest_electron_2017'] = FakeEle_rate_2017")
    LineWrite(settname, "rateParams['FRest_muon_2018'] = FakeMu_rate_2018")
    LineWrite(settname, "rateParams['FRest_electron_2018'] = FakeEle_rate_2018")
    LineWrite(settname, "")

    LineWrite(settname, "rateParams['TTest_muon_2016M'] = TTbarmu_rate_2016M")
    LineWrite(settname, "rateParams['TTest_electron_2016M'] = TTbarele_rate_2016M")
    LineWrite(settname, "rateParams['TTest_muon_2017'] = TTbarmu_rate_2017")
    LineWrite(settname, "rateParams['TTest_electron_2017'] = TTbarele_rate_2017")
    LineWrite(settname, "rateParams['TTest_muon_2018'] = TTbarmu_rate_2018")
    LineWrite(settname, "rateParams['TTest_electron_2018'] = TTbarele_rate_2018")
    LineWrite(settname, "")

    LineWrite(settname, "rateParams['DYest_muon_2016M'] = DYmu_rate_2016M")
    LineWrite(settname, "rateParams['DYest_electron_2016M'] = DYele_rate_2016M")
    LineWrite(settname, "rateParams['DYest_muon_2017'] = DYmu_rate_2017")
    LineWrite(settname, "rateParams['DYest_electron_2017'] = DYele_rate_2017")
    LineWrite(settname, "rateParams['DYest_muon_2018'] = DYmu_rate_2018")
    LineWrite(settname, "rateParams['DYest_electron_2018'] = DYele_rate_2018")
    LineWrite(settname, "")

    LineWrite(settname, "#*********************************")
    LineWrite(settname, "#                                *")
    LineWrite(settname, "#       List of systematics      *")
    LineWrite(settname, "#                                *")
    LineWrite(settname, "#*********************************")
    LineWrite(settname, "")
    LineWrite(settname, "syst = collections.OrderedDict()")
    LineWrite(settname, "")
    LineWrite(settname, "syst['lumi_2016M'] = ['lnN', 'all', 1.012]")
    LineWrite(settname, "syst['lumi_2017'] = ['lnN', 'all', 1.023]")
    LineWrite(settname, "syst['lumi_2018'] = ['lnN', 'all', 1.025]")
    LineWrite(settname, "syst['FR_sys_muon_2016M'] = ['lnN', 'Fake', 1.3]")
    LineWrite(settname, "syst['FR_sys_electron_2016M'] = ['lnN', 'Fake', 1.3]")
    LineWrite(settname, "syst['FR_sys_muon_2017'] = ['lnN', 'Fake', 1.3]")
    LineWrite(settname, "syst['FR_sys_electron_2017'] = ['lnN', 'Fake', 1.3]")
    LineWrite(settname, "syst['FR_sys_muon_2018'] = ['lnN', 'Fake', 1.3]")
    LineWrite(settname, "syst['FR_sys_electron_2018'] = ['lnN', 'Fake', 1.3]")
    LineWrite(settname, "syst['autoMCstat'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'Fake', 'sig'), 'uncorr']")
    LineWrite(settname, "syst['PF'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['pu'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['puID'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['lep'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'uncorr']")
    LineWrite(settname, "syst['btag'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['mistag'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['tau_vsjet'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'uncorr']")
    LineWrite(settname, "syst['tau_vsele'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'uncorr']")
    LineWrite(settname, "syst['tau_vsmu'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'uncorr']")
    LineWrite(settname, "syst['pdf_total'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['QCDScale'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['ISR'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['FSR'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['jes'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['jer'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'uncorr']")
    LineWrite(settname, "syst['TES'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['FES'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['VBS'] = [shapesyst, ('WpWpJJ_QCD', 'sig'), 'uncorr']")
    LineWrite(settname, "")

    LineWrite(settname, "systgroups = collections.OrderedDict()")
    LineWrite(settname, "")
    LineWrite(settname, "rpname=''")
    LineWrite(settname, "for idk, krp in enumerate(rateParams.keys()):")
    LineWrite(settname, "\tif idk%6 == 0:")
    LineWrite(settname, "\t\trpname = ''")
    LineWrite(settname, "\t\trpname = krp.split('_')[0].replace('est', 'norm group')")
    LineWrite(settname, "\t\tsystgroups[rpname] = [krp]")
    LineWrite(settname, "\telse:")
    LineWrite(settname, "\t\tsystgroups[rpname].append(krp)")
    LineWrite(settname, "")
    
    LineWrite(settname, "systgroups['FRsys group'] = ['FR_sys_muon_2016M', 'FR_sys_electron_2016M', 'FR_sys_muon_2017', 'FR_sys_electron_2017', 'FR_sys_muon_2018', 'FR_sys_electron_2018']")
    LineWrite(settname, "systgroups['theory group'] = ['ISR', 'FSR', 'QCDScale', 'pdf_total']")
    LineWrite(settname, "systgroups['btag group'] = ['btag', 'mistag']")
    LineWrite(settname, "systgroups['Pileup group'] = ['pu', 'puID']")
    LineWrite(settname, "systgroups['jet group'] = ['jes', 'jer']")
    LineWrite(settname, "systgroups['PF group'] = ['PF']")
    LineWrite(settname, "systgroups['tau group'] = ['TES', 'FES', 'tau_vsjet', 'tau_vsele', 'tau_vsmu']")
    LineWrite(settname, "systgroups['lumi group'] = ['lumi_2016M', 'lumi_2017', 'lumi_2018']")
    LineWrite(settname, "systgroups['lepton group'] = ['lep', 'PF']")
    LineWrite(settname, "systgroups['VBS group'] = ['VBS']")
    LineWrite(settname, "")
    
    LineWrite(settname, "years = setlist[3].split(',')")
    LineWrite(settname, "")

    LineWrite(settname, "#*********************************")
    LineWrite(settname, "#                                *")
    LineWrite(settname, "#         List of signals        *")
    LineWrite(settname, "#                                *")
    LineWrite(settname, "#*********************************")
    LineWrite(settname, "")

    LineWrite(settname, "if ':' in model and not model.startswith('WpWp'):")
    LineWrite(settname, "\tops = model.split(':')")
    LineWrite(settname, "\tsetpiecs = []")
    LineWrite(settname, "\tfor op in ops:")
    LineWrite(settname, "\t\tif len(op.split('_')) > 1:")
    LineWrite(settname, "\t\t\tsetpiecs.append(('_')+op.split('_')[-1])")
    LineWrite(settname, "\tcombo = copy.deepcopy(model)")
    LineWrite(settname, "\tfor setpiec in setpiecs:")
    LineWrite(settname, "\t\tcombo = combo.replace(setpiec, \"\")")
    LineWrite(settname, "\tsigs = [")
    LineWrite(settname, "\t\t'SM',")
    LineWrite(settname, "\t]")
    LineWrite(settname, "\tfor op in ops:")
    LineWrite(settname, "\t\tsigs.append(op + '_SM')")
    LineWrite(settname, "\t\tsigs.append(op + '_BSM')")
    LineWrite(settname, "")
    LineWrite(settname, "\tlssamples_1D = {")
    LineWrite(settname, "\t\tcombo:collections.OrderedDict([])")
    LineWrite(settname, "\t}")
    LineWrite(settname, "\tlssamples_1D[combo]['sm'] = 'VBS_SSWW_SM'")
    LineWrite(settname, "\tfor idop, op in enumerate(ops):")
    LineWrite(settname, "\t\tlssamples_1D[combo]['sm_lin_quad_'+op.split('_')[0]] = 'VBS_SSWW_' + sigs[1+idop*2]")
    LineWrite(settname, "\t\tif op.startswith('F'):")
    LineWrite(settname, "\t\t\tlssamples_1D[combo]['sm_lin_quad_'+op.split('_')[0]] += ',VBS_SSWW_' + sigs[2*(1+idop)]")
    LineWrite(settname, "\t\tlssamples_1D[combo]['quad_'+op.split('_')[0]] = 'VBS_SSWW_' + sigs[2*(1+idop)]")
    LineWrite(settname, "\t\tfor idothop in range(0, idop):")
    LineWrite(settname, "\t\t\tlssamples_1D[combo]['quad_mixed_'+op.split('_')[0]+'_'+ops[idothop].split('_')[0]] = 'VBS_SSWW_' + sigs[2*(1+idop)] + ',VBS_SSWW_' + sigs[2*(1+idothop)]")
    LineWrite(settname, "\t\t\tlssamples_1D[combo]['quad_mixed_'+op.split('_')[0]+'_'+ops[idothop].split('_')[0]] = 'VBS_SSWW_' + sigs[2*(1+idop)] + ',VBS_SSWW_' + sigs[2*(1+idothop)]")
    LineWrite(settname, "\t\t\tif not op.startswith('F') and not ops[idothop].startswith('F'):")
    LineWrite(settname, "\t\t\t\tlssamples_1D[combo]['quad_mixed_'+op.split('_')[0]+'_'+ops[idothop].split('_')[0]] += ',VBS_SSWW_' + op + '_' + ops[idothop] + ',VBS_SSWW_' + ops[idothop] + '_' + op")
    LineWrite(settname, "")
    LineWrite(settname, "elif ':' in model and model.startswith('WpWp'):")
    LineWrite(settname, "\tsigs = model.split(':')")
    LineWrite(settname, "\tlssamples_1D = {")
    LineWrite(settname, "\t\tmodel:collections.OrderedDict([")
    LineWrite(settname, "\t\t\t('sm', sigs[0]),")
    LineWrite(settname, "\t\t\t('sm_lin_quad_cW', sigs[0]),")
    LineWrite(settname, "\t\t\t('quad_cW', sigs[0]),")
    LineWrite(settname, "\t\t]),")
    LineWrite(settname, "\t}")
    LineWrite(settname, "")
    LineWrite(settname, "elif model.endswith('SM'):")
    LineWrite(settname, "\tsigs = [model]")
    LineWrite(settname, "\tlssamples_1D = {")
    LineWrite(settname, "\t\tmodel:collections.OrderedDict([")
    LineWrite(settname, "\t\t\t('sm', 'VBS_SSWW_' + sigs[0]),")
    LineWrite(settname, "\t\t\t('sm_lin_quad_cW', 'VBS_SSWW_' + sigs[0]),")
    LineWrite(settname, "\t\t\t('quad_cW', 'VBS_SSWW_' + sigs[0]),")
    LineWrite(settname, "\t\t]),")
    LineWrite(settname, "\t}")
    LineWrite(settname, "")
    LineWrite(settname, "elif model.startswith('c'):")
    LineWrite(settname, "\tsigs = [")
    LineWrite(settname, "\t\t'SM',")
    LineWrite(settname, "\t\tmodel + '_SM',")
    LineWrite(settname, "\t\tmodel + '_BSM',")
    LineWrite(settname, "\t]")
    LineWrite(settname, "\tlssamples_1D = {")
    LineWrite(settname, "\t\tmodel:collections.OrderedDict([")
    LineWrite(settname, "\t\t\t('sm', 'VBS_SSWW_' + sigs[0]),")
    LineWrite(settname, "\t\t\t('sm_lin_quad_' + model, 'VBS_SSWW_' + sigs[1]),")
    LineWrite(settname, "\t\t\t('quad_' + model, 'VBS_SSWW_' + sigs[2]),")
    LineWrite(settname, "\t\t]),")
    LineWrite(settname, "\t}")
    LineWrite(settname, "")
    LineWrite(settname, "elif model.startswith('F'):")
    LineWrite(settname, "\tsigs = [")
    LineWrite(settname, "\t\tmodel + '_0',")
    LineWrite(settname, "\t\tmodel + '_SM',")
    LineWrite(settname, "\t\tmodel + '_BSM',")
    LineWrite(settname, "\t]")
    LineWrite(settname, "\tlssamples_1D = {")
    LineWrite(settname, "\t\tmodel.split(\"_\")[0]:collections.OrderedDict([")
    LineWrite(settname, "\t\t\t('sm', 'VBS_SSWW_' + sigs[0]),")
    LineWrite(settname, "\t\t\t('sm_lin_quad_' + model, 'VBS_SSWW_' + sigs[1]),")
    LineWrite(settname, "\t\t\t('quad_' + model, 'VBS_SSWW_' + sigs[2]),")
    LineWrite(settname, "\t\t]),")
    LineWrite(settname, "\t}")
    LineWrite(settname, "")
    LineWrite(settname, "elif model.startswith('WpWp'):")
    LineWrite(settname, "\tsigs = [model]")
    LineWrite(settname, "\tlssamples_1D = {")
    LineWrite(settname, "\t\tmodel:collections.OrderedDict([")
    LineWrite(settname, "\t\t\t('sm', sigs[0]),")
    LineWrite(settname, "\t\t\t('sm_lin_quad_'+model, sigs[0]),")
    LineWrite(settname, "\t\t\t('quad_'+model, sigs[0]),")
    LineWrite(settname, "\t\t]),")
    LineWrite(settname, "\t}")
    LineWrite(settname, "else:")
    LineWrite(settname, "\traise RuntimeError('Warning! Please insert valid model!')")
    LineWrite(settname, "")

    LineWrite(settname, "sigpoints = [sigs]")

def WriteMeta(srvar, crvar, folder, model, cut, year = "2016M,2017,2018"):
    metasett = open("../python/metasett_" + model + "_" + srvar + "_" + crvar + ".txt", "w")
    LineWrite(metasett, srvar + "," + crvar)
    LineWrite(metasett, folder)
    LineWrite(metasett, model)
    LineWrite(metasett, year)
    LineWrite(metasett, cut)
    metasett.close()

def RecursiveImport(module):
    if module in sys.modules:
        del sys.modules[module]
    globals()['gensettings'] = importlib.import_module(module)
    
def AreVarsIncluded(varlist):
    varexcluded = ""
    for potvar in varlist:
        IsIncluded = False
        for variable in variables:
            if potvar == variable.name:
                IsIncluded = True
                print potvar, "is acceptable as variable to fit!"
                break
        if not IsIncluded:
            varexcluded = potvar
            return False, varexcluded
        else:
            return True, varexcluded

def IterateVars(srvarlist, crvarlist):
    print srvarlist, crvarlist
    fitvars = srvarlist.split(",")
    if not AreVarsIncluded(fitvars)[0]:
        raise RuntimeError(AreVarsIncluded(fitvars)[1] + " are not included in the variables! Please either insert it among the variables, or change it!")

    crvars = []
    if crvarlist == "same":
        for fitvar in fitvars:
            crvars.append(fitvar)
    else:
        crvars = crvarlist.split(",")
        if len(fitvars)!=len(crvars):
            raise RuntimeError("Number of variables for CRs (" + len(crvars) + ") must be equal to the number of variables for SR (" + len(fitvars) + ")!")

    if not AreVarsIncluded(crvars)[0]:
        raise RuntimeError(AreVarsIncluded(crvars)[1] + " is not included in the variables! Please either insert it among the variables, or change it!")

    return zip(fitvars, crvars)

def PrepareToRun(model, srvar, crvar, fold, year = "2016M,2017,2018"):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag
    os.system("python PrepareEOSfolder.py " + fold + " " + model + "_" + srvar + "_" + crvar)
    os.system("rm histo_" + folder + "_" + model + ".root")

def RunSMSignificance(model, srvar, crvar, fold, year = "2016M,2017,2018", username = "apiccine"):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/plot/'
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag
    
    try:
        os.system("python collectHistos.py -i " + plotrepo + " -o histo_" + folder + "_" + model + ".root --model " + model + "_" + srvar + "_" + crvar)
    except:
        raise RuntimeError("Problems when collecting histos for the fit")
    os.system("python createDatacards.py -i  histo_" + folder + "_" + model + ".root -d " + folder + " --model " + model + "_" + srvar + "_" + crvar)
    os.system("python runCombine.py -y " + year + " -d " + folder + " -m hist --model " + model + "_" + srvar + "_" + crvar)

def RunEWvsQCD(model, srvar, crvar, fold, year = "2016M,2017,2018", username = "apiccine"):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/plot/'
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag
    
    try:
        os.system("python collectHistos.py -i " + plotrepo + " -o histo_" + folder + "_" + model + ".root")
    except:
        raise RuntimeError("Problems when collecting histos for the fit")
    os.system("python createDatacards.py -i  histo_" + folder + "_" + model + ".root -d " + folder + " --model " + model)
    
    os.system("python runCombine.py -y " + year + " -d " + folder + " -m hist --EWvsQCD --model " + model)

def RunEFTFit(model, srvar, crvar, fold, year = "2016M,2017,2018", username = "apiccine"):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/plot/'
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag

    os.system("python collectHistos.py -i " + plotrepo + " -o histo_" + folder + "_" + model + ".root --ls " + model + " --model " + model + "_" + srvar + "_" + crvar)
    os.system("python createDatacards.py -i histo_" + folder + "_" + model + ".root -d " + folder + " --ls " + model + " --model " + model + "_" + srvar + "_" + crvar)
    os.system("python runCombine.py -y " + year + " -d " + folder + " -m hist --ls " + model + " --model " + model + "_" + srvar + "_" + crvar)
    
def DoImpacts(model, srvar, crvar, fold, year = "2016M,2017,2018", username = "apiccine"):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    ipwd = os.getcwd()
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag
    if model == "SM":
        dcname = "VBS_SSWW_SM_hist"
        dcpath = ipwd + "/" + folder + "/VBS_SSWW_SM/" + dcname + ".txt"
    else:
        dcname = model + "_hist"
        dcpath = ipwd + "/" + folder + "/" + model + "/" + dcname + ".txt"

    impactfolder = ipwd + "/" + folder + "/Checks_" + model + "/"
    if not os.path.exists(impactfolder):
        os.system("mkdir " + impactfolder)
    wscard = impactfolder + dcname + ".root"
    tag = model + "_" + srvar + "_" + crvar
    os.chdir(impactfolder)
    os.system("text2workspace.py " + dcpath + " -o " + wscard)

    os.system("combine -M FitDiagnostics -d " + wscard + " -t -1 --robustFit 1 --expectSignal 0 --rMin 0.01  --cminDefaultMinimizerStrategy 0 -n " + tag + "_t0")
    os.system("python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py -a fitDiagnostics" + tag + "_t0.root -g plots" + tag + "_t0.root >> " + impactfolder + "fitResults" + tag + "_t0.log")

    os.system("combine -M FitDiagnostics -d " + wscard + " -t -1 --robustFit 1 --expectSignal 1 --rMin 0.001 --cminDefaultMinimizerStrategy 0 -n " + tag + "_t1")
    os.system("python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics" + tag + "_t1.root -g plots" + tag + "_t1.root >> "+ impactfolder + "fitResults" + tag + "_t1.log")

    os.system("combineTool.py -M Impacts -d " + wscard + " -t -1 --robustFit 1 --expectSignal 0 --rMin 0.01 --doInitialFit --allPars -m 1 -n " + tag + "_t0 --parallel 10")

    os.system("combineTool.py -M Impacts -d " + wscard + " -t -1 --robustFit 1 --expectSignal 1 --rMin 0.01 --doInitialFit --allPars -m 1 -n " + tag + "_t1 --parallel 10")

    os.system("combineTool.py -M Impacts -d " + wscard + " -o " + impactfolder + "impacts" + tag + "_t0.json -t -1 --robustFit 1 --expectSignal 0 --rMin 0.01 --doFits -m 1 -n " + tag + "_t0 --parallel 10")
    os.system("combineTool.py -M Impacts -d " + wscard + " -o " + impactfolder + "impacts" + tag + "_t1.json -t -1 --robustFit 1 --expectSignal 1 --rMin 0.01 --doFits -m 1 -n " + tag + "_t1 --parallel 10")

    os.system("combineTool.py -M Impacts -d " + wscard + " -m 1 -n " + tag + "_t0 -o " + impactfolder + "impacts" + tag + "_t0.json --parallel 10")
    os.system("combineTool.py -M Impacts -d " + wscard + " -m 1 -n " + tag + "_t1 -o " + impactfolder + "impacts" + tag + "_t1.json --parallel 10")

    os.system("plotImpacts.py -i " + impactfolder + "impacts" + tag + "_t0.json -o " + impactfolder + "impacts" + tag + "_t0")
    os.system("plotImpacts.py -i " + impactfolder + "impacts" + tag + "_t1.json -o " + impactfolder + "impacts" + tag + "_t1")

    os.chdir(ipwd)
    #os.system("mv higgsCombine*" + tag + "* " + impactfolder)
    #os.system("mv fitDiagnostics" + tag + "_t* plots" + tag + "_t* combine_logger_" + model + ".out " + impactfolder)
    
def PrepareAndDoPostFit(model, srvar, crvar, plotvars, fold, cut, year = "2016M,2017,2018", username = "apiccine", unblind = False):
    pwd = os.getcwd()
    vartopost = []
    yeartag = year.replace("2016M,2017,2018", "RunII") + "_"
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/plot/'

    if plotvars == "all":
        vartopost = variables
    else:
        for var in variables:
            if var.name in plotvars.split(","):
                vartopost.append(var)
    
    for var in vartopost:
        varname = var.name
        folder = fold + '_' + yeartag + varname
        print varname, folder
    
        WriteMeta(varname, varname, fold, model, cut, year)
        RecursiveImport("Stat.Limits.settings_" + model + "_" + varname + "_" + varname)
    
        #os.system("python PrepareEOSfolder.py " + fold)
        os.system("rm " + yeartag + varname + "_" + model + ".root")
        
        appendix = ""
        
        if not "SM" in model and not model.startswith("WpWp"):
            appendix += " --ls " + model
        
        os.system("python collectHistos.py -i " + plotrepo + " -o " + yeartag + varname + "_" + model + ".root" + appendix + " --model " + model + "_" + varname + "_" + varname)
        os.system("python createDatacards.py -i " + yeartag + varname + "_" + model + ".root -d " + folder + appendix + " --model " + model + "_" + varname + "_" + varname)
        
        WriteMeta(srvar, crvar, fold, model, cut, yeartag[:-1])
        RecursiveImport("Stat.Limits.settings_" + model + "_" + srvar + "_" + crvar)
        os.chdir("postdatacards")
        os.system("python createPostFit.py --vars " + varname + " --folder " + fold + " --year " + year + " --model " + model + " --tag " + model + "_" + srvar + "_" + crvar)
        
        os.chdir("plotter")
    
        poststring = "python PreFitPostFit_v2.py --era " + yeartag[:-1] + " --folder " + fold + " --vars " + var.name + " --fitted " + srvar + "," + crvar + " --model " + model + " --tag " + model + "_" + srvar + "_" + crvar
        if unblind:
            poststring += " -u"
        os.system(poststring)
        os.chdir(pwd)
        
def ProduceCLPlots(srvars, crvars, folder, eftop, era):
    command = "python ciplots.py --sr " + srvars + " --cr " + crvars + " --folder " + folder + " --op " + eftop + " --era " + era
    os.system(command)

def UncBreak(model, srvar, crvar, fold, year = "2016M,2017,2018", username = "apiccine"):
    optionalss = " --robustFit=1 --cminDefaultMinimizerStrategy=0 --setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND"# --fastScan"
    RecursiveImport("Stat.Limits.settings_" + model + "_" + srvar + "_" + crvar)
    settmod = importlib.import_module("Stat.Limits.settings_" + model + "_" + srvar + "_" + crvar)
    systgroups = settmod.systgroups
    syst = settmod.syst
    upwd = os.getcwd()
    yeartag = year.replace("2016M,2017,2018", "RunII")# + "_"
    folder = 'fit_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag
    #file_to_move = []
    years = year.split(",")
    if model == "SM":
        dcname = "VBS_SSWW_SM_hist"
        dcpath = upwd + "/" + folder + "/VBS_SSWW_SM/" + dcname + ".txt"
    else:
        dcname = model + "_hist"
        dcpath = upwd + "/" + folder + "/" + model + "/" + dcname + ".txt"

    with open(dcpath, 'a') as dcfile:
        dcfile.write("\n")
        for systgroup, subsysts in systgroups.items():
            sysrow = systgroup + "\t="
            approw = ""
            for idsy, systname in enumerate(subsysts):
                if "norm " in systgroup:
                    approw += " " + systname
                elif syst[systname][0] == "lnN":
                    approw += " " + systname
                elif syst[systname][0] == "shape":
                    if syst[systname][-1] == "corr":
                        approw += " " + systname
                    elif syst[systname][-1] == "uncorr":
                        for yr in years:
                            approw += " " + systname + "_" + yr
            sysrow += approw
            dcfile.write("\n" + sysrow)
    print "datacard:", dcpath
        
    impactfolder = upwd + "/" + folder + "/Checks_" + model + "/"
    if not os.path.exists(impactfolder):
        os.system("mkdir " + impactfolder)
    wscard = impactfolder + dcname + ".root"
    os.chdir(impactfolder)
    os.system("text2workspace.py " + dcpath + " -o " + wscard)
    
    total = dcname + "_" + model + ".total"
    totalfile = "higgsCombine" + total + ".MultiDimFit.mH120.root"
    #print("combine " + wscard + " -M MultiDimFit -t -1 -m 120 --rMin -2 --rMax 2 --points 200 --saveWorkspace -n " + total + " --algo grid  --cminDefaultMinimizerStrategy 1 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT")
    os.system("combine " + wscard + " -M MultiDimFit -t -1 -m 120 --rMin -5 --rMax 5 --points 10 --saveWorkspace -n " + total + " --algo grid " + optionalss) #"  --cminDefaultMinimizerStrategy 1 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT")
    #file_to_move.append(totalfile)
    
    md = "combine " + totalfile + " -M MultiDimFit -t -1 -m 120 --rMin -5 --rMax 5 --points 10 --algo grid " + optionalss #"--cminDefaultMinimizerStrategy 0 --snapshotName MultiDimFit --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT"
    
    plotcomm = "plot1DScan.py " + totalfile + " --main-label \"Total uncert.\" --others "
    bdstr = " -o freeze_ALL_st_" + model + " --breakdown \""
    freeze = md + " --freezeNuisanceGroups "

    for idsy, systgroup in enumerate(systgroups.keys()):
        groupname = systgroup.split(" ")[0]    
        if idsy > 0:
            if idsy < len(systgroups):# - 1:
                freeze += ","
            bdstr += ","
        bdstr += groupname
        if idsy < len(systgroups):# - 1:
            freeze += groupname
            freezename = dcname + ".freeze_" + groupname + "_" + model
            freezefile = "higgsCombine" + freezename + ".MultiDimFit.mH120.root"
            freezecommand = freeze + " -n " + freezename
            os.system(freezecommand)
            #file_to_move.append(freezefile)
            plotcomm += "\'" + freezefile + ":Freeze " + groupname + ":" + colors[idsy] + "\' "
        
    freezeall = md + " --freezeParameters allConstrainedNuisances -n"
    freezeallname = dcname + ".freeze_all" + "_" + model
    freezeallfile = "higgsCombine" + freezeallname + ".MultiDimFit.mH120.root"
    freezeall += " " + freezeallname
    #print(freezeall)
    os.system(freezeall)
    #file_to_move.append(freezeallfile)
    plotcomm += "\'" + freezeallfile + ":Freeze all:" + colors[len(systgroup)] + "\' "
    bdstr += ",MCstat,Stat\""

    #file_to_move.append("freeze_ALL_st_" + model + ".png")
    #file_to_move.append("freeze_ALL_st_" + model + ".pdf")
    #file_to_move.append("freeze_ALL_st_" + model + ".root")
    plotcomm += bdstr
    os.system(plotcomm)
    os.chdir(upwd)
    #for ftm in file_to_move:
        #os.system("mv ./" + ftm + " " + impactfolder)
