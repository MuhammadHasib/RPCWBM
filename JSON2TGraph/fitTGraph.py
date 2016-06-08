from ROOT import TFile,TGraph,TCanvas,TLatex
import copy

def addLegendText(text):
  tex2 = TLatex(-20.,50.,text)
  tex2.SetX(0.25),        tex2.SetY(0.83)
  tex2.SetNDC(),          tex2.SetTextAlign(12)
  tex2.SetTextColor(2),   tex2.SetTextFont(42) 
  return tex2

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
  myfunc=tg.GetFunction("pol1")
  p0=myfunc.GetParameter(0)
  p1=myfunc.GetParameter(1)
  functext="y = "+str(round(p0*1000)/1000)+"x + "+str(round(p1*100000)/100000.)

  tex=addLegendText(functext)
  tex.Draw()
  c1.Print(tg.GetName()+".png")
  return c1,tg,tex

def main():
  import sys
  if len(sys.argv) < 2:
    print "usage : python fitTGraph.py filename"
    sys.exit()

  filename = sys.argv[1]
  import os
  loc = os.getcwd()
  f = TFile.Open(loc+"/"+filename+".root")
  tgs = getTGraphFlat(f)

  temp = {}
  for i,tg in enumerate(tgs):
    temp[i]=fitTGraph(tg,i)

  return temp

if __name__ == "__main__":
    test=main()


