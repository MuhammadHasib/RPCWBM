from ROOT import TFile,TGraph,TCanvas
import copy

def getTGraphFlat(f1):
  tgs = []
  for key in [x.GetName() for x in f1.GetListOfKeys()]:
    obj = f1.Get(key)
    if obj == None: continue
    elif obj.IsA().InheritsFrom("TGraph"):
     tgs.append( copy.deepcopy(obj) )
  return tgs

def fitTGraph(tg,idx):
  print ""
  print ""
  c1 = TCanvas("c1"+str(idx),"",400,400)
  tg.Draw()
  tg.Fit("pol1")
  c1.Print(tg.GetName()+".png")
  return c1,tg

import os
loc = os.getcwd()
f = TFile.Open(loc+"/HV_current_BE.root")
tgs = getTGraphFlat(f)

temp = {}
for i,tg in enumerate(tgs):
  temp[i]=fitTGraph(tg,i)


