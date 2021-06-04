set folder='SR_CRWJandTTandQCD_BDT_output'#_BDTcut'
set oper = "cHW"
set EOSSPACE = /eos/home-a/apiccine
reset
python PrepareEOSfolder.py v70
rm histo2017_$folder.root
python collectHistos.py -i $EOSSPACE/VBS/nosynch/v70/plot/ -o histo2017_$folder.root #--ls $oper
python createDatacards.py -i histo2017_$folder.root -d $folder #--ls $oper
##python runCombine.py -c SR_2017 -y 2017 -d $folder --runSingleCat -m hist
python runCombine.py -y 2017 -d $folder -m hist #--ls $oper #--runSingleCat -m hist
##python getLimitData.py -y 2016 -d $folder/
##python brazilPlot.py -y 2016 -l $folder
