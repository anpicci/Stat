set folder='SRandCRWJ_0522_m_o1_lepBDTcut'
set EOSSPACE = /eos/home-a/apiccine
reset
rm histo2017.root
python PrepareEOSfolder.py v70
python collectHistos.py -i $EOSSPACE/VBS/nosynch/v70/plot/ -o histo2017.root 
python createDatacards.py -i histo2017.root -d $folder 
##python runCombine.py -c SR_2017 -y 2017 -d $folder --runSingleCat -m hist
python runCombine.py -y 2017 -d $folder -m hist #--runSingleCat -m hist
##python getLimitData.py -y 2016 -d $folder/
##python brazilPlot.py -y 2016 -l $folder
