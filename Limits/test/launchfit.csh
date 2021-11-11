set folder='fit_v100_tted'#fit_v90_BDT_output_dim8'#_BDTcut''LS_SR_CRWJTTQCD_m_o1'#
set oper="cW"#FS0_5" # FM1_5" #FT2_0p5" #  cHW" # 
set inf='v100_tagger_DataSplit_MCnoSplit'
set year = '2018'#'2017'#
set year_ = '2018_'#'2017_'#
#set EOSSPACE = /eos/home-a/apiccine
set EOSSPACE = /eos/home-t/ttedesch
reset
python PrepareEOSfolder.py $inf
rm histo$year_$folder.root
python collectHistos.py -i $EOSSPACE/VBS/nosynch/$inf/plot/ -o histo$year_$folder.root # --ls $oper
python createDatacards.py -i histo$year_$folder.root -d $folder # --ls $oper
##python runCombine.py -c SR_$year -y $year -d $folder --runSingleCat -m hist
python runCombine.py -y $year -d $folder -m hist # --ls $oper #--runSingleCat -m hist
##python getLimitData.py -y 2016 -d $folder/
##python brazilPlot.py -y 2016 -l $folder
