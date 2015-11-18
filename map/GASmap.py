#!/usr/bin/env python
import copy

# GAS map
# DB:OMDS, table:CMS_RPC_PVSS_COND.RPCGASCHANNEL

mapLast = {}
mapLast[16310] = "W00_S01_RB1"
mapLast[16311] = "W00_S01_RB2"
mapLast[16312] = "W00_S01_RB3"
mapLast[16313] = "W00_S01_RB4"
mapLast[16314] = "W00_S02_RB1"
mapLast[16315] = "W00_S02_RB2"
mapLast[16316] = "W00_S02_RB3"
mapLast[16317] = "W00_S02_RB4"
mapLast[16318] = "W00_S03_RB1"
mapLast[16319] = "W00_S03_RB2"
mapLast[16320] = "W00_S03_RB3"
mapLast[16321] = "W00_S03_RB4"
mapLast[16322] = "W00_S04_RB1"
mapLast[16323] = "W00_S04_RB2"
mapLast[16324] = "W00_S04_RB3"
mapLast[16325] = "W00_S04_RB4L"
mapLast[16326] = "W00_S04_RB4R"
mapLast[16327] = "W00_S05_RB1"
mapLast[16328] = "W00_S05_RB2"
mapLast[16329] = "W00_S05_RB3"
mapLast[16330] = "W00_S05_RB4"
mapLast[16331] = "W00_S06_RB1"
mapLast[16332] = "W00_S06_RB2"
mapLast[16333] = "W00_S06_RB3"
mapLast[16334] = "W00_S06_RB4"
mapLast[16335] = "W00_S07_RB1"
mapLast[16336] = "W00_S07_RB2"
mapLast[16337] = "W00_S07_RB3"
mapLast[16338] = "W00_S07_RB4"
mapLast[16339] = "W00_S08_RB1"
mapLast[16340] = "W00_S08_RB2"
mapLast[16341] = "W00_S08_RB3"
mapLast[16342] = "W00_S08_RB4"
mapLast[16343] = "W00_S09_RB1"
mapLast[16344] = "W00_S09_RB2"
mapLast[16345] = "W00_S09_RB3"
mapLast[16346] = "W00_S09_RB4"
mapLast[16347] = "W00_S10_RB1"
mapLast[16348] = "W00_S10_RB2"
mapLast[16349] = "W00_S10_RB3"
mapLast[16350] = "W00_S10_RB4L"
mapLast[16351] = "W00_S10_RB4R"
mapLast[16352] = "W00_S11_RB1"
mapLast[16353] = "W00_S11_RB2"
mapLast[16354] = "W00_S11_RB3"
mapLast[16355] = "W00_S11_RB4"
mapLast[16356] = "W00_S12_RB1"
mapLast[16357] = "W00_S12_RB2"
mapLast[16358] = "W00_S12_RB3"
mapLast[16359] = "W00_S12_RB4"
mapLast[16360] = "WM1_S01_RB1"
mapLast[16361] = "WM1_S01_RB2"
mapLast[16362] = "WM1_S01_RB3"
mapLast[16363] = "WM1_S01_RB4"
mapLast[16364] = "WM1_S02_RB1"
mapLast[16365] = "WM1_S02_RB2"
mapLast[16366] = "WM1_S02_RB3"
mapLast[16367] = "WM1_S02_RB4"
mapLast[16368] = "WM1_S03_RB1"
mapLast[16369] = "WM1_S03_RB2"
mapLast[16370] = "WM1_S03_RB3"
mapLast[16371] = "WM1_S03_RB4"
mapLast[16372] = "WM1_S04_RB1"
mapLast[16373] = "WM1_S04_RB2"
mapLast[16374] = "WM1_S04_RB3"
mapLast[16375] = "WM1_S04_RB4L"
mapLast[16376] = "WM1_S04_RB4R"
mapLast[16377] = "WM1_S05_RB1"
mapLast[16378] = "WM1_S05_RB2"
mapLast[16379] = "WM1_S05_RB3"
mapLast[16380] = "WM1_S05_RB4"
mapLast[16381] = "WM1_S06_RB1"
mapLast[16382] = "WM1_S06_RB2"
mapLast[16383] = "WM1_S06_RB3"
mapLast[16384] = "WM1_S06_RB4"
mapLast[16385] = "WM1_S07_RB1"
mapLast[16386] = "WM1_S07_RB2"
mapLast[16387] = "WM1_S07_RB3"
mapLast[16388] = "WM1_S07_RB4"
mapLast[16389] = "WM1_S08_RB1"
mapLast[16390] = "WM1_S08_RB2"
mapLast[16391] = "WM1_S08_RB3"
mapLast[16392] = "WM1_S08_RB4"
mapLast[16393] = "WM1_S09_RB1"
mapLast[16394] = "WM1_S09_RB2"
mapLast[16395] = "WM1_S09_RB3"
mapLast[16396] = "WM1_S09_RB4"
mapLast[16397] = "WM1_S10_RB1"
mapLast[16398] = "WM1_S10_RB2"
mapLast[16399] = "WM1_S10_RB3"
mapLast[16400] = "WM1_S10_RB4L"
mapLast[16401] = "WM1_S10_RB4R"
mapLast[16402] = "WM1_S11_RB1"
mapLast[16403] = "WM1_S11_RB2"
mapLast[16404] = "WM1_S11_RB3"
mapLast[16405] = "WM1_S11_RB4"
mapLast[16406] = "WM1_S12_RB1"
mapLast[16407] = "WM1_S12_RB2"
mapLast[16408] = "WM1_S12_RB3"
mapLast[16409] = "WM1_S12_RB4"
mapLast[16410] = "WM2_S01_RB1"
mapLast[16411] = "WM2_S01_RB2"
mapLast[16412] = "WM2_S01_RB3"
mapLast[16413] = "WM2_S01_RB4"
mapLast[16414] = "WM2_S02_RB1"
mapLast[16415] = "WM2_S02_RB2"
mapLast[16416] = "WM2_S02_RB3"
mapLast[16417] = "WM2_S02_RB4"
mapLast[16418] = "WM2_S03_RB1"
mapLast[16419] = "WM2_S03_RB2"
mapLast[16420] = "WM2_S03_RB3"
mapLast[16421] = "WM2_S03_RB4"
mapLast[16422] = "WM2_S04_RB1"
mapLast[16423] = "WM2_S04_RB2"
mapLast[16424] = "WM2_S04_RB3"
mapLast[16425] = "WM2_S04_RB4L"
mapLast[16426] = "WM2_S04_RB4R"
mapLast[16427] = "WM2_S05_RB1"
mapLast[16428] = "WM2_S05_RB2"
mapLast[16429] = "WM2_S05_RB3"
mapLast[16430] = "WM2_S05_RB4"
mapLast[16431] = "WM2_S06_RB1"
mapLast[16432] = "WM2_S06_RB2"
mapLast[16433] = "WM2_S06_RB3"
mapLast[16434] = "WM2_S06_RB4"
mapLast[16435] = "WM2_S07_RB1"
mapLast[16436] = "WM2_S07_RB2"
mapLast[16437] = "WM2_S07_RB3"
mapLast[16438] = "WM2_S07_RB4"
mapLast[16439] = "WM2_S08_RB1"
mapLast[16440] = "WM2_S08_RB2"
mapLast[16441] = "WM2_S08_RB3"
mapLast[16442] = "WM2_S08_RB4"
mapLast[16443] = "WM2_S09_RB1"
mapLast[16444] = "WM2_S09_RB2"
mapLast[16445] = "WM2_S09_RB3"
mapLast[16446] = "WM2_S09_RB4"
mapLast[16447] = "WM2_S10_RB1"
mapLast[16448] = "WM2_S10_RB2"
mapLast[16449] = "WM2_S10_RB3"
mapLast[16450] = "WM2_S10_RB4L"
mapLast[16451] = "WM2_S10_RB4R"
mapLast[16452] = "WM2_S11_RB1"
mapLast[16453] = "WM2_S11_RB2"
mapLast[16454] = "WM2_S11_RB3"
mapLast[16455] = "WM2_S11_RB4"
mapLast[16456] = "WM2_S12_RB1"
mapLast[16457] = "WM2_S12_RB2"
mapLast[16458] = "WM2_S12_RB3"
mapLast[16459] = "WM2_S12_RB4"
mapLast[16460] = "WP1_S01_RB1"
mapLast[16461] = "WP1_S01_RB2"
mapLast[16462] = "WP1_S01_RB3"
mapLast[16463] = "WP1_S01_RB4"
mapLast[16464] = "WP1_S02_RB1"
mapLast[16465] = "WP1_S02_RB2"
mapLast[16466] = "WP1_S02_RB3"
mapLast[16467] = "WP1_S02_RB4"
mapLast[16468] = "WP1_S03_RB1"
mapLast[16469] = "WP1_S03_RB2"
mapLast[16470] = "WP1_S03_RB3"
mapLast[16471] = "WP1_S03_RB4"
mapLast[16472] = "WP1_S04_RB1"
mapLast[16473] = "WP1_S04_RB2"
mapLast[16474] = "WP1_S04_RB3"
mapLast[16475] = "WP1_S04_RB4L"
mapLast[16476] = "WP1_S04_RB4R"
mapLast[16477] = "WP1_S05_RB1"
mapLast[16478] = "WP1_S05_RB2"
mapLast[16479] = "WP1_S05_RB3"
mapLast[16480] = "WP1_S05_RB4"
mapLast[16481] = "WP1_S06_RB1"
mapLast[16482] = "WP1_S06_RB2"
mapLast[16483] = "WP1_S06_RB3"
mapLast[16484] = "WP1_S06_RB4"
mapLast[16485] = "WP1_S07_RB1"
mapLast[16486] = "WP1_S07_RB2"
mapLast[16487] = "WP1_S07_RB3"
mapLast[16488] = "WP1_S07_RB4"
mapLast[16489] = "WP1_S08_RB1"
mapLast[16490] = "WP1_S08_RB2"
mapLast[16491] = "WP1_S08_RB3"
mapLast[16492] = "WP1_S08_RB4"
mapLast[16493] = "WP1_S09_RB1"
mapLast[16494] = "WP1_S09_RB2"
mapLast[16495] = "WP1_S09_RB3"
mapLast[16496] = "WP1_S09_RB4"
mapLast[16497] = "WP1_S10_RB1"
mapLast[16498] = "WP1_S10_RB2"
mapLast[16499] = "WP1_S10_RB3"
mapLast[16500] = "WP1_S10_RB4L"
mapLast[16501] = "WP1_S10_RB4R"
mapLast[16502] = "WP1_S11_RB1"
mapLast[16503] = "WP1_S11_RB2"
mapLast[16504] = "WP1_S11_RB3"
mapLast[16505] = "WP1_S11_RB4"
mapLast[16506] = "WP1_S12_RB1"
mapLast[16507] = "WP1_S12_RB2"
mapLast[16508] = "WP1_S12_RB3"
mapLast[16509] = "WP1_S12_RB4"
mapLast[16510] = "WP2_S01_RB1"
mapLast[16511] = "WP2_S01_RB2"
mapLast[16512] = "WP2_S01_RB3"
mapLast[16513] = "WP2_S01_RB4"
mapLast[16514] = "WP2_S02_RB1"
mapLast[16515] = "WP2_S02_RB2"
mapLast[16516] = "WP2_S02_RB3"
mapLast[16517] = "WP2_S02_RB4"
mapLast[16518] = "WP2_S03_RB1"
mapLast[16519] = "WP2_S03_RB2"
mapLast[16520] = "WP2_S03_RB3"
mapLast[16521] = "WP2_S03_RB4"
mapLast[16522] = "WP2_S04_RB1"
mapLast[16523] = "WP2_S04_RB2"
mapLast[16524] = "WP2_S04_RB3"
mapLast[16525] = "WP2_S04_RB4L"
mapLast[16526] = "WP2_S04_RB4R"
mapLast[16527] = "WP2_S05_RB1"
mapLast[16528] = "WP2_S05_RB2"
mapLast[16529] = "WP2_S05_RB3"
mapLast[16530] = "WP2_S05_RB4"
mapLast[16531] = "WP2_S06_RB1"
mapLast[16532] = "WP2_S06_RB2"
mapLast[16533] = "WP2_S06_RB3"
mapLast[16534] = "WP2_S06_RB4"
mapLast[16535] = "WP2_S07_RB1"
mapLast[16536] = "WP2_S07_RB2"
mapLast[16537] = "WP2_S07_RB3"
mapLast[16538] = "WP2_S07_RB4"
mapLast[16539] = "WP2_S08_RB1"
mapLast[16540] = "WP2_S08_RB2"
mapLast[16541] = "WP2_S08_RB3"
mapLast[16542] = "WP2_S08_RB4"
mapLast[16543] = "WP2_S09_RB1"
mapLast[16544] = "WP2_S09_RB2"
mapLast[16545] = "WP2_S09_RB3"
mapLast[16546] = "WP2_S09_RB4"
mapLast[16547] = "WP2_S10_RB1"
mapLast[16548] = "WP2_S10_RB2"
mapLast[16549] = "WP2_S10_RB3"
mapLast[16550] = "WP2_S10_RB4L"
mapLast[16551] = "WP2_S10_RB4R"
mapLast[16552] = "WP2_S11_RB1"
mapLast[16553] = "WP2_S11_RB2"
mapLast[16554] = "WP2_S11_RB3"
mapLast[16555] = "WP2_S11_RB4"
mapLast[16556] = "WP2_S12_RB1"
mapLast[16557] = "WP2_S12_RB2"
mapLast[16558] = "WP2_S12_RB3"
mapLast[16559] = "WP2_S12_RB4"
mapLast[117745] = "EM1_R02_C06_C11_DW"
mapLast[117746] = "EM1_R02_C06_C11_UP"
mapLast[117747] = "EM1_R02_C12_C17_DW"
mapLast[117748] = "EM1_R02_C12_C17_UP"
mapLast[117749] = "EM1_R02_C18_C23_DW"
mapLast[117750] = "EM1_R02_C18_C23_UP"
mapLast[117751] = "EM1_R02_C24_C29_DW"
mapLast[117752] = "EM1_R02_C24_C29_UP"
mapLast[117753] = "EM1_R02_C30_C35_DW"
mapLast[117754] = "EM1_R02_C30_C35_UP"
mapLast[117755] = "EM1_R02_C36_C05_DW"
mapLast[117756] = "EM1_R02_C36_C05_UP"
mapLast[117757] = "EM1_R03_C06_C11_DW"
mapLast[117758] = "EM1_R03_C06_C11_UP"
mapLast[117759] = "EM1_R03_C12_C17_DW"
mapLast[117760] = "EM1_R03_C12_C17_UP"
mapLast[117761] = "EM1_R03_C18_C23_DW"
mapLast[117762] = "EM1_R03_C18_C23_UP"
mapLast[117763] = "EM1_R03_C24_C29_DW"
mapLast[117764] = "EM1_R03_C24_C29_UP"
mapLast[117765] = "EM1_R03_C30_C35_DW"
mapLast[117766] = "EM1_R03_C30_C35_UP"
mapLast[117767] = "EM1_R03_C36_C05_DW"
mapLast[117768] = "EM1_R03_C36_C05_UP"
mapLast[117769] = "EM2_R02_R03_C03_C05_DW"
mapLast[117770] = "EM2_R02_R03_C03_C05_UP"
mapLast[117771] = "EM2_R02_R03_C06_C08_DW"
mapLast[117772] = "EM2_R02_R03_C06_C08_UP"
mapLast[117773] = "EM2_R02_R03_C09_C11_DW"
mapLast[117774] = "EM2_R02_R03_C09_C11_UP"
mapLast[117775] = "EM2_R02_R03_C12_C14_DW"
mapLast[117776] = "EM2_R02_R03_C12_C14_UP"
mapLast[117777] = "EM2_R02_R03_C15_C17_DW"
mapLast[117778] = "EM2_R02_R03_C15_C17_UP"
mapLast[117779] = "EM2_R02_R03_C18_C20_DW"
mapLast[117780] = "EM2_R02_R03_C18_C20_UP"
mapLast[117781] = "EM2_R02_R03_C21_C23_DW"
mapLast[117782] = "EM2_R02_R03_C21_C23_UP"
mapLast[117783] = "EM2_R02_R03_C24_C26_DW"
mapLast[117784] = "EM2_R02_R03_C24_C26_UP"
mapLast[117785] = "EM2_R02_R03_C27_C29_DW"
mapLast[117786] = "EM2_R02_R03_C27_C29_UP"
mapLast[117787] = "EM2_R02_R03_C30_C32_DW"
mapLast[117788] = "EM2_R02_R03_C30_C32_UP"
mapLast[117789] = "EM2_R02_R03_C33_C35_DW"
mapLast[117790] = "EM2_R02_R03_C33_C35_UP"
mapLast[117791] = "EM2_R02_R03_C36_C02_DW"
mapLast[117792] = "EM2_R02_R03_C36_C02_UP"
mapLast[117793] = "EM3_R02_R03_C01_C03_DW"
mapLast[117794] = "EM3_R02_R03_C01_C03_UP"
mapLast[117795] = "EM3_R02_R03_C04_C06_DW"
mapLast[117796] = "EM3_R02_R03_C04_C06_UP"
mapLast[117797] = "EM3_R02_R03_C07_C09_DW"
mapLast[117798] = "EM3_R02_R03_C07_C09_UP"
mapLast[117799] = "EM3_R02_R03_C10_C12_DW"
mapLast[117800] = "EM3_R02_R03_C10_C12_UP"
mapLast[117801] = "EM3_R02_R03_C13_C15_DW"
mapLast[117802] = "EM3_R02_R03_C13_C15_UP"
mapLast[117803] = "EM3_R02_R03_C16_C18_DW"
mapLast[117804] = "EM3_R02_R03_C16_C18_UP"
mapLast[117805] = "EM3_R02_R03_C19_C21_DW"
mapLast[117806] = "EM3_R02_R03_C19_C21_UP"
mapLast[117807] = "EM3_R02_R03_C22_C24_DW"
mapLast[117808] = "EM3_R02_R03_C22_C24_UP"
mapLast[117809] = "EM3_R02_R03_C25_C27_DW"
mapLast[117810] = "EM3_R02_R03_C25_C27_UP"
mapLast[117811] = "EM3_R02_R03_C28_C30_DW"
mapLast[117812] = "EM3_R02_R03_C28_C30_UP"
mapLast[117813] = "EM3_R02_R03_C31_C33_DW"
mapLast[117814] = "EM3_R02_R03_C31_C33_UP"
mapLast[117815] = "EM3_R02_R03_C34_C36_DW"
mapLast[117816] = "EM3_R02_R03_C34_C36_UP"
mapLast[117817] = "EP1_R02_C06_C11_DW"
mapLast[117818] = "EP1_R02_C06_C11_UP"
mapLast[117819] = "EP1_R02_C12_C17_DW"
mapLast[117820] = "EP1_R02_C12_C17_UP"
mapLast[117821] = "EP1_R02_C18_C23_DW"
mapLast[117822] = "EP1_R02_C18_C23_UP"
mapLast[117823] = "EP1_R02_C24_C29_DW"
mapLast[117824] = "EP1_R02_C24_C29_UP"
mapLast[117825] = "EP1_R02_C30_C35_DW"
mapLast[117826] = "EP1_R02_C30_C35_UP"
mapLast[117827] = "EP1_R02_C36_C05_DW"
mapLast[117828] = "EP1_R02_C36_C05_UP"
mapLast[117829] = "EP1_R03_C06_C11_DW"
mapLast[117830] = "EP1_R03_C06_C11_UP"
mapLast[117831] = "EP1_R03_C12_C17_DW"
mapLast[117832] = "EP1_R03_C12_C17_UP"
mapLast[117833] = "EP1_R03_C18_C23_DW"
mapLast[117834] = "EP1_R03_C18_C23_UP"
mapLast[117835] = "EP1_R03_C24_C29_DW"
mapLast[117836] = "EP1_R03_C24_C29_UP"
mapLast[117837] = "EP1_R03_C30_C35_DW"
mapLast[117838] = "EP1_R03_C30_C35_UP"
mapLast[117839] = "EP1_R03_C36_C05_DW"
mapLast[117840] = "EP1_R03_C36_C05_UP"
mapLast[117841] = "EP2_R02_R03_C03_C05_DW"
mapLast[117842] = "EP2_R02_R03_C03_C05_UP"
mapLast[117843] = "EP2_R02_R03_C06_C08_DW"
mapLast[117844] = "EP2_R02_R03_C06_C08_UP"
mapLast[117845] = "EP2_R02_R03_C09_C11_DW"
mapLast[117846] = "EP2_R02_R03_C09_C11_UP"
mapLast[117847] = "EP2_R02_R03_C12_C14_DW"
mapLast[117848] = "EP2_R02_R03_C12_C14_UP"
mapLast[117849] = "EP2_R02_R03_C15_C17_DW"
mapLast[117850] = "EP2_R02_R03_C15_C17_UP"
mapLast[117851] = "EP2_R02_R03_C18_C20_DW"
mapLast[117852] = "EP2_R02_R03_C18_C20_UP"
mapLast[117853] = "EP2_R02_R03_C21_C23_DW"
mapLast[117854] = "EP2_R02_R03_C21_C23_UP"
mapLast[117855] = "EP2_R02_R03_C24_C26_DW"
mapLast[117856] = "EP2_R02_R03_C24_C26_UP"
mapLast[117857] = "EP2_R02_R03_C27_C29_DW"
mapLast[117858] = "EP2_R02_R03_C27_C29_UP"
mapLast[117859] = "EP2_R02_R03_C30_C32_DW"
mapLast[117860] = "EP2_R02_R03_C30_C32_UP"
mapLast[117861] = "EP2_R02_R03_C33_C35_DW"
mapLast[117862] = "EP2_R02_R03_C33_C35_UP"
mapLast[117863] = "EP2_R02_R03_C36_C02_DW"
mapLast[117864] = "EP2_R02_R03_C36_C02_UP"
mapLast[117865] = "EP3_R02_R03_C01_C03_DW"
mapLast[117866] = "EP3_R02_R03_C01_C03_UP"
mapLast[117867] = "EP3_R02_R03_C04_C06_DW"
mapLast[117868] = "EP3_R02_R03_C04_C06_UP"
mapLast[117869] = "EP3_R02_R03_C07_C09_DW"
mapLast[117870] = "EP3_R02_R03_C07_C09_UP"
mapLast[117871] = "EP3_R02_R03_C10_C12_DW"
mapLast[117872] = "EP3_R02_R03_C10_C12_UP"
mapLast[117873] = "EP3_R02_R03_C13_C15_DW"
mapLast[117874] = "EP3_R02_R03_C13_C15_UP"
mapLast[117875] = "EP3_R02_R03_C16_C18_DW"
mapLast[117876] = "EP3_R02_R03_C16_C18_UP"
mapLast[117877] = "EP3_R02_R03_C19_C21_DW"
mapLast[117878] = "EP3_R02_R03_C19_C21_UP"
mapLast[117879] = "EP3_R02_R03_C22_C24_DW"
mapLast[117880] = "EP3_R02_R03_C22_C24_UP"
mapLast[117881] = "EP3_R02_R03_C25_C27_DW"
mapLast[117882] = "EP3_R02_R03_C25_C27_UP"
mapLast[117883] = "EP3_R02_R03_C28_C30_DW"
mapLast[117884] = "EP3_R02_R03_C28_C30_UP"
mapLast[117885] = "EP3_R02_R03_C31_C33_DW"
mapLast[117886] = "EP3_R02_R03_C31_C33_UP"
mapLast[117887] = "EP3_R02_R03_C34_C36_DW"
mapLast[117888] = "EP3_R02_R03_C34_C36_UP"
mapLast[199944] = "rpc_ggm_ch01"
mapLast[199945] = "rpc_ggm_ch02"
mapLast[199946] = "rpc_ggm_ch03"
mapLast[199947] = "rpc_ggm_ch04"
mapLast[199948] = "rpc_ggm_ch05"
mapLast[199949] = "rpc_ggm_ch06"
mapLast[199950] = "rpc_ggm_ch07"
mapLast[199951] = "rpc_ggm_ch08"
mapLast[219565] = "EM4_R02_R03_C01_C02_DW"
mapLast[219566] = "EM4_R02_R03_C01_C02_UP"
mapLast[219567] = "EM4_R02_R03_C03_C04_DW"
mapLast[219568] = "EM4_R02_R03_C03_C04_UP"
mapLast[219569] = "EM4_R02_R03_C05_C06_DW"
mapLast[219570] = "EM4_R02_R03_C05_C06_UP"
mapLast[219571] = "EM4_R02_R03_C07_C08_DW"
mapLast[219572] = "EM4_R02_R03_C07_C08_UP"
mapLast[219573] = "EM4_R02_R03_C09_C10_DW"
mapLast[219574] = "EM4_R02_R03_C09_C10_UP"
mapLast[219575] = "EM4_R02_R03_C11_C12_DW"
mapLast[219576] = "EM4_R02_R03_C11_C12_UP"
mapLast[219577] = "EM4_R02_R03_C13_C14_DW"
mapLast[219578] = "EM4_R02_R03_C13_C14_UP"
mapLast[219579] = "EM4_R02_R03_C15_C16_DW"
mapLast[219580] = "EM4_R02_R03_C15_C16_UP"
mapLast[219581] = "EM4_R02_R03_C17_C18_DW"
mapLast[219582] = "EM4_R02_R03_C17_C18_UP"
mapLast[219583] = "EM4_R02_R03_C19_C20_DW"
mapLast[219584] = "EM4_R02_R03_C19_C20_UP"
mapLast[219585] = "EM4_R02_R03_C21_C22_DW"
mapLast[219586] = "EM4_R02_R03_C21_C22_UP"
mapLast[219587] = "EM4_R02_R03_C23_C24_DW"
mapLast[219588] = "EM4_R02_R03_C23_C24_UP"
mapLast[219589] = "EM4_R02_R03_C25_C26_DW"
mapLast[219590] = "EM4_R02_R03_C25_C26_UP"
mapLast[219591] = "EM4_R02_R03_C27_C28_DW"
mapLast[219592] = "EM4_R02_R03_C27_C28_UP"
mapLast[219593] = "EM4_R02_R03_C29_C30_DW"
mapLast[219594] = "EM4_R02_R03_C29_C30_UP"
mapLast[219595] = "EM4_R02_R03_C31_C32_DW"
mapLast[219596] = "EM4_R02_R03_C31_C32_UP"
mapLast[219597] = "EM4_R02_R03_C33_C34_DW"
mapLast[219598] = "EM4_R02_R03_C33_C34_UP"
mapLast[219599] = "EM4_R02_R03_C35_C36_DW"
mapLast[219600] = "EM4_R02_R03_C35_C36_UP"
mapLast[219601] = "EP1_R01_C01_C04_DW"
mapLast[219602] = "EP1_R01_C01_C04_UP"
mapLast[219603] = "EP4_R02_R03_C01_C02_DW"
mapLast[219604] = "EP4_R02_R03_C01_C02_UP"
mapLast[219605] = "EP4_R02_R03_C03_C04_DW"
mapLast[219606] = "EP4_R02_R03_C03_C04_UP"
mapLast[219607] = "EP4_R02_R03_C05_C06_DW"
mapLast[219608] = "EP4_R02_R03_C05_C06_UP"
mapLast[219609] = "EP4_R02_R03_C07_C08_DW"
mapLast[219610] = "EP4_R02_R03_C07_C08_UP"
mapLast[219611] = "EP4_R02_R03_C09_C10_DW"
mapLast[219612] = "EP4_R02_R03_C09_C10_UP"
mapLast[219613] = "EP4_R02_R03_C11_C12_DW"
mapLast[219614] = "EP4_R02_R03_C11_C12_UP"
mapLast[219615] = "EP4_R02_R03_C13_C14_DW"
mapLast[219616] = "EP4_R02_R03_C13_C14_UP"
mapLast[219617] = "EP4_R02_R03_C15_C16_DW"
mapLast[219618] = "EP4_R02_R03_C15_C16_UP"
mapLast[219619] = "EP4_R02_R03_C17_C18_DW"
mapLast[219620] = "EP4_R02_R03_C17_C18_UP"
mapLast[219621] = "EP4_R02_R03_C19_C20_DW"
mapLast[219622] = "EP4_R02_R03_C19_C20_UP"
mapLast[219623] = "EP4_R02_R03_C21_C22_DW"
mapLast[219624] = "EP4_R02_R03_C21_C22_UP"
mapLast[219625] = "EP4_R02_R03_C23_C24_DW"
mapLast[219626] = "EP4_R02_R03_C23_C24_UP"
mapLast[219627] = "EP4_R02_R03_C25_C26_DW"
mapLast[219628] = "EP4_R02_R03_C25_C26_UP"
mapLast[219629] = "EP4_R02_R03_C27_C28_DW"
mapLast[219630] = "EP4_R02_R03_C27_C28_UP"
mapLast[219631] = "EP4_R02_R03_C29_C30_DW"
mapLast[219632] = "EP4_R02_R03_C29_C30_UP"
mapLast[219633] = "EP4_R02_R03_C31_C32_DW"
mapLast[219634] = "EP4_R02_R03_C31_C32_UP"
mapLast[219635] = "EP4_R02_R03_C33_C34_DW"
mapLast[219636] = "EP4_R02_R03_C33_C34_UP"
mapLast[219637] = "EP4_R02_R03_C35_C36_DW"
mapLast[219638] = "EP4_R02_R03_C35_C36_UP"

