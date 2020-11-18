set folder='prova_syst'
python collectHistos.py -i $EOSSPACE/Wprime/nosynch/v13/plot/ -o histo2016.root
python createDatacards.py -i histo2016.root -d $folder
#python runCombine.py -c SR_2016 -y 2016 -d $folder --runSingleCat -m hist
#python runCombine.py -y 2016 -d $folder -m hist #--runSingleCat -m hist
#python getLimitData.py -y 2016 -d $folder/
#python brazilPlot.py -y 2016 -l $folder
