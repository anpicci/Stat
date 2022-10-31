#python FitAndPlot.py --year RunII --folder vUL040 --eft cW --fit DNN_cW_UL025_bal_v2,DNN_cHW_UL025_bal,BDT_cW_xgb_UL025_bal_noopt,BDT_cHW_xgb_UL025_bal_noopt,m_o1 --doPost --notImpacts --notCI
#python FitAndPlot_dev.py --year RunII --folder vUL040 --eft cW:FT0_1p0 --fit m_o1 --notUncBreak --tDMcut --notImpacts --notCI --Lambda8
#python FitAndPlot_dev.py --year RunII --folder vUL040 --eft FM1_0p9 --fit m_o1 --tDMcut --notUncBreak --notImpacts --notCI
#python FitAndPlot_loc.py --year RunII --folder vUL040 --eft cHW:FS0_1p0 --fit m_o1 --tDMcut --notUncBreak --notImpacts --notCI

#python FitAndPlot.py --year RunII --folder vUL040 --eft cW:FM1_0p9 --fit m_o1 --notImpacts --notUncBreak --notCI
#python FitAndPlot.py --year RunII --folder vUL040 --eft FM1_0p9 --fit m_o1 --notImpacts --notUncBreak --notCI
#python FitAndPlot.py --year RunII --folder vUL040 --eft FS2_1p0 --fit m_o1,DNN_aQGC_UL040_novar,DNN_FS_UL040_novar_fix --notImpacts --notUncBreak --tDMcut --noFit
#python FitAndPlot.py --year RunII --folder vUL040 --eft FS2_1p0 --fit DNN_FS_UL040_novar_fix --notUncBreak --tDMcut --noFit --notCI
#python FitAndPlot_dev.py --year RunII --folder vUL040 --eft FT0_1p0 --fit DNN_FT_UL040_novar_fix --notUncBreak --tDMcut --noFit
#python FitAndPlot_dev.py --year RunII --folder vUL040 --eft cW --fit m_1T --notCI --notUncBreak --notCI --tDMcut --noFit
#python FitAndPlot.py --year RunII --folder vUL040 --eft FM7_1p0 --fit DNN_FM_UL040_novar --tDMcut --notUncBreak --noFit --notCI

#python FitAndPlot.py --year RunII --folder vUL040 --sm --vbs --fit BDT_SM_UL040_v2 --doPost --plot m_o1
#python FitAndPlot.py --year RunII --folder vUL040 --sm --vbs --fit DNN_SM_UL040_v2 --doPost --plot m_o1
#python FitAndPlot.py --year RunII --folder vUL040 --sm --vbs --fit m_o1 --doPost --plot m_o1 --notImpacts --notUncBreak

#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwp --fit BDT_SM_UL040_v2 --doPost --plot m_o1 --notImpacts --notUncBreak
#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwp --fit DNN_SM_UL040_v2 --doPost --plot m_o1
#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwp --fit m_o1 --doPost --plot m_o1 --notImpacts --notUncBreak

#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwpEW --fit BDT_SM_UL040_v2 --doPost --plot m_o1 --notImpacts --notUncBreak
#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwpEW --fit DNN_SM_UL040_v2 --doPost --plot m_o1
#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwpEW --fit m_jj --notUncBreak --notImpacts --tDMcut
#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwp --fit m_jj --notUncBreak --tDMcut --WithFakeCR --PDFWithTTDY --noFit #--doPost --plot m_o1
#python FitAndPlot.py --year RunII --folder vUL040 --eft cW --fit m_o1 --notCI --notUncBreak --notImpacts --tDMcut 

#python FitAndPlot_loc.py --year RunII --folder vUL045 --eft cHWB_1 --fit DNN_dim6_final_1 --notCI --notUncBreak --notImpacts --PDFWithTTDY --WithFakeCR --tDMcut

#python FitAndPlot.py --year RunII --folder vUL045 --eft cW,cHW,FT0_1p0,FT1_1p0,FT2_0p9,FM0_1p0,FM1_0p9,FM7_1p0,FS0_1p0,FS1_1p0,FS2_1p0 --fit m_o1,DNN_dim6_final_1,DNN_dim8_final_1 --noFit --notUncBreak --notImpacts --PDFWithTTDY --WithFakeCR --tDMcut 
#python FitAndPlot.py --year RunII --folder vUL045 --eft FT0_1p0,FT1_1p0,FT2_0p9,FM0_1p0,FM1_0p9,FM7_1p0,FS0_1p0,FS1_1p0,FS2_1p0 --fit m_o1,DNN_dim6_final_1 --noFit --notUncBreak --notImpacts --PDFWithTTDY --WithFakeCR --tDMcut 
#python FitAndPlot.py --year RunII --folder vUL045 --eft cW,cHW --fit m_o1,DNN_dim6_final_1,DNN_dim8_final_1 --noFit --notUncBreak --notImpacts --PDFWithTTDY --WithFakeCR --tDMcut 

python FitAndPlot.py --year RunII --folder vUL045 --eft FM7_1p0 --fit m_o1 --notUncBreak --notImpacts --PDFWithTTDY --WithFakeCR --tDMcut 

#python FitAndPlot.py --year RunII --folder vUL040 --sm --vbs --fit m_o1,BDT_SM_UL040_v2,DNN_SM_UL040_v2 --notUncBreak
#python FitAndPlot.py --year RunII --folder vUL040 --sm --vbs --fit m_o1,BDT_SM_UL040_v2,DNN_SM_UL040_v2 --notImpacts

#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwp --fit m_o1 --notImpacts 
#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwpEW --fit m_o1 --doPost --plot m_o1 --notImpacts --notUncBreak

#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwp --fit m_o1,BDT_SM_UL040_v2,DNN_SM_UL040_v2 --notUncBreak --notImpacts --doPost
#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwp --fit m_o1,BDT_SM_UL040_v2,DNN_SM_UL040_v2 --notUncBreak
#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwp --fit m_o1,BDT_SM_UL040_v2,DNN_SM_UL040_v2 --notImpacts

#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwpEW --fit m_o1,BDT_SM_UL040_v2,DNN_SM_UL040_v2 --notUncBreak --notImpacts --doPost
#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwpEW --fit m_o1,BDT_SM_UL040_v2,DNN_SM_UL040_v2 --notUncBreak
#python FitAndPlot.py --year RunII --folder vUL040 --sm --wpwpEW --fit m_o1,BDT_SM_UL040_v2,DNN_SM_UL040_v2 --notImpacts


#python FitAndPlot.py --year 2017 --folder vUL040 --sm --vbs --pol LL --fit m_o1 --notImpacts --notUncBreak

#python FitAndPlot.py --year RunII --folder vUL040 --eft cHW --fit DNN_cHW_UL025_bal,DNN_cHW_UL025_bal,DNN_cW_UL025_bal_v2,m_o1,m_o1 --cr countings,DNN_cHW_UL025_bal,DNN_cW_UL025_bal_v2,countings,m_o1 --notImpacts --noFit --doPost
#python FitAndPlot.py --year RunII --folder vUL020 --eft cW --fit m_o1,m_o1 --cr countings,m_o1 --notImpacts
#python FitAndPlot_dev.py --year RunII --folder vUL040 --EWvsQCD --fit m_o1 --notUncBreak --notImpacts --tDMcut

#python FitAndPlot.py --year RunII --folder vUL040 --eft cW,cHW,FT0_1p0,FT1_1p0,FT2_0p9,FM0_1p0,FM1_0p9,FM6_1p0,FM7_1p0,FS0_1p0,FS1_1p0,FS2_1p0 --fit m_o1 --notImpacts --notUncBreak --noFit
#python FitAndPlot.py --year RunII --folder vUL040 --eft cW,cHW --fit m_o1 --notImpacts --notUncBreak --noFit
#python FitAndPlot.py --year RunII --folder vUL040 --eft FM0_1p0,FM1_0p9,FM6_1p0,FM7_1p0,FS0_1p0,FS1_1p0,FS2_1p0 --fit m_o1,DNN_cHW_50I_TV2,DNN_cW_50I_TV0,DNN_fS_50I_TV1,DNN_fT_50I_TV1,DNN_fM_50I_TV1 --tDMcut --notImpacts --notUncBreak --noFit
#python FitAndPlot.py --year RunII --folder vUL040 --eft cW,cHW --fit m_o1,DNN_cHW_50I_TV2,DNN_cW_50I_TV0,DNN_fS_50I_TV1,DNN_fT_50I_TV1,DNN_fM_50I_TV1 --tDMcut --notImpacts --notUncBreak --noFit
#python FitAndPlot.py --year RunII --folder vUL040 --eft FT0_1p0,FT1_1p0,FT2_0p9 --fit m_o1,DNN_cHW_50I_TV2,DNN_cW_50I_TV0,DNN_fS_50I_TV1,DNN_fT_50I_TV1,DNN_fM_50I_TV1 --tDMcut --notImpacts --notUncBreak --noFit
#python FitAndPlot.py --year RunII --folder vUL040 --eft FM0_1p0 --fit m_o1,DNN_cHW_50I_TV2,DNN_cW_50I_TV0,DNN_fS_50I_TV1,DNN_fT_50I_TV1,DNN_fM_50I_TV1 --tDMcut --notImpacts --notUncBreak --noFit
#python FitAndPlot_dev.py --year RunII --folder vUL040 --eft FM0_1p0 --fit m_o1 --notUncBreak --tDMcut
#python FitAndPlot_dev.py --year RunII --folder vUL040 --eft cW --fit m_o1 --notUncBreak --tDMcut
