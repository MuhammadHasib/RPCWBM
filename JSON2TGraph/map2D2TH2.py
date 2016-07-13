import json
from ctypes import *

def loadJson(name):
  with open(name) as data_file:
    data = json.load(data_file)
    return data

def makeTH2(filename):
  data=loadJson(filename+".json")
  #print data["WM1"].keys()
  #print data["WM1"]["RB3+"]

  from ROOT import TH2D,TFile 
  from array import array
  import copy

  hists = []
  WD = [ x for x in data.keys() if (x.find("W")>-1 or x.find("E")>-1) and x.find("*")==-1 ] 

  for aa in WD :
    xbin = 12
    if aa.find("E")>-1: xbin=36

    aWD = data[aa]
    #print str(type(aWD))+"   "+str(len(aWD) )
    if type(aWD) == dict:
      ybin =len(aWD.keys())-1
      h = TH2D("h2_"+aa,aa, xbin,0,xbin,ybin,0,ybin)  
      bbb=1
      for b,bb in enumerate(sorted(aWD.keys())):
        #print "bb : "+bb+", "+str(aWD[bb])
        if bb.find("W")==-1 and bb.find("E")==-1:
          h.GetYaxis().SetBinLabel(bbb,bb)
          for c,cc in enumerate(aWD[bb]):
            if cc is not None and type(cc) is not unicode :
              #print str(cc)+"  "+str(type(cc))
              #print cc
              h.SetBinContent( c+1, bbb, cc )
          bbb+=1
        else :
          for c,cc in enumerate(aWD[bb]):
            if bb.find("W")>-1 or bb.find("E")>-1:
              h.GetXaxis().SetBinLabel(c+1,cc)
      hists.append(copy.deepcopy(h))
  f = TFile(filename+".root", "recreate") 
  for hist in hists:
    hist.Write()

  f.Write()
  f.Close()

def main():
  import sys
  if len(sys.argv) < 2:
    print "usage : python RPCWBM_JSON2TGraph.py filename"
    sys.exit()

  filename = sys.argv[1]
 
  makeTH2(filename)

if __name__ == "__main__":
    test=main()

