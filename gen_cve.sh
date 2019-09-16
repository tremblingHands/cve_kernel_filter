#!/bin/sh

docker run -it --privileged -v /home1/Project/Linux_kernel_bugs/zxh/:/Linux_kernel_bugs -w /Linux_kernel_bugs  python:3.7 python cve.py

sort -n ./output.csv | uniq > ./tmpppp
sort -n ./tmpppp | uniq > ./output.csv
rm ./tmpppp
