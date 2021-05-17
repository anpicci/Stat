import os
import sys

folder='SR_2017_1405'#'CR0B_2018_comb_23Mar21_plot_newfit_23Mar21_split_rateparam'
year = '2017'
histo_rep = '/eos/user/a/apiccine/VBS/nosynch/' + sys.argv[1] + '/plot/'
fit = 1
fit_diag = 1
impact = 0
gof = 0
unblind = 0

if fit:
    if unblind:
        os.system('python collectHistos.py -i ' + histo_rep + ' -o histo' + str(year) + '.root -u')
        os.system('python createDatacards.py -i histo' + str(year) + '.root -d  ' + folder + ' -u')
        #python runCombine.py -c SR_$year -y $year -d  ' + folder + ' --runSingleCat -m hist
        os.system('python runCombine.py -y ' + str(year) + ' -d ' + folder + ' -m hist') #--runSingleCat
        os.system('python getLimitData.py -d ' + folder) #--runSingleCat
        #os.system('python brazilPlot.py  -l ' + folder + ' -o' + ' -y ' + str(year)) #--runSingleCat
    else:
        os.system('python collectHistos.py -i ' + histo_rep + ' -o histo' + str(year) + '.root')
        os.system('python createDatacards.py -i histo' + str(year) + '.root -d  ' + folder)
        #python runCombine.py -c SR_$year -y $year -d  ' + folder + ' --runSingleCat -m hist
        os.system('python runCombine.py -y ' + str(year) + ' -d ' + folder + ' -m hist') #--runSingleCat
        os.system('python getLimitData.py -d ' + folder) #--runSingleCat
        #os.system('python brazilPlot.py  -l ' + folder + ' -y ' + str(year)) #--runSingleCat


signal = 'VBS_SSWW_SM'
metadatacard_out = folder + '/' + signal +'/'+ signal + '_hist'

#do fit diagonistics
if fit_diag:
    os.system('text2workspace.py ' + metadatacard_out + '.txt')
    print "combine -M FitDiagnostics -d " + metadatacard_out + ".root --saveShapes --saveWithUncertainties --plots --saveNormalizations"# --robustFit 1 --customStartingPoint --stepSize 0.004 --out " + folder + " --profilingMode all --keepFailures  --autoBoundsPOIs r"
    os.system("combine -M FitDiagnostics -d " + metadatacard_out + ".root --saveShapes --saveWithUncertainties --plots --saveNormalizations")# --robustFit 1 --customStartingPoint --stepSize 0.004 --out " + folder + " --profilingMode all --keepFailures  --autoBoundsPOIs r")

# do impact plot?
if impact:
    os.system('text2workspace.py ' + metadatacard_out + '.txt -m 125')
    fit_option = '--autoBoundsPOIs r  --autoRange 1'
    os.system("combineTool.py -M Impacts -d  " + metadatacard_out + ".root -m 125 --robustFit 1 --doInitialFit " + fit_option) # 
    os.system("combineTool.py -M Impacts -d  " + metadatacard_out + ".root -m 125 --robustFit 1 --doFits " + fit_option) #--autoBoundsPOIs r  --autoRange 1 --parallel 4
    os.system("combineTool.py -M Impacts -d  " + metadatacard_out + ".root -m 125 -o prova.json")
    os.system("plotImpacts.py -i prova.json -o impacts")
    os.system("rm prova.json")
    #os.system("mv impacts.pdf "+opt.lep+"/impacts_"+opt.process+"_"+opt.lep+".pdf")

# do gof test?
suffix = folder
ntoys = 500
xmax = 180
if gof:
    os.system("combine -M GoodnessOfFit " + metadatacard_out + ".txt --algo=saturated --toysFrequentist --bypassFrequentistFit -n gof_data_" + suffix + " --rMax 250 --rMin -250")
    os.system("combine -M GoodnessOfFit " + metadatacard_out + ".txt --algo=saturated -t " + str(ntoys) + " --toysFrequentist --bypassFrequentistFit -n gof_" + suffix + " --rMax 250 --rMin -250")
    os.system('python drawgof.py -s ' + suffix + ' --xmax ' + str(xmax))


