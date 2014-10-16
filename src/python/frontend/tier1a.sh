# Sample runs of the Tier 1a atmosphere diagnostics.

# 1. Sea Level Pressure, PSL
diags --packages AMWG --outputdir ~/tmp/diagout/1 --path ~/metrics_data/cam35_data --path2 ~/metrics_data/obs_data_5.6 --filter2 "f_startswith('ERAI')" --seasons ANN --sets 5 --vars PSL
# 2. SW Cloud Forcing, SWCF
diags --packages AMWG --outputdir ~/tmp/diagout/2 --path ~/metrics_data/cam35_data --path2 ~/metrics_data/obs_data_5.6 --filter2 "f_startswith('CERES-EBAF')" --seasons ANN --sets 5 --vars SWCF
# 3. LW Cloud Forcing, LWCF
diags --packages AMWG --outputdir ~/tmp/diagout/3 --path ~/metrics_data/cam35_data --path2 ~/metrics_data/obs_data_5.6 --filter2 "f_startswith('CERES-EBAF')" --seasons ANN --sets 5 --vars LWCF
# 4 Global Precipitation, PRECT
diags --packages AMWG --outputdir ~/tmp/diagout/4 --path ~/metrics_data/cam35_data --path2 ~/metrics_data/obs_data_5.6 --filter2 "f_startswith('GPCP')" --seasons ANN --sets 5 --vars PRECT
# 5 Land 2-m temperature, TREFHT
diags --packages AMWG --outputdir ~/tmp/diagout/5 --path ~/metrics_data/cam35_data --path2 ~/metrics_data/obs_data_5.6 --filter2 "f_startswith('WILLMOTT')" --seasons ANN --sets 5 --vars TREFHT
# 6 Oceanic Surface Wind Stress, STRESS
diags --packages AMWG --outputdir ~/tmp/diagout/6 --path ~/metrics_data/cam35_data/ --path2 ~/metrics_data/obs_data_5.6 --filter2 "f_startswith('ERS')" --set 6 --var STRESS --seasons ANN
# 7. 300 mb Zonal Wind, U
diags --packages AMWG --outputdir ~/tmp/diagout/7 --path ~/metrics_data/cam35_data --path2 ~/metrics_data/obs_data_5.6 --filter2 "f_startswith('ERAI')" --seasons ANN --sets 5 --vars U --varopts 300
# 8. Zonal Mean Relative Humidity, RELHUM
diags --packages AMWG --outputdir ~/tmp/diagout/8 --path ~/metrics_data/cam35_data --path2 ~/metrics_data/obs_data_5.6 --filter2 "f_startswith('ERAI')" --seasons ANN --sets 4 --vars RELHUM
# 9. Zonal Mean Temperature, T
diags --packages AMWG --outputdir ~/tmp/diagout/9 --path ~/metrics_data/cam35_data --path2 ~/metrics_data/obs_data_5.6 --filter2 "f_startswith('ERAI')" --seasons ANN --sets 4 --vars T
# 10. Aerosol Optical Depth, AODVIS
diags --packages AMWG --outputdir ~/tmp/diagout/10 --path ~/metrics_data/acme_data --path2 ~/metrics_data/acme_obs --filter2 "f_startswith('sat')" --seasons ANN --sets 5 --vars AODVIS

# Scalars are in the "plot set 1" table:
diags --packages AMWG --outputdir ~/tmp/diagout --path ~/metrics_data/cam_output --path2 ~/metrics_data/obs_data_5.6 --seasons ANN --sets 1
