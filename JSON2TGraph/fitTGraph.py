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
  ytitle=""
  for key in [x.GetName() for x in f1.GetListOfKeys()]:
    obj = f1.Get(key)
    if obj == None: continue
    elif obj.IsA().InheritsFrom("TGraph"):
     if ytitle=="" : ytitle=obj.GetYaxis().GetTitle()
     tgs.append( copy.deepcopy(obj) )
  return tgs,ytitle

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
  p0err=myfunc.GetParError(0) 

  p1=myfunc.GetParameter(1)
  p1err=myfunc.GetParError(1) 
  ndf = myfunc.GetNDF()
  chi2 = myfunc.GetChisquare()

  functext="y = "+str(round(p1*10000)/10000)+"x + "+str(round(p0*10000)/10000.)
  functexAll[tg.GetName()] = functext
  tfs[tg.GetName()]={"p0":p0,"p1":p1,"p0err":p0err,"p1err":p1err,"ndf":ndf,"chi2":chi2}

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
    lumi10=tfs[xa]["p1"]*10*lumi+tfs[xa]["p0"]
    lumi5=tfs[xa]["p1"]*5*lumi+tfs[xa]["p0"]
    out[xa]={"lumi10":lumi10,"lumi5":lumi5, "data":tfs[xa]}
  return out

def printValueInALumi(values,ytitle):
  aaa = "name, "+ytitle+"(10^34),  "+ytitle+"(5x10^34), funcP0, funcP1, funcP0err, funcP1err, NDF, Chi^2 \n"
  for i,xa in enumerate(sorted(values.keys())):
    aaa+= xa+", "+str(values[xa]["lumi10"])+", "+str(values[xa]["lumi5"])
    aaa+= ", "+str(values[xa]["data"]["p0"])+", "+str(values[xa]["data"]["p1"])
    aaa+= ", "+str(values[xa]["data"]["p0err"])+", "+str(values[xa]["data"]["p1err"])
    aaa+= ", "+str(values[xa]["data"]["ndf"])+", "+str(values[xa]["data"]["chi2"])
    aaa+="\n"
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
  tgs,ytitle = getTGraphFlat(f)

  temp = {}
  functexAll = {}
  tfs = {}

  for i,tg in enumerate(tgs):
    temp[i]=fitTGraph(tg,i,functexAll,tfs)

  aaa = makeCanvasAll("b",tfs,"p0")
  bbb = makeCanvasAll("a",tfs,"p1")
  ccc = getValueInALumi(tfs)
  ddd = printValueInALumi(ccc,ytitle)

  with open("Output_"+filename+".csv", "w") as text_file:
      text_file.write(ddd)

  return functexAll,temp,tfs,aaa,bbb


if __name__ == "__main__":
    test=main()


