from ROOT import TFile,TGraph,TCanvas

import os
loc = os.getcwd()
f = TFile.Open(loc+"/HV_current_BE.root")

tg = f.Get("Barrel")
tg2 = f.Get("Endcap")

c1 = TCanvas("c1","",800,400)
c1.Divide(2,1)
c1.cd(1)
print tg.GetName()
tg.Draw()
tg.Fit("pol1")

print ""
print ""

c1.cd(2)
print tg2.GetName()
tg2.Draw()
tg2.Fit("pol1")

