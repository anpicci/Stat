#set folder='fit_v100_m_1T'
set oper="FT2_2p5"#cHW"# FM1_5" #FT2_0p5" #  cHW" # 
#set inf='v100_tagger_DataSplit_MCnoSplit'
set inf='v100'#_xg_sample_29_10_21_n1T4features_depth2_retrainedBDT'
#set year = '2017'
set year = '2018'
#set year = '2017,2018'
#set year_ = '2017_'
set year_ = '2018_'
#set year_ = '2017-2018_'
#set folder='fit_v100_m_1T_2018'
set folder='fit_v100_BDT_SM_2018'
#set folder='fit_v100_m_1T_2017-2018'
set EOSSPACE = /eos/home-a/apiccine
#set EOSSPACE = /eos/home-t/ttedesch
reset
#python PrepareEOSfolder.py $inf
#rm histo$year_$folder.root
#python collectHistos.py -i $EOSSPACE/VBS/nosynch/$inf/plot/ -o histo$year_$folder.root #--ls $oper
#python createDatacards.py -i histo$year_$folder.root -d $folder #--ls $oper
##python runCombine.py -c SR_$year -y $year -d $folder --runSingleCat -m hist
python runCombine.py -y $year -d $folder -m hist #--ls $oper #--runSingleCat -m hist
##python getLimitData.py -y 2016 -d $folder/
##python brazilPlot.py -y 2016 -l $folder
