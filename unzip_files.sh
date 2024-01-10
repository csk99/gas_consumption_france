# $1 is the first argument which should be the data where gzip are located
#change it in accordance with the yaml configuration file
for file in $1/*.gz ; do gunzip -c "$file" > "${file%.*}" ; done
