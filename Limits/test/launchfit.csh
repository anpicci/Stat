#set folder='fit_v100_m_1T'
set oper="SM"#cW"#FS0_5"#FM1_5" #FT2_0p5" #  cHW" # 
#set srvar="m_jj"
#set srvar="m_o1"
#set srvar="m_1T"
#set srvar="BDT_SM_xgb_UL010_allBKG"
#set srvar="BDT_cW_xgb_UL010_allBKG"
set srvar="DNN_SM_UL010_allBKG"
#set srvar="DNN_cW_UL010_allBKG"
#set srvar="DNN_cHW_UL010_allBKG"
#set srvar="BDT_cW_xgb_UL008_no"
#set srvar="BDT_cHW_xgb_UL008_no"
#set srvar = 'BDT_fT1_xgb_RR_no'
#set srvar = 'BDT_aQGC_xgb_RR_no'#branch con BDT allenata sul classico aQGC
#set srvar = 'BDT_fS0_xgb_RR_no'#branch con BDT allenata su tutti i fS0
#set srvar = 'BDT_fS0_25_xgb_RR_no'#branch con BDT allenata solo su fS0 = 25
#set crvar="countings"
#set crvar="m_jj"
set crvar="DNN_SM_UL010_allBKG"
#set crvar="DNN_cHW_UL010_allBKG"
#set inf='v100'#_tagger_DataSplit_MCnoSplit'
set inf='vUL025'#_xg_sample_29_10_21_n1T4features_depth2_retrainedBDT'
#set year = '2016M'
#set year = '2017'
#set year = '2018'
#set year = '2017,2018'
set year = '2016M,2017,2018'
#set year_ = '2016M_'
#set year_ = '2017_'
#set year_ = '2018_'
#set year_ = '2017-2018_'
set year_ = 'RunII_'
set folder='fit_'$inf'_'$srvar'_'$crvar'_'$year_ #'onlySR'
set EOSSPACE = /eos/home-a/apiccine
#set EOSSPACE = /eos/home-t/ttedesch

reset
python PrepareEOSfolder.py $inf
rm histo$year_$folder.root
python collectHistos.py -i $EOSSPACE/VBS/nosynch/$inf/plot/ -o histo$year_$folder.root #--ls $oper
python createDatacards.py -i histo$year_$folder.root -d $folder #--ls $oper
#python runCombine.py -c SR_$year -y $year -d $folder --runSingleCat -m hist
python runCombine.py -y $year -d $folder -m hist #--ls $oper #--runSingleCat -m hist
##python getLimitData.py -y 2016 -d $folder/
##python brazilPlot.py -y 2016 -l $folder

############ impacts ############
#reset
set DATACARD_FOLDER = $folder/VBS_SSWW_SM
set DATACARD_NAME = VBS_SSWW_SM_hist
#set DATACARD_FOLDER = $folder/$oper
#set DATACARD_NAME = $oper\_hist

set DATACARD_PATH = ${DATACARD_FOLDER}/${DATACARD_NAME}

#echo 'DATACARD_FOLDER' $DATACARD_FOLDER
#echo 'DATACARD_NAME' $DATACARD_NAME
#echo 'DATACARD_PATH' $DATACARD_PATH
rm higgsCombine_*
rm -rf $folder/Checks_$oper/ #${DATACARD_NAME}
mkdir $folder/Checks_$oper/ #${DATACARD_NAME}

set cardName = ${DATACARD_PATH}
set cardNameWorkspace = $folder/Checks_$oper/${DATACARD_NAME}
set outputFolder = $folder/Checks_$oper/

#echo 'cardName' $cardName
#echo 'cardNameWorkspace' $cardNameWorkspace
#echo 'outputFolder' $outputFolder
text2workspace.py ${cardName}.txt -o ${cardNameWorkspace}.root

#cd $outputFolder

combine -M FitDiagnostics -d ${cardNameWorkspace}.root -t -1 --toysFreq --expectSignal 0 --rMin -10 --forceRecreateNLL -n _t0 
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t0.root -g plots_t0.root >> ${outputFolder}/fitResults_t0.log

combine -M FitDiagnostics -d ${cardNameWorkspace}.root -t -1 --toysFreq --expectSignal 1  --forceRecreateNLL -n _t1 
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> ${outputFolder}/fitResults_t1.log

combineTool.py -M Impacts -d ${cardNameWorkspace}.root -t -1 --toysFreq --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0 --parallel 10 
combineTool.py -M Impacts -d ${cardNameWorkspace}.root -t -1 --toysFreq --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1 --parallel 10 

combineTool.py -M Impacts -d ${cardNameWorkspace}.root -o ${outputFolder}/impacts_t0.json -t -1 --toysFreq --expectSignal 0 --rMin -10 --doFits -m 1 -n t0 --parallel 10 
combineTool.py -M Impacts -d ${cardNameWorkspace}.root -o ${outputFolder}/impacts_t1.json -t -1 --toysFreq --expectSignal 1 --rMin -10 --doFits -m 1 -n t1 --parallel 10  

combineTool.py -M Impacts -d ${cardNameWorkspace}.root -m 1 -n t0 -o ${outputFolder}/impacts_t0.json --parallel 10
combineTool.py -M Impacts -d ${cardNameWorkspace}.root -m 1 -n t1 -o ${outputFolder}/impacts_t1.json --parallel 10

plotImpacts.py -i  ${outputFolder}/impacts_t0.json -o  ${outputFolder}/impacts_t0
plotImpacts.py -i  ${outputFolder}/impacts_t1.json -o  ${outputFolder}/impacts_t1

mv higgsCombine_* $outputFolder
mv fitDiagnostics_t* plots_t* combine_logger.out $outputFolder
