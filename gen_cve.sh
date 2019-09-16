#!/bin/sh

versions=('2.6.0' '3.4.0' '3.10.0' '4.1.0' '4.19.0')
outputdir=/home1/Project/Linux_kernel_bugs/zxh/output

for version in ${versions[@]};do
    ## 生成cveID列表
    docker run -it --privileged -v /home1/Project/Linux_kernel_bugs/zxh/:/Linux_kernel_bugs -w /Linux_kernel_bugs  python:3.7 python cve.py ${version} 
    ## 去重。eg: 4.1 和 4.1.0相同
    sort -n ./output.csv | uniq > ./tmpppp
    sort -n ./tmpppp | uniq > ./output.csv
    rm ./tmpppp

    ## 获取函数及函数所在的文件路径
    bash apply.sh ${outputdir}/${version}
    sort -n ${outputdir}/${version} | uniq > ${outputdir}/kernel_${version}
    rm ${outputdir}/${version}
done
