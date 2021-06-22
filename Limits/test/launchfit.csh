set folder='SR_CRWJTTQCD_BDT_output_SM'#_BDTcut''LS_SR_CRWJTTQCD_m_o1'#
set oper="FT2_0p5" # cW" # FS0_5" # FM1_5" # 
set inf='v80'
set EOSSPACE = /eos/home-a/apiccine
reset
#python PrepareEOSfolder.py $inf
rm histo2017_$folder.root
python collectHistos.py -i $EOSSPACE/VBS/nosynch/$inf/plot/ -o histo2017_$folder.root --ls $oper
python createDatacards.py -i histo2017_$folder.root -d $folder --ls $oper
##python runCombine.py -c SR_2017 -y 2017 -d $folder --runSingleCat -m hist
python runCombine.py -y 2017 -d $folder -m hist --ls $oper #--runSingleCat -m hist
##python getLimitData.py -y 2016 -d $folder/
##python brazilPlot.py -y 2016 -l $folder
