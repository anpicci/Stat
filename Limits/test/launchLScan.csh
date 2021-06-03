set OPER = cW
set kop = k_$OPER
set year = "2017"
set folder = "SR_CRWJandTT_BDT_output"

#set string = "k_"$OPER", "$year
text2workspace.py ./$folder/$OPER/$OPER\_hist.txt -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative -o $OPER\_test.root --X-allow-no-signal --PO eftOperators=$OPER

combine -M MultiDimFit $OPER\_test.root  --algo=grid --points 2000  -m 125   -t -1     \
    --redefineSignalPOIs k_$OPER \
    --freezeParameters r  \
    --setParameters r=1    --setParameterRanges k_$OPER=-10,10     \
    --verbose -1

#root -l higgsCombineTest.MultiDimFit.mH125.root  higgsCombineTest.MultiDimFit.mH125.root  draw.cxx\(\"k_$OPER\"\)
python drawLS.py higgsCombineTest.MultiDimFit.mH125.root higgsCombineTest.MultiDimFit.mH125.root $kop $year
