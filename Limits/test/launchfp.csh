#python FitAndPlot.py --year RunII --folder vUL030 --eft cW --fit DNN_cW_UL025_bal_v2,DNN_cHW_UL025_bal,BDT_cW_xgb_UL025_bal_noopt,BDT_cHW_xgb_UL025_bal_noopt,m_o1 --doPost --notImpacts --notCI
#python FitAndPlot.py --year 2017 --folder vUL030 --eft cW --fit m_o1 --notCI --notImpacts --notUncBreak

#python FitAndPlot.py --year RunII --folder vUL035 --eft cW:FT0_1p0 --fit m_o1 --notCI --notImpacts --notUncBreak
#python FitAndPlot.py --year RunII --folder vUL035 --eft cW --fit m_o1,m_1T,DNN_cW_UL035_novar,BDT_cW_UL035_novar --notImpacts --notUncBreak
#python FitAndPlot.py --year RunII --folder vUL035 --eft FT1_1p0 --fit m_o1 --notCI --notImpacts --notUncBreak
python FitAndPlot.py --year RunII --folder vUL035 --eft FT0_1p0 --fit DNN_aQGC_UL035_novar --noFit --notUncBreak --notImpacts

#python FitAndPlot.py --year RunII --folder vUL035 --sm --vbs --fit BDT_SM_UL035_v2 --doPost --plot m_o1
#python FitAndPlot.py --year RunII --folder vUL035 --sm --vbs --fit DNN_SM_UL035_v2 --doPost --plot m_o1
#python FitAndPlot.py --year RunII --folder vUL035 --sm --vbs --fit m_o1 --doPost --plot m_o1 --notImpacts --notUncBreak

#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwp --fit BDT_SM_UL035_v2 --doPost --plot m_o1 --notImpacts --notUncBreak
#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwp --fit DNN_SM_UL035_v2 --doPost --plot m_o1
#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwp --fit m_o1 --doPost --plot m_o1 --notImpacts --notUncBreak

#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwpEW --fit BDT_SM_UL035_v2 --doPost --plot m_o1 --notImpacts --notUncBreak
#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwpEW --fit DNN_SM_UL035_v2 --doPost --plot m_o1
#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwpEW --fit m_o1 --notUncBreak --notImpacts



#python FitAndPlot.py --year RunII --folder vUL035 --sm --vbs --fit m_o1,BDT_SM_UL035_v2,DNN_SM_UL035_v2 --notUncBreak
#python FitAndPlot.py --year RunII --folder vUL035 --sm --vbs --fit m_o1,BDT_SM_UL035_v2,DNN_SM_UL035_v2 --notImpacts

#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwp --fit m_o1 --notImpacts 
#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwpEW --fit m_o1 --doPost --plot m_o1 --notImpacts --notUncBreak

#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwp --fit m_o1,BDT_SM_UL035_v2,DNN_SM_UL035_v2 --notUncBreak --notImpacts --doPost
#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwp --fit m_o1,BDT_SM_UL035_v2,DNN_SM_UL035_v2 --notUncBreak
#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwp --fit m_o1,BDT_SM_UL035_v2,DNN_SM_UL035_v2 --notImpacts

#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwpEW --fit m_o1,BDT_SM_UL035_v2,DNN_SM_UL035_v2 --notUncBreak --notImpacts --doPost
#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwpEW --fit m_o1,BDT_SM_UL035_v2,DNN_SM_UL035_v2 --notUncBreak
#python FitAndPlot.py --year RunII --folder vUL035 --sm --wpwpEW --fit m_o1,BDT_SM_UL035_v2,DNN_SM_UL035_v2 --notImpacts


#python FitAndPlot.py --year 2017 --folder vUL030 --sm --vbs --pol LL --fit m_o1 --notImpacts --notUncBreak

#python FitAndPlot.py --year RunII --folder vUL030 --eft cHW --fit DNN_cHW_UL025_bal,DNN_cHW_UL025_bal,DNN_cW_UL025_bal_v2,m_o1,m_o1 --cr countings,DNN_cHW_UL025_bal,DNN_cW_UL025_bal_v2,countings,m_o1 --notImpacts --noFit --doPost
#python FitAndPlot.py --year RunII --folder vUL020 --eft cW --fit m_o1,m_o1 --cr countings,m_o1 --notImpacts
#python FitAndPlot_dev.py --year RunII --folder vUL030 --EWvsQCD --fit m_o1 --notUncBreak --notImpacts
