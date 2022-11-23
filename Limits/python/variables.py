from array import array

class variabile(object):
    def __init__(self, name, title, ApplySyst, nbins, xmin, xmax=None, smtitle = "def"):
        self.name=name
        self.title=title
        self.nbins=nbins
        self.xmin=xmin
        self.ApplySyst = ApplySyst
        if smtitle == "def":
            self.smtitle = title.replace(" [GeV]", "") 
        else:
            self.smtitle = smtitle
        if xmax==None:
            self._xmax=xmin[nbins]
            self._iscustom = True
        else:
            self._xmax=xmax
            self._iscustom = False

    def ApplySyst(self):
        self._ApplySyst = True

    def IsSystApplied(self):
        return self._ApplySyst

variables = []

variables.append(variabile('countings', 'countings', True, 1, -0.5, 0.5, smtitle = "evts"))#
'''        
bin_bdtsm = array("d", [0., 0.1, 0.2, 0.4, 0.6, 0.8, 1.])
nbin_bdtsm = len(bin_bdtsm) - 1
'''

#bin_bdtsm_dev = array("d", [0., 0.5, 0.6, 0.7, 0.8, 0.9, 1.])
#bin_bdtsm_dev = array("d", [0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.])                                           
bin_bdtsm_dev = array("d", [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.82, 0.84, 0.86, 0.88, 0.90, 0.92, 0.94, 0.96, 0.98, 1.])
nbin_bdtsm_dev = len(bin_bdtsm_dev) - 1

variables.append(variabile('DNN_SM_final_1', 'SM DNN output (final 1)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM DNN (final)"))
variables.append(variabile('DNN_SM_rec', 'SM DNN output (reco)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM DNN (reco)"))

variables.append(variabile('DNN_dim6_final_2', 'dim6 DNN output (final 2)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "dim6"))
variables.append(variabile('DNN_dim8_final_3', 'dim8 DNN output (final 3)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "dim8 f3"))
variables.append(variabile('DNN_dim8_final_3_1to2', 'dim8 DNN output (final 3 1to2)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "dim8 f3 1to2"))
variables.append(variabile('DNN_dim8_final_3_again', 'dim8 DNN output (final 3)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "dim8 f3 again"))
variables.append(variabile('DNN_dim6_final_2_noQUAD', 'dim6 DNN output (final 2 noQUAD)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "dim6 LIN"))
variables.append(variabile('DNN_dim8_final_3_noQUAD_fix', 'dim8 DNN output (final 3 noQUAD)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "dim8 LIN"))
variables.append(variabile('DNN_dim8_final_3_NOMOREDY_test', 'dim8 DNN output (f3 NMR test)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "dim8 f3 NMR test"))


variables.append(variabile('DNN_SM_final_1_NOMOREDY_test', 'SM DNN output (f1 NMR test)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM DNN (f1 NMR test)"))
variables.append(variabile('DNN_dim8_final_3_NOMOREDY_test', 'dim8 DNN output (f3 NMR test)', True, nbin_bdtsm_dev, bin_bdtsm_dev, "dim8 DNN f3 NMR test"))
#variables.append(variabile('DNN_dim6_final_2_NOMOREDY_test', 'dim6 DNN output (f2 NMR test)', True, nbin_bdtsm_dev, bin_bdtsm_dev, "dim6 DNN f2 NMR test"))



variables.append(variabile('DNN_SM_final_1_NOMOREDY_lower', 'SM DNN output (lower LR)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM DNN  (f1 NMR lower)"))
variables.append(variabile('DNN_SM_final_1_NOMOREDY_lower_4000', 'SM DNN output (lower LR 4000)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM DNN (f1 NMR lower 4000)"))
variables.append(variabile('DNN_SM_final_1_NOMOREDY_lower_4001', 'SM DNN output (lower LR 4001)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM DNN (f1 NMR lower 4001)"))
variables.append(variabile('DNN_SM_final_1_NOMOREDY_lower_bisnotopt', 'SM DNN output (lower LR bis)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM DNN (f1 NMR lower bis)"))
variables.append(variabile('DNN_SM_final_1_NOMOREDY_lower_bisnotopt_4000', 'SM DNN output (lower LR bis 4000)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM DNN (f1 NMR lower bis 4000)"))
variables.append(variabile('DNN_SM_final_1_NOMOREDY_lower_bisnotopt_4001', 'SM DNN output (lower LR bis 4001)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM DNN (f1 NMR lower bis 4001)"))
variables.append(variabile('DNN_dim6_final_2_NOMOREDY_test_nodivide', 'dim6 DNN output (f2 NMR test nodivide)', True, nbin_bdtsm_dev, bin_bdtsm_dev, "dim6 f2 NMR test nodivide"))
variables.append(variabile('DNN_dim6_final_2_NOMOREDY_lower_halfway', 'dim6 DNN output (f2 NMR lower halfway)', True, nbin_bdtsm_dev, bin_bdtsm_dev, "dim6 f2 NMR lower hw"))
variables.append(variabile('DNN_dim8_final_3_NOMOREDY_lower', 'dim8 DNN output (f3 NMR lower)', True, nbin_bdtsm_dev, bin_bdtsm_dev, "dim8 f3 NMR lower"))


#variables.append(variabile('DNN_pol_final_1', 'pol DNN output (final 1)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "pol DNN (final)"))

#variables.append(variabile('BDT_SM_final_1', 'SM BDT output (final 1)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM BDT (final)"))
#variables.append(variabile('BDT_dim6_final_1', 'dim6 BDT output (final 1)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "dim6 BDT (final)"))
#variables.append(variabile('BDT_dim8_final_1', 'dim8 BDT output (final 1)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "dim8 BDT (final)"))
#variables.append(variabile('BDT_pol_final_1', 'pol BDT output (final 1)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "pol BDT (final)"))


#variables.append(variabile('DNN_SM_50I_TV', 'SM DNN output (50I TV)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM DNN (50I TV)"))

#variables.append(variabile('DNN_cHW_50I_TV2', 'c_{HW} DNN output (50I TV2)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "c_{HW} DNN (50I TV2)"))
#variables.append(variabile('DNN_cW_50I_TV0', 'c_{HW} DNN output (50I TV0)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "c_{W} DNN (50I TV0)"))#

#variables.append(variabile('DNN_fS_50I_TV1', 'f_{S} DNN output (50I TV1)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "f_{S} DNN (50I TV1)"))
#variables.append(variabile('DNN_fT_50I_TV1', 'f_{T} DNN output (50I TV1)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "f_{T} DNN (50I TV1)"))
#variables.append(variabile('DNN_fM_50I_TV1', 'f_{M} DNN output (50I TV1)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "f_{M} DNN (50I TV1)"))

#variables.append(variabile('DNN_POL_50I_TV', 'Pol. DNN output (50I TV)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM DNN (50I TV)"))

#variables.append(variabile('DNN_cHW_final_1', 'c_{HW} DNN output (final 1)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "c_{HW} DNN (final 1)"))
#variables.append(variabile('DNN_dim6_final_2', 'dim6 DNN output (final 2)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "dim6 DNN (final 2)"))
#variables.append(variabile('DNN_dim8_final_2', 'dim8 DNN output (final 2)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "dim8 DNN (final 2)"))
#variables.append(variabile('DNN_dim8_final_3', 'dim8 DNN output (final 3)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "dim8 DNN (final 3)"))
'''
variables.append(variabile('DNN_SM_50I_TV1', 'SM DNN output (50I TV1)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM DNN (50I TV1)"))
variables.append(variabile('DNN_SM_ACAT', 'SM DNN output (ACAT)', True, nbin_bdtsm_dev, bin_bdtsm_dev, smtitle = "SM DNN (ACAT)"))
#variables.append(variabile('DNN_SM_UL035_v2', 'SM DNN output', True, 5, 0., 1., smtitle = "SM DNN"))
variables.append(variabile('DNN_SM_UL035_novar', 'SM DNN output', True, 5, 0., 1., smtitle = "SM DNN"))
variables.append(variabile('DNN_SM_UL035_novar_truesr_allbkg', 'SM DNN output', True, 5, 0., 1., smtitle = "SM DNN"))
#variables.append(variabile('DNN_SM_UL035_T_DYL', 'SM DNN output', True, 5, 0., 1., smtitle = "SM DNN"))
#variables.append(variabile('DNN_cW_UL035_v2', 'c_{W} DNN output', True, 5, 0., 1., smtitle = "c_{W} DNN"))
variables.append(variabile('DNN_cW_UL035_novar', 'c_{W} DNN output', True, 5, 0., 1., smtitle = "c_{W} DNN"))
#variables.append(variabile('DNN_cHW_UL035_v2', 'c_{HW} DNN output', True, 5, 0., 1., smtitle = "c_{HW} DNN"))
variables.append(variabile('DNN_cHW_UL035_novar', 'c_{HW} DNN output', True, 5, 0., 1., smtitle = "c_{HW} DNN"))
#variables.append(variabile('DNN_aQGC_UL035_v2', 'aQGC DNN output', True, 5, 0., 1., smtitle = "a_{QGC} DNN"))
variables.append(variabile('DNN_aQGC_UL035_novar', 'aQGC DNN output', True, 5, 0., 1., smtitle = "a_{QGC} DNN"))
variables.append(variabile('DNN_FT_UL035_novar', 'f_{T} DNN output', True, 5, 0., 1., smtitle = "f_{T} DNN"))
variables.append(variabile('DNN_FM_UL035_novar', 'f_{M} DNN output', True, 5, 0., 1., smtitle = "f_{M} DNN"))
variables.append(variabile('DNN_FS_UL035_novar', 'f_{S} DNN output', True, 5, 0., 1., smtitle = "f_{S} DNN"))
variables.append(variabile('DNN_FT_UL035_novar_fix', 'f_{T} DNN output', True, 5, 0., 1., smtitle = "f_{T} DNN"))
variables.append(variabile('DNN_FM_UL035_novar_fix', 'f_{M} DNN output', True, 5, 0., 1., smtitle = "f_{M} DNN"))
variables.append(variabile('DNN_FS_UL035_novar_fix', 'f_{S} DNN output', True, 5, 0., 1., smtitle = "f_{S} DNN"))
'''
'''
variables.append(variabile('BDT_SM_UL035_v2', 'SM BDT output', True, 5, 0., 1., smtitle = "SM BDT"))
variables.append(variabile('BDT_SM_UL035_novar_SR', 'SM BDT output', True, 5, 0., 1., smtitle = "SM BDT"))
variables.append(variabile('BDT_SM_UL035_novar', 'SM BDT output', True, 5, 0., 1., smtitle = "SM BDT"))
variables.append(variabile('BDT_SM_UL035_T_DYL', 'SM BDT output', True, 5, 0., 1., smtitle = "SM BDT"))
variables.append(variabile('BDT_cW_UL035_v2', 'c_{W} BDT output', True, 5, 0., 1., smtitle = "c_{W} BDT"))
variables.append(variabile('BDT_cW_UL035_novar', 'c_{W} BDT output', True, 5, 0., 1., smtitle = "c_{W} BDT"))
variables.append(variabile('BDT_cHW_UL035_v2', 'c_{HW} BDT output', True, 5, 0., 1., smtitle = "c_{HW} BDT"))
variables.append(variabile('BDT_aQGC_UL035_v2', 'aQGC BDT output', True, 5, 0., 1., smtitle = "a_{QGC} BDT"))
'''
#variables.append(variabile('DNN_pol_UL030', 'LL vs TX VBS DNN output', True, 5, 0., 1., smtitle = "pol DNN"))
#variables.append(variabile('BDT_pol_UL030', 'LL vs TX VBS BDT output', True, 5, 0., 1., smtitle = "pol BDT"))

bin_m1 = array("d", [0., 100., 150., 200., 300., 500.])
nbin_m1 = len(bin_m1) - 1 
variables.append(variabile('m_1T', 'M_{1T} [GeV]', True, nbin_m1, bin_m1))
variables.append(variabile('m_o1', 'M_{o1} [GeV]', True, nbin_m1, bin_m1))

bin_mjj = array("d", [0., 300., 500., 700., 1000., 1500., 2000.])
nbin_mjj = len(bin_mjj) - 1 
variables.append(variabile('m_jj', 'invariant mass j_{1} j_{2} [GeV]', True, nbin_mjj, bin_mjj))

'''
######### without systematics ###########

#variables.append(variabile('lepton_eta', 'lepton  #eta', True, 12, -3., 3.))
##variables.append(variabile('lepton_phi', 'lepton  #phi', False, 14, -3.50, 3.50))

bin_lepton_pt = array("d", [0., 30., 45., 60., 80., 100., 150, 250.])
nbin_lepton_pt = len(bin_lepton_pt)-1
variables.append(variabile('lepton_pt', 'lepton  p_{T} [GeV]', True, nbin_lepton_pt, bin_lepton_pt))

variables.append(variabile('lepton_eta', 'lepton #eta', True, 10, -2.5, 2.5))
variables.append(variabile('lepton_phi', 'lepton #phi',  True, 7, -3.50, 3.50))

bin_zepp = array("d", [-1., -0.75, -0.5, -0.25, 0., 0.25, 0.5, 0.75, 1.])
nbin_zepp = len(bin_zepp)-1
variables.append(variabile('event_Zeppenfeld_over_deltaEta_jj', 'event Zeppenfeld', True, 8, -1., 1.))

bin_taupt = array("d", [30., 45., 60., 80., 100., 125., 150, 200., 250.])
nbin_taupt = len(bin_taupt) - 1
variables.append(variabile('tau_pt', '#tau p_{T} [GeV]', True, nbin_taupt, bin_taupt))

bin_taum = array("d", [0., 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6])
nbin_taum = len(bin_taum) - 1
variables.append(variabile('tau_mass', '#tau mass [GeV]', True, nbin_taum, bin_taum))

variables.append(variabile('tau_eta','#tau #eta', True, 10, -2.5, 2.5))
##variables.append(variabile('tau_Zeppenfeld_over_deltaEta_jj', 'z_{#tau}', False, 12, -1.5, 1.5))

variables.append(variabile('tau_phi','#tau #Phi', True,  7, -3.50, 3.50))
##variables.append(variabile('tau_DecayMode', '#tau decay mode', False, 12, -0.5, 11.5))
    
variables.append(variabile('tauleadTk_ptOverTau',  '#tau LeadTk relative p_{T}', True, 10, 0, 1))
##variables.append(variabile('tauleadTk_deltaPhi',  '#tau LeadTk relative #Delta#phi', False, 8, -0.2, 0.4))
##variables.append(variabile('tauleadTk_deltaEta',  '#tau LeadTk relative #Delta#eta', False, 8, -0.4, 0.4))
variables.append(variabile('tauleadTk_Gamma',  '#tau LeadTk #Upsilon', True, 12, -1., 1.2))
variables.append(variabile('tau_DecayMode', '#tau Decay Mode', True, 12, -0.5, 11.5))

#bintaujetrelpt = array("d", [0.85, 0.9, 0.92, 0.94, 0.96, 0.98, 1.])
#nbin_taujetrelpt = len(bin_taujetrelpt) - 1
##variables.append(variabile('taujet_relpt',  '#tau jet relative p_{T}', False, nbin_taujetrelpt, bin_taujetrelpt))
##variables.append(variabile('taujet_deltaPhi',  '#tau jet relative #Delta#phi', False, 5, -0.25, 0.24))
##variables.append(variabile('taujet_deltaEta',  '#tau jet relative #Delta#eta', False, 5, -0.25, 0.25))


#bintaujetrelpt = array("d", [-1., -0.4, -0.2, 0., 0.2, 0.4, 0.6, 0.8, 1.])
#nbin_taujetrelpt = len(bin_taujetrelpt) - 1

#bintaujethg = array("d", [-1., -0.4, -0.2, 0., 0.2, 0.4, 0.6, 0.8, 1.])
#nbin_taujethg = len(bin_taujethg) - 1
##variables.append(variabile('taujet_HadGamma',  '#tau jet had. #Upsilon', False, nbin_taujethg, bin_taujethg))
##variables.append(variabile('taujet_EmGamma',  '#tau jet em. #Gamma', False, 8, -1., 1.))
##variables.append(variabile('taujet_HEGamma',  '#tau jet had.+em. #Gamma', False, 8, -1., 1.))

variables.append(variabile('tau_DeepTauVsEle_raw', '#tau DeepTauVsEle raw', True,  10, 0.35, 1.35))
variables.append(variabile('tau_DeepTauVsMu_raw', '#tau DeepTauVsMu raw', True,  10, 0.2, 1.2))
##variables.append(variabile('tau_DeepTauVsJet_raw', '#tau DeepTauVsJet raw', False,  10, 0., 1.))

###variables.append(variabile('tau_DeepTauVsEle_WP', '#tau DeepTauVsEle WP', False,  11, -0.5, 10.5))
###variables.append(variabile('tau_DeepTauVsMu_WP', '#tau DeepTauVsMu WP', False,  11, -0.5, 10.5))
###variables.append(variabile('tau_DeepTauVsJet_WP', '#tau DeepTauVsJet WP', False,  11, -0.5, 10.5))

binleadjet_pt = array("d", [0., 50., 100., 150., 250., 400.])
nbin_leadjet_pt = len(binleadjet_pt)-1
variables.append(variabile('leadjet_pt',  'Lead jet p_{T} [GeV]', True, nbin_leadjet_pt, binleadjet_pt))
variables.append(variabile('leadjet_eta', 'Lead jet #eta', True, 10, -5., 5.))
variables.append(variabile('leadjet_phi', 'Lead jet #Phi', True,  7, -3.50, 3.50))

##variables.append(variabile('leadjet_qgl', 'Lead jet QGL', False,  8, 0., 1.))
##variables.append(variabile('subleadjet_qgl', 'Sublead jet QGL', False,  8, 0., 1.))

bin_leadjet_mass = array("d", [0., 10., 20., 30., 50.])
nbin_leadjet_mass = len(bin_leadjet_mass)-1
variables.append(variabile('leadjet_mass',  'Lead jet mass [GeV]', True, nbin_leadjet_mass, bin_leadjet_mass))

binsubleadjet_pt = array("d", [0., 50., 100., 200.])
nbin_subleadjet_pt = len(binsubleadjet_pt) - 1
variables.append(variabile('subleadjet_pt', 'Sublead jet p_{T} [GeV]', True, nbin_subleadjet_pt, binsubleadjet_pt))
variables.append(variabile('subleadjet_eta', 'Sublead jet #eta', True, 10, -5., 5.))
variables.append(variabile('subleadjet_phi', 'Sublead jet #Phi', True,  7, -3.50, 3.50))

variables.append(variabile('nJets', 'n jets', True,  11, -0.5, 10.5))
variables.append(variabile('nBJets', 'n bjets (DeepJet M)', True,  6, -0.5, 5.5))

binmetpt = array("d", [0., 20., 50., 100., 150., 200., 300., 500.])
nbin_metpt = len(binmetpt) - 1
variables.append(variabile('MET_pt', 'p_{T}^{miss} [GeV]', True, nbin_metpt, binmetpt))

bin_invm = array("d", [0., 150., 300., 450., 600., 750., 900., 1200., 1400., 1600., 1800., 2000., 2500.])
nbin_invm = len(bin_invm) - 1 
variables.append(variabile('m_jjtau', 'invariant mass j_{1} j_{2} tau [GeV]', True, nbin_invm, bin_invm))

#variables.append(variabile('m_jjtaulep', 'invariant mass j_{1} j_{2} #tau l [GeV]', True, nbin_invm, bin_invm))
##variables.append(variabile('m_jjleps', 'invariant mass j_{1} j_{2} #tau l [GeV]', False, nbin_invm, bin_invm))

bin_invmtl = array("d", [0., 50., 100., 150., 200., 300.])
nbin_invmtl = len(bin_invmtl) - 1 
variables.append(variabile('m_taulep', 'invariant mass #tau l [GeV]', True, nbin_invmtl, bin_invmtl))

bin_mTs = array("d", [0., 50., 100., 150., 300.])
nbin_mTs = len(bin_mTs) - 1
variables.append(variabile('mT_lep_MET', 'M_{T}(' + 'lepton , MET) [GeV]', True, nbin_mTs, bin_mTs))
variables.append(variabile('mT_tau_MET', 'M_{T}( tau, MET) [GeV]', True, nbin_mTs, bin_mTs))
variables.append(variabile('mT_leptau_MET', 'M_{T}(l,  tau, MET) [GeV]', True, nbin_mTs, bin_mTs))

bin_deltaeta_jj = array("d", [-8., -6., -5., -4.5, -4., -3.5, -3., -2.5, 2.5, 3., 3.5, 4., 4.5, 5., 6., 8.])
nbin_deltaeta_jj = len(bin_deltaeta_jj) - 1
variables.append(variabile('deltaEta_jj', '#Delta #eta_{jj}', True, nbin_deltaeta_jj, bin_deltaeta_jj))

variables.append(variabile('deltaPhi_jj', '#Delta #phi_{jj}', True,  14, -3.5, 3.5))
##variables.append(variabile('deltaPhi_taulep', '#Delta #phi_{#tau l}', False,  14, -3.5, 3.5))
variables.append(variabile('deltaPhi_tau' + 'j1', '#Delta #phi_{tau j_{1}}', True,  14, -3.5, 3.5))
variables.append(variabile('deltaPhi_tau' + 'j2', '#Delta #phi_{tau j_{2}}', True,  14, -3.5, 3.5))
variables.append(variabile('deltaPhi_lepj1', '#Delta #phi_{' + 'lepton  j_{1}}', True, 14, -3.5, 3.5))
variables.append(variabile('deltaPhi_lepj2', '#Delta #phi_{' + 'lepton  j_{2}}', True, 14, -3.5, 3.5))

bindeltaeta_ll = array("d", [-6., -3., -2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2., 3., 6.])
nbin_deltaeta_ll = len(bindeltaeta_ll) - 1

variables.append(variabile('deltaEta_taulep', '#Delta #eta_{#tau l}', True,  nbin_deltaeta_ll, bindeltaeta_ll))

#bindeltaeta_lj = array("d", [-6., -4., -3., -2., -1., 0., 1., 2., 3., 4., 6.])
#nbin_deltaeta_lj = len(bin_deltaeta_lj) - 1
##variables.append(variabile('deltaEta_tau' + 'j1', '#Delta #eta_{tau j_{1}}', False,  nbin_deltaeta_lj, bin_deltaeta_lj))
##variables.append(variabile('deltaEta_tau' + 'j2', '#Delta #eta_{tau j_{2}}', False, nbin_deltaeta_lj, bin_deltaeta_lj))
##variables.append(variabile('deltaEta_lepj1', '#Delta #eta_{' + 'lepton  j_{1}}', False, nbin_deltaeta_lj, bin_deltaeta_lj))
##variables.append(variabile('deltaEta_lepj2', '#Delta #eta_{' + 'lepton  j_{2}}', False, nbin_deltaeta_lj, bin_deltaeta_lj))

bin_deltatheta_jj = array("d", [-1., -0.8, -0.4, 0.4, 0.8, 1.])
nbin_deltatheta_jj = len(bin_deltatheta_jj) - 1
variables.append(variabile('deltaTheta_taulep', 'cos(#Delta#theta_{#tau lep})', True,  nbin_deltatheta_jj, bin_deltatheta_jj))

bin_ptRel = array("d", [0., 25., 50., 75., 100., 150., 200.])
bin_ptRel_2 = array("d", [0., 25., 50., 100., 150., 250.])
nbin_ptRel = len(bin_ptRel) - 1
nbin_ptRel_2 = len(bin_ptRel_2) - 1    
#variables.append(variabile('ptRel_jj', 'relative p_{T} j_{1} j_{2}', False, nbin_ptRel, bin_ptRel))
##variables.append(variabile('ptRel_taulep', 'relative p_{T} ' + lep12[1], False, nbin_ptRel_2, bin_ptRel_2))
variables.append(variabile('ptRel_tau' + 'j1', 'relative p_{T} tau j_{1}', True, nbin_ptRel_2, bin_ptRel_2))
variables.append(variabile('ptRel_tau' + 'j2', 'relative p_{T} tau j_{2}', True, nbin_ptRel_2, bin_ptRel_2))
variables.append(variabile('ptRel_lepj1', 'relative p_{T} ' + 'lepton  j_{1}', True, nbin_ptRel, bin_ptRel))
variables.append(variabile('ptRel_lepj2', 'relative p_{T} ' + 'lepton  j_{2}', True, nbin_ptRel, bin_ptRel))

variables.append(variabile('event_RT', 'R_{T}', True, 15, 0., 3.))

variables.append(variabile('leadjet_DeepFlv_b', 'leading jet DeepFlavour b raw', True, 5, 0., 1.))
variables.append(variabile('subleadjet_DeepFlv_b', 'subleading jet DeepFlavour b raw', True, 5, 0., 1.))
'''
