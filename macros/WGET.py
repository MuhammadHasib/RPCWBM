#!/usr/bin/env python

import os

datelist = []
outputNameHVN4 = []
outputNameHIN4 = []
outputNameHVP4 = []
outputNameHIP4 = []
#for only 2015
for i in range(1,10):
  if i<10 : datelist.append( ("2015.0%d.01%%2000:00:00"%i) )
  else    : datelist.append( ("2015.%d.01%%2000:00:00"%i) )
  outputNameHVN4.append( ("HV_EN4_2015_%d.txt"%i) )
  outputNameHIN4.append( ("HI_EN4_2015_%d.txt"%i) )
  outputNameHVP4.append( ("HV_EP4_2015_%d.txt"%i) )
  outputNameHIP4.append( ("HI_EP4_2015_%d.txt"%i) )


command1 = "wget -O "
command2 = " --load-cookies ~/private/ssocookie.txt https://cmswbmoff.web.cern.ch/cmswbmoff/cmsdb/servlet/RPCHVTime?TopMenu=RPCHVTime\&TopMenu2=ZeroPage\&"
hv = "isSP=0\&"
hi = "isSP=1\&"
option = "SubMenu=0\&Type=1\&TimeLine=0\&Backdoor=1\&"
EN4 = "Region=1\&Disk=0\&ChamberD4=36\&"
EP4 = "Region=1\&Disk=7\&ChamberD4=36\&"

for i in range(0,len(datelist)-1):
  date1 = "beginDate="+datelist[i]+"\&"
  date2 = "endDate="+datelist[i+1]+"\&"
  commandHVN4 = command1+outputNameHVN4[i]+command2+hv+option+date2+EN4
  commandHIN4 = command1+outputNameHIN4[i]+command2+hi+option+date2+EN4

  commandHVP4 = command1+outputNameHVP4[i]+command2+hv+option+date2+EP4
  commandHIP4 = command1+outputNameHIP4[i]+command2+hi+option+date2+EP4


  print commandHVN4
  print commandHIN4
  os.system(commandHVN4)
  os.system(commandHIN4)

  print commandHVP4
  print commandHIP4
  os.system(commandHVP4)
  os.system(commandHIP4)


