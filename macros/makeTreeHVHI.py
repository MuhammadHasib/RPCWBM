#!/usr/bin/env python
import json
from ROOT import *
import datetime

###########
#HI_EN4_2015_2.txt
#HV_EN4_2015_2.txt

gROOT.ProcessLine(".L FlatTree.h+");
class merge():
    def __init__(self):
        self.data=[]
        self.names=[]

    def mergeJSON(self,Jsons):
      for i,dataA in enumerate(Jsons):
        if self.data == [] :
          self.data = dataA
          for j,adataA in enumerate(dataA):
             self.names.append(adataA["name"])
             print str(adataA["name"])
        else :
          for j,adataA in enumerate(dataA):
            if self.data[i]["name"].find(adataA["name"])>-1:
              self.data[i]["data"]+=adataA["data"]
          #print adataA
        #check missing name
        for j,adataA in enumerate(dataA):
          isFind=False
          for k in self.names:
            if k.find(adataA["name"])>-1 : isFind=True
          if isFind==False:
            self.names.append(adataA["name"])
            self.data.append(adataA)
            print str(adataA["name"])
    def getData(self):
        return self.data

def getJSON(name_):
  jsons = []
  for i in range(1,9): 
    Name_ = (name_+"_2015_%d.txt"%i)
    json1_ = open(Name_)
    print Name_
    data2_ = json.load(json1_)
  
    data_ = data2_['data']
    #print data_
    jsons.append( data_)
  return jsons

#def mergeJSON(Jsons):
  #jsonM = []
  #for i,dataA in enumerate(Jsons):
    #if i==0:
      #jsonM = dataA
      #print str(dataA[0])
    #else :
      #for j,adataA in enumerate(dataA):
       # if jsonM[i]["name"].find(adataA["name"])>-1:
          #jsonM[i]["data"]+=adataA["data"]
       # print adataA

  #return jsonM

############################################
def makeTree(jsonAm, jsonBm):
  tree_ = TTree("tree",'RPC WBM tree')
  fevent_ =FlatTree()
  fevent_.book(tree_)
  ###############
  for i,dataA3 in enumerate(jsonAm):
    xx=[]
    yy=[]
    j=-1
    name = "%s"%dataA3['name']
    for ii,dataB3 in enumerate(jsonBm): 
      if name.find(dataB3['name'])>-1 : j=ii
    #print "j: "+str(j)
    dataB3 = jsonBm[j]['data']
    dpid = 0
    value2_=-1
    if len(dataA3['id'])==1 : dpid=dataA3['id'][0]
    #print "type(name) : " + type(name)
    for ii in dataA3['data']:
      fevent_.clear()
      yyMMdd = int(datetime.datetime.fromtimestamp( int(ii[0])/1000 ).strftime('%Y%m%d'))
      hhmmss = int(datetime.datetime.fromtimestamp( int(ii[0])/1000 ).strftime('%H%M%S'))
      fevent_.yyyyMMdd_ = yyMMdd
      fevent_.hhmmss_   = hhmmss 
      fevent_.value_=float(ii[1])
      fevent_.dpid_=int(dpid)
      fevent_.name_.push_back(str(name))
    
      for jj in dataB3:
        #print "jj[0]:"+str(jj[0])
        yyMMdd2 = int(datetime.datetime.fromtimestamp( int(jj[0])/1000 ).strftime('%Y%m%d'))
        hhmmss2 = int(datetime.datetime.fromtimestamp( int(jj[0])/1000 ).strftime('%H%M%S'))
        #print str(yyMMdd2) +" "+ str(hhmmss2) +" "+str(jj[1])
        if (yyMMdd2 < yyMMdd) or (yyMMdd2 == yyMMdd) and (hhmmss2 < hhmmss or hhmmss2==hhmmss) : value2_ = float(jj[1])
        #if yyMMdd2 < yyMMdd and hhmmss2 < hhmmss : value2_ = float(jj[1])
      fevent_.value2_ = value2_
      #print "name1:"+name+", name2:"+dataB2[j]['name']
      if value2_>-1 : tree_.Fill()
  return tree_
############################################





jsonAs = getJSON("HV_EN1")
jsonBs = getJSON("HI_EN1")
jsonCs = getJSON("HV_EN2")
jsonDs = getJSON("HI_EN2")
jsonEs = getJSON("HV_EN3")
jsonFs = getJSON("HI_EN3")
jsonGs = getJSON("HV_EN4")
jsonHs = getJSON("HI_EN4")
jsonIs = getJSON("HV_EP1")
jsonJs = getJSON("HI_EP1")
jsonKs = getJSON("HV_EP2")
jsonLs = getJSON("HI_EP2")
jsonTs = getJSON("HV_EP3")
jsonNs = getJSON("HI_EP3")
jsonOs = getJSON("HV_EP4")
jsonPs = getJSON("HI_EP4")

#print "bbbbbbbbbbb"+str(jsonAs)+"bbbbbbbb"
#print "aaaaaaaaaaaaaa"+str(jsonAs)+"aaaaaaaaa"
jsonAm= merge();
jsonBm=merge();

jsonAm.mergeJSON(jsonAs)
jsonBm.mergeJSON(jsonBs)
jsonAm.mergeJSON(jsonCs)
jsonBm.mergeJSON(jsonDs)
jsonAm.mergeJSON(jsonEs)
jsonBm.mergeJSON(jsonFs)
jsonAm.mergeJSON(jsonGs)
jsonBm.mergeJSON(jsonHs)
jsonAm.mergeJSON(jsonIs)
jsonBm.mergeJSON(jsonJs)
jsonAm.mergeJSON(jsonKs)
jsonBm.mergeJSON(jsonLs)
jsonAm.mergeJSON(jsonTs)
jsonBm.mergeJSON(jsonNs)
jsonAm.mergeJSON(jsonOs)
jsonBm.mergeJSON(jsonPs)
FulljsonaftermargeAm=jsonAm.getData()
FulljsonaftermargeBm=jsonAm.getData()
#print "bbbbbbbbbbb"+str(jsonBm)+"bbbbbbbb"
#print "bbbbbbbbbbb"+str(FulljsonaftermargeAm)+"bbbbbbbb"
#print "bbbbbbbbbbb"+str(FulljsonaftermargeBm)+"bbbbbbbb"
#print "aaaaaaaaaaaaaa"+str(jsonAm)+"aaaaaaaaa"

f = TFile('RPCWBM.root','RECREATE')
#tree_ = makeTree(jsonAm, jsonBm)
tree_ = makeTree(FulljsonaftermargeAm, FulljsonaftermargeBm)
f.Write()
f.Close()


