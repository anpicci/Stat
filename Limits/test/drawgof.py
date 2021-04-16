import ROOT
import optparse

ROOT.gROOT.SetBatch() #don't pop up canvases
ROOT.gStyle.SetOptStat(0) #don't pop up canvases

usage = 'python dragof.py -s suffix'
parser = optparse.OptionParser(usage)
parser.add_option('-s', '--suffix', dest='suffix', type=str, default = '', help='Please enter a suffix name')
parser.add_option('--xmax', dest='xmax', type=int, default=50, help='Maximum for the gof plot')
(opt, args) = parser.parse_args()

suffix = opt.suffix
xmax = opt.xmax

toyfile = ROOT.TFile.Open('higgsCombinegof_'+suffix+'.GoodnessOfFit.mH120.123456.root')
toytree = toyfile.Get('limit')
h = ROOT.TH1F('h',';r;Events', xmax, 0, xmax)
toytree.Project('h', 'limit')
print h.Integral()
datafile = ROOT.TFile.Open('higgsCombinegof_data_'+suffix+'.GoodnessOfFit.mH120.root')
datatree = datafile.Get('limit')
datatree.GetEntry(0)
xar = datatree.limit
print xar
canvas = ROOT.TCanvas('gof',"c1",50,50,700,600)
canvas.Draw()
h.Draw('SAME')
yar = h.GetBinContent(h.FindBin(xar))
if yar < h.GetMaximum():
    yar = h.GetMaximum()
else:
    yar += 3
arrow = ROOT.TArrow(xar,0,xar,yar,0.02,"<|")
arrow.SetAngle(40)
arrow.SetLineWidth(2)
arrow.SetLineColor(2)
arrow.SetFillColor(2)
arrow.Draw()
alpha = h.Integral(h.FindBin(xar), xmax)/h.Integral()
latex = ROOT.TLatex()
latex.SetTextSize(0.045);
latex.SetTextAlign(13)
latex.DrawLatex(xmax/2,h.GetMaximum()/2,"#alpha = " + str(alpha))
#latex.DrawLatex(.3,.9,"K^{*0}")
#latex.SetTextAlign(12)
canvas.Print(suffix + '_gof_plot.png')
canvas.Print(suffix + '_gof_plot.pdf')
