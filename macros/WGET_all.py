#!/usr/bin/env python

import os

wheel = ["WM2","WM1","W0","WP1","WP2"]
wheelN = range(0,5)
disk = ["EN4","EN3","EN2","EN1","EP1","EP2","EP3","EP4"]
diskNN = ["4","3","2","1","1","2","3","4"]
diskN = range(0,8)

MM =["01","02","03","04","05","06","06","07","08","09","11","12"]
print MM

def dateSets(YYYY,M1,YYYY2, M2 ):
  dateSet = []
  YY =str(YYYY)
  YY2 =str(YYYY2)
  DHMS1 = ".01+12%3A40%3A09"#".01%%2000:00:00"
  DHMS2 = ".10+12%3A40%3A09"#".10%%2000:00:00"
  DHMS3 = ".20+12%3A40%3A09"#".20%%2000:00:00"
  DHMS4 = ".01+12%3A40%3A09"#".01%%2000:00:00"
  YY3 = YYYY2-YYYY
  for i in range(0, (YY3*12)+(M2-M1)+1 ): 
    if M1+i-1>-1 and M1+i-1<12           :  MM1=  YY+"."+MM[M1+i-1]
    elif M1+i-1>11 and (YYYY+1) <= YYYY2 :  MM1=  str(YYYY+1)+"."+MM[M1+i-1-12]

    if M1+i>-1 and M1+i<12               :  MM2=  YY+"."+MM[M1+i]
    elif M1+i>11 and (YYYY+1) <= YYYY2   :  MM2=  str(YYYY+1)+"."+MM[M1+i-12]

    dateSet.append( "beginDate="+MM1+DHMS1+"\&endDate="+MM1+DHMS2+"\&" )
    dateSet.append( "beginDate="+MM1+DHMS2+"\&endDate="+MM1+DHMS3+"\&" )
    dateSet.append( "beginDate="+MM1+DHMS3+"\&endDate="+MM2+DHMS4+"\&" )
  return dateSet

###############################################
def diskSel(diskN_):
  if diskN_==3 or diskN_==4 : return ("Region=1\&Disk=%d\&RingD1=3\&RingD2=2\&RingD3=2\&ChamberD1R23=36\&"% diskN_ )
  else                      : return ("Region=1\&Disk=%d\&RingD1=3\&RingD2=2\&RingD3=2\&ChamberD%s=36\&"% (diskN_,diskNN[diskN_]) )
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
DateSets = dateSets(2015,1,2015,2)

#print DateSets

#ddd="""
CMDSets = []
for j,dateSet in enumerate(DateSets):
  for i,w in enumerate(wheel):
    output1 = "HV_"+w+"_"+str(j)+".txt"
    output2 = "HI_"+w+"_"+str(j)+".txt"
    selection1 = hv+option+WheelSel[i]+dateSet
    selection2 = hi+option+WheelSel[i]+dateSet
    #CMDSets.append( makeCMD(command1,output1,command2, selection1 ) )
    #CMDSets.append( makeCMD(command1,output2,command2, selection2 ) )
  for i,e in enumerate(disk):
    #if e.find("EN1")>-1 or e.find("EP1")>-1:
    if True:
      output1 = "HV_"+e+"_"+str(j)+".txt"
      output2 = "HI_"+e+"_"+str(j)+".txt"
      selection1 = hv+option+DiskSel[i]+dateSet
      selection2 = hi+option+DiskSel[i]+dateSet
      CMDSets.append( makeCMD(command1,output1,command2, selection1 ) )
      CMDSets.append( makeCMD(command1,output2,command2, selection2 ) )

for cmd in CMDSets:
  print cmd
  os.system(cmd)
#"""

