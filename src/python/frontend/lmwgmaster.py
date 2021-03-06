### See master-README for description of this file.

diags_varlist = {}
diags_collection = {}
diags_obslist = {}
from metrics.frontend.defines import *

# These are special "variables" that we need to skip over when iterating over real variables. 
# They are usually flags or parameters for the entire collection.
# Make sure no actual variables have these names, but that shouldn't be a problem.
collection_special_vars = ['desc', 'preamble', 'regions', 'seasons', 'package', 'options', 'combined', 'imagesonly', 'tables', 'mixed_plots', 'parallel']

### Collection 1
diags_collection['1'] = {}
diags_collection['1']['desc'] = 'Line plots of annual trends in energy balance, soil water/ice and temperature, runoff, snow water/ice, photosynthesis'
diags_collection['1']['package'] = 'LMWG'
diags_collection['1']['options'] = {'logo':'no'}
diags_collection['1']['seasons'] = ['ANN']
diags_collection['1']['PFT_FIRE_CLOSS'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['LITHR'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['QSOIL'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['WA'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['RETRANSN_TO_NPOOL'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['ACTUAL_IMMOB'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['WT'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['POTENTIAL_IMMOB'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['RR'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['CANOPY_EVAPORATION'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['CWDC_LOSS'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SMINN_TO_NPOOL'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SOIL3N'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['LITTERC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SOIL3C'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['GR'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['RETRANSN'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['AGNPP'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['GPP'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['FIRE_PROB'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['RSSUN'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['ANN_FAREA_BURNED'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SOIL4N'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SOIL4C'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['NPP'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['TLAI'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['LAISHA'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['HR'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['TOTVEGC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['TSA'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['NDEP_TO_SMINN'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['QCHARGE'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SOMHR'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['ZWT'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['RSSHA'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['LIVECROOTC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SOILC_HR'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['COL_NTRUNC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['QVEGT'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['CPOOL'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['PFT_CTRUNC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['FPI'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SOILLIQ'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SOILC_LOSS'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['XSMRPOOL'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['LEAFC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SOILICE'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['COL_FIRE_NLOSS'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['ER'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['QDRAI'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['WOODC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['FCOV'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['TSAI'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['ESAI'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['FIRESEASONL'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['MR'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SNOWICE'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['PSNSHADE_TO_CPOOL'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['CWDC_HR'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['NEE'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['FROOTC_LOSS'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['NEP'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['TOTLITC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SMINN_LEACHED'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['BGNPP'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['PFT_FIRE_NLOSS'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['LEAFC_ALLOC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['TOTRUNOFF'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['CO2_PPMV'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['BTRAN'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['DEADCROOTC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SNOWLIQ'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['CWDC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['TOTCOLC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SR'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SUPPLEMENT_TO_SMINN'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['PREC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['LIVESTEMC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['COL_FIRE_CLOSS'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['QOVER'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['MEAN_FIRE_PROB'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SOILPSI'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['LEAFC_LOSS'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['NET_NMIN'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SMINN'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['FROOTC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['WOODC_LOSS'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['ELAI'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['TOTSOILLIQ'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['DEADSTEMC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['SOILC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['NDEPLOY'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['TOTSOMC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['FROOTC_ALLOC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['WOODC_ALLOC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['TOTECOSYSC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['TOTSOILICE'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['QRGWL'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['GROSS_NMIN'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['QINFL'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['TOTECOSYSN'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['PFT_NTRUNC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['FPSN'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['FPG'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['TSOI'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['QINTR'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['LITTERC_HR'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['AR'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['LITTERC_LOSS'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['LAISUN'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['COL_CTRUNC'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['DENIT'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['NFIX_TO_SMINN'] = {'plottype':'1', 'obs':['NA']}
diags_collection['1']['PSNSUN_TO_CPOOL'] = {'plottype':'1', 'obs':['NA']}

### Collection 2
diags_collection['2'] = {}
diags_collection['2']['desc'] = 'Horizontal contour plots of DJF, MAM, JJA, SON, and ANN means'
diags_collection['2']['seasons'] = ['DJF', 'MAM', 'JJA', 'SON','ANN']
diags_collection['2']['package'] = 'LMWG'
diags_collection['2']['options'] = {'logo':'no'}
diags_collection['2']['PFT_FIRE_CLOSS'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['LITHR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['QSOIL'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['WA'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['RETRANSN_TO_NPOOL'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['RNET'] = {'plottype':'2', 'obs':['NA'], 'options':{'requiresraw':True}}
diags_collection['2']['ACTUAL_IMMOB'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['ZBOT'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['WT'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['LHEAT'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['NBSA'] = {'plottype':'2', 'obs':['MODIS_1']}
diags_collection['2']['POTENTIAL_IMMOB'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['RR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSNO'] = {'plottype':'2', 'obs':['NOAA_1']}
diags_collection['2']['FGR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['CWDC_LOSS'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SMINN_TO_NPOOL'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SOIL3N'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['LITTERC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SOIL3C'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSDSVDLN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['QBOT'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['GR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['RETRANSN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['XIM'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TBOT'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['AGNPP'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['GPP'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TAUX'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FIRE_PROB'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TAUY'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['RSSUN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['ANN_FAREA_BURNED'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SOIL4N'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSDSNDLN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SOIL4C'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['NPP'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TLAI'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSDS'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSDSVI'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['LAISHA'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['HR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TOTVEGC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['Q2M'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSDSVD'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TSA'] = {'plottype':'2', 'obs':['WILLMOTT_1']}
diags_collection['2']['QDRIP'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['NDEP_TO_SMINN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['QCHARGE'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SOMHR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['H2OCAN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['ZWT'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['RSSHA'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['LIVECROOTC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SOILC_HR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SNOWDP'] = {'plottype':'2', 'obs':['FOSTERDAVY_1', 'CMC_SNOW_1']}
diags_collection['2']['SABV'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSRNDLN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['ERRSEB'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['QVEGT'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSRNI'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['ERRH2O'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SABG'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['CPOOL'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TREFMXAV'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['EVAPFRAC'] = {'plottype':'2', 'obs':['NA'], 'options':{'requiresraw':True}}
diags_collection['2']['FPI'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SOILLIQ'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SOILC_LOSS'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['XSMRPOOL'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['LEAFC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SOILICE'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['COL_FIRE_NLOSS'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['ER'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['QDRAI'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['WOODC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FCOV'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TSAI'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSRVDLN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['ESAI'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FIRESEASONL'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['MR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSH_G'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SNOWICE'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['WIND'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['PSNSHADE_TO_CPOOL'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSA'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['QVEGE'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['VWSA'] = {'plottype':'2', 'obs':['MODIS_1'], 'options':{'requiresraw':True}}
diags_collection['2']['FSH'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['CWDC_HR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['NEE'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FROOTC_LOSS'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FGNET'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['NEP'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TOTLITC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SMINN_LEACHED'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TREFMNAV'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TLAKE'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['BGNPP'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['ASA'] = {'plottype':'2', 'obs':['MODIS_1'], 'options':{'requiresraw':True}}
diags_collection['2']['PFT_FIRE_NLOSS'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSRND'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['LEAFC_ALLOC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TOTRUNOFF'] = {'plottype':'2', 'obs':['GRDC_1']}
diags_collection['2']['BTRAN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['DEADCROOTC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SNOWLIQ'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSRVI'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSDSND'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FLDS'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSDSNI'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['CWDC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FCTR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TOTCOLC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['P-E'] = {'plottype':'2', 'obs':['NA'], 'options':{'requiresraw':True}}
diags_collection['2']['SR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SUPPLEMENT_TO_SMINN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['PREC'] = {'plottype':'2', 'obs':['WILLMOTT_1']}
diags_collection['2']['LIVESTEMC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FCEV'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TG'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSH_V'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['COL_FIRE_CLOSS'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FGEV'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['QOVER'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['QMELT'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['MEAN_FIRE_PROB'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['LEAFC_LOSS'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['NET_NMIN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SMINN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FROOTC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['WOODC_LOSS'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['ELAI'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['DEADSTEMC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SOILC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['H2OSOI'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['NDEPLOY'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TV'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TOTSOMC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FROOTC_ALLOC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['WOODC_ALLOC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TOTECOSYSC'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['QRGWL'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SNOWAGE'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['GROSS_NMIN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['QINFL'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['VBSA'] = {'plottype':'2', 'obs':['MODIS_1'], 'options':{'requiresraw':True}}
diags_collection['2']['FPSN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TSNOW'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSRVD'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FPG'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['TSOI'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FIRE'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['QINTR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FIRA'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['RAIN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['LITTERC_HR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['AR'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['ERRSOL'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['ERRSOI'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['LITTERC_LOSS'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['H2OSNO'] = {'plottype':'2', 'obs':['CMC_SWE_1']}
diags_collection['2']['LAISUN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['SNOW'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['THBOT'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['DENIT'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['FSM'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['NWSA'] = {'plottype':'2', 'obs':['MODIS_1'], 'options':{'requiresraw':True}}
diags_collection['2']['NFIX_TO_SMINN'] = {'plottype':'2', 'obs':['NA']}
diags_collection['2']['PSNSUN_TO_CPOOL'] = {'plottype':'2', 'obs':['NA']}

### Collection 3
diags_collection['3'] = {}
diags_collection['3']['desc'] = 'Line plots of monthly climatology: regional air temperature, precipitation, runoff, snow depth, radiative fluxes, and turbulent fluxes'
diags_collection['3']['seasons'] = ['ANN']
diags_collection['3']['package'] = 'LMWG'
diags_collection['3']['options'] = {'logo':'no'}
diags_collection['3']['Radiative_Fluxes'] = {'plottype':'3', 'obs':['NA'], 'options':{'requiresraw':True}} #RNET, ASA, Albedos require raw data
diags_collection['3']['Carbon_Nitrogen_Fluxes'] = {'plottype':'3', 'obs':['NA']}
diags_collection['3']['Snow_vs_Obs'] = {'plottype':'3', 'obs':['CMC_SNOW_1', 'USAF_1'], 'options':{'twoobs':'yes'}}
diags_collection['3']['Turbulent_Fluxes'] = {'plottype':'3', 'obs':['NA']}
diags_collection['3']['Albedo_vs_Obs'] = {'plottype':'3', 'obs':['MODIS_1'], 'options':{'requiresraw':True}}
diags_collection['3']['Fire_Fluxes'] = {'plottype':'3', 'obs':['NA']}
diags_collection['3']['Total_Precip'] = {'plottype':'3', 'obs':['CMC_SNOW_1', 'WILLMOTT_1'], 'options':{'twoobs':'yes'}}
diags_collection['3']['Hydrology'] = {'plottype':'3', 'obs':['NA']}
diags_collection['3']['Energy_Moisture_Control_of_Evap'] = {'plottype':'3', 'obs':['NA'], 'options':{'requiresraw':True}} #EVAPFRAC

### Collection 5
### Underlying code checks for difference vs default validity (looks for num_models == 2 before caring about varopts)
diags_collection['5'] = {}
diags_collection['5']['desc'] = 'Tables of annual means'
diags_collection['5']['seasons'] = ['ANN']
diags_collection['5']['package'] = 'LMWG'
# This one defaults to all regions. It ignores passed in --regions options.
diags_collection['5']['Regional_Hydrologic_Cycle'] = {'plottype':'5', 'obs':['NA'], 'varopts':['difference', 'default']}
diags_collection['5']['Global_Biogeophysics'] = {'plottype':'5', 'obs':['NA'], 'options':{'requiresraw':True}, 'varopts':['difference', 'default']}
diags_collection['5']['Global_Carbon_Nitrogen'] = {'plottype':'5', 'obs':['NA'], 'varopts':['difference', 'default']}
diags_collection['5']['tables'] = True

### Collection 6
diags_collection['6'] = {}
diags_collection['6']['desc'] = 'Line plots of annual trends in regional soil water/ice and temperature, runoff, snow water/ice, photosynthesis'
diags_collection['6']['seasons'] = ['ANN']
diags_collection['6']['package'] = 'LMWG'
diags_collection['6']['options'] = {'logo':'no'}
# Technically only soil_temp, radiative_fluxes, and hydrology ACTUALLY require raw, but we need some sort of
# annual average climatology file to generate the others. Setting to RAW for now.
diags_collection['6']['Soil_Temp'] = {'plottype':'6', 'obs':['NA'], 'options':{'requiresraw':True}}
diags_collection['6']['Radiative_Fluxes'] = {'plottype':'6', 'obs':['NA'], 'options':{'requiresraw':True}}
diags_collection['6']['Carbon_Nitrogen_Fluxes'] = {'plottype':'6', 'obs':['NA'], 'options':{'requiresraw':True}}
diags_collection['6']['TotalSoilIce_TotalSoilH2O'] = {'plottype':'6', 'obs':['NA'], 'options':{'requiresraw':True}}
diags_collection['6']['SoilLiq_Water'] = {'plottype':'6', 'obs':['NA'], 'options':{'requiresraw':True}}
diags_collection['6']['TotalSnowH2O_TotalSnowIce'] = {'plottype':'6', 'obs':['NA'], 'options':{'requiresraw':True}}
diags_collection['6']['Turbulent_Fluxes'] = {'plottype':'6', 'obs':['NA'], 'options':{'requiresraw':True}}
diags_collection['6']['SoilIce'] = {'plottype':'6', 'obs':['NA'], 'options':{'requiresraw':True}}
diags_collection['6']['Fire_Fluxes'] = {'plottype':'6', 'obs':['NA'], 'options':{'requiresraw':True}}
diags_collection['6']['Total_Precip'] = {'plottype':'6', 'obs':['NA'], 'options':{'requiresraw':True}}
diags_collection['6']['Hydrology'] = {'plottype':'6', 'obs':['NA'], 'options':{'requiresraw':True}}

### Collection 7
diags_collection['7T'] = {}
diags_collection['7T']['desc'] = 'Line plots, tables, and maps of RTM river flow and discharge to oceans'
diags_collection['7T']['RTM_Tables'] = {'plottype':'7', 'obs':['NA']}
diags_collection['7T']['tables'] = True
diags_collection['7'] = {}
diags_collection['7']['desc'] = 'Line plots, tables, and maps of RTM river flow and discharge to oceans'
diags_collection['7']['Scatter_plots'] = {'plottype':'7', 'obs':['NA']}

### Collection 9
diags_collection['9'] = {}
diags_collection['9']['desc'] = '(Requires 2 datasets) Contour plots and statistics for precipitation and temperature. Statistics include DJF, JJA, and ANN biases, and RMSE, correlation and standard deviation of the annual cycle relative to observations'
diags_collection['9']['seasons'] = ['DJF', 'MAM', 'JJA', 'SON', 'ANN']
diags_collection['9']['package'] = 'LMWG'
diags_collection['9']['options'] = {'logo':'no'}
diags_collection['9']['options'] = {'requirestwosets':'yes'}
diags_collection['9']['RMSE'] = {'plottype':'9', 'obs':['MODIS_1'], 'varopts':['TSA', 'PREC', 'ASA'], 'seasons':['NA']}
diags_collection['9']['Seasonal_Bias'] = {'plottype':'9', 'obs':['MODIS_1'], 'varopts':['TSA', 'PREC', 'ASA']}
diags_collection['9']['Correlation'] = {'plottype':'9', 'obs':['MODIS_1'], 'varopts':['TSA', 'PREC', 'ASA'], 'seasons':['NA']}
diags_collection['9']['Standard_Deviation'] = {'plottype':'9', 'obs':['MODIS_1'], 'varopts':['TSA', 'PREC', 'ASA'], 'seasons':['NA']}
diags_collection['9']['Tables'] = {'plottype':'9', 'obs':['NA']}

# *** Variables List ***
# Right now this is just used for creating descriptive names on web pages. It could have more useful info about the
# variable. It could also go away if data was more CF compliant and we could just extract this info from datasets
diags_varlist['TREFHT'] = {'desc': '2-meter temperature (land) (Northern)'}
diags_varlist['FSNTOAC'] = {'desc': 'TOA clearsky new SW flux'}
diags_varlist['CLDHGH'] = {'desc': 'High cloud amount (IR clouds) (Northern)'}
diags_varlist['TTRP'] = {'desc': 'Tropopause temperature'}
diags_varlist['Z3'] = {'desc': 'Geopotential height (Northern)'}
diags_varlist['FSNS'] = {'desc': 'Surf Net SW flux'}
diags_varlist['CLDLOW'] = {'desc': 'Low cloud amount (IR clouds) (Northern)'}
diags_varlist['TS'] = {'desc': 'Surface temperature (Northern)'}
diags_varlist['TCLDAREA'] = {'desc': 'Total cloud area (Day)'}
diags_varlist['T'] = {'desc': 'Temperature'}
diags_varlist['PRECT'] = {'desc': 'Precipitation rate (Northern)'}
diags_varlist['PS'] = {'desc': 'Surface pressure (Northern)'}
diags_varlist['PREH2O'] = {'desc': 'Total precipitable water'}
diags_varlist['CLDMED'] = {'desc': 'Mid cloud amount (IR clouds)'}
diags_varlist['FSDS'] = {'desc': 'Surf SW downwelling flux'}
diags_varlist['FSNTOA'] = {'desc': 'TOA new SW flux'}
diags_varlist['CLDLOW'] = {'desc': 'Low cloud amount (IR clouds)'}
diags_varlist['FLDSC'] = {'desc': 'Clearsky Surf LW downwelling flux (Northern)'}
diags_varlist['FSNTOA'] = {'desc': 'TOA net SW flux (Northern)'}
diags_varlist['CLDMED_VISIR'] = {'desc': 'Mid cloud amount (VIS/IR/NIR) clouds) (Northern)'}
diags_varlist['MEANTAU'] = {'desc': 'Mean cloud optical thickness (Day)'}
diags_varlist['SWCF'] = {'desc': 'TOA shortwave cloud forcing'}
diags_varlist['ALBEDO'] = {'desc': 'TOA Albedo'}
diags_varlist['MEANTTOP'] = {'desc': 'Mean cloud top temperature (Day)'}
diags_varlist['FLDS'] = {'desc': 'Surf LW downwelling flux (Northern)'}
diags_varlist['FSNSC'] = {'desc': 'Clearsky Surf Net SW flux (Northern)'}
diags_varlist['RESTOA'] = {'desc': 'TOA residual energy flux'}
diags_varlist['SHFLX'] = {'desc': 'Surface sensible heat flux (Northern)'}
diags_varlist['SHFLX'] = {'desc': 'Surface sensible heat flux'}
diags_varlist['FLNSC'] = {'desc': 'Clearsky Surf Net LW Flux'}
diags_varlist['ALBEDOC'] = {'desc': 'TOA clearsky albedo (Northern)'}
diags_varlist['ALBEDOC'] = {'desc': 'TOA clearsky albedo'}
diags_varlist['RELHUM'] = {'desc': 'Relative humidity'}
diags_varlist['EP'] = {'desc': 'Evaporation - precipitation'}
diags_varlist['QFLX'] = {'desc': 'Surface water flux'}
diags_varlist['PSL'] = {'desc': 'Sea-level pressure'}
diags_varlist['CLDTOT_VISIR'] = {'desc': 'Total cloud amount (VIS/IR/NIR) clouds) (Northern)'}
diags_varlist['SST'] = {'desc': 'Sea surface temperature'}
diags_varlist['FLNS'] = {'desc': 'Surf Net LW flux'}
diags_varlist['ICEFRAC'] = {'desc': 'Sea-ice area (Northern)'}
diags_varlist['CLDLOW_VISIR'] = {'desc': 'Low cloud amount (VIS/IR/NIR clouds)'}
diags_varlist['PRECT'] = {'desc': 'Precipitation rate'}
diags_varlist['PRECT_LAND'] = {'desc': 'Precipitation rate (land)'}
diags_varlist['PRECIP'] = {'desc': 'Cumulative precipitation (land)'}
diags_varlist['TMQ'] = {'desc': 'Precipitable Water'}
diags_varlist['LWCF'] = {'desc': 'TOA longwave cloud forcing'}
diags_varlist['FLDS'] = {'desc': 'Surf LW downwelling flux'}
diags_varlist['SWCFSRF'] = {'desc': 'Surf SW Cloud Forcing'}
diags_varlist['OMEGA'] = {'desc': 'Pressure vertical velocity'}
diags_varlist['FLUT'] = {'desc': 'TOA upward LW flux'}
diags_varlist['FLUT'] = {'desc': 'TOA upward LW flux (Northern)'}
diags_varlist['TREFHT'] = {'desc': '2-meter air temperature (land)'}
diags_varlist['CLDLOW_VISIR'] = {'desc': 'Low cloud amount (VIS/IR/NIR) clouds) (Northern)'}
diags_varlist['Atmospheric_Heat'] = {'desc': 'Atmospheric Heat', 'filekey':'ATM_HEAT'}
diags_varlist['FSDSC'] = {'desc': 'Clearsky Surf SW downwelling flux'}
diags_varlist['QFLX'] = {'desc': 'Surface water flux (Northern)'}
diags_varlist['CLDHGH_VISIR'] = {'desc': 'High cloud amount (VIS/IR/NIR clouds)'}
diags_varlist['SURF_STRESS'] = {'desc': 'Surface wind stress (ocean)'}
diags_varlist['STRESS'] = {'desc': 'Surface wind stress (ocean)'}
diags_varlist['FLDSC'] = {'desc': 'Clearsky Surf LW downwelling flux'}
diags_varlist['CLDHGH'] = {'desc': 'High cloud amount (IR clouds)'}
diags_varlist['FSNS'] = {'desc': 'Surf Net SW flux (Northern)'}
diags_varlist['FLUTC'] = {'desc': 'TOA clearsky upward LW flux'}
diags_varlist['Ocean_Freshwater'] = {'desc': 'Ocean Freshwater', 'filekey':'OCN_FRESH'}
diags_varlist['CLDTOT'] = {'desc': 'Total cloud amount (IR clouds) (Northern)'}
diags_varlist['MSE'] = {'desc': 'Moist Static Energy'}
diags_varlist['SHUM'] = {'desc': 'Specific humidity'}
diags_varlist['FLNS'] = {'desc': 'Surf Net LW flux (Northern)'}
diags_varlist['FSDSC'] = {'desc': 'Clearsky Surf SW downwelling flux (Northern)'}
diags_varlist['ALBEDO'] = {'desc': 'TOA albedo (Northern)'}
diags_varlist['TS'] = {'desc': 'Surface temperature'}
diags_varlist['TGCLDLWP'] = {'desc': 'Cloud liquid water'}
diags_varlist['CLOUD'] = {'desc': 'Cloud Fraction'}
diags_varlist['CLDTOT_VISIR'] = {'desc': 'Total cloud amount (VIS/IR/NIR clouds)'}
diags_varlist['LHFLX'] = {'desc': 'Surface latent heat flux'}
diags_varlist['FLUTC'] = {'desc': 'TOA clearsky upward LW flux (Northern)'}
diags_varlist['CLDTOT'] = {'desc': 'Mid cloud amount (IR clouds)'}
diags_varlist['CLDMED'] = {'desc': 'Mid cloud amount (IR clouds) (Northern)'}
diags_varlist['Q'] = {'desc': 'Specific Humidity'}
diags_varlist['H'] = {'desc': 'Moist Static Energy'}
diags_varlist['FSDS'] = {'desc': 'Surf SW downwelling flux (Northern)'}
diags_varlist['U'] = {'desc': 'Zonal Wind'}
diags_varlist['Ocean_Heat'] = {'desc': 'Ocean Heat', 'filekey':'OCN_HEAT'}
diags_varlist['Surface_Heat'] = {'desc': 'Surface Heat', 'filekey':'SRF_HEAT'}
diags_varlist['LWCFSRF'] = {'desc': 'Surf LW Cloud Forcing'}
diags_varlist['SWCF_LWCF'] = {'desc': 'SW/LW Cloud Forcing'}
diags_varlist['FSNSC'] = {'desc': 'Clearsky Surf Net SW Flux'}
diags_varlist['SURF_WIND'] = {'desc': 'Near surface wind (Northern)'}
diags_varlist['CLDMED_VISIR'] = {'desc': 'Mid cloud amount (VIS/IR/NIR clouds)'}
diags_varlist['MEANPTOP'] = {'desc': 'Mean cloud top pressure (Day)'}
diags_varlist['CLDHGH_VISIR'] = {'desc': 'High cloud amount (VIS/IR/NIR) clouds) (Northern)'}
diags_varlist['FLNSC'] = {'desc': 'Clearsky Surf Net LW flux (Northern)'}
diags_varlist['PSL'] = {'desc': 'Sea-level pressure (Northern)'}
diags_varlist['AODVIS'] = {'desc': 'Aerosol optical depth'}
diags_varlist['FSNTOAC'] = {'desc': 'TOA clearsky net SW flux (Northern)'}


print 'ToDO: Clarify when to use CMC_SNOW and CMC_SME'
diags_obslist['CMC_SNOW_1'] = {'filekey':'CMC_SNOWD', 'desc':'CMC Snow Depth'}
diags_obslist['CMC_SWE_1'] = {'filekey':'CMC_SWE', 'desc':'CMC Snow/Water Equivalent Depth'}
diags_obslist['FOSTERDAVY_1'] = {'filekey':'FOSTERDAVY', 'desc':'Foster-Davy'}
diags_obslist['NOAA_1'] = {'filekey':'NOAA', 'desc':'NOAA'}
diags_obslist['GRDC_1'] = {'filekey':'GRDC', 'desc':'GRDC'}
diags_obslist['USAF_1'] = {'filekey':'USAF', 'desc':'USAF'}

diags_obslist['HADISST_PD_1'] = {'filekey': 'HADISST_PD', 'desc': 'HadISST/OI.v2 (Present Day) 1999-2008'}
diags_obslist['WARREN_1'] = {'filekey': 'WARREN', 'desc': 'Warren Cloud Surface OBS'}
diags_obslist['LEGATES_1'] = {'filekey': 'LEGATES', 'desc': 'Legates and Willmott 1920-80'}
diags_obslist['SGP_1'] = {'filekey': 'SGP', 'desc': 'Southern Great Plains (SGP)'}
diags_obslist['ERA40_1'] = {'filekey': 'ERA40', 'desc': 'ERA40 Reanalysis 1980-2001'}
diags_obslist['ERS_1'] = {'filekey': 'ERS', 'desc': 'ERS Scatterometer 1992-2000'}
diags_obslist['CLOUDSAT_1'] = {'filekey': 'CLOUDSAT', 'desc': 'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008'}
diags_obslist['WHOI_1'] = {'filekey': 'WHOI', 'desc': 'Woods Hole OAFLUX 1958-2006'}
diags_obslist['NCEP_1'] = {'filekey': 'NCEP', 'desc': 'NCEP Reanalysis 1979-98'}
diags_obslist['AOD_550_1'] = {'filekey': 'sat', 'desc': 'AOD Data'}
diags_obslist['NSA_1'] = {'filekey': 'NSA', 'desc': 'North Slope of Alaska (NSA)'}
diags_obslist['JRA25_1'] = {'filekey': 'JRA25', 'desc': 'JRA25 Reanalysis 1979-04'}
diags_obslist['TWP2_1'] = {'filekey': 'TWP2', 'desc': 'Tropical Western Pacific--Region 2 (TWP2)'}
diags_obslist['ERBE_1'] = {'filekey': 'ERBE', 'desc': 'ERBE Feb1985-Apr1989'}
diags_obslist['CERES_1'] = {'filekey': 'CERES', 'desc': 'CERES 2000-2003'}
diags_obslist['WILLMOTT_1'] = {'filekey': 'WILLMOTT', 'desc': 'Willmott and Matsuura 1950-99'}
diags_obslist['PRECL_1'] = {'filekey': 'PRECL', 'desc': 'PREC/L (CMAP) 1948-2001'}
diags_obslist['TWP3_1'] = {'filekey': 'TWP3', 'desc': 'Tropical Western Pacific--Region 3 (TWP3)'}
diags_obslist['TWP1_1'] = {'filekey': 'TWP1', 'desc': 'Tropical Western Pacific--Region 1 (TWP1)'}
diags_obslist['GPCP_1'] = {'filekey': 'GPCP', 'desc': 'GPCP 1979-2003'}
diags_obslist['CERES2_1'] = {'filekey': 'CERES2', 'desc': 'CERES2 March 2000-October 2005'}
diags_obslist['CRU_1'] = {'filekey': 'CRU', 'desc': 'IPCC/CRU Climatology 1961-90'}
diags_obslist['ERAI_1'] = {'filekey': 'ERAI', 'desc': 'ERA Interim Reanalysis'}
diags_obslist['HADISST_PI_1'] = {'filekey': 'HADISST_PI', 'desc': 'HadISST/OI.v2 (Pre-Indust) 1870-1900'}
diags_obslist['TRMM_1'] = {'filekey': 'TRMM', 'desc': 'TRMM (3B43) 1998-Feb2004 - Tropics'}
diags_obslist['CERES-EBAF_1'] = {'filekey': 'CERES-EBAF', 'desc': 'CERES-EBAF'}
diags_obslist['AIRS_1'] = {'filekey': 'AIRS', 'desc': 'AIRS IR Sounder 2002-06'}
diags_obslist['NVAP_1'] = {'filekey': 'NVAP', 'desc': 'NVAP 1988-1999'}
diags_obslist['SHEBA_1'] = {'filekey': 'SHEBA', 'desc': 'Surface Heat Budget of the Arctic Ocean (SHEBA)'}
diags_obslist['LARYEA_1'] = {'filekey': 'LARYEA', 'desc': 'Large-Yeager 1984-2004'}
diags_obslist['NA_1'] = {'filekey': 'N/A', 'desc': 'NA'}
diags_obslist['MODIS_1'] = {'filekey': 'MODIS', 'desc': 'MODIS Mar2000-Aug2004'}
diags_obslist['ISCCP_1'] = {'filekey': 'ISCCP', 'desc': 'ISCCP D1 Daytime Jul1983-Sep2001'}
diags_obslist['HADISST_1'] = {'filekey': 'HADISST', 'desc': 'HadISST/OI.v2 (Climatology) 1982-2001'}
diags_obslist['XA_1'] = {'filekey': 'XA', 'desc': 'CMAP (Xie-Arkin) 1979-98'}
diags_obslist['SSMI_1'] = {'filekey': 'SSMI', 'desc': 'SSM/I (Wentz) 1987-2000'}
diags_obslist['ECMWF_1'] = {'filekey': 'ECMWF', 'desc': 'ECMWF Reanalysis 1979-93'}
diags_obslist['RAOBS_1'] = {'filekey': 'RAOBS', 'desc':'raobs station data'}

