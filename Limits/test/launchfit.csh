set folder='prova'
set EOSSPACE = /eos/home-a/apiccine
#python collectHistos.py -i $EOSSPACE/VBS/nosynch/v76/plot/ -o histo2017.root
python createDatacards.py -i histo2017.root -d $folder
#python runCombine.py -c SR_2016 -y 2016 -d $folder --runSingleCat -m hist
#python runCombine.py -y 2016 -d $folder -m hist #--runSingleCat -m hist
#python getLimitData.py -y 2016 -d $folder/
#python brazilPlot.py -y 2016 -l $folder
