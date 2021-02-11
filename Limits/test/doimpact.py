import os
folder = 'fit_v16_full_DD_DDFitWJetsTT_MttST/'
signal = 'WP_M4000W40_RH'
metadatacard_out = folder + '/' + signal +'/'+ signal + '_hist'
os.system('text2workspace.py ' + metadatacard_out + '.txt -m 125')
fit_option = '--autoBoundsPOIs r  --autoRange 1'
os.system("combineTool.py -M Impacts -d  " + metadatacard_out + ".root -m 125 --robustFit 1 --doInitialFit " + fit_option) # 
os.system("combineTool.py -M Impacts -d  " + metadatacard_out + ".root -m 125 --robustFit 1 --doFits " + fit_option) #--autoBoundsPOIs r  --autoRange 1 --parallel 4
os.system("combineTool.py -M Impacts -d  " + metadatacard_out + ".root -m 125 -o prova.json")
os.system("plotImpacts.py -i prova.json -o impacts")
os.system("rm prova.json")
#os.system("mv impacts.pdf "+opt.lep+"/impacts_"+opt.process+"_"+opt.lep+".pdf")
