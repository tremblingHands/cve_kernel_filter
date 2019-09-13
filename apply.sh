#!/bin/bash

filename=/home1/Project/Linux_kernel_bugs/zxh/output.csv
datadir=/home1/Project/Linux_kernel_bugs/zxh/emulation_data
outputfile=/home1/Project/Linux_kernel_bugs/zxh/result.csv

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

        echo -n "$line," >> $outputfile
        path=""
        grep -r -P '@@|\+\+\+ b'  $dir  | grep -P ' @@ [a-zA-Z0-9\*\s_]+\([a-zA-Z0-9\*\s_,]+\)|\+\+\+ [\S]+' -o |  awk '{gsub(/^\s@@\s/, "");print}' | while read str
        do
            if [[ "$str" =~ ^\+\+\+.* ]]; then            
                path=`echo $str | awk '{gsub(/^\+\+\+ b\//, "");print}'`
                #echo "path = $path"
            else
                if [[ "$path" =~ ^drivers\/ ]]; then
                    continue
                fi
                echo -n "$path," >> $outputfile
                echo -n "$str," >> $outputfile
            fi
        done
        echo "" >> $outputfile
    fi
done





