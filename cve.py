# -*- coding: utf-8 -*-
import json
import re
import csv

def filterDriver(description):
    m = re.findall(r'driver', description, re.IGNORECASE)
    if m:
        return True
    return False


def findFuncNames(description):
    functions = []
    patterns = [r'(?:The|the) ([A-Za-z0-9_]+) function[,\.\s]', r'([A-Za-z0-9_]+)\(\)', r'([A-Za-z0-9]+_[A-Za-z0-9_]+) in [A-Za-z0-9_/]+\.[cS]', r'(?:The|the) function ([A-Za-z0-9_]+)', r'(?:The|the) ([A-Za-z0-9_]+) and ([A-Za-z0-9_]+) functions', r'(?:The|the) \(1\) ([A-Za-z0-9_]+) and \(2\) ([A-Za-z0-9_]+) functions']
    for pattern in patterns:
        m = re.findall(pattern, description)
        if m:
            for name in m:
                if isinstance(name ,tuple):
                    for da in name:
                        functions.append(da)
                else:
                    functions.append(name)

    path = []
    m = re.findall(r' [A-Za-z0-9_/]+\.[cS][,\.\s]', description)
    if m:
        for name in m:
            path.append(name)        

    return " ".join(functions), " ".join(path)
    

def numMatch(str1, str2, op):
    if int(str1) < int(str2):
        if op == "<=" or op == "<":
            return True
        else:
            return False
    elif int(str1) > int(str2):
        if op == ">=" or op == ">":
            return True
        else:
            return False
    else:
        if op == "=" or op == "<=" or op == ">=":
            return True
        else:
            return False


debug = False
# debug = True

def versionIsMatch(target, relationship, version):
    targetTokens = re.split("\D+", target)
    versionTokens = re.split("\D+", version)

    # 发现 <= 之前都是 = 
    return targetTokens == versionTokens

    if debug:
        print(target)
        print(version)
        print(targetTokens)
        print(versionTokens)
        print(relationship)
    if version == "*" or version == "-":
        return False
    for i in range(len(versionTokens)):
        if i >= len(targetTokens):
            # target的version没了，而cve里的version还有
            return False
        if int(targetTokens[i]) == int(versionTokens[i]):
            continue
        else:
            return numMatch(targetTokens[i], versionTokens[i], relationship)
    # equal
    if relationship == "=" or relationship == "<=" or relationship == ">=":
        return True
    return False
    
    # versionMatch = re.findall(r"\D+", version)
    # targetMatch = re.findall(r"\D+", target)
    # print("----------")
    # print(target)
    # print(relationship)
    # print(version)
    # for i in range(len(versionMatch)):
    #     versionTokenBefore = version[:version.index(versionMatch[i])]
    #     targetTokenBefore = target[:target.index(targetMatch[i])]
    #     versionTokenAfter = version[version.index(versionMatch[i])+len(versionMatch[i]):]
    #     targetTokenAfter = target[target.index(targetMatch[i])+len(targetMatch[i]):]
    #     print("i: "+str(i))
    #     print(versionTokenBefore)
    #     print(targetTokenBefore)
    #     print(versionTokenAfter)
    #     print(targetTokenAfter)
    #     if int(targetTokenBefore[0]) == int(versionTokenBefore[0]):
    #         if i == len(versionMatch) - 1:
    #             print("****")
    #             return numMatch(targetTokenAfter, versionTokenAfter, relationship)
    #         else:
    #             version = version[version.index(versionMatch[i])+len(versionMatch[i]):]
    #             target = target[target.index(targetMatch[i])+len(targetMatch[i]):]
    #     else:
    #         return numMatch(targetTokenBefore[0], versionTokenBefore[0], relationship)

# version = "0.53b"
# relationship = "="
# target = "0.71"
# print(versionIsMatch(version, relationship, target))

targetSoftware = [
#    {
#        "name":"putty",
#        "version":"0.71",
#        "ever_found":"",
#        "count":0,
#    },{
#        "name":"ixgbe",
#        "version":"5.5.5",
#        "ever_found":"",
#        "count":0,
#    },{
#        "name":"libvirt",
#        "version":"5.4.0",
#        "ever_found":"",
#        "count":0,
#    },{
#        "name":"ixgbevf",
#        "version":"4.5.3",
#        "ever_found":"",
#        "count":0,
#    },{
#        "name":"ffmpeg",
#        "version":"4.1.3",
#        "ever_found":"",
#        "count":0,
#    },{
#        "name":"openssh",
#        "version":"8.0p1",
#        "ever_found":"",
#        "count":0,
#    },{
#        "name":"cygwin",
#        "version":"3.0.7",
#        "ever_found":"",
#        "count":0,
#    },{
#        "name":"xl2tpd",
#        "version":"1.3.4",
#        "ever_found":"",
#        "count":0,
#    },{
#        "name":"trusted_firmware-a",
#        "version":"2.1",
#        "ever_found":"",
#        "count":0,
#    },{
#        "name":"ziparchive",
#        "version":"2.2.2",
#        "ever_found":"",
#        "count":0,
#    },{
#        "name":"linux_kernel",
#        "version":"3.10",
#        "ever_found":"",
#        "count":0,
#    }
    {
        "name":"linux_kernel",
        "version":"2.6.0",
        "ever_found":"",
        "count":0,
    },
    {
        "name":"linux_kernel",
        "version":"3.4.0",
        "ever_found":"",
        "count":0,
    },
    {
        "name":"linux_kernel",
        "version":"3.10.0",
        "ever_found":"",
        "count":0,
    },
    {
        "name":"linux_kernel",
        "version":"4.1.0",
        "ever_found":"",
        "count":0,
    },
    {
        "name":"linux_kernel",
        "version":"4.1.9",
        "ever_found":"",
        "count":0,
    }

]
# targetSoftware = ["putty","ixgbe","libvirt", "ixgbevf","ffmpeg","openssh","cygwin","xl2tpd", "trusted_firmware-a","ziparchive"] #"linux_kernel"
# targetVersion = ["0.71","5.5.5","5.4.0", "4.5.3","4.1.3","8.0p1","3.0.7","1.3.14","2.1","2.2.2"] # "3.10"
with open("./output.csv", 'w') as csvOutputFile:
    writer = csv.writer(csvOutputFile)
    for year in range(2013, 2020):
        print("scanning year "+str(year))
        with open('./nvdcve-json/nvdcve-1.0-'+str(year)+'.json', encoding = "utf-8") as f:
            data = json.load(f)
            # print(len(data["CVE_Items"]))
            for cve in data["CVE_Items"]:
                id = cve["cve"]["CVE_data_meta"]["ID"]
                vendorDatas = cve["cve"]["affects"]["vendor"]["vendor_data"]
                for vdd in vendorDatas:
                    for product in vdd["product"]["product_data"]:
                        for i in range(0, len(targetSoftware)):
                            productName = product["product_name"]
                            if productName == targetSoftware[i]["name"]:
                                targetSoftware[i]["ever_found"] = "true"
                                for version in product["version"]["version_data"]:
                                    if debug:
                                        print("-----------------------------year:"+str(year)+"  "+product["product_name"]+" "+id)
                                    if versionIsMatch(targetSoftware[i]["version"], version["version_affected"], version["version_value"]):
                                        targetSoftware[i]["count"] += 1
                                        cweType = cve["cve"]["problemtype"]["problemtype_data"][0]["description"][0]["value"]
                                        version = "3"
                                        if not version in cve["impact"]:
                                            version = "2"
                                        baseScore = cve["impact"]["baseMetricV"+version]["cvssV"+version]["baseScore"]
                                        # impactScore = cve["impact"]["baseMetricV"+version]["impactScore"]
                                        vector = cve["impact"]["baseMetricV"+version]["cvssV"+version]["vectorString"]
                                        description = cve["cve"]["description"]["description_data"][0]["value"]
                                        refs = cve["cve"]["references"]["reference_data"]
                                        patchUrls = ""
                                        for j in range(len(refs)):
                                            ref = refs[j]
                                            patchReference = False
                                            tags = ref["tags"]
                                            for k in range(len(tags)):
                                                if tags[k] == "Patch":
                                                    patchReference = True
                                                    break
                                            if patchReference:
                                                patchUrls = patchUrls + "\n" + ref["url"]
                                        funcStr, funcPath = findFuncNames(description)
                                        if filterDriver(description):
                                            continue
                                        #for name in funcNames:
                                        #    funcStr = funcStr + name + ",  "
                                        writer.writerow([id])
                                        # print(targetSoftware[i]["name"]+"\t"+id+"\t"+targetSoftware[i]["version"]+"\t"+version["version_affected"]+"\t"+version["version_value"])


for i in range(0, len(targetSoftware)):
    if not targetSoftware[i]["ever_found"]:
        print(targetSoftware[i]["name"]+" not ever found")
    else:
        print(targetSoftware[i]["name"] + " : " + targetSoftware[i]["version"] + " found " + str(targetSoftware[i]["count"]))
