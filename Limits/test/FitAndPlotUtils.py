import os
import ROOT
from Stat.Limits.variables import *
#from Stat.Limits.settings import syst, systgroups
import importlib
import sys
import optparse
from collections import OrderedDict
LineWrite = lambda fname, s : fname.write(s + "\n") 

colors = [
    str(ROOT.kGray+3),
    str(ROOT.kRed),
    str(ROOT.kGreen+1),
    str(ROOT.kBlue+1),
    str(ROOT.kMagenta),
    str(ROOT.kCyan),
    str(ROOT.kYellow+1),
    str(ROOT.kViolet-6),
    str(ROOT.kOrange+4),
    str(ROOT.kSpring+10),
    str(ROOT.kPink+1),
    str(ROOT.kGray),
    str(ROOT.kAzure+2), 
    str(ROOT.kOrange-3), 
    str(ROOT.kYellow+4),
    str(ROOT.kTeal-9),
]

regs = OrderedDict()
regs['SR'] =  "\t'SR':hist_pre + sr_var + '_SR',"
regs['CRTT'] =  "\t'CRTT':hist_pre + sr_var + '_ttbar_CR',"
regs['CRTTL'] =  "\t'CRTTL':hist_pre + sr_var + '_ttbarL_CR',"
regs['CROS'] =  "\t'CROS':hist_pre + sr_var + '_OS_CR_bvetoL',"
regs['CRF'] = "\t'CRF':hist_pre + cr_var + '_fakes_CR',"                                                                                        
leptags = OrderedDict()
leptags['electron'] = 'ele'
leptags['muon'] = 'mu'

def WriteSett(srvar, crvar, folder, model, cut, year, PDFWithTTDY, DYrp, pdftype, flnN, Frp, regions, leptons, settitle, noQCDScale, shapeN = True):
    if 'CRF' in regions:
        WithFakeCR = True
    else:
        WithFakeCR = False
    leps = leptons
    print("Producing " + settitle)
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
    LineWrite(settname, "setfile = open('/afs/cern.ch/work/a/apiccine/CMSSW_10_2_13/src/Stat/Limits/python/metasett_" + model + "_" + srvar + "_" + crvar + "_" + folder + ".txt', 'r')")
    LineWrite(settname, "setlist = [line.replace('\\n', '') for line in setfile.readlines()]")
    LineWrite(settname, "sr_var, cr_var = setlist[0].split(',')")
    LineWrite(settname, "intfolder = setlist[1]")
    LineWrite(settname, "model = setlist[2]")
    LineWrite(settname, "cut = setlist[4]")
    LineWrite(settname, "")
    LineWrite(settname, "shapesyst = ''")
    LineWrite(settname, "if model.startswith('c') or model.startswith('F'):")
    if shapeN:
        LineWrite(settname, "\tshapesyst = 'shapeN'")
    else:
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
    for region in regions:
        LineWrite(settname, regs[region])
        #LineWrite(settname, "\t'SR':hist_pre + sr_var + '_SR',")
        #LineWrite(settname, "\t'CRTT':hist_pre + sr_var + '_ttbar_CR',")
        #LineWrite(settname, "\t'CROS':hist_pre + sr_var + '_OS_CR_bvetoL',")

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
    for region in regions:
        for lep in leps:
            chstring = "\t'" + region + "_" + lep + "',"
            LineWrite(settname, chstring)
    LineWrite(settname, "]")

    LineWrite(settname, "")
    LineWrite(settname, "leptons = [")
    for lep in leps:
        lepstr = "\t\'" + lep + "\',"
        LineWrite(settname, lepstr)
    LineWrite(settname, "]")

    LineWrite(settname, "")
    LineWrite(settname, "channels_labels = {")
    LineWrite(settname, "\t'SR':'Signal Region',")
    LineWrite(settname, "\t'CROS':'Opposite Sign CR',")
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
    #LineWrite(settname, "\tdyjets_sample,")
    LineWrite(settname, "\t'TTTo2L2Nu',")
    LineWrite(settname, "\t'Fake',")
    LineWrite(settname, "]")
    LineWrite(settname, "")

    LineWrite(settname, "class rateParam(object):")
    LineWrite(settname, "\tpass")
    LineWrite(settname, "rateParams = collections.OrderedDict()")
    LineWrite(settname, "")
    
    if Frp:
        for lep in leps:
            frpname = "Fake" + leptags[lep] + "_rate_2016M"
            LineWrite(settname, frpname + " = rateParam()")
            LineWrite(settname, frpname + ".chs = [")
            for region in regions:
                systregstring = "\t'" + region + "_" + lep + "',"      
                LineWrite(settname, systregstring)
            LineWrite(settname, "]")
            LineWrite(settname, frpname + ".bkg = 'Fake'")
            frpkey = "FRest_" + lep + "_2016M"
            LineWrite(settname, "rateParams['" + frpkey + "'] = " + frpname)
            LineWrite(settname, "")        

            frpname = "Fake" + leptags[lep] + "_rate_2017"
            LineWrite(settname, frpname + " = rateParam()")
            LineWrite(settname, frpname + ".chs = [")
            for region in regions:
                systregstring = "\t'" + region + "_" + lep + "',"      
                LineWrite(settname, systregstring)
            LineWrite(settname, "]")
            LineWrite(settname, frpname + ".bkg = 'Fake'")
            frpkey = "FRest_" + lep + "_2017"
            LineWrite(settname, "rateParams['" + frpkey + "'] = " + frpname)
            LineWrite(settname, "")        

            frpname = "Fake" + leptags[lep] + "_rate_2018"
            LineWrite(settname, frpname + " = rateParam()")
            LineWrite(settname, frpname + ".chs = [")
            for region in regions:
                systregstring = "\t'" + region + "_" + lep + "',"      
                LineWrite(settname, systregstring)
            LineWrite(settname, "]")
            LineWrite(settname, frpname + ".bkg = 'Fake'")
            frpkey = "FRest_" + lep + "_2018"
            LineWrite(settname, "rateParams['" + frpkey + "'] = " + frpname)
            LineWrite(settname, "")        

    for lep in leps:
        
        ttrpname = "TTbar" + leptags[lep] + "_rate_2016M"
        LineWrite(settname, ttrpname + " = rateParam()")
        LineWrite(settname, ttrpname + ".chs = [")
        for region in regions:
            if not (region == "SR" or region.startswith("CRTT")):
                continue
            systregstring = "\t'" + region + "_" + lep + "',"      
            LineWrite(settname, systregstring)
        LineWrite(settname, "]")
        LineWrite(settname, ttrpname + ".bkg = 'TTTo2L2Nu'")
        ttrpkey = "TTest_" + lep + "_2016M"
        LineWrite(settname, "rateParams['" + ttrpkey + "'] = " + ttrpname)
        LineWrite(settname, "")        

        ttrpname = "TTbar" + leptags[lep] + "_rate_2017"
        LineWrite(settname, ttrpname + " = rateParam()")
        LineWrite(settname, ttrpname + ".chs = [")
        for region in regions:
            if not (region == "SR" or region.startswith("CRTT")):
                continue
            systregstring = "\t'" + region + "_" + lep + "',"      
            LineWrite(settname, systregstring)
        LineWrite(settname, "]")
        LineWrite(settname, ttrpname + ".bkg = 'TTTo2L2Nu'")
        ttrpkey = "TTest_" + lep + "_2017"
        LineWrite(settname, "rateParams['" + ttrpkey + "'] = " + ttrpname)
        LineWrite(settname, "")        

        ttrpname = "TTbar" + leptags[lep] + "_rate_2018"
        LineWrite(settname, ttrpname + " = rateParam()")
        LineWrite(settname, ttrpname + ".chs = [")
        for region in regions:
            if not (region == "SR" or region.startswith("CRTT")):
                continue
            systregstring = "\t'" + region + "_" + lep + "',"      
            LineWrite(settname, systregstring)
        LineWrite(settname, "]")
        LineWrite(settname, ttrpname + ".bkg = 'TTTo2L2Nu'")
        ttrpkey = "TTest_" + lep + "_2018"
        LineWrite(settname, "rateParams['" + ttrpkey + "'] = " + ttrpname)
        LineWrite(settname, "")        
        
    if DYrp: #not (model == "SM" or model.startswith("WpWp")):
        for lep in leps:
            osrpname = "OS" + leptags[lep] + "_rate_2016M"
            LineWrite(settname, osrpname + " = rateParam()")
            LineWrite(settname, osrpname + ".chs = [")
            for region in regions:
                if not (region == "SR" or region == "CROS"):
                    continue
                systregstring = "\t'" + region + "_" + lep + "',"      
                LineWrite(settname, systregstring)
            LineWrite(settname, "]")
            LineWrite(settname, osrpname + ".bkg = 'WrongSign'")
            osrpkey = "OSest_" + lep + "_2016M"
            LineWrite(settname, "rateParams['" + osrpkey + "'] = " + osrpname)
            LineWrite(settname, "")        

            osrpname = "OS" + leptags[lep] + "_rate_2017"
            LineWrite(settname, osrpname + " = rateParam()")
            LineWrite(settname, osrpname + ".chs = [")
            for region in regions:
                if not (region == "SR" or region == "CROS"):
                    continue
                systregstring = "\t'" + region + "_" + lep + "',"      
                LineWrite(settname, systregstring)
            LineWrite(settname, "]")
            LineWrite(settname, osrpname + ".bkg = 'WrongSign'")
            osrpkey = "OSest_" + lep + "_2017"
            LineWrite(settname, "rateParams['" + osrpkey + "'] = " + osrpname)
            LineWrite(settname, "")        

            osrpname = "OS" + leptags[lep] + "_rate_2018"
            LineWrite(settname, osrpname + " = rateParam()")
            LineWrite(settname, osrpname + ".chs = [")
            for region in regions:
                if not (region == "SR" or region == "CROS"):
                    continue
                systregstring = "\t'" + region + "_" + lep + "',"      
                LineWrite(settname, systregstring)
            LineWrite(settname, "]")
            LineWrite(settname, osrpname + ".bkg = 'WrongSign'")
            osrpkey = "OSest_" + lep + "_2018"
            LineWrite(settname, "rateParams['" + osrpkey + "'] = " + osrpname)
            LineWrite(settname, "")        

    LineWrite(settname, "#*********************************")
    LineWrite(settname, "#                                *")
    LineWrite(settname, "#       List of systematics      *")
    LineWrite(settname, "#                                *")
    LineWrite(settname, "#*********************************")
    LineWrite(settname, "")
    LineWrite(settname, "syst = collections.OrderedDict()")
    LineWrite(settname, "")
    #LineWrite(settname, "syst['lumi_2016M'] = ['lnN', 'all', 1.016]")
    #LineWrite(settname, "syst['lumi_2017'] = ['lnN', 'all', 1.023]")
    #LineWrite(settname, "syst['lumi_2018'] = ['lnN', 'all', 1.025]")
    LineWrite(settname, "syst['lumi_2016M'] = ['lnN', 'all', 1.010]")
    LineWrite(settname, "syst['lumi_2017'] = ['lnN', 'all', 1.020]")
    LineWrite(settname, "syst['lumi_2018'] = ['lnN', 'all', 1.015]")
    LineWrite(settname, "syst['lumi_161718_2016M'] = ['lnN', 'all', 1.006]")
    LineWrite(settname, "syst['lumi_161718_2017'] = ['lnN', 'all', 1.009]")
    LineWrite(settname, "syst['lumi_161718_2018'] = ['lnN', 'all', 1.020]")
    LineWrite(settname, "syst['lumi_1718_2017'] = ['lnN', 'all', 1.006]")
    LineWrite(settname, "syst['lumi_1718_2018'] = ['lnN', 'all', 1.002]")
    if "CROS" in regions:
        for lep in leps:
            LineWrite(settname, "syst['mischarge_" + lep + "_2016M'] = ['lnN', ('WrongSign', 'TTTo2L2Nu'), 1.15]")
            LineWrite(settname, "syst['mischarge_" + lep + "_2017'] = ['lnN', ('WrongSign', 'TTTo2L2Nu'), 1.15]")
            LineWrite(settname, "syst['mischarge_" + lep + "_2018'] = ['lnN', ('WrongSign', 'TTTo2L2Nu'), 1.15]")

    if flnN:
        for lep in leps:
            LineWrite(settname, "syst['FR_sys_" + lep + "_2016M'] = ['lnN', 'Fake', 1.3]")
            LineWrite(settname, "syst['FR_sys_" + lep + "_2017'] = ['lnN', 'Fake', 1.3]")
            LineWrite(settname, "syst['FR_sys_" + lep + "_2018'] = ['lnN', 'Fake', 1.3]")
            #LineWrite(settname, "syst['FR_sys_" + lep + "'] = ['lnN', 'Fake', 1.3]")

    #if ApplyFStats:
    LineWrite(settname, "syst['autoMCstat'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'Fake', 'sig'), 'uncorr']")
    #else:
        #LineWrite(settname, "syst['autoMCstat'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'uncorr']")
    LineWrite(settname, "syst['PF'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['pu'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['puID'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['lep'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'uncorr']")
    LineWrite(settname, "syst['btag'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['mistag'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['tau_vsjet'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'uncorr']")
    for lep in leps:
        LineWrite(settname, "syst['tau_vs" + leptags[lep] + "'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'uncorr']")

    pdfstr = "pdf_" + pdftype.split("_")[0]
    if pdftype.endswith("sep"):
        LineWrite(settname, "if model != 'WpWpJJ':")
        LineWrite(settname, "\tsyst['" + pdfstr + "_WpWpJJ_QCD'] = [shapesyst, ('WpWpJJ_QCD'), 'corr']")
        LineWrite(settname, "syst['" + pdfstr + "_VG'] = [shapesyst, ('VG'), 'corr']")
        LineWrite(settname, "syst['" + pdfstr + "_TVX'] = [shapesyst, ('TVX'), 'corr']")
        #LineWrite(settname, "syst['" + pdfstr + "_DY'] = [shapesyst, (dyjets_sample), 'corr']")
        LineWrite(settname, "syst['" + pdfstr + "_WZ'] = [shapesyst, ('WZ'), 'corr']")
        LineWrite(settname, "syst['" + pdfstr + "_Triboson'] = [shapesyst, (triboson_sample), 'corr']")
        LineWrite(settname, "syst['" + pdfstr + "_WrongSign'] = [shapesyst, ('WrongSign'), 'corr']")
        LineWrite(settname, "syst['" + pdfstr + "_ZZtoLep'] = [shapesyst, ('ZZtoLep'), 'corr']")
        LineWrite(settname, "syst['" + pdfstr + "_sig'] = [shapesyst, ('sig'), 'corr']")
        if PDFWithTTDY:
            LineWrite(settname, "syst['" + pdfstr + "_TTTo2L2Nu'] = [shapesyst, ('TTTo2L2Nu'), 'corr']")
            
    else:
        if not PDFWithTTDY:
            LineWrite(settname, "syst['" + pdfstr + "'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
        else:
            LineWrite(settname, "syst['" + pdfstr + "'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")

    #LineWrite(settname, "syst['QCDScale'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    
    if not noQCDScale:
        LineWrite(settname, "syst['QCDScale_sig'] = [shapesyst, ('sig'), 'corr']")
        LineWrite(settname, "if model !='WpWpJJ':")
        LineWrite(settname, "\tsyst['QCDScale_WpWpJJ_QCD'] = [shapesyst, ('WpWpJJ_QCD'), 'corr']")
        LineWrite(settname, "syst['QCDScale_VG'] = [shapesyst, ('VG'), 'corr']")
        LineWrite(settname, "syst['QCDScale_TVX'] = [shapesyst, ('TVX'), 'corr']")
        #LineWrite(settname, "syst['QCDScale_DY'] = [shapesyst, (dyjets_sample), 'corr']")
        LineWrite(settname, "syst['QCDScale_TTTo2L2Nu'] = [shapesyst, ('TTTo2L2Nu'), 'corr']")
        LineWrite(settname, "syst['QCDScale_WZ'] = [shapesyst, ('WZ'), 'corr']")
        LineWrite(settname, "syst['QCDScale_Triboson'] = [shapesyst, (triboson_sample), 'corr']")
        LineWrite(settname, "syst['QCDScale_WrongSign'] = [shapesyst, ('WrongSign'), 'corr']")
        LineWrite(settname, "syst['QCDScale_ZZtoLep'] = [shapesyst, ('ZZtoLep'), 'corr']")
    
    LineWrite(settname, "syst['ISR'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    #LineWrite(settname, "if model !='WpWpJJ':")
    #LineWrite(settname, "\tsyst['ISR_WpWpJJ_QCD'] = [shapesyst, ('WpWpJJ_QCD'), 'corr']")
    #LineWrite(settname, "syst['ISR_VG'] = [shapesyst, ('VG'), 'corr']")
    #LineWrite(settname, "syst['ISR_TVX'] = [shapesyst, ('TVX'), 'corr']")
    #LineWrite(settname, "syst['ISR_TTTo2L2Nu'] = [shapesyst, ('TTTo2L2Nu'), 'corr']")
    #LineWrite(settname, "syst['ISR_WZ'] = [shapesyst, ('WZ'), 'corr']")
    #LineWrite(settname, "syst['ISR_Triboson'] = [shapesyst, (triboson_sample), 'corr']")
    #LineWrite(settname, "syst['ISR_WrongSign'] = [shapesyst, ('WrongSign'), 'corr']")
    #LineWrite(settname, "syst['ISR_ZZtoLep'] = [shapesyst, ('ZZtoLep'), 'corr']")
    #LineWrite(settname, "syst['ISR_sig'] = [shapesyst, ('sig'), 'corr']")

    LineWrite(settname, "syst['FSR'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    #LineWrite(settname, "if model !='WpWpJJ':")
    #LineWrite(settname, "\tsyst['FSR_WpWpJJ_QCD'] = [shapesyst, ('WpWpJJ_QCD'), 'corr']")
    #LineWrite(settname, "syst['FSR_VG'] = [shapesyst, ('VG'), 'corr']")
    #LineWrite(settname, "syst['FSR_TVX'] = [shapesyst, ('TVX'), 'corr']")
    #LineWrite(settname, "syst['FSR_TTTo2L2Nu'] = [shapesyst, ('TTTo2L2Nu'), 'corr']")
    #LineWrite(settname, "syst['FSR_WZ'] = [shapesyst, ('WZ'), 'corr']")
    #LineWrite(settname, "syst['FSR_Triboson'] = [shapesyst, (triboson_sample), 'corr']")
    #LineWrite(settname, "syst['FSR_WrongSign'] = [shapesyst, ('WrongSign'), 'corr']")
    #LineWrite(settname, "syst['FSR_ZZtoLep'] = [shapesyst, ('ZZtoLep'), 'corr']")
    #LineWrite(settname, "syst['FSR_sig'] = [shapesyst, ('sig'), 'corr']")
    
    #LineWrite(settname, "syst['jes'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'uncorr']")
    #LineWrite(settname, "syst['jes'] = ['lnN', ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 0., 'uncorr']")
    LineWrite(settname, "syst['jes_sig'] = ['lnN', ('sig'), 0., 'uncorr']")
    LineWrite(settname, "if model !='WpWpJJ':")
    LineWrite(settname, "\tsyst['jes_WpWpJJ_QCD'] = ['lnN', ('WpWpJJ_QCD'), 0., 'uncorr']")
    LineWrite(settname, "syst['jes_VG'] = ['lnN', ('VG'), 0., 'uncorr']")
    LineWrite(settname, "syst['jes_TVX'] = ['lnN', ('TVX'), 0., 'uncorr']")
    #LineWrite(settname, "syst['jes_DY'] = ['lnN', (dyjets_sample), 0., 'uncorr']")
    LineWrite(settname, "syst['jes_TTTo2L2Nu'] = ['lnN', ('TTTo2L2Nu'), 0., 'uncorr']")
    LineWrite(settname, "syst['jes_WZ'] = ['lnN', ('WZ'), 0., 'uncorr']")
    LineWrite(settname, "syst['jes_Triboson'] = ['lnN', (triboson_sample), 0., 'uncorr']")
    LineWrite(settname, "syst['jes_WrongSign'] = ['lnN', ('WrongSign'), 0., 'uncorr']")
    LineWrite(settname, "syst['jes_ZZtoLep'] = ['lnN', ('ZZtoLep'), 0., 'uncorr']")

    LineWrite(settname, "syst['metUnclust'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['jer'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'uncorr']")
    LineWrite(settname, "syst['TES'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['FES'] = [shapesyst, ('WpWpJJ_QCD', 'VG', 'TVX', 'TTTo2L2Nu', 'WZ', triboson_sample, 'WrongSign', 'ZZtoLep', 'sig'), 'corr']")
    LineWrite(settname, "syst['VBS'] = [shapesyst, ('WpWpJJ_QCD', 'sig'), 'uncorr']")
    LineWrite(settname, "")

    LineWrite(settname, "systgroups = collections.OrderedDict()")
    LineWrite(settname, "")
    
    if flnN:
        LineWrite(settname, "systgroups['FRsys group'] = [")
        for lep in leps:
            LineWrite(settname, "\t'FR_sys_" + lep + "_2016M',")
            LineWrite(settname, "\t'FR_sys_" + lep + "_2017',")
            LineWrite(settname, "\t'FR_sys_" + lep + "_2018',")
        LineWrite(settname, "]")
    if not pdftype.endswith("sep"):
        if not noQCDScale:
            LineWrite(settname, "systgroups['theory group'] = ['ISR', 'FSR', 'QCDScale_sig', 'QCDScale_VG', 'QCDScale_TVX', 'QCDScale_TTTo2L2Nu', 'QCDScale_WZ', 'QCDScale_Triboson', 'QCDScale_WrongSign', 'QCDScale_ZZtoLep', '" + pdfstr + "']")
            #LineWrite(settname, "systgroups['theory group'] = ['ISR_sig', 'ISR_VG', 'ISR_TVX', 'ISR_TTTo2L2Nu', 'ISR_WZ', 'ISR_Triboson', 'ISR_WrongSign', 'ISR_ZZtoLep', 'FSR_sig', 'FSR_VG', 'FSR_TVX', 'FSR_TTTo2L2Nu', 'FSR_WZ', 'FSR_Triboson', 'FSR_WrongSign', 'FSR_ZZtoLep', 'QCDScale_sig', 'QCDScale_VG', 'QCDScale_TVX', 'QCDScale_TTTo2L2Nu', 'QCDScale_WZ', 'QCDScale_Triboson', 'QCDScale_WrongSign', 'QCDScale_ZZtoLep', '" + pdfstr + "']")
            LineWrite(settname, "if model != 'WpWpJJ':")
            LineWrite(settname, "\tsystgroups['theory group'].append('QCDScale_WpWpJJ_QCD')")
        else:
            LineWrite(settname, "systgroups['theory group'] = ['ISR', 'FSR', '" + pdfstr + "']")
        #LineWrite(settname, "\tsystgroups['theory group'].append('ISR_WpWpJJ_QCD')")
        #LineWrite(settname, "\tsystgroups['theory group'].append('FSR_WpWpJJ_QCD')")
    else:
        if not DYrp:
            if PDFWithTTDY:
                if not noQCDScale:
                    LineWrite(settname, "systgroups['theory group'] = ['ISR', 'FSR', 'QCDScale_sig', 'QCDScale_VG', 'QCDScale_TVX', 'QCDScale_TTTo2L2Nu', 'QCDScale_WZ', 'QCDScale_Triboson', 'QCDScale_WrongSign', 'QCDScale_ZZtoLep', '" + pdfstr + "_sig', '" + pdfstr + "_VG', '" + pdfstr + "_TVX', '" + pdfstr + "_DY', '" + pdfstr + "_TTTo2L2Nu', '" + pdfstr + "_WZ', '" + pdfstr + "_Triboson', '" + pdfstr + "_WrongSign', '" + pdfstr + "_ZZtoLep']")
                    #LineWrite(settname, "systgroups['theory group'] = ['ISR_sig', 'ISR_VG', 'ISR_TVX', 'ISR_TTTo2L2Nu', 'ISR_WZ', 'ISR_Triboson', 'ISR_WrongSign', 'ISR_ZZtoLep', 'FSR_sig', 'FSR_VG', 'FSR_TVX', 'FSR_TTTo2L2Nu', 'FSR_WZ', 'FSR_Triboson', 'FSR_WrongSign', 'FSR_ZZtoLep', 'QCDScale_sig', 'QCDScale_VG', 'QCDScale_TVX', 'QCDScale_TTTo2L2Nu', 'QCDScale_WZ', 'QCDScale_Triboson', 'QCDScale_WrongSign', 'QCDScale_ZZtoLep', '" + pdfstr + "_sig', '" + pdfstr + "_VG', '" + pdfstr + "_TVX', '" + pdfstr + "_DY', '" + pdfstr + "_TTTo2L2Nu', '" + pdfstr + "_WZ', '" + pdfstr + "_Triboson', '" + pdfstr + "_WrongSign', '" + pdfstr + "_ZZtoLep']")
                    LineWrite(settname, "if model != 'WpWpJJ':")
                    LineWrite(settname, "\tsystgroups['theory group'].append('QCDScale_WpWpJJ_QCD')")
                    LineWrite(settname, "\tsystgroups['theory group'].append('" + pdfstr + "_WpWpJJ_QCD')")
                else:
                    LineWrite(settname, "systgroups['theory group'] = ['ISR', 'FSR', '" + pdfstr + "_sig', '" + pdfstr + "_VG', '" + pdfstr + "_TVX', '" + pdfstr + "_DY', '" + pdfstr + "_TTTo2L2Nu', '" + pdfstr + "_WZ', '" + pdfstr + "_Triboson', '" + pdfstr + "_WrongSign', '" + pdfstr + "_ZZtoLep']")
                #LineWrite(settname, "\tsystgroups['theory group'].append('ISR_WpWpJJ_QCD')")
                #LineWrite(settname, "\tsystgroups['theory group'].append('FSR_WpWpJJ_QCD')")

            else:
                if not noQCDScale:
                    LineWrite(settname, "systgroups['theory group'] = ['ISR', 'FSR', 'QCDScale_sig', 'QCDScale_VG', 'QCDScale_TVX', 'QCDScale_TTTo2L2Nu', 'QCDScale_WZ', 'QCDScale_Triboson', 'QCDScale_WrongSign', 'QCDScale_ZZtoLep', '" + pdfstr + "_sig', '" + pdfstr + "_VG', '" + pdfstr + "_TVX', '" + pdfstr + "_DY', '" + pdfstr + "_WZ', '" + pdfstr + "_Triboson', '" + pdfstr + "_WrongSign', '" + pdfstr + "_ZZtoLep']")
                    #LineWrite(settname, "systgroups['theory group'] = ['ISR_sig', 'ISR_VG', 'ISR_TVX', 'ISR_TTTo2L2Nu', 'ISR_WZ', 'ISR_Triboson', 'ISR_WrongSign', 'ISR_ZZtoLep', 'FSR_sig', 'FSR_VG', 'FSR_TVX', 'FSR_TTTo2L2Nu', 'FSR_WZ', 'FSR_Triboson', 'FSR_WrongSign', 'FSR_ZZtoLep', 'QCDScale_sig', 'QCDScale_VG', 'QCDScale_TVX', 'QCDScale_TTTo2L2Nu', 'QCDScale_WZ', 'QCDScale_Triboson', 'QCDScale_WrongSign', 'QCDScale_ZZtoLep', '" + pdfstr + "_sig', '" + pdfstr + "_VG', '" + pdfstr + "_TVX', '" + pdfstr + "_DY', '" + pdfstr + "_WZ', '" + pdfstr + "_Triboson', '" + pdfstr + "_WrongSign', '" + pdfstr + "_ZZtoLep']")
                    LineWrite(settname, "if model != 'WpWpJJ':")
                    LineWrite(settname, "\tsystgroups['theory group'].append('QCDScale_WpWpJJ_QCD')")
                    LineWrite(settname, "\tsystgroups['theory group'].append('" + pdfstr + "_WpWpJJ_QCD')")
                else:
                    LineWrite(settname, "systgroups['theory group'] = ['ISR', 'FSR', '" + pdfstr + "_sig', '" + pdfstr + "_VG', '" + pdfstr + "_TVX', '" + pdfstr + "_DY', '" + pdfstr + "_WZ', '" + pdfstr + "_Triboson', '" + pdfstr + "_WrongSign', '" + pdfstr + "_ZZtoLep']")
                #LineWrite(settname, "\tsystgroups['theory group'].append('ISR_WpWpJJ_QCD')")
                #LineWrite(settname, "\tsystgroups['theory group'].append('FSR_WpWpJJ_QCD')")
        else:
            if PDFWithTTDY:
                if not noQCDScale:
                    LineWrite(settname, "systgroups['theory group'] = ['ISR', 'FSR', 'QCDScale_sig', 'QCDScale_VG', 'QCDScale_TVX', 'QCDScale_TTTo2L2Nu', 'QCDScale_WZ', 'QCDScale_Triboson', 'QCDScale_WrongSign', 'QCDScale_ZZtoLep', '" + pdfstr + "_sig', '" + pdfstr + "_VG', '" + pdfstr + "_TVX', '" + pdfstr + "_DY', '" + pdfstr + "_TTTo2L2Nu', '" + pdfstr + "_WZ', '" + pdfstr + "_Triboson', '" + pdfstr + "_WrongSign', '" + pdfstr + "_ZZtoLep']")
                    #LineWrite(settname, "systgroups['theory group'] = ['ISR_sig', 'ISR_VG', 'ISR_TVX', 'ISR_TTTo2L2Nu', 'ISR_WZ', 'ISR_Triboson', 'ISR_WrongSign', 'ISR_ZZtoLep', 'FSR_sig', 'FSR_VG', 'FSR_TVX', 'FSR_TTTo2L2Nu', 'FSR_WZ', 'FSR_Triboson', 'FSR_WrongSign', 'FSR_ZZtoLep', 'QCDScale_sig', 'QCDScale_VG', 'QCDScale_TVX', 'QCDScale_TTTo2L2Nu', 'QCDScale_WZ', 'QCDScale_Triboson', 'QCDScale_WrongSign', 'QCDScale_ZZtoLep', '" + pdfstr + "_sig', '" + pdfstr + "_VG', '" + pdfstr + "_TVX', '" + pdfstr + "_DY', '" + pdfstr + "_TTTo2L2Nu', '" + pdfstr + "_WZ', '" + pdfstr + "_Triboson', '" + pdfstr + "_WrongSign', '" + pdfstr + "_ZZtoLep']")
                    LineWrite(settname, "if model != 'WpWpJJ':")
                    LineWrite(settname, "\tsystgroups['theory group'].append('QCDScale_WpWpJJ_QCD')")
                    LineWrite(settname, "\tsystgroups['theory group'].append('" + pdfstr + "_WpWpJJ_QCD')")
                else:
                    LineWrite(settname, "systgroups['theory group'] = ['ISR', 'FSR', '" + pdfstr + "_sig', '" + pdfstr + "_VG', '" + pdfstr + "_TVX', '" + pdfstr + "_DY', '" + pdfstr + "_TTTo2L2Nu', '" + pdfstr + "_WZ', '" + pdfstr + "_Triboson', '" + pdfstr + "_WrongSign', '" + pdfstr + "_ZZtoLep']")
                #LineWrite(settname, "\tsystgroups['theory group'].append('ISR_WpWpJJ_QCD')")
                #LineWrite(settname, "\tsystgroups['theory group'].append('FSR_WpWpJJ_QCD')")
            else:
                if not noQCDScale:
                    LineWrite(settname, "systgroups['theory group'] = ['ISR', 'FSR', 'QCDScale_sig', 'QCDScale_VG', 'QCDScale_TVX', 'QCDScale_TTTo2L2Nu', 'QCDScale_WZ', 'QCDScale_Triboson', 'QCDScale_WrongSign', 'QCDScale_ZZtoLep', '" + pdfstr + "_sig', '" + pdfstr + "_VG', '" + pdfstr + "_TVX', '" + pdfstr + "_WZ', '" + pdfstr + "_Triboson', '" + pdfstr + "_WrongSign', '" + pdfstr + "_ZZtoLep']")
                    #LineWrite(settname, "systgroups['theory group'] = ['ISR_sig', 'ISR_VG', 'ISR_TVX', 'ISR_TTTo2L2Nu', 'ISR_WZ', 'ISR_Triboson', 'ISR_WrongSign', 'ISR_ZZtoLep', 'FSR_sig', 'FSR_VG', 'FSR_TVX', 'FSR_TTTo2L2Nu', 'FSR_WZ', 'FSR_Triboson', 'FSR_WrongSign', 'FSR_ZZtoLep', 'QCDScale_sig', 'QCDScale_VG', 'QCDScale_TVX', 'QCDScale_TTTo2L2Nu', 'QCDScale_WZ', 'QCDScale_Triboson', 'QCDScale_WrongSign', 'QCDScale_ZZtoLep', '" + pdfstr + "_sig', '" + pdfstr + "_VG', '" + pdfstr + "_TVX', '" + pdfstr + "_WZ', '" + pdfstr + "_Triboson', '" + pdfstr + "_WrongSign', '" + pdfstr + "_ZZtoLep']")
                    LineWrite(settname, "if model != 'WpWpJJ':")
                    LineWrite(settname, "\tsystgroups['theory group'].append('QCDScale_WpWpJJ_QCD')")
                    LineWrite(settname, "\tsystgroups['theory group'].append('" + pdfstr + "_WpWpJJ_QCD')")
                else:
                    LineWrite(settname, "systgroups['theory group'] = ['ISR', 'FSR', '" + pdfstr + "_sig', '" + pdfstr + "_VG', '" + pdfstr + "_TVX', '" + pdfstr + "_WZ', '" + pdfstr + "_Triboson', '" + pdfstr + "_WrongSign', '" + pdfstr + "_ZZtoLep']")
                #LineWrite(settname, "\tsystgroups['theory group'].append('ISR_WpWpJJ_QCD')")
                #LineWrite(settname, "\tsystgroups['theory group'].append('FSR_WpWpJJ_QCD')")

    LineWrite(settname, "rpname=''")
    LineWrite(settname, "for idk, krp in enumerate(rateParams.keys()):")
    LineWrite(settname, "\tif idk%6 == 0:")
    LineWrite(settname, "\t\trpname = ''")
    LineWrite(settname, "\t\trpname = krp.split('_')[0].replace('est', 'norm group')")
    LineWrite(settname, "\t\tsystgroups[rpname] = [krp]")
    LineWrite(settname, "\telse:")
    LineWrite(settname, "\t\tsystgroups[rpname].append(krp)")
    LineWrite(settname, "")

    LineWrite(settname, "systgroups['PF group'] = ['PF']")
    LineWrite(settname, "systgroups['lumi group'] = ['lumi_2016M', 'lumi_2017', 'lumi_2018']")
    LineWrite(settname, "systgroups['btag group'] = ['btag', 'mistag']")
    LineWrite(settname, "systgroups['jet group'] = ['jes_sig', 'jes_VG', 'jes_TVX', 'jes_TTTo2L2Nu', 'jes_WZ', 'jes_Triboson', 'jes_WrongSign', 'jes_ZZtoLep', 'jer']")
    LineWrite(settname, "systgroups['Pileup group'] = ['pu', 'puID']")
    LineWrite(settname, "systgroups['VBS group'] = ['VBS']")
    LineWrite(settname, "systgroups['MET group'] = ['metUnclust']")
    LineWrite(settname, "systgroups['tau group'] = [")
    LineWrite(settname, "\t'TES',")
    LineWrite(settname, "\t'FES',")
    LineWrite(settname, "\t'tau_vsjet',")
    for lep in leps:
        LineWrite(settname, "\t'tau_vs" + leptags[lep] + "',")
    LineWrite(settname, "]")
    LineWrite(settname, "systgroups['lepton group'] = ['lep', 'PF']")
    if "CROS" in regions:
        LineWrite(settname, "systgroups['mischarge group'] = [")
        for lep in leps:
            LineWrite(settname, "\t'mischarge_" + lep + "_2016M',")
            LineWrite(settname, "\t'mischarge_" + lep + "_2017',")
            LineWrite(settname, "\t'mischarge_" + lep + "_2018',")
        LineWrite(settname, "]")
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
    LineWrite(settname, "\tsetpiecs.sort(reverse=True)")
    LineWrite(settname, "\tfor setpiec in setpiecs:")
    LineWrite(settname, "\t\tcombo = combo.replace(setpiec, \"\")")
    LineWrite(settname, "\tif ops[0].startswith('c') and not '_' in ops[0]:")
    LineWrite(settname, "\t\tsigs = [")
    LineWrite(settname, "\t\t\t'SM',")
    LineWrite(settname, "\t\t]")
    LineWrite(settname, "\telse:")
    LineWrite(settname, "\t\tsigs = [")
    LineWrite(settname, "\t\t\tops[0]+'_0',")
    LineWrite(settname, "\t\t]")
    LineWrite(settname, "\tfor op in ops:")
    LineWrite(settname, "\t\tsigs.append(op + '_SM')")
    LineWrite(settname, "\t\tsigs.append(op + '_BSM')")
    LineWrite(settname, "")
    LineWrite(settname, "\tlssamples_1D = {")
    LineWrite(settname, "\t\tcombo:collections.OrderedDict([])")
    LineWrite(settname, "\t}")
    #LineWrite(settname, "\tlssamples_1D[combo]['sm'] = 'VBS_SSWW_SM'")
    LineWrite(settname, "\tlssamples_1D[combo]['sm'] = 'VBS_SSWW_' + sigs[0]")
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
    LineWrite(settname, "elif model.startswith('c') and not \"_\" in model:")
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
    LineWrite(settname, "elif model.startswith('F') or (model.startswith('c') and \"_\" in model):")
    LineWrite(settname, "\tsigs = [")
    LineWrite(settname, "\t\tmodel + '_0',")
    LineWrite(settname, "\t\tmodel + '_SM',")
    LineWrite(settname, "\t\tmodel + '_BSM',")
    LineWrite(settname, "\t]")
    LineWrite(settname, "\tlssamples_1D = {")
    LineWrite(settname, "\t\tmodel.split(\"_\")[0]:collections.OrderedDict([")
    LineWrite(settname, "\t\t\t('sm', 'VBS_SSWW_' + sigs[0]),")
    LineWrite(settname, "\t\t\t('sm_lin_quad_' + model.split(\"_\")[0], 'VBS_SSWW_' + sigs[1]),")
    LineWrite(settname, "\t\t\t('quad_' + model.split(\"_\")[0], 'VBS_SSWW_' + sigs[2]),")
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
    LineWrite(settname, "print 'sigs:', sigs")
    LineWrite(settname, "print 'lssamples in settings:', lssamples_1D")
    LineWrite(settname, "sigpoints = [sigs]")

def WriteMeta(srvar, crvar, folder, model, cut, year = "2016M,2017,2018"):
    metasett = open("../python/metasett_" + model + "_" + srvar + "_" + crvar + "_" + folder + ".txt", "w")
    LineWrite(metasett, srvar + "," + crvar)
    LineWrite(metasett, folder)
    LineWrite(metasett, model)
    LineWrite(metasett, year)
    LineWrite(metasett, cut)
    metasett.close()

def RecursiveImport(module):
    if module in sys.modules:
        del sys.modules[module]
    print "Importing module", module 
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

def PrepareToRun(fold, year, tagfold, folder): 
    eosfolder = '/eos/home-a/apiccine/VBS/nosynch/' + fold + "/plot"
    if tagfold != "":
        eosfolder += tagfold
    eosfolder += "/"

    subfolders = [dirr for dirr in os.listdir(eosfolder) if not "_" in dirr]
    new_sf = [odirr.split("_")[0] for odirr in subfolders]
    yearsss = year.split(",")

    for i, odir in enumerate(new_sf):
        ofilelist = []
        for y in yearsss:
            ylist = [f for f in os.listdir(eosfolder + odir) if not 'countings' in f and y in f]
            for yfile in ylist:
                ofilelist.append(yfile)

            for of in ofilelist:
                if not (of.startswith('FakeMu_') or of.startswith('FakeEle_')):
                    continue
                    
                new_dest = eosfolder + new_sf[i] + "/"
                new_dest += of.replace("Mu", "").replace("Ele", "")

                if (os.path.exists(new_dest) and os.path.getmtime(new_dest) < os.path.getmtime(eosfolder + new_sf[i] + "/" + of)) or not os.path.exists(new_dest):
                    print "cp " + eosfolder + odir + "/" + of + " " + new_dest
                    os.system("cp " + eosfolder + odir + "/" + of + " " + new_dest)

def RunSMSignificance(model, srvar, crvar, fold, year, username, tagfold, pdftype, UseHybridNew, settmod, folder, unblind):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = filerepo + 'plot'
    plotrepo += tagfold + "/"
    
    folderhisto = folder + "/shapes"

    collhist = "python collectHistos.py -i " + plotrepo + " -o " + folderhisto + "/histo_" + model + ".root --model " + model + "_" + srvar + "_" + crvar + " --settmod " + settmod + " --pdf " + pdftype
    createdata = "python createDatacards.py -i " + folderhisto + "/histo_" + model + ".root -d " + folder + " --model " + model + "_" + srvar + "_" + crvar + " --settmod " + settmod
    runcomb = "python runCombine.py -y " + year + " -d " + folder + " -m hist --model " + model + "_" + srvar + "_" + crvar + " --settmod " + settmod
    if UseHybridNew:
        runcomb += " --HN"
    if unblind:
        runcomb += " -u"
    print '\n'
    print collhist
    os.system(collhist)
    print '\n'
    print createdata
    os.system(createdata)
    print '\n'    
    print runcomb
    os.system(runcomb)
    

def RunEWvsQCD(model, srvar, crvar, fold, year, username, tagfold, pdftype, settmod, folder, unblind):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = filerepo + 'plot'
    plotrepo += tagfold + "/"

    folderhisto = folder + "/shapes"

    collhist = "python collectHistos.py -i " + plotrepo + " -o " + folderhisto + "/histo_" + model + ".root --model " + model + "_" + srvar + "_" + crvar + " --settmod " + settmod + " --pdf " + pdftype
    createdata = "python createDatacards.py -i " + folderhisto + "/histo_" + model + ".root -d " + folder + " --model " + model + "_" + srvar + "_" + crvar + " --settmod " + settmod
    runcomb = "python runCombine.py -y " + year + " -d " + folder + " -m hist --model " + model + "_" + srvar + "_" + crvar + " --settmod " + settmod
    if unblind:
        runcomb += " -u"

    print '\n'
    print collhist
    os.system(collhist)
    print '\n'
    print createdata
    os.system(createdata)
    print '\n'
    print runcomb
    os.system(runcomb)

def RunEFTFit(model, srvar, crvar, fold, year, username, tagfold, addLambda8, pdftype, profile, settmod, folder, unblind):
    yeartag = year.replace("2016M,2017,2018", "RunII")
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = filerepo + 'plot'
    plotrepo += tagfold + "/"

    folderhisto = folder + "/shapes"

    collhist = "python collectHistos.py -i " + plotrepo + " -o " + folderhisto + "/histo_" + model + ".root --ls " + model + " --model " + model + "_" + srvar + "_" + crvar + " --settmod " + settmod + " --pdf " + pdftype
    createdata = "python createDatacards.py -i " + folderhisto + "/histo_" + model + ".root -d " + folder + " --ls " + model+ " --model " + model + "_" + srvar + "_" + crvar + " --settmod " + settmod
    runcomb = "python runCombine.py -y " + year + " -d " + folder + " -m hist --ls " + model + " --model " + model + "_" + srvar + "_" + crvar + " --settmod " + settmod 

    if addLambda8:
        collhist += " --Lambda8"
    if profile:
        runcomb += " --profile"
    if unblind:
        runcomb += " -u"
   
    print "\n"
    print collhist
    os.system(collhist)
    
    print "\n"
    print createdata
    os.system(createdata)
    
    print "\n"
    print runcomb
    os.system(runcomb)
    
def DoImpacts(modeltot, srvar, crvar, year, username, setmodd, folder, unblind):
    #optionals = " --cminDefaultMinimizerStrategy=1 --cminDefaultMinimizerTolerance 0.01 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.001 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND "#--fastScan" 
    #optionals = "  " 
    optionals = " --cminDefaultMinimizerStrategy=0 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT"# --cminDefaultMinimizerTolerance 0.01" --stepSize=0.001"# --robustFit=1"
    if not unblind:
        optionals += " -t -1 "
    else:
        pass

    settitle = setmodd
    RecursiveImport(settitle)
    settmod = importlib.import_module(settitle)
    systgroups = settmod.systgroups
    syst = settmod.syst
    ipwd = os.getcwd()
    yeartag = year.replace("2016M,2017,2018", "RunII")# + "_"
    channels = settmod.channels
    yearsett = settmod.years
    method = "hist"

    folderhisto = folder + "/shapes"

    partmodel = modeltot.split(":")

    isEFT = False
    if modeltot.startswith("c") or modeltot.startswith("F") or ":" in modeltot:
        isEFT = True 

    model = ""
    for idmt, mod in enumerate(partmodel):
        if idmt > 0:
            model += ":"
        if isEFT and mod.startswith("F"):
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
                cmdmer += cat+"_"+year+"=VBS_SSWW_%s_%s_%s_%s.txt " %(model, cat, year, method)
            else:
                cmdmer += cat+"_"+year+"=%s_%s_%s_%s.txt " %(model, cat, year, method)
    if not isEFT and not "WpWp" in model:
        cmdmer += "> VBS_SSWW_%s_%s.txt" % (model, method)
    else:
        cmdmer += "> %s_%s.txt" % (model, method)
    print cmdmer
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
            else:
                intervals.append("-100,100")

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
    
    cmd0 = "combine -M FitDiagnostics -d " + wscard + "  -n " + tag + "_t0"
    cmd1 = "combine -M FitDiagnostics -d " + wscard + "  -n " + tag + "_t1"

    if isEFT:               
        cmd0 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges " + intervalstr + " --setParameters r=1,"
        cmd1 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges " + intervalstr + " --setParameters r=1,"
        for idc, coeff in enumerate(coeffs):
            if idc > 0:
                cmd1 += ","
                cmd0 += ","
            cmd1 += "k_" + coeff + "=1"
            cmd0 += "k_" + coeff + "=0"
   
    
    else:
        cmd0 += " --expectSignal 0 --rMin -10"
        cmd1 += " --expectSignal 1 --rMin -10"
    
    cmd0 += " " + optionals
    cmd1 += " " + optionals
    
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
        

    imp0_0 = "combineTool.py -M Impacts -d " + wscard + "  --doInitialFit --allPars -m 1 -n " + tag + "_t0 --parallel 50 --autoRange 1 --autoBoundsPOIs r" 
    imp0_1 = "combineTool.py -M Impacts -d " + wscard + "  --doInitialFit --allPars -m 1 -n " + tag + "_t1 --parallel 50  --autoRange 1 --autoBoundsPOIs r"
    if isEFT:
        imp0_0 += "," + modComb
        imp0_1 += "," + modComb
        imp0_0 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges "+ intervalstr + " --setParameters r=1,"
        imp0_1 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges "+ intervalstr + " --setParameters r=1,"
        for idc, coeff in enumerate(coeffs):
            if idc > 0:
                imp0_1 += ","
                imp0_0 += ","
            imp0_1 += "k_" + coeff + "=1"
            imp0_0 += "k_" + coeff + "=0"
    
    else:
        imp0_0 += " --expectSignal 0 --rMin -10"
        imp0_1 += " --expectSignal 1 --rMin -10"

    imp0_0 += " " + optionals
    imp0_1 += " " + optionals


    imp1_0 = "combineTool.py -M Impacts -d " + wscard + " -o " + "impacts" + tag + "_t0.json  --doFits -m 1 -n " + tag + "_t0 --parallel 50 --autoRange 1 --autoBoundsPOIs r"
    imp1_1 = "combineTool.py -M Impacts -d " + wscard + " -o " + "impacts" + tag + "_t1.json  --doFits -m 1 -n " + tag + "_t1 --parallel 50 --autoRange 1 --autoBoundsPOIs r"

    if isEFT:
        imp1_0 += "," + modComb
        imp1_1 += "," + modComb

        imp1_0 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges "+ intervalstr + " --setParameters r=1,"
        imp1_1 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges "+ intervalstr + " --setParameters r=1,"
        for idc, coeff in enumerate(coeffs):
            if idc > 0:
                imp1_1 += ","
                imp1_0 += ","
            imp1_1 += "k_" + coeff + "=1"
            imp1_0 += "k_" + coeff + "=0"
   
    else:
        imp1_0 += " --expectSignal 0 --rMin -10"
        imp1_1 += " --expectSignal 1 --rMin -10"

    imp1_0 += " " + optionals
    imp1_1 += " " + optionals
    
    ctimp0 = "combineTool.py -M Impacts -d " + wscard + " -m 1 -n " + tag + "_t0 -o " +  "impacts" + tag + "_t0.json --parallel 50 --autoRange 1 --autoBoundsPOIs r"
    ctimp1 = "combineTool.py -M Impacts -d " + wscard + " -m 1 -n " + tag + "_t1 -o " +  "impacts" + tag + "_t1.json --parallel 50 --autoRange 1 --autoBoundsPOIs r"
  
    if isEFT:
        ctimp0 += "," + modComb
        ctimp1 += "," + modComb

        ctimp0 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges " + intervalstr + " --setParameters r=1,"
        ctimp1 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges " + intervalstr + " --setParameters r=1,"
        for idc, coeff in enumerate(coeffs):
            if idc > 0:
                ctimp1 += ","
                ctimp0 += ","
            ctimp1 += "k_" + coeff + "=1"
            ctimp0 += "k_" + coeff + "=0"
   
    else:
        ctimp0 += " --expectSignal 0 --rMin -10"
        ctimp1 += " --expectSignal 1 --rMin -10"

    ctimp0 += " " + optionals
    ctimp1 += " " + optionals
    
    printimp0 = "plotImpacts.py -i " +  "impacts" + tag + "_t0.json -o " +  "impacts" + tag + "_t0"
    printimp1 = "plotImpacts.py -i " +  "impacts" + tag + "_t1.json -o " +  "impacts" + tag + "_t1"

    printimp0 += " --blind "
    printimp1 += " --blind "

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
    
    os.system("rm higgsCombine_paramFit*")
    os.chdir(ipwd)

def DoGoF(modeltot, srvar, crvar, year, username, setmodd, folder, unblind):
    #optionals = "  " 
    algo = "saturated"
    ntoys = "1000"
    seed = "12345"
    optionals = " --cminDefaultMinimizerStrategy=0 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT"# --cminDefaultMinimizerTolerance 0.01" --stepSize=0.001"# --robustFit=1"
    #if not unblind:
    #toysop = " -t -1 "
    settitle = setmodd
    RecursiveImport(settitle)
    settmod = importlib.import_module(settitle)
    systgroups = settmod.systgroups
    syst = settmod.syst
    ipwd = os.getcwd()
    yeartag = year.replace("2016M,2017,2018", "RunII")# + "_"
    channels = settmod.channels
    yearsett = settmod.years
    method = "hist"

    folderhisto = folder + "/shapes"

    partmodel = modeltot.split(":")

    isEFT = False
    if modeltot.startswith("c") or modeltot.startswith("F") or ":" in modeltot:
        isEFT = True 

    model = ""
    for idmt, mod in enumerate(partmodel):
        if idmt > 0:
            model += ":"
        if isEFT and mod.startswith("F"):
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
                cmdmer += cat+"_"+year+"=VBS_SSWW_%s_%s_%s_%s.txt " %(model, cat, year, method)
            else:
                cmdmer += cat+"_"+year+"=%s_%s_%s_%s.txt " %(model, cat, year, method)
    if not isEFT and not "WpWp" in model:
        cmdmer += "> VBS_SSWW_%s_%s.txt" % (model, method)
    else:
        cmdmer += "> %s_%s.txt" % (model, method)
    print cmdmer
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
            else:
                intervals.append("-100,100")

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
   
    goffolder = folder + "/Checks_" + model + "/"
    #print goffolder
    if not os.path.exists(goffolder):
        os.system("mkdir " + goffolder)
    else:
        os.system("rm " + goffolder + "/higgsCombineTest*GoodnessOfFit*")
        os.system("rm " + goffolder + "/gof*")
    wscard = dcname + ".root"
    tag = model + "_" + srvar + "_" + crvar
    os.system("pwd")
    print "cd " + goffolder
    os.chdir(goffolder)
    
    cmdt2w ="text2workspace.py " + dcpath + " -o " + wscard
    if isEFT:
        cmdt2w += " -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative --X-allow-no-signal --PO eftOperators=" + opstring
    
    print cmdt2w
    os.system(cmdt2w)
    
    tagdata = "_data"
    tagtoys = "_toys"

    cmd0 = "combine -M GoodnessOfFit " + wscard + " --algo=saturated -n " + tagdata
    cmd1 = "combine -M GoodnessOfFit " + wscard + " --algo=saturated -t " + ntoys + " -s " + seed + " --toysFreq -n " + tagtoys

    if isEFT:               
        cmd0 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges " + intervalstr + " --setParameters r=1,"
        cmd1 += " --redefineSignalPOIs " + modComb + " --freezeParameters r  --setParameterRanges " + intervalstr + " --setParameters r=1,"
        for idc, coeff in enumerate(coeffs):
            if idc > 0:
                cmd1 += ","
                cmd0 += ","
            cmd1 += "k_" + coeff + "=1"
            cmd0 += "k_" + coeff + "=0"
    else:
        pass
        #cmd0 += " --expectSignal 0 --rMin -10"
        #cmd1 += " --expectSignal 1 --rMin -10"
    
    cmd0 += " " + optionals
    cmd1 += " " + optionals
    
    #if not ":" in modeltot:
    print cmd0
    os.system(cmd0)
    print cmd1
    os.system(cmd1)

    dataroot = "higgsCombine" + tagdata + ".GoodnessOfFit.mH120.root"
    toysroot = "higgsCombine" + tagtoys + ".GoodnessOfFit.mH120." + seed + ".root"
    gofjson = "combineTool.py -M CollectGoodnessOfFit --input " + dataroot + " " + toysroot + " -m 120.0 -o gof.json"
    gofprint = "plotGof.py gof.json --statistic saturated --mass 120.0 -o gof_plot --title-right=\"GoF saturated test\""

    print gofjson
    os.system(gofjson)
    print gofprint
    os.system(gofprint)

    os.chdir(ipwd)

    
def PrepareAndDoPostFit(model, srvar, crvar, plotvars, fold, cut, year, username, tagfold, addLambda8, PDFWithTTDY, DYrp, noQCDscale, pdftype, flnN, frp, setmodd, setitlee, fitfolderr, folder, regions, leptons, unblind):
    
    pwd = os.getcwd()
    vartopost = []
    yeartag = year.replace("2016M,2017,2018", "RunII")# + "_"
    filerepo = '/eos/home-' + username[0]+'/' + username+'/VBS/nosynch/' + fold + '/'
    plotrepo = filerepo + 'plot'
    plotrepo += tagfold + "/"

    fparts = fitfolderr.split("/")
    #eospost = filerepo + "postfit_" #+ pdftype + tagfold
    eospost = filerepo + "POST" + fparts[0].replace("_" + fold, "").replace("_DF", "").replace("_TF", "").replace("RESULTS", "").replace("Results", "")
    #"POSTFIT_" #+ pdftype + tagfold

    eospost += "_" + fparts[1] + "/" + fparts[2] + "/" + fparts[3]
    print "eospost:", eospost
    #raise ValueError("bye!")

    if plotvars == "all":
        vartopost = variables
    else:
        for var in variables:
            if var.name in plotvars.split(","):
                vartopost.append(var)

    for var in vartopost:
        varname = var.name
        folderhisto = folder + "/" + varname + "/shapes"
        print folderhisto
    
        if not os.path.exists(folder):
            os.system("mkdir -p " + folder) 
        if not os.path.exists(folderhisto):
            os.system("mkdir -p " + folderhisto) 

        #print varname, folder
    
        setitlevn = setitlee.replace(srvar, varname).replace(crvar, varname)
        WriteMeta(varname, varname, fold, model, cut, year)
        WriteSett(varname, varname, fold, model, cut, year, PDFWithTTDY, DYrp, pdftype, flnN, frp, regions, leptons, setitlevn, noQCDscale, False)

        setmodvn = setmodd.replace(srvar, varname).replace(crvar, varname)
        print "settings to import for control variable:", setitlevn, setmodvn
        RecursiveImport(setmodvn)
        #os.system("python PrepareEOSfolder.py " + fold)
    
        appendix = ""
        
        if not "SM" in model and not model.startswith("WpWp"):
            appendix += " --ls " + model
        
        datafolder = folder + "/" + varname
        #print datafolder
        
        if not os.path.exists(datafolder):
            os.system("mkdir " + datafolder)

        collhist = "python collectHistos.py -i " + plotrepo + " -o " + folderhisto + "/histo_" + model + "_" + varname + ".root " + appendix + " --model " + model + "_" + varname + "_" + varname + " --settmod " + setmodvn + " --pdf " + pdftype
        createdata = "python createDatacards.py -i " + folderhisto + "/histo_" + model + "_" + varname + ".root -d " + datafolder + appendix + " --model " + model + "_" + varname + "_" + varname + " --settmod " + setmodvn

        os.system(collhist)
        os.system(createdata)
    
        print "settings to import for fitting variable:", setitlee
    
        WriteMeta(srvar, crvar, fold, model, cut, year)
        WriteSett(srvar, crvar, fold, model, cut, year, PDFWithTTDY, DYrp, pdftype, flnN, frp, regions, leptons, setitlee, noQCDscale, False)
        RecursiveImport(setmodd)
    
        createpostfit = "python createPostFit.py --var " + varname + " --fitfolder " + fitfolderr + " --year " + year + " --model " + model + " --settmod " + setmodd + " --postfolder " + folder
        
        print "\n"
        print "unblind?", unblind
        if unblind:
            createpostfit += " -u "
        
        print createpostfit
        os.system(createpostfit)
        
        poststring = "python plotter/PreFitPostFit_v2.py --era " + yeartag + " --folder " + folder + " --vars " + var.name + " --fitted " + srvar + "," + crvar + " --model " + model + " --settmod " + setmodd + " --eos " + eospost
    
        if unblind:
            poststring += " -u"
        print "\n"
        print poststring
    
        if varname.startswith("DNN_"):
            os.system(poststring + " --lastbins")
            ##os.system(poststring + " --lastbins --scale")
            os.system(poststring + " --lastbins --linscale")
            ##os.system(poststring + " --lastbins --scale --linscale")

        os.system(poststring)
        os.system(poststring + " --linscale")
        ##os.system(poststring + " --scale --linscale")
        
        os.chdir(pwd)
    

def ProduceCLPlots(srvar, crvar, eftop, era, folder):
    command = "python ciplots.py --folder " + folder + " --op " + eftop + " --era " + era + " --srvar " + srvar + " --crvar " + crvar
    print command
    os.system(command)

def UncBreak(modeltot, srvar, crvar, year, username, setmodd, folder, unblind):
    optionalss = " --cminDefaultMinimizerStrategy=0 --X-rtd SIMNLL_NO_LEE --X-rtd NO_ADDNLL_FASTEXIT"# --setRobustFitTolerance=0.1 --cminDefaultMinimizerTolerance 0.1 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND"# --fastScan"
    if not unblind:
        optionalss += " -t -1 "
    if not ":" in modeltot:
        #points = "10"
        points = "750"#"10000"
    else:
        points = "20000"

    settitle = setmodd
    RecursiveImport(settitle)
    settmod = importlib.import_module(settitle)
    systgroups = settmod.systgroups
    syst = settmod.syst
    upwd = os.getcwd()
    
    yeartag = year.replace("2016M,2017,2018", "RunII")# + "_"
    channels = settmod.channels
    yearsett = settmod.years
    method = "hist"
    folderhisto = folder + "/shapes"

    partmodel = modeltot.split(":")

    isEFT = False
    if modeltot.startswith("c") or modeltot.startswith("F") or ":" in modeltot:
        isEFT = True 

    model = ""
    for idmt, mod in enumerate(partmodel):
        if idmt > 0:
            model += ":"
        if isEFT and mod.startswith("F"):
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
                cmdmer += cat+"_"+year+"=VBS_SSWW_%s_%s_%s_%s.txt " %(model, cat, year, method)
            else:
                cmdmer += cat+"_"+year+"=%s_%s_%s_%s.txt " %(model, cat, year, method)
    if not isEFT and not "WpWp" in model:
        cmdmer += "> VBS_SSWW_%s_%s.txt" % (model, method)
    else:
        cmdmer += "> %s_%s.txt" % (model, method)
    print cmdmer
    
    os.system(cmdmer)
    os.chdir(upwd)
        
    years = yearsett#.split(",")
    
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
            else:
                intervals.append("-100,100")

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
        print "YEARS", years
        for systgroup, subsysts in systgroups.items():
            sysrow = systgroup + "\t="
            approw = ""
            #print "\n\nsyst", syst
            print "\nsubsysts", subsysts
            for idsy, systname in enumerate(subsysts):
                if "norm " in systgroup:
                    approw += " " + systname
                elif syst[systname][0] == "lnN":
                    print systname, syst[systname]
                    #approw += " " + systname
                    if syst[systname][-1] == "uncorr":
                        print "hello1"
                        for yr in years:
                            approw += " " + systname + "_" + yr
                            print yr, approw
                    else:
                        print "hello2"
                        approw += " " + systname
                elif syst[systname][0].startswith("shape"):
                    print systname, syst[systname]
                    if syst[systname][-1] == "corr":
                        approw += " " + systname
                    elif syst[systname][-1] == "uncorr":
                        for yr in years:
                            approw += " " + systname + "_" + yr
            sysrow += approw
            dcfile.write("\n" + sysrow)
    print "datacard:", dcpath
    #raise ValueError("bye")
    impactfolder = upwd + "/" + folder + "/Checks_" + model + "/"
    if not os.path.exists(impactfolder):
        os.system("mkdir " + impactfolder)
    wscard = impactfolder + dcname + ".root"
    os.chdir(impactfolder)


    cmdt2w ="text2workspace.py " + dcpath + " -o " + wscard
    
    #raise ValueError("bye")
    if isEFT:
        cmdt2w += " -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative --X-allow-no-signal --PO eftOperators=" + opstring
    print cmdt2w
    os.system(cmdt2w)
    
    total = dcname + "_" + model + ".total"
    totalfile = "higgsCombine" + total + ".MultiDimFit.mH120.root"
    
    cmdmd = "combine " + wscard + " -M MultiDimFit -m 120 --points " + points + " --saveWorkspace -n " + total + " --algo grid"
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
        cmdmd += " --rMin -5 --rMax 5 --expectSignal=1"

    cmdmd += " " + optionalss

    print cmdmd
    os.system(cmdmd)
    
    md = "combine " + totalfile + " -M MultiDimFit -m 120 --points " + points + " --algo grid "
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
        md += " --rMin -5 --rMax 5 --expectSignal=1"
    
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

    mdfa = "combine " + totalfile + " -M MultiDimFit -m 120 --points " + points + " --algo grid "
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
        mdfa += " --rMin -5 --rMax 5 --expectSignal=1"
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
    
    os.system("rm higgsCombineWpWpJJ_hist.freeze*")
    os.chdir(upwd)
