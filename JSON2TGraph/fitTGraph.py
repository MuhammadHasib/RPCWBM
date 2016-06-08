from ROOT import TFile,TGraph,TCanvas,TLatex,TLegend,TH1D
from array import array
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

def fitTGraph(tg,idx,functexAll,tfs):
  print ""
  print ""
  c1 = TCanvas("c1"+str(idx),"",400,400)
  tg.Draw()
  tg.Fit("pol1")
  myfunc=tg.GetFunction("pol1")
  print "myfunc "+str(type(myfunc))

  myfunc.SetLineColor(idx)
  myfunc.SetName(tg.GetName())

  p0=myfunc.GetParameter(0)
  p1=myfunc.GetParameter(1)
  functext="y = "+str(round(p0*1000)/1000)+"x + "+str(round(p1*100000)/100000.)
  functexAll[tg.GetName()] = functext
  tfs[tg.GetName()]={"p0":p0,"p1":p1}

  tex=addLegendText(functext)
  tex.Draw()
  c1.Print("plots/"+tg.GetName()+".png")
  return c1,tg,tex

def makeCanvasAll(name,tfs,pol):
  c1 = TCanvas("c1"+name,"",1200,400)
  x,y,z=[],[],[]
  for i,xa in enumerate(sorted(tfs.keys())):
    y.append(tfs[xa][pol])
    x.append(i+1)
    z.append(xa)

  xx = array("d", x)
  yy = array("d", y)
  g = TGraph(len(xx), xx,yy)
  xax = g.GetXaxis()
  g.SetTitle(name+" of fit functions y=ax+b")

  for i in range(len(xx)):
    binIndex = xax.FindBin(i+1)
    g.GetXaxis().SetBinLabel(binIndex,z[i])

  g.Draw()

  return c1,g

def getValueInALumi(tfs):
  out = {}
  lumi = 10000
  for i,xa in enumerate(sorted(tfs.keys())):
    lumi10=tfs[xa]["p0"]*10*lumi+tfs[xa]["p1"]
    lumi5=tfs[xa]["p0"]*5*lumi+tfs[xa]["p1"]
    out[xa]={"lumi10":lumi10,"lumi5":lumi5}
  return out

def printValueInALumi(values):
  aaa = ""
  for i,xa in enumerate(sorted(values.keys())):
    aaa+= xa+", "+str(values[xa]["lumi10"])+", "+str(values[xa]["lumi5"])+"\n"
  return aaa

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
  functexAll = {}
  tfs = {}

  for i,tg in enumerate(tgs):
    temp[i]=fitTGraph(tg,i,functexAll,tfs)

  aaa = makeCanvasAll("a",tfs,"p0")
  bbb = makeCanvasAll("b",tfs,"p1")
  ccc = getValueInALumi(tfs)
  ddd = printValueInALumi(ccc)

  with open("Output_"+filename+".txt", "w") as text_file:
      text_file.write(ddd)

  return functexAll,temp,tfs,aaa,bbb


if __name__ == "__main__":
    test=main()


