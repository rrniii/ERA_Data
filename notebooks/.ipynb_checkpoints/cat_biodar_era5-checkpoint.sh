#!/bin/bash

#Set these
data_dir="/Volumes/Neely/BioDAR/surface"
out_dir="/Volumes/Neely/BioDAR/surface/time_series_raw"
cat_files_dir="/Volumes/Neely/BioDAR/surface/cat_files"
file_type="surface"

#start of program
#assumes nco is install correctly

cd $data_dir

for d in */ ; do
    echo "$d"
    mkdir $out_dir/$(basename "$d")
    cd $d
    infiles=`ls *.nc`
    for file in ${infiles} ; do 
        ncks -O --mk_rec_dmn time ${file} /$out_dir/$(basename "$d")/${file}; 
    done
    
    cd $out_dir/$(basename "$d")
    file_count=`ls *.nc | wc -l`  # returns number of files
    other_filecount="$((${file_count}-1))"  # returns number of files minus 1 
    first_file=`ls *.nc | head -1`  #  grab the first file
    other_files=`ls *.nc | tail -${other_filecount}`  # add remaining files to list 
    cp ${first_file} $cat_files_dir/$(basename "$d")_ERA5_${file_type}_timeseries.nc   # create master copy to populate
    for file in ${other_files} ; do 
        echo ${file}
        ncrcat -O $cat_files_dir/$(basename "$d")_ERA5_${file_type}_timeseries.nc  ${file} $cat_files_dir/$(basename "$d")_ERA5_${file_type}_timeseries.nc; 
        done   # loop through and add files by time
    cd ..

done