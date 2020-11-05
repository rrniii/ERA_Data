#!/bin/bash

#Set these
data_dir="/Volumes/Neely/BioDAR/ERA5/Myrna_TrapLocations_0_25_Box/suction/surface"
cat_files_dir="/Volumes/Neely/BioDAR/ERA5/Myrna_TrapLocations_0_25_Box/cat_files/suction/surface"
out_dir="/Volumes/Neely/BioDAR/ERA5/Myrna_TrapLocations_0_25_Box/time_series_raw/suction/surface"
file_type="suction_surface"
code_dir='/Users/rrniii/Google_Drive/code/PycharmProjects/ERA_Data/'
#start of program
#assumes nco is install correctly

cd $data_dir

for d in */ ; do
$code_dir/cat_biodar_era5_dostuff.sh $d $out_dir $cat_files_dir $file_type $data_dir

done

#parallel $code_dir/cat_biodar_era5_dostuff.sh {} $out_dir $cat_files_dir $file_type $data_dir ::: */