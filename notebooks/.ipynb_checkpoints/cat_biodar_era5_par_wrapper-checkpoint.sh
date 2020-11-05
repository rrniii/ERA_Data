#!/bin/bash

#Set these
data_dir="/Volumes/Neely/BioDAR/surface"
out_dir="/Volumes/Neely/BioDAR/time_series_raw"
cat_files_dir="/Volumes/Neely/BioDAR/cat_files"
file_type="surface"
code_dir='/Users/rrniii/Google_Drive/code/PycharmProjects/ERA_Data/notebooks'
#start of program
#assumes nco is install correctly

cd $data_dir

parallel $code_dir/cat_biodar_era5_dostuff.sh {} $out_dir $cat_files_dir $file_type $data_dir ::: */