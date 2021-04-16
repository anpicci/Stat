set folder=''
set signal='WP_M2000W20_RH'
set datacard=$signal'_hist.txt'
echo $datacard
set option='--saveWorkspace'
combine -M GoodnessOfFit $folder/$signal/$datacard --algo=saturated -t 500 --toysFrequentist --fixedSignalStrength=0 --bypassFrequentistFit -n gof_toys #--saveToys
combine -M GoodnessOfFit $folder/$signal/$datacard --algo=saturated --fixedSignalStrength=0 -n gof_data

