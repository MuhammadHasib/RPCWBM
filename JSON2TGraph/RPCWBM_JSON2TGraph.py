import json
def loadJson(name):
  with open(name) as data_file:
    data = json.load(data_file)
    return data

def makeTGraphs(filename):
  data=loadJson(filename+".json")

  from ROOT import TGraph,TFile 
  from array import array
  import copy

  hists = []

  for aa in data["data"]:
    x,y = [],[]
    for bb in aa["data"]:
      x.append(bb[0])
      y.append(bb[1])
    xx = array("d", x)
    yy = array("d", y)
    g = TGraph(len(xx), xx,yy)
    g.SetName(aa["name"]) 
    g.SetTitle(aa["name"]) 
    g.GetXaxis().SetTitle(data["xtitle"])
    g.GetYaxis().SetTitle(data["ytitle"])
    hists.append(copy.deepcopy(g))

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
 
  makeTGraphs(filename)
  #makeTGraphs("HV_current_BE")

if __name__ == "__main__":
    test=main()

