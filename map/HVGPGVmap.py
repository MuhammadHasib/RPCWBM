#!/usr/bin/env python
import copy

# HV GP GV map

mapGV = {}
# DB:OMDS, table:CMS_RPC_PVSS_COND.RPCGLOBALVALUE
#current(HV) for wheel and disk
# name : DPID
mapGV[113413] = "W-2" 
mapGV[113412] = "W-1" 
mapGV[113411] = "W0"  
mapGV[113410] = "W+1" 
mapGV[113409] = "W+2" 
mapGV[203884] = "RE-4"
mapGV[146840] = "RE-3"
mapGV[146841] = "RE-2"
mapGV[146842] = "RE-1"
mapGV[146845] = "RE+1"
mapGV[146844] = "RE+2"
mapGV[146843] = "RE+3"
mapGV[203885] = "RE+4"


mapGP = {}
# DB:OMDS, table:CMS_RPC_PVSS_COND.RPCGLOBALPERC
# name : DPID
mapGP[184299] = "Barrel_Imon"    
mapGP[184301] = "Endcap_Imon"    
mapGP[184304] = "Barrel_Imon7000"
mapGP[184303] = "Endcap_Imon7000"
mapGP[184298] = "Barrel_Vmon"    
mapGP[184300] = "Endcap_Vmon"    


