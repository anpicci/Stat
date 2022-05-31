#python FitAndPlot.py --year RunII --folder vUL030 --sm --fit DNN_SM_UL025_bal,DNN_SM_UL025_nobal,m_o1 --doPost
python FitAndPlot.py --year RunII --folder vUL030 --eft cW --fit DNN_cW_UL025_bal_v2,DNN_cW_UL025_bal_v2,DNN_cHW_UL025_bal,m_o1,m_o1 --cr countings,DNN_cW_UL025_bal_v2,DNN_cHW_UL025_bal,countings,m_o1 --notImpacts
python FitAndPlot.py --year RunII --folder vUL030 --eft cHW --fit DNN_cHW_UL025_bal,DNN_cHW_UL025_bal,DNN_cW_UL025_bal_v2,m_o1,m_o1 --cr countings,DNN_cHW_UL025_bal,DNN_cW_UL025_bal_v2,countings,m_o1 --notImpacts
#python FitAndPlot.py --year RunII --folder vUL020 --eft cW --fit m_o1,m_o1 --cr countings,m_o1 --notImpacts

