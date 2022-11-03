import os
import ROOT
from Stat.Limits.variables import *
#from Stat.Limits.settings import syst, systgroups
import importlib
import sys
import optparse

LineWrite = lambda fname, s : fname.write(s + "\n") 

colors = ["920", "632", "416", "600", "400", "616", "432", "800", "820", "840", "860", "880", "900", "403","814","435"]

def WriteSett(srvar, crvar, folder, model, cut, year, WithFakeCR, PDFWithTTDY):
    settitle = "../python/settings_" + model + "_" + srvar + "_" + crvar 
    if WithFakeCR:
        settitle += "_WithFakeCR"
    if PDFWithTTDY:
        settitle += "_PDFWithTTDY"
    settitle += ".py"
    settname = open(settitle, "w")
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
    LineWrite(settname, "\tshapesyst = 'shapeN'")
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
    LineWrite(settname, "\t'CRTT':hist_pre + sr_var + '_ttbar_CR',")
    LineWrite(settname, "\t'CRWS':hist_pre + sr_var + '_OS_CR_bvetoL',")
    if WithFakeCR:
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
    if WithFakeCR:
        LineWrite(settname, "\t'CRF_muon',")
    LineWrite(settname, "\t'SR_electron',")
    LineWrite(settname, "\t'CRTT_electron',")
    LineWrite(settname, "\t'CRWS_electron',")
    if WithFakeCR:
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
    if WithFakeCR:
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
    #if WithFakeCR:
        #LineWrite(settname, "FakeMu_rate_2016M = rateParam()")
        #LineWrite(settname, "FakeMu_rate_2016M.chs = [")
        #LineWrite(settname, "\t'SR_muon',")
        #LineWrite(settname, "\t'CRF_muon',")
        #LineWrite(settname, "]")
        #LineWrite(settname, "FakeMu_rate_2016M.bkg = 'Fake'")
        #LineWrite(settname, "")
        #LineWrite(settname, "FakeEle_rate_2016M = rateParam()")
        #LineWrite(settname, "FakeEle_rate_2016M.chs = [")
        #LineWrite(settname, "\t'SR_electron',")
        #LineWrite(settname, "\t'CRF_electron',")
        #LineWrite(settname, "]")
        #LineWrite(settname, "FakeEle_rate_2016M.bkg = 'Fake'")
        #LineWrite(settname, "")
    
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

    if True: #not (model == "SM" or model.startswith("WpWp")):
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
    #if WithFakeCR:
        #LineWrite(settname, "FakeMu_rate_2017 = rateParam()")
        #LineWrite(settname, "FakeMu_rate_2017.chs = [")
        #LineWrite(settname, "\t'SR_muon',")
        #LineWrite(settname, "\t'CRF_muon',")
        #LineWrite(settname, "]")
        #LineWrite(settname, "FakeMu_rate_2017.bkg = 'Fake'")
        #LineWrite(settname, "")
        #LineWrite(settname, "FakeEle_rate_2017 = rateParam()")
        #LineWrite(settname, "FakeEle_rate_2017.chs = [")
        #LineWrite(settname, "\t'SR_electron',")
        #LineWrite(settname, "\t'CRF_electron',")
        #LineWrite(settname, "]")
        #LineWrite(settname, "FakeEle_rate_2017.bkg = 'Fake'")
        #LineWrite(settname, "")

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

    if True: #not (model == "SM" or model.startswith("WpWp")):
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
    #if WithFakeCR:
        #LineWrite(settname, "FakeMu_rate_2018 = rateParam()")
        #LineWrite(settname, "FakeMu_rate_2018.chs = [")
        #LineWrite(settname, "\t'SR_muon',")
        #LineWrite(settname, "\t'CRF_muon',")
        #LineWrite(settname, "]")
        #LineWrite(settname, "FakeMu_rate_2018.bkg = 'Fake'")
        #LineWrite(settname, "")
        #LineWrite(settname, "FakeEle_rate_2018 = rateParam()")
        #LineWrite(settname, "FakeEle_rate_2018.chs = [")
        #LineWrite(settname, "\t'SR_electron',")
        #LineWrite(settname, "\t'CRF_electron',")
        #LineWrite(settname, "]")
        #LineWrite(settname, "FakeEle_rate_2018.bkg = 'Fake'")
        #LineWrite(settname, "")
    
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

    if True: #not (model == "SM" or model.startswith("WpWp")):
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
    #if WithFakeCR:
        #LineWrite(settname, "rateParams['FRest_muon_2016M'] = FakeMu_rate_2016M")
        #LineWrite(settname, "rateParams['FRest_electron_2016M'] = FakeEle_rate_2016M")
        #LineWrite(settname, "rateParams['FRest_muon_2017'] = FakeMu_rate_2017")
        #LineWrite(settname, "rateParams['FRest_electron_2017'] = FakeEle_rate_2017")
        #LineWrite(settname, "rateParams['FRest_muon_2018'] = FakeMu_rate_2018")
        #LineWrite(settname, "rateParams['FRest_electron_2018'] = FakeEle_rate_2018")
        #LineWrite(settname, "")
        
    LineWrite(settname, "rateParams['TTest_muon_2016M'] = TTbarmu_rate_2016M")
    LineWrite(settname, "rateParams['TTest_electron_2016M'] = TTbarele_rate_2016M")
    LineWrite(settname, "rateParams['TTest_muon_2017'] = TTbarmu_rate_2017")
    LineWrite(settname, "rateParams['TTest_electron_2017'] = TTbarele_rate_2017")
    LineWrite(settname, "rateParams['TTest_muon_2018'] = TTbarmu_rate_2018")
    LineWrite(settname, "rateParams['TTest_electron_2018'] = TTbarele_rate_2018")
    LineWrite(settname, "")

    if False:#True: #not (model == "SM" or model.startswith("WpWp")):
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
    LineWrite(settname, "syst['lumi_2016M'] = ['lnN', 'all', 1.016]")
    LineWrite(settname, "syst['lumi_2017'] = ['lnN', 'all', 1.016]")
    LineWrite(settname, "syst['lumi_2018'] = ['lnN', 'all', 1.016]")
    #LineWrite(settname, "syst['FR_sys_muon_2016M'] = ['lnN', 'Fake', 1.3]")
    #LineWrite(settname, "syst['FR_sys_electron_2016M'] = ['lnN', 'Fake', 1.3]")
    #LineWrite(settname, "syst['FR_sys_muon_2017'] = ['lnN', 'Fake', 1.3]")
    #LineWrite(settname, "syst['FR_sys_electron_2017'] = ['lnN', 'Fake', 1.3]")
    #LineWrite(settname, "syst['FR_sys_muon_2018'] = ['lnN', 'Fake', 1.3]")
    #LineWrite(settname, "syst['FR_sys_electron_2018'] = ['lnN', 'Fake', 1.3]")
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
    if PDFWithTTDY:
        LineWrite(settname, "syst['pdf_total'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    else:
        LineWrite(settname, "syst['pdf_total'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    #LineWrite(settname, "syst['QCDScale'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    
    LineWrite(settname, "syst['QCDScale_sig'] = [shapesyst, ('sig'), 'corr']")
    LineWrite(settname, "syst['QCDScale_WpWpJJ_QCD'] = [shapesyst, ('WpWpJJ_QCD'), 'corr']")
    LineWrite(settname, "syst['QCDScale_VG'] = [shapesyst, ('VG'), 'corr']")
    LineWrite(settname, "syst['QCDScale_TVX'] = [shapesyst, ('TVX'), 'corr']")
    LineWrite(settname, "syst['QCDScale_DY'] = [shapesyst, (dyjets_sample), 'corr']")
    LineWrite(settname, "syst['QCDScale_TTdilep'] = [shapesyst, ('TTTo2L2Nu'), 'corr']")
    LineWrite(settname, "syst['QCDScale_WZ'] = [shapesyst, ('WZ'), 'corr']")
    LineWrite(settname, "syst['QCDScale_Triboson'] = [shapesyst, (triboson_sample), 'corr']")
    LineWrite(settname, "syst['QCDScale_WrongSign'] = [shapesyst, ('WrongSign'), 'corr']")
    LineWrite(settname, "syst['QCDScale_ZZtoLep'] = [shapesyst, ('ZZtoLep'), 'corr']")
    
    LineWrite(settname, "syst['ISR'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['FSR'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['jes'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['metUnclust'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', dyjets_sample, 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
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
    
    #LineWrite(settname, "systgroups['FRsys group'] = ['FR_sys_muon_2016M', 'FR_sys_electron_2016M', 'FR_sys_muon_2017', 'FR_sys_electron_2017', 'FR_sys_muon_2018', 'FR_sys_electron_2018']")
    LineWrite(settname, "systgroups['theory group'] = ['ISR', 'FSR', 'QCDScale_sig', 'QCDScale_WpWpJJ_QCD', 'QCDScale_VG', 'QCDScale_TVX', 'QCDScale_DY', 'QCDScale_TTdilep', 'QCDScale_WZ', 'QCDScale_Triboson', 'QCDScale_WrongSign', 'QCDScale_ZZtoLep', 'pdf_total']")
    LineWrite(settname, "systgroups['btag group'] = ['btag', 'mistag']")
    LineWrite(settname, "systgroups['Pileup group'] = ['pu', 'puID']")
    LineWrite(settname, "systgroups['jet group'] = ['jes', 'jer']")
    LineWrite(settname, "systgroups['MET group'] = ['metUnclust']")
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

def PrepareToRun(model, srvar, crvar, fold, year, tagfold, addLambda8, WithFakeCR, PDFWithTTDY): 
    yeartag = year.replace("2016M,2017,2018", "RunII")

    folder = 'fitbis_' + fold + '/' + srvar + '_' + crvar + '_' + yeartag
    if WithFakeCR:
        folder += "_WithFakeCR"
    if PDFWithTTDY:
        folder += "_PDFWithTTDY"
    if tagfold == "":
        tagfold = "none"
        folder += "/nom"
    else:
        folder += "/" + tagfold.replace("_", "")
    if addLambda8:
        folder += "_Lambda8" 

    if not os.path.exists(folder):
        os.system("mkdir -p " + folder)
    #print "python PrepareEOSfolder.py " + fold + " " + model + "_" + srvar + "_" + crvar + " \"" + tagfold + "\""
    os.system("python PrepareEOSfolder.py " + fold + " " + model + "_" + srvar + "_" + crvar + " " + tagfold)
    #os.system("rm histo_" + folder + "_" + model + ".root")

def RunSMSignificance(model, srvar, crvar, fold, year, username, tagfold, WithFakeCR, PDFWithTTDY):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = filerepo + 'plot'
    plotrepo += tagfold + "/"
    
    folder = 'fitbis_' + fold + '/' + srvar + '_' + crvar + '_' + yeartag
    if WithFakeCR:
        folder += "_WithFakeCR"
    if PDFWithTTDY:
        folder += "_PDFWithTTDY"
    if tagfold == "":
        tagfold = "none"
        folder += "/nom"
    else:
        folder +="/" + tagfold.replace("_", "")
    folderhisto = folder + "/shapes"

    collhist = "python collectHistos.py -i " + plotrepo + " -o " + folderhisto + "/histo_" + model + ".root --model " + model + "_" + srvar + "_" + crvar
    createdata = "python createDatacards.py -i " + folderhisto + "/histo_" + model + ".root -d " + folder + " --model " + model + "_" + srvar + "_" + crvar
    runcomb = "python runCombine.py -y " + year + " -d " + folder + " -m hist --model " + model + "_" + srvar + "_" + crvar
    if WithFakeCR:
        collhist += " --WithFakeCR"
        createdata += " --WithFakeCR"
        runcomb += " --WithFakeCR"
    if PDFWithTTDY:
        collhist += " --PDFWithTTDY"
        createdata += " --PDFWithTTDY"
        runcomb += " --PDFWithTTDY"
    
    try:
        os.system(collhist)
    except:
        raise RuntimeError("Problems when collecting histos for the fit")
    
    print createdata
    os.system(createdata)
    os.system(runcomb)

def RunEWvsQCD(model, srvar, crvar, fold, year, username, tagfold, WithFakeCR, PDFWithTTDY):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = filerepo + 'plot'
    plotrepo += tagfold + "/"

    folder = 'fitbis_' + fold + '/' + srvar + '_' + crvar + '_' + yeartag
    if WithFakeCR:
        folder += "_WithFakeCR"
    if PDFWithTTDY:
        folder += "_PDFWithTTDY"
    if tagfold == "":
        tagfold = "none"
        folder += "/nom"
    else:
        folder +="/" + tagfold.replace("_", "")
    folderhisto = folder + "/shapes"

    collhist = "python collectHistos.py -i " + plotrepo + " -o " + folderhisto + "/histo_" + model + ".root --model " + model + "_" + srvar + "_" + crvar
    createdata = "python createDatacards.py -i " + folderhisto + "/histo_" + model + ".root -d " + folder + " --model " + model + "_" + srvar + "_" + crvar
    runcomb = "python runCombine.py -y " + year + " -d " + folder + " -m hist --model " + model + "_" + srvar + "_" + crvar
    if WithFakeCR:
        collhist += " --WithFakeCR"
        createdata += " --WithFakeCR"
        runcomb += " --WithFakeCR"
    if PDFWithTTDY:
        collhist += " --PDFWithTTDY"
        createdata += " --PDFWithTTDY"
        runcomb += " --PDFWithTTDY"

    try:
        os.system(collhist)
    except:
        raise RuntimeError("Problems when collecting histos for the fit")
    os.system(createdata)
    os.system(runcomb)

def RunEFTFit(model, srvar, crvar, fold, year, username, tagfold, addLambda8, WithFakeCR, PDFWithTTDY):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = filerepo + 'plot'
    plotrepo += tagfold + "/"

    folder = 'fitbis_' + fold + '/' + srvar + '_' + crvar + '_' + yeartag
    if WithFakeCR:
        folder += "_WithFakeCR"
    if PDFWithTTDY:
        folder += "_PDFWithTTDY"
    if tagfold == "":
        tagfold = "none"
        folder += "/nom"
    else:
        folder += "/" + tagfold.replace("_", "")
    if addLambda8:
        folder += "_Lambda8"

    folderhisto = folder + "/shapes"

    collhist = "python collectHistos.py -i " + plotrepo + " -o " + folderhisto + "/histo_" + model + ".root --ls " + model + " --model " + model + "_" + srvar + "_" + crvar
    createdata = "python createDatacards.py -i " + folderhisto + "/histo_" + model + ".root -d " + folder + " --ls " + model+ " --model " + model + "_" + srvar + "_" + crvar
    runcomb = "python runCombine.py -y " + year + " -d " + folder + " -m hist --ls " + model + " --model " + model + "_" + srvar + "_" + crvar
    if WithFakeCR:
        collhist += " --WithFakeCR"
        createdata += " --WithFakeCR"
        runcomb += " --WithFakeCR"
    if PDFWithTTDY:
        collhist += " --PDFWithTTDY"
        createdata += " --PDFWithTTDY"
        runcomb += " --PDFWithTTDY"
    if addLambda8:
        collhist += " --Lambda8"
    
    try:
        os.system(collhist)
    except:
        raise RuntimeError("Problems when collecting histos for the fit")
    os.system(createdata)
    os.system(runcomb)
    
def DoImpacts(modeltot, srvar, crvar, fold, year, username, tagfold, addLambda8, WithFakeCR, PDFWithTTDY):
    #optionals = " --cminDefaultMinimizerStrategy=1 --cminDefaultMinimizerTolerance 0.01 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.001 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND "#--fastScan" 
    #optionals = "  " 
    optionals = " --cminDefaultMinimizerStrategy=0 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT"# --cminDefaultMinimizerTolerance 0.01" --stepSize=0.001"# --robustFit=1"
    settitle = "Stat.Limits.settings_" + modeltot + "_" + srvar + "_" + crvar
    if WithFakeCR:
        settitle += "_WithFakeCR"
    if PDFWithTTDY:
        settitle += "_PDFWithTTDY"

    RecursiveImport(settitle)
    settmod = importlib.import_module(settitle)
    systgroups = settmod.systgroups
    syst = settmod.syst
    ipwd = os.getcwd()
    yeartag = year.replace("2016M,2017,2018", "RunII")# + "_"
    #folder = 'fitbis_' + fold + '_' + srvar + '_' + crvar + '_' + yeartag
    channels = settmod.channels
    yearsett = settmod.years
    method = "hist"

    folder = 'fitbis_' + fold + '/' + srvar + '_' + crvar + '_' + yeartag
    if WithFakeCR:
        folder += "_WithFakeCR"
    if PDFWithTTDY:
        folder += "_PDFWithTTDY"
    if tagfold == "":
        tagfold = "none"
        folder += "/nom"
    else:
        folder += "/" + tagfold.replace("_", "")
    if addLambda8:
        folder += "_Lambda8"

    folderhisto = folder + "/shapes"

    partmodel = modeltot.split(":")

    isEFT = False
    if modeltot.startswith("c") or modeltot.startswith("F") or ":" in modeltot:
        isEFT = True 

    model = ""
    for idmt, mod in enumerate(partmodel):
        if idmt > 0:
            model += ":"
        if isEFT:
            model += mod.split("_")[0]
        else:
            model += mod
    
    if modeltot == "SM":
        dcname = "VBS_SSWW_SM_hist"
        dcfold = ipwd + "/" + folder + "/VBS_SSWW_SM/"
    else:
        dcname = model + "_hist"
        dcfold = ipwd + "/" + folder + "/" + model + "/"
    dcpath = dcfold + dcname + ".txt"

    os.chdir(dcfold)
    #os.system("pwd")
    
    
    cmdmer = "combineCards.py "
    for year in yearsett:
        for cat in channels:
            if not isEFT and not "WpWp" in model:
                cmdmer += cat+year+"=VBS_SSWW_%s_%s_%s_%s.txt " %(model, cat, year, method)
            else:
                cmdmer += cat+year+"=%s_%s_%s_%s.txt " %(model, cat, year, method)
    if not isEFT and not "WpWp" in model:
        cmdmer += "> VBS_SSWW_%s_%s.txt" % (model, method)
    else:
        cmdmer += "> %s_%s.txt" % (model, method)
    #print cmdmer
    os.system(cmdmer)
    os.chdir(ipwd)

    if isEFT:
        coeffs = modeltot.split(":")
        setpiecs = []
        for idc, coeff in enumerate(coeffs):
            if len(coeff.split("_")) > 1:
                setpiecs.append(("_")+coeff.split("_")[-1])
            coeffs[idc] = coeff.split("_")[0].replace("F", "c")

        extraoption = ""
        intervals = []
        modComb = ""
        opstring = ""
        for idc, coeff in enumerate(coeffs):
            if coeff.startswith("cS") or coeff.startswith("cM"):
                intervals.append("-80,80")
            elif coeff.startswith("cT"):
                intervals.append("-10,10")
            elif coeff.startswith("cHW"):
                intervals.append("-30,30")
            elif coeff.startswith("cW"):
                intervals.append("-5,5")

            if idc > 0:
                modComb += ","
                opstring += ","
            modComb += "k_" + coeff
            opstring += coeff

        intervalstr = ""
        for idc, coeff in enumerate(coeffs):
            if idc > 0:
                intervalstr += ":"
            intervalstr += "k_" + coeff + "=" + intervals[idc]
   
    impactfolder = ipwd + "/" + folder + "/Checks_" + model + "/"
    impactfolder = folder + "/Checks_" + model + "/"
    print impactfolder
    if not os.path.exists(impactfolder):
        os.system("mkdir " + impactfolder)
    else:
        os.system("rm " + impactfolder + "/higgsCombine_paramFit*")
    wscard = dcname + ".root"
    tag = model + "_" + srvar + "_" + crvar
    os.system("pwd")
    print "cd " + impactfolder
    os.chdir(impactfolder)
    
    cmdt2w ="text2workspace.py " + dcpath + " -o " + wscard
    if isEFT:
        cmdt2w += " -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative --X-allow-no-signal --PO eftOperators=" + opstring
    
    print cmdt2w
    os.system(cmdt2w)
    
    cmd0 = "combine -M FitDiagnostics -d " + wscard + " -t -1  -n " + tag + "_t0"
    cmd1 = "combine -M FitDiagnostics -d " + wscard + " -t -1  -n " + tag + "_t1"

    if isEFT:               
        cmd0 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges " + intervalstr + " --rMin -10 --setParameters r=1,"
        cmd1 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges " + intervalstr + " --setParameters "#r=1"
        for idc, coeff in enumerate(coeffs):
            if idc > 0:
                cmd1 += ","
                cmd0 += ","
            cmd1 += "k_" + coeff + "=1"
            cmd0 += "k_" + coeff + "=0"
   
        cmd0 += " " + optionals
        cmd1 += " " + optionals
    
    else:
        cmd0 += " --expectSignal 0 --rMin -10 --cminDefaultMinimizerStrategy=0"
        cmd1 += " --expectSignal 1 --rMin -10 --cminDefaultMinimizerStrategy=0"
    
    if not ":" in modeltot:
        print cmd0
        os.system(cmd0)
        if not isEFT:
            print cmd1
            os.system(cmd1)

    cmddN0 = "python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py -a fitDiagnostics" + tag + "_t0.root -g plots" + tag + "_t0.root "
    cmddN1 = "python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py -a fitDiagnostics" + tag + "_t1.root -g plots" + tag + "_t1.root "
    
    if isEFT:
        cmddN0 += " --poi "
        cmddN1 += " --poi "
        for idxc, coeff in enumerate(coeffs):
            if idxc > 0:
                cmddN0 += ","
                cmddN1 += ","
            cmddN0 += "k_" + coeff
            cmddN1 += "k_" + coeff

    cmddN0 += " >> " + "fitResults" + tag + "_t0.log"
    cmddN1 += " >> " + "fitResults" + tag + "_t0.log"
    cmddN0html = cmddN0 + " --format html >> " + "fitResults" + tag + "_t0.html"
    cmddN1html = cmddN1 + " --format html >> " + "fitResults" + tag + "_t1.html"

    if not ":" in modeltot:
        print cmddN0
        os.system(cmddN0)
        print cmddN0html
        os.system(cmddN0html)
        if not isEFT:
            print cmddN1
            os.system(cmddN1)
            print cmddN1html
            os.system(cmddN1html)
        

    imp0_0 = "combineTool.py -M Impacts -d " + wscard + " -t -1  --doInitialFit --allPars -m 1 -n " + tag + "_t0 --parallel 50 --autoRange 1 --autoBoundsPOIs r" 
    imp0_1 = "combineTool.py -M Impacts -d " + wscard + " -t -1  --doInitialFit --allPars -m 1 -n " + tag + "_t1 --parallel 50  --autoRange 1 --autoBoundsPOIs r"
    if isEFT:
        imp0_0 += "," + modComb
        imp0_1 += "," + modComb
        imp0_0 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges "+ intervalstr + " --rMin -10 --setParameters r=1,"
        imp0_1 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges "+ intervalstr + " --setParameters "#r=1"
        for idc, coeff in enumerate(coeffs):
            if idc > 0:
                imp0_1 += ","
                imp0_0 += ","
            imp0_1 += "k_" + coeff + "=1"
            imp0_0 += "k_" + coeff + "=0"
        imp0_0 += " " + optionals
        imp0_1 += " " + optionals
    
    else:
        imp0_0 += " --expectSignal 0 --rMin -10 --cminDefaultMinimizerStrategy=0"
        imp0_1 += " --expectSignal 1 --rMin -10 --cminDefaultMinimizerStrategy=0"

    imp1_0 = "combineTool.py -M Impacts -d " + wscard + " -o " + "impacts" + tag + "_t0.json -t -1  --doFits -m 1 -n " + tag + "_t0 --parallel 50 --autoRange 1 --autoBoundsPOIs r"
    imp1_1 = "combineTool.py -M Impacts -d " + wscard + " -o " + "impacts" + tag + "_t1.json -t -1  --doFits -m 1 -n " + tag + "_t1 --parallel 50 --autoRange 1 --autoBoundsPOIs r"

    if isEFT:
        imp1_0 += "," + modComb
        imp1_1 += "," + modComb

        imp1_0 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges "+ intervalstr + " --rMin -10 --setParameters r=1,"
        imp1_1 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges "+ intervalstr + " --setParameters "#r=1"
        for idc, coeff in enumerate(coeffs):
            if idc > 0:
                imp1_1 += ","
                imp1_0 += ","
            imp1_1 += "k_" + coeff + "=1"
            imp1_0 += "k_" + coeff + "=0"
        imp1_0 += " " + optionals
        imp1_1 += " " + optionals
   
    else:
        imp1_0 += " --expectSignal 0 --rMin -10 --cminDefaultMinimizerStrategy=0"
        imp1_1 += " --expectSignal 1 --rMin -10 --cminDefaultMinimizerStrategy=0"
    
    ctimp0 = "combineTool.py -M Impacts -d " + wscard + " -m 1 -n " + tag + "_t0 -o " +  "impacts" + tag + "_t0.json --parallel 50 --autoRange 1 --autoBoundsPOIs r"
    ctimp1 = "combineTool.py -M Impacts -d " + wscard + " -m 1 -n " + tag + "_t1 -o " +  "impacts" + tag + "_t1.json --parallel 50 --autoRange 1 --autoBoundsPOIs r"
  
    if isEFT:
        ctimp0 += "," + modComb
        ctimp1 += "," + modComb

        ctimp0 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges " + intervalstr + " --rMin -10 --setParameters r=1,"
        ctimp1 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges " + intervalstr + " --setParameters "#r=1 "
        for idc, coeff in enumerate(coeffs):
            if idc > 0:
                ctimp1 += ","
                ctimp0 += ","
            ctimp1 += "k_" + coeff + "=1"
            ctimp0 += "k_" + coeff + "=0"
        ctimp0 += " " + optionals
        ctimp1 += " " + optionals
   
    else:
        ctimp0 += " --expectSignal 0 --rMin -10 --cminDefaultMinimizerStrategy=0"
        ctimp1 += " --expectSignal 1 --rMin -10 --cminDefaultMinimizerStrategy=0"
    
    printimp0 = "plotImpacts.py -i " +  "impacts" + tag + "_t0.json -o " +  "impacts" + tag + "_t0"
    printimp1 = "plotImpacts.py -i " +  "impacts" + tag + "_t1.json -o " +  "impacts" + tag + "_t1"

    if isEFT:
        printimp0 += " --POI "
        printimp1 += " --POI "
        for idxc, coeff in enumerate(coeffs):
            if idxc > 0:
                printimp0 += ","
                printimp1 += ","
            printimp0 += "k_" + coeff
            printimp1 += "k_" + coeff

    print imp0_0
    os.system(imp0_0)
    if not isEFT:
        print imp0_1
        os.system(imp0_1)
    
    print imp1_0
    os.system(imp1_0)
    if not isEFT:
        print imp1_1
        os.system(imp1_1)
    
    print ctimp0
    os.system(ctimp0)
    if not isEFT:
        print ctimp1
        os.system(ctimp1)
    
    print printimp0
    os.system(printimp0)
    if not isEFT:
        print printimp1
        os.system(printimp1)
    
    os.chdir(ipwd)
    
def PrepareAndDoPostFit(model, srvar, crvar, plotvars, fold, cut, year, username, unblind, tagfold, addLambda8, WithFakeCR, PDFWithTTDY):
    pwd = os.getcwd()
    vartopost = []
    yeartag = year.replace("2016M,2017,2018", "RunII")# + "_"
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = filerepo + 'plot'
    plotrepo += tagfold + "/"

    print year
    
    if plotvars == "all":
        vartopost = variables
    else:
        for var in variables:
            if var.name in plotvars.split(","):
                vartopost.append(var)

    for var in vartopost:
        varname = var.name

        folder = 'postfit_' + fold + '/' + srvar + '_' + crvar + '_' + yeartag
        if WithFakeCR:
            folder += "_WithFakeCR"
        if PDFWithTTDY:
            folder += "_PDFWithTTDY"
        if tagfold == "":
            tagfold = "none"
            folder += "/nom"
        else:
            folder +="/" + tagfold.replace("_", "")
        if addLambda8:
            folder += "_Lambda8" 

        folderhisto = folder + "/" + varname + "/shapes"

        if not os.path.exists(folder):
            os.system("mkdir -p " + folder) 
        if not os.path.exists(folderhisto):
            os.system("mkdir -p " + folderhisto) 

        print varname, folder
    
        WriteMeta(varname, varname, fold, model, cut, year)
        WriteSett(varname, varname, fold, model, cut, year, WithFakeCR, PDFWithTTDY)

        settitle = "Stat.Limits.settings_" + model + "_" + varname + "_" + varname
        if WithFakeCR:
            settitle += "_WithFakeCR"
        if PDFWithTTDY:
            settitle += "_PDFWithTTDY"

        RecursiveImport(settitle)
        #os.system("python PrepareEOSfolder.py " + fold)
        
        appendix = ""
        
        if not "SM" in model and not model.startswith("WpWp"):
            appendix += " --ls " + model
        
        datafolder = folder + "/" + varname
        print datafolder
        
        if not os.path.exists(datafolder):
            os.system("mkdir " + datafolder)

        collhist = "python collectHistos.py -i " + plotrepo + " -o " + folderhisto + "/histo_" + model + "_" + varname + ".root " + appendix + " --model " + model + "_" + varname + "_" + varname
        createdata = "python createDatacards.py -i " + folderhisto + "/histo_" + model + "_" + varname + ".root -d " + datafolder + appendix + " --model " + model + "_" + varname + "_" + varname
        if WithFakeCR:
            collhist += " --WithFakeCR"
            createdata += " --WithFakeCR"
        if PDFWithTTDY:
            collhist += " --PDFWithTTDY"
            createdata += " --PDFWithTTDY"
        if addLambda8:
            collhist += " --Lambda8"
        
        os.system(collhist)
        os.system(createdata)

        settitle2 = "Stat.Limits.settings_" + model + "_" + srvar + "_" + crvar
        if WithFakeCR:
            settitle2 += "_WithFakeCR"
        if PDFWithTTDY:
            settitle2 += "_PDFWithTTDY"        
        WriteMeta(srvar, crvar, fold, model, cut, year)#, WithFakeCR, PDFWithTTDY)
        RecursiveImport(settitle2)
    
        createpostfit = "python createPostFit.py --vars " + varname + " --folder " + fold + " --year " + year + " --model " + model + " --tag " + model + "_" + srvar + "_" + crvar + " --tagfold " + tagfold
        if WithFakeCR:
            createpostfit += " --WithFakeCR"
        if PDFWithTTDY:
            createpostfit += " --PDFWithTTDY"
        
        os.system(createpostfit)
        
        poststring = "python plotter/PreFitPostFit_v2.py --era " + yeartag + " --folder " + fold + " --vars " + var.name + " --fitted " + srvar + "," + crvar + " --model " + model + " --tag " + model + "_" + srvar + "_" + crvar
        if tagfold != "":
            poststring += " --tagfolder " + tagfold
        if unblind:
            poststring += " -u"
        if WithFakeCR:
            poststring += " --WithFakeCR"
        if PDFWithTTDY:
            poststring += " --PDFWithTTDY"
        
        print poststring
        os.system(poststring)
        
        #os.chdir(pwd)
    
def ProduceCLPlots(srvars, crvars, folder, eftop, era, tagfold, WithFakeCR, PDFWithTTDY):
    command = "python ciplots.py --sr " + srvars + " --cr " + crvars + " --folder " + folder + " --op " + eftop + " --era " + era
    if WithFakeCR:
        command += " --WithFakeCR"
    if PDFWithTTDY:
        command += " --PDFWithTTDY"
    
    if tagfold == "":
        tagfolder = "nom"
    else:
        tagfolder = tagfold.replace("_", "")
    
    command += " --tagfolder " + tagfolder
    os.system(command)

def UncBreak(modeltot, srvar, crvar, fold, year, username, tagfold, addLambda8, WithFakeCR, PDFWithTTDY):
    optionalss = " --cminDefaultMinimizerStrategy=0 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT"# --setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND"# --fastScan"
    if not ":" in modeltot:
        points = "500"#"10000"
    else:
        points = "20000"

    settitle = "Stat.Limits.settings_" + modeltot + "_" + srvar + "_" + crvar
    if WithFakeCR:
        settitle += "_WithFakeCR"
    if PDFWithTTDY:
        settitle += "_PDFWithTTDY"

    RecursiveImport(settitle)
    #print("../python/settings_" + modeltot + "_" + srvar + "_" + crvar)
    settmod = importlib.import_module(settitle)
    systgroups = settmod.systgroups
    syst = settmod.syst
    upwd = os.getcwd()
    
    yeartag = year.replace("2016M,2017,2018", "RunII")# + "_"
    channels = settmod.channels
    yearsett = settmod.years
    method = "hist"
    
    folder = 'fitbis_' + fold + '/' + srvar + '_' + crvar + '_' + yeartag
    if WithFakeCR:
        folder += "_WithFakeCR"
    if PDFWithTTDY:
        folder += "_PDFWithTTDY"
    if tagfold == "":
        tagfold = "none"
        folder += "/nom"
    else:
        folder += "/" + tagfold.replace("_", "")
    if addLambda8:
        folder += "_Lambda8"

    folderhisto = folder + "/shapes"

    partmodel = modeltot.split(":")

    isEFT = False
    if modeltot.startswith("c") or modeltot.startswith("F") or ":" in modeltot:
        isEFT = True 

    model = ""
    for idmt, mod in enumerate(partmodel):
        if idmt > 0:
            model += ":"
        if isEFT:
            model += mod.split("_")[0]
        else:
            model += mod
    
    if modeltot == "SM":
        dcname = "VBS_SSWW_SM_hist"
        dcfold = upwd + "/" + folder + "/VBS_SSWW_SM/"
    else:
        dcname = model + "_hist"
        dcfold = upwd + "/" + folder + "/" + model + "/"
    dcpath = dcfold + dcname + ".txt"

    os.chdir(dcfold)
    os.system("pwd")
    
    cmdmer = "combineCards.py "
    for year in yearsett:
        for cat in channels:
            if not isEFT and not "WpWp" in model:
                cmdmer += cat+year+"=VBS_SSWW_%s_%s_%s_%s.txt " %(model, cat, year, method)
            else:
                cmdmer += cat+year+"=%s_%s_%s_%s.txt " %(model, cat, year, method)
    if not isEFT and not "WpWp" in model:
        cmdmer += "> VBS_SSWW_%s_%s.txt" % (model, method)
    else:
        cmdmer += "> %s_%s.txt" % (model, method)
    #print cmdmer
    os.system(cmdmer)
    os.chdir(upwd)
        
    years = year.split(",")
    
    if isEFT:
        coeffs = modeltot.split(":")
        setpiecs = []
        for idc, coeff in enumerate(coeffs):
            if len(coeff.split("_")) > 1:
                setpiecs.append(("_")+coeff.split("_")[-1])
            coeffs[idc] = coeff.split("_")[0].replace("F", "c")

        extraoption = ""
        intervals = []
        modComb = ""
        opstring = ""
        for idc, coeff in enumerate(coeffs):
            if coeff.startswith("cS"):
                intervals.append("-85,85")
            elif coeff.startswith("cM"):
                intervals.append("-50,50")
            elif coeff.startswith("cT"):
                intervals.append("-10,10")
            elif coeff.startswith("cHW"):
                intervals.append("-30,30")
            elif coeff.startswith("cW"):
                intervals.append("-5,5")

            if idc > 0:
                modComb += ","
                opstring += ","
            modComb += "k_" + coeff
            opstring += coeff

        intervalstr = ""
        for idc, coeff in enumerate(coeffs):
            if idc > 0:
                intervalstr += ":"
            intervalstr += "k_" + coeff + "=" + intervals[idc]


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
                elif syst[systname][0].startswith("shape"):
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


    cmdt2w ="text2workspace.py " + dcpath + " -o " + wscard
    
    if isEFT:
        cmdt2w += " -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative --X-allow-no-signal --PO eftOperators=" + opstring
    print cmdt2w
    os.system(cmdt2w)
    
    total = dcname + "_" + model + ".total"
    totalfile = "higgsCombine" + total + ".MultiDimFit.mH120.root"
    
    cmdmd = "combine " + wscard + " -M MultiDimFit -t -1 -m 120 --points " + points + " --saveWorkspace -n " + total + " --algo grid"
    cmdmd += " --autoBoundsPOIs r"
    if isEFT:
        cmdmd += "," + modComb
        cmdmd += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges "+ intervalstr
        
        if modeltot.startswith("F") or modeltot.startswith("c"):
            cmdmd += " --setParameters r=1,"
            for idc, coeff in enumerate(coeffs):
                if idc > 0:
                    cmdmd += ","
                cmdmd+= "k_" + coeff + "=0"
        
    else:
        cmdmd += " --rMin -5 --rMax 5"

    cmdmd += " " + optionalss

    print cmdmd
    os.system(cmdmd)
    
    md = "combine " + totalfile + " -M MultiDimFit -t -1 -m 120 --points " + points + " --algo grid "
    md += " --autoBoundsPOIs r"
    if isEFT:
        md += "," + modComb
        md += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges "+ intervalstr
        
        if modeltot.startswith("F") or modeltot.startswith("c"):
            md += " --setParameters r=1,"
            for idc, coeff in enumerate(coeffs):
                if idc > 0:
                    md += ","
                md+= "k_" + coeff + "=0"
        
    else:
        md += " --rMin -5 --rMax 5"
    
    md += optionalss 
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
     
            plotcomm += "\'" + freezefile + ":Freeze " + groupname + ":" + colors[idsy] + "\' "

    mdfa = "combine " + totalfile + " -M MultiDimFit -t -1 -m 120 --points " + points + " --algo grid "
    mdfa += " --autoBoundsPOIs r" 
    if isEFT:
        mdfa += "," + modComb
        mdfa += " --redefineSignalPOIs " + modComb + " --setParameterRanges "+ intervalstr
        
        if modeltot.startswith("F") or modeltot.startswith("c"):
            mdfa += " --setParameters r=1,"
            for idc, coeff in enumerate(coeffs):
                if idc > 0:
                    mdfa += ","
                mdfa += "k_" + coeff + "=0"
        
    else:
        mdfa += " --rMin -5 --rMax 5"
    mdfa += " " + optionalss 
    freezeall = mdfa + " --freezeParameters "
    if isEFT:
        freezeall += "r,"
    freezeall += "allConstrainedNuisances -n"
    freezeallname = dcname + ".freeze_all" + "_" + model
    freezeallfile = "higgsCombine" + freezeallname + ".MultiDimFit.mH120.root"
    freezeall += " " + freezeallname
    print(freezeall)
    os.system(freezeall)
    
    plotcomm += "\'" + freezeallfile + ":Freeze all:" + colors[len(systgroup)] + "\' "
    bdstr += ",MCstat,Stat\""

    plotcomm += bdstr
    if isEFT:
        plotcomm += " --POI " + modComb
    print(plotcomm)
    if not ":" in modeltot:
        os.system(plotcomm)
    
    os.chdir(upwd)
