#!/usr/bin/env python

import os

wheel = ["WM2","WM1","W0","WP1","WP2"]
wheelN = range(0,5)
disk = ["EN4","EN3","EN2","EN1","EP1","EP2","EP3","EP4"]
diskNN = ["4","3","2","1","1","2","3","4"]
diskN = range(0,8)
#print diskN

def dateSets(YYYY,M1, M2 ):
  dateSet = []
  YY =str(YYYY)
  DHMS = ".01%%2000:00:00"
  for i in range(0,M2-M1): 
    MM1=  str( ("0%d"% (M1+i)  ) )
    MM2=  str( ("0%d"% (M1+i+1)) )
    if (M1+i)>9    :  MM1=  str( ("%d"% (M1+i)  ) )
    if (M1+i+1)>9  :  MM2=  str( ("%d"% (M1+i+1)) )
    dateSet.append( "beginDate="+YY+"."+MM1+DHMS+"\&endDate="+YY+"."+MM2+DHMS+"\&" )
  return dateSet

###############################################
def diskSel(diskN_):
  if diskN_==3 or diskN_==4 : return ("Region=1\&Disk=%d\&ChamberD1R23=36\&"% diskN_ )
  else                      : return ("Region=1\&Disk=%d\&ChamberD%s=36\&"% (diskN_,diskNN[diskN_]) )
def diskSels():
  DiskSel = []
  for i in diskN : DiskSel.append( diskSel(i) )
  return DiskSel

def wheelSel(wheelN_):
  return ("Region=0\&Wheel=%d\&Station=4\&Sector=12\&SubSector34=5\&"% wheelN_ )
def wheelSels():
  WheelSel = []
  for i in wheelN: WheelSel.append( wheelSel(i) )
  return WheelSel
###############
def makeCMD(cmd1_,output,cmd2,selection):
  return cmd1_+output+cmd2+selection
######################


###################################################
command1 = "wget -O "
command2 = " --load-cookies ~/private/ssocookie.txt https://cmswbmoff.web.cern.ch/cmswbmoff/cmsdb/servlet/RPCHVTime?TopMenu=RPCHVTime\&TopMenu2=ZeroPage\&"
hv = "isSP=0\&"
hi = "isSP=1\&"
option = "SubMenu=0\&Type=1\&TimeLine=0\&Backdoor=1\&"

DiskSel = diskSels()
WheelSel = wheelSels()
#print str(DiskSel)
DateSets = dateSets(2015,1,9)

print WheelSel 

CMDSets = []
for j,dateSet in enumerate(DateSets):
  for i,w in enumerate(wheel):
    output1 = "HV_"+w+"_"+str(j)+".txt"
    output2 = "HI_"+w+"_"+str(j)+".txt"
    selection1 = hv+option+WheelSel[i]+dateSet
    selection2 = hi+option+WheelSel[i]+dateSet
    CMDSets.append( makeCMD(command1,output1,command2, selection1 ) )
    CMDSets.append( makeCMD(command1,output2,command2, selection2 ) )
  for i,e in enumerate(disk):
    output1 = "HV_"+e+"_"+str(j)+".txt"
    output2 = "HI_"+e+"_"+str(j)+".txt"
    selection1 = hv+option+DiskSel[i]+dateSet
    selection2 = hi+option+DiskSel[i]+dateSet
    CMDSets.append( makeCMD(command1,output1,command2, selection1 ) )
    CMDSets.append( makeCMD(command1,output2,command2, selection2 ) )

for cmd in CMDSets:
  print cmd
  os.system(cmd)

