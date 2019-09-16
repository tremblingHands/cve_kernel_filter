#!/bin/sh

versions=('2.6.0' '3.4.0' '3.10.0' '4.1.0' '4.19.0')

for version in ${versions[@]};do
    docker run -it --privileged -v /home1/Project/Linux_kernel_bugs/zxh/:/Linux_kernel_bugs -w /Linux_kernel_bugs  python:3.7 python cve.py ${version} 
    sort -n ./output.csv | uniq > ./tmpppp
    sort -n ./tmpppp | uniq > ./output.csv
    rm ./tmpppp

    outputdir=/home1/Project/Linux_kernel_bugs/zxh/output
    bash apply.sh ${outputdir}/${version}
    sort -n ${outputdir}/${version} | uniq > ${outputdir}/kernel_${version}
    rm ${outputdir}/${version}
done
