#!/bin/sh

#Compute zz pers of all points from 0 to $2 included.

echo "Usage : launch_calc ifile odir start end"
echo "Example of usage : launch_calc cloud.xyz output/ 0 300"

for i in `seq $3 $4`
  do ./rips-zz -i $i $1 "$2/$i.pers"
done
