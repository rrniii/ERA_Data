#!/bin/bash
d=$1
out_dir=$2
cat_files_dir=$3
file_type=$4
data_dir=$5

echo "$d"
mkdir $out_dir/$(basename "$d")
cd $data_dir/$d
echo "Made OutDir, In DataDir"
infiles=$(find . -type f -name "*.nc")
echo "Found all the Files"
for file in ${infiles} ; do 
    ncks -O --mk_rec_dmn time ${file} /$out_dir/$(basename "$d")/${file}; 
done
echo "Made all the recdims"
cd $out_dir/$(basename "$d")
file_count=`find -f *.nc | wc -l`  # returns number of files
other_filecount="$((${file_count}-1))"  # returns number of files minus 1 
first_file=`find -f *.nc | head -1`  #  grab the first file
other_files=`find -f *.nc | tail -${other_filecount}`  # add remaining files to list 
cp ${first_file} $cat_files_dir/$(basename "$d")_ERA5_${file_type}_timeseries.nc   # create master copy to populate
for file in ${other_files} ; do 
    echo ${file}
    ncrcat -O $cat_files_dir/$(basename "$d")_ERA5_${file_type}_timeseries.nc  ${file} $cat_files_dir/$(basename "$d")_ERA5_${file_type}_timeseries.nc; 
done   # loop through and add files by time
