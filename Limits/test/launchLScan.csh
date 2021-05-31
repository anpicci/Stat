set OPER = cHW
set year = "2016"

set string = "k_"$OPER", "$year
#text2workspace.py ./LS_$OPER\_mo1/$OPER/$OPER\_hist.txt -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative -o model_test.root --X-allow-no-signal --PO eftOperators=$OPER

#combine -M MultiDimFit model_test.root  --algo=grid --points 2000  -m 125   -t -1     \
    #--redefineSignalPOIs k_$OPER \
    #--freezeParameters r  \
    #--setParameters r=1    --setParameterRanges k_$OPER=-10,10     \
    #--verbose -1

root -l higgsCombineTest.MultiDimFit.mH125.root  higgsCombineTest.MultiDimFit.mH125.root  draw.cxx\(\"k_$OPER\"\)

