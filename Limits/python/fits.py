from ROOT import RooRealVar, RooDataHist, RooArgList, RooGenericPdf, RooExtendPdf, RooWorkspace, RooFit


class fitFunc(object):
    pass

fitParam = {}

mT = RooRealVar(  "m_T",    "m_{T}",          1500., 3900., "GeV")





fitBDT0_2016 = fitFunc()
fitBDT0_2016.p1 = RooRealVar("CMS2016_BDT0_p1", "p1", -18.0947, -1000., 1000.)
fitBDT0_2016.p2 = RooRealVar("CMS2016_BDT0_p2", "p2", 22.8504, -10., 10.)
fitBDT0_2016.p3 = RooRealVar("CMS2016_BDT0_p3", "p3", 3.72973, -10., 10.)
fitBDT0_2016.modelBkg = RooGenericPdf("Bkg", "Bkg. fit (3 par.)", "pow(1 - @0/13000, @1) / pow(@0/13000, @2+@3*log(@0/13000))", RooArgList(mT, fitBDT0_2016.p1, fitBDT0_2016.p2, fitBDT0_2016.p3))

fitParam["BDT0_2016"] = fitBDT0_2016

fitBDT1_2016 = fitFunc()
fitBDT1_2016.p1 = RooRealVar("CMS2016_BDT1_p1", "p1",-13.1451, -1000., 1000.) 
fitBDT1_2016.p2 = RooRealVar("CMS2016_BDT1_p2", "p2", 13.1451, -10., 10.) 
fitBDT1_2016.p3 = RooRealVar("CMS2016_BDT1_p3", "p3", 2.91787, -10., 10.)
fitBDT1_2016.modelBkg = RooGenericPdf("Bkg", "Bkg. fit (3 par.)", "pow(1 - @0/13000, @1) / pow(@0/13000, @2+@3*log(@0/13000))", RooArgList(mT, fitBDT1_2016.p1, fitBDT1_2016.p2, fitBDT1_2016.p3))

fitParam["BDT1_2016"] = fitBDT1_2016

fitBDT2_2016 = fitFunc()
fitBDT2_2016.p1 = RooRealVar("CMS2016_BDT2_p1", "p1", 12.5899, -1000., 1000.)
fitBDT2_2016.p2 = RooRealVar("CMS2016_BDT2_p2", "p2", 6.71091, -10., 10.)
fitBDT2_2016.p3 = RooRealVar("CMS2016_BDT2_p3", "p3", 0.265957, -10., 10.)
fitBDT2_2016.modelBkg = RooGenericPdf("Bkg", "Bkg. fit (3 par.)", "pow(1 - @0/13000, @1) / pow(@0/13000, @2+@3*log(@0/13000))", RooArgList(mT, fitBDT2_2016.p1, fitBDT2_2016.p2, fitBDT2_2016.p3))

fitParam["BDT2_2016"] = fitBDT2_2016
 

fitCRBDT0_2016 = fitFunc()
fitCRBDT0_2016.p1 = RooRealVar("CMS2016_CRBDT0_p1", "p1", -4.55213, -1000., 1000.)
fitCRBDT0_2016.p2 = RooRealVar("CMS2016_CRBDT0_p2", "p2", 12.1878, -10., 10.)
fitCRBDT0_2016.p3 = RooRealVar("CMS2016_CRBDT0_p3", "p3", 1.34559, -10., 10.)
fitCRBDT0_2016.modelBkg = RooGenericPdf("Bkg", "Bkg. fit (3 par.)", "pow(1 - @0/13000, @1) / pow(@0/13000, @2+@3*log(@0/13000))", RooArgList(mT, fitCRBDT0_2016.p1, fitCRBDT0_2016.p2, fitCRBDT0_2016.p3))

fitParam["CRBDT0_2016"] =  fitCRBDT0_2016

fitCRBDT1_2016 = fitFunc()
fitCRBDT1_2016.p1 = RooRealVar("CMS2016_CRBDT1_p1", "p1", 5.17884, -1000., 1000.)
fitCRBDT1_2016.p2 = RooRealVar("CMS2016_CRBDT1_p2", "p2", 8.02836, -10., 10.)
fitCRBDT1_2016.p3 = RooRealVar("CMS2016_CRBDT1_p3", "p3", 0.293937, -10., 10.)
fitCRBDT1_2016.modelBkg = RooGenericPdf("Bkg", "Bkg. fit (3 par.)", "pow(1 - @0/13000, @1) / pow(@0/13000, @2+@3*log(@0/13000))", RooArgList(mT, fitCRBDT1_2016.p1, fitCRBDT1_2016.p2, fitCRBDT1_2016.p3))

fitParam["CRBDT1_2016"] = fitCRBDT1_2016

fitCRBDT2_2016 = fitFunc()
fitCRBDT2_2016.p1 = RooRealVar("CMS2016_CRBDT2_p1", "p1", 0.293937, -1000., 1000.)
fitCRBDT2_2016.p2 = RooRealVar("CMS2016_CRBDT2_p2", "p2", 6.03482, -10., 10.)
fitCRBDT2_2016.p3 = RooRealVar("CMS2016_CRBDT2_p3", "p3", -0.444019, -10., 10.)
fitCRBDT2_2016.modelBkg = RooGenericPdf("Bkg", "Bkg. fit (3 par.)", "pow(1 - @0/13000, @1) / pow(@0/13000, @2+@3*log(@0/13000))", RooArgList(mT, fitCRBDT2_2016.p1, fitCRBDT2_2016.p2, fitCRBDT2_2016.p3))

fitParam["CRBDT2_2016"] = fitCRBDT2_2016

#2017

fitBDT0_2017 = fitFunc()
fitBDT0_2017.p1 = RooRealVar("CMS2017_BDT0_p1", "p1", 2.97867, -1000., 1000.)
fitBDT0_2017.p2 = RooRealVar("CMS2017_BDT0_p2", "p2", 8.66029, -10., 10.)
fitBDT0_2017.p3 = RooRealVar("CMS2017_BDT0_p3", "p3", 0.983998, -10., 10.)
fitBDT0_2017.modelBkg = RooGenericPdf("Bkg", "Bkg. fit (3 par.)", "pow(1 - @0/13000, @1) / pow(@0/13000, @2+@3*log(@0/13000))", RooArgList(mT, fitBDT0_2017.p1, fitBDT0_2017.p2, fitBDT0_2017.p3))

fitParam["BDT0_2017"] = fitBDT0_2017

fitBDT1_2017 = fitFunc()
fitBDT1_2017.p1 = RooRealVar("CMS2017_BDT1_p1", "p1", -8.51945, -1000., 1000.)
fitBDT1_2017.p2 = RooRealVar("CMS2017_BDT1_p2", "p2", 17.6666, -10., 10.)
fitBDT1_2017.p3 = RooRealVar("CMS2017_BDT1_p3", "p3", 2.55651, -10., 10.)
fitBDT1_2017.modelBkg = RooGenericPdf("Bkg", "Bkg. fit (3 par.)", "pow(1 - @0/13000, @1) / pow(@0/13000, @2+@3*log(@0/13000))", RooArgList(mT, fitBDT1_2017.p1, fitBDT1_2017.p2, fitBDT1_2017.p3))

fitParam["BDT1_2017"] = fitBDT1_2017

fitBDT2_2017 = fitFunc()
fitBDT2_2017.p1 = RooRealVar("CMS2017_BDT2_p1", "p1", 16.1984, -1000., 1000.)
fitBDT2_2017.p2 = RooRealVar("CMS2017_BDT2_p2", "p2", 7.87966, -10., 10.)
fitBDT2_2017.p3 = RooRealVar("CMS2017_BDT2_p3", "p3", 7.87966, -10., 10.)
fitBDT2_2017.modelBkg = RooGenericPdf("Bkg", "Bkg. fit (3 par.)", "pow(1 - @0/13000, @1) / pow(@0/13000, @2+@3*log(@0/13000))", RooArgList(mT, fitBDT2_2017.p1, fitBDT2_2017.p2, fitBDT2_2017.p3))

fitParam["BDT2_2017"] = fitBDT2_2017

fitCRBDT0_2017 = fitFunc()
fitCRBDT0_2017.p1 = RooRealVar("CMS2017_CRBDT0_p1", "p1", -3.43573, -1000., 1000.)
fitCRBDT0_2017.p2 = RooRealVar("CMS2017_CRBDT0_p2", "p2", 12.1742, -10., 10.)
fitCRBDT0_2017.p3 = RooRealVar("CMS2017_CRBDT0_p3", "p3", 1.38987, -10., 10.)
fitCRBDT0_2017.modelBkg = RooGenericPdf("Bkg", "Bkg. fit (3 par.)", "pow(1 - @0/13000, @1) / pow(@0/13000, @2+@3*log(@0/13000))", RooArgList(mT, fitCRBDT0_2017.p1, fitCRBDT0_2017.p2, fitCRBDT0_2017.p3))

fitParam["CRBDT0_2017"] = fitCRBDT0_2017

fitCRBDT1_2017 = fitFunc()
fitCRBDT1_2017.p1 = RooRealVar("CMS2017_CRBDT1_p1", "p1", 3.09858, -1000., 1000.)
fitCRBDT1_2017.p2 = RooRealVar("CMS2017_CRBDT1_p2", "p2", 8.63151, -10., 10.)
fitCRBDT1_2017.p3 = RooRealVar("CMS2017_CRBDT1_p3", "p3", 0.338806, -10., 10.)
fitCRBDT1_2017.modelBkg = RooGenericPdf("Bkg", "Bkg. fit (3 par.)", "pow(1 - @0/13000, @1) / pow(@0/13000, @2+@3*log(@0/13000))", RooArgList(mT, fitCRBDT1_2017.p1, fitCRBDT1_2017.p2, fitCRBDT1_2017.p3))

fitParam["CRBDT1_2017"] = fitCRBDT1_2017

fitCRBDT2_2017 = fitFunc()
fitCRBDT2_2017.p1 = RooRealVar("CMS2017_CRBDT2_p1", "p1", 11.0279, -1000., 1000.)
fitCRBDT2_2017.p2 = RooRealVar("CMS2017_CRBDT2_p2", "p2", 5.72807, -10., 10.)
fitCRBDT2_2017.p3 = RooRealVar("CMS2017_CRBDT2_p3", "p3", -0.512612, -10., 10.)
fitCRBDT2_2017.modelBkg = RooGenericPdf("Bkg", "Bkg. fit (3 par.)", "pow(1 - @0/13000, @1) / pow(@0/13000, @2+@3*log(@0/13000))", RooArgList(mT, fitCRBDT2_2017.p1, fitCRBDT2_2017.p2, fitCRBDT2_2017.p3))

fitParam["CRBDT2_2017"] = fitCRBDT2_2017
