import os
import sys
#from Stat.Limits.settings import *
print sys.argv
folder = '/eos/home-a/apiccine/VBS/nosynch/' + sys.argv[1] + "/plot"
#folder = '/eos/home-t/ttedesch/VBS/nosynch/' + sys.argv[1] + "/plot"
folder += sys.argv[3] + "/"

#import importlib
#settmod = importlib.import_module("Stat.Limits.settings_" + sys.argv[2])
#bkg = settmod.bkg
#histos = settmod.histos
#years = settmod.years
#leptons = settmod.leptons
#sigpoints = settmod.sigpoints
#lssamples_1D = settmod.lssamples_1D
#syst = settmod.syst

subfolders = [dirr for dirr in os.listdir(folder) if not "_" in dirr]#"mu" in dirr or "ele" in dirr]

new_sf = [odirr.split("_")[0] for odirr in subfolders]

years = ["2016M", "2017", "2018"]

for i, odir in enumerate(new_sf):#subfolders):#
    ofilelist = []
    for y in years:
        ylist = [f for f in os.listdir(folder + odir) if not 'countings' in f and y in f]

        for yfile in ylist:
            ofilelist.append(yfile)
        
        for of in ofilelist:        
            if not (of.startswith('FakeMuPromptTau') or of.startswith('FakeMuFakeTau') or of.startswith('PromptMuFakeTau') or of.startswith('FakeElePromptTau') or of.startswith('FakeEleFakeTau') or of.startswith('PromptEleFakeTau')):
                new_dest = folder + new_sf[i] + "/"
                #print of, new_dest
                
                if of.startswith("FakeMu_") or of.startswith("FakeEle_"):
                    new_dest = new_dest + of.replace("Mu", "").replace("Ele", "")
                else:
                    new_dest = new_dest + of
                if str(folder + odir + "/" + of) != str(new_dest):
                    if not os.path.exists(new_dest):
                        os.system("cp " + folder + odir + "/" + of + " " + new_dest)
                    #print "cp " + folder + odir + "/" + of + " " + new_dest
                else:
                    continue
