#!/bin/bash

#Set these
data_dir="/Users/rrniii/Desktop/Chapel_Allerton_ERA5/Raw"
cat_files_dir="/Users/rrniii/Desktop/Chapel_Allerton_ERA5/Cat"
out_dir="/Users/rrniii/Desktop/Chapel_Allerton_ERA5/Rec_dim"
file_type="Chapel_Allerton"
code_dir='/Users/rrniii/Google_Drive/code/PycharmProjects/ERA_Data/'
#start of program
#assumes nco is install correctly

cd $data_dir

#for d in */ ; do
#d='Ayr'
#$code_dir/cat_biodar_era5_dostuff.sh $d $out_dir $cat_files_dir $file_type $data_dir
#done

$code_dir/cat_chapel_allerton_era5_dostuff.sh $data_dir $out_dir $cat_files_dir $file_type $data_dir