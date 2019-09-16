#!/bin/bash

home=$(dirname $(readlink -f "$0"))

#filename=/home1/Project/Linux_kernel_bugs/zxh/output.csv
#datadir=/home1/Project/Linux_kernel_bugs/zxh/emulation_data
#outputfile=/home1/Project/Linux_kernel_bugs/zxh/result.csv
filename=$home/output.csv
datadir=$home/nvd_data/patch
outputfile=$home/result.csv

if [ $# == 1 ];then
    outputfile=$1
fi


cat $filename | while read line
do
    line=${line%?}
    dir="$datadir/$line"
    if [ -d "$dir" ]; then
        ## 输出函数名
        #res=`grep -r '@@' $dir | grep -P " [0-9a-zA-Z_\*]+[\s]?\(" -o | grep -P "[0-9a-zA-Z_\*]+" -o`
        ## 输出函数签名
        #res=`grep -r '@@' $dir  | grep -P ' @@ [a-zA-Z0-9\*\s_]+\([a-zA-Z0-9\*\s_,]+\)' -o | awk '{gsub(/^\s@@\s/, "");print}'`
        
        ## 输出文件路径以及函数签名
        #res=`grep -r -P '@@|\+\+\+ b'  $dir  | grep -P ' @@ [a-zA-Z0-9\*\s_]+\([a-zA-Z0-9\*\s_,]+\)|\+\+\+ [\S]+' -o |  awk '{gsub(/^\s@@\s/, "");print}'` 
        

        #for v in ${tmp};do
        #    echo $v
        #done
        #echo $res | while read v
        #do
        #    echo $v
        #    echo " "
        #done

        #echo -n "$line," >> $outputfile
        #grep -r -P '@@|\+\+\+ b'  $dir  | grep -P ' @@ [a-zA-Z0-9\*\s_]+\([a-zA-Z0-9\*\s_,]+\)|\+\+\+ [\S]+' -o |  awk '{gsub(/^\s@@\s/, "");print}' | while read str
        path=""
        grep -r -P '@@|\+\+\+ b'  $dir/*patch  | grep -P ' [0-9a-zA-Z_\*]+[\s]?\(|\+\+\+ [\S]+' -o | awk '{gsub(/^\s+\*|\($/, "");print}'  |while read str
        do
            if [[ "$str" =~ ^\+\+\+.* ]]; then            
                path=`echo $str | awk '{gsub(/^\+\+\+ b\//, "");print}'`
                #echo "path = $path"
            else
                if [[ "$path" =~ ^drivers\/ ]]; then
                    continue
                fi
        	echo -n "$line," >> $outputfile
                echo -n "$path," >> $outputfile
                echo -n "$str," >> $outputfile
		echo "" >> $outputfile
            fi
        done
        #echo "" >> $outputfile
    fi
done





