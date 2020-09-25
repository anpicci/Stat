# Stat
Machinery to produce datacards and run limits


To convert input files to combine-friendly format:

> python collectHistos.py  -i inputFolfer/ -o histos.root

The script will retrieve the year from the histos names.
In order to merge 2016 and 2017 root file, do:

> hadd histosFile.root histos2016.root histos2017.root

This file will be given as input to createDatacards.py script
to create a set of datacrds, for each region and for the combination

> python createDatacards.py -i histosFile.root -d outdir -m mode (hist or template) -c channels (list of regions, or all for including all of them) -u (to unblind)

To run all limits together in local: 

> python runCombine.py -c channel -y year -m method -d outdir 

To run all limits on the batch queques:

>  python batchLimits.py -c channel -y year -m method -d outdir 
 
> python getLimitData.py -y 2016 -d limitsRun2_v2/ -m template

> python brazilPlot.py -y year -m template 
