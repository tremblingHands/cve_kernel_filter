
bash gen_cve.sh

输出结果在 ./output 下

## gen_cve.sh

依据 versions 内的版本生成软件+版本对应的cveID并筛选出ID对应的函数及函数所在的文件

## cve.py

输出软件+版本对应的漏洞ID，其中
output.csv 为输出文件

## apply.sh

输出文件路径以及函数名，其中

filename ： 需要处理的漏洞ID

datadir ： patch 文件所在的目录

outputfile ： 输出的文件路径

