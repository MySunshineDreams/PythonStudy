#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'nginx日志统计'
from datetime import datetime, timedelta
import os

nginxLogFileNameList = []
productIdDict = {}

def unzipLog(zipFileName, fileName):
    os.system("gunzip -c " + zipFileName + " > " + fileName)

def splitLogginFile(fileName):
    os.system("split -b 1000m " + fileName + " -d -a 2 /letv/shell/nginx_api_log_")

def getFilesToTraversal(dir, filePrefix):
    allFileNamesList = os.listdir(dir)
    for fileName in allFileNamesList:
        if fileName.__contains__(filePrefix) != False:
            nginxLogFileNameList.append(fileName)

def removeAllFilesUsed(dir, fileMatch):
    os.system("rm -f " + dir + fileMatch)

if __name__ == "__main__":
    fileName = "/letv/logs/bak/api." + (datetime.now() - timedelta(days=1)).strftime('%Y%m%d') + ".log"
    zipFileName = fileName + ".gz"
    unzipLog(zipFileName, fileName)
    splitLogginFile(fileName)
    getFilesToTraversal("/letv/shell/", "nginx_api_log_")
    print("文件列表", nginxLogFileNameList)
    for nginxFileName in nginxLogFileNameList:
        print("开始处理", nginxFileName)
        with open(nginxFileName, 'r') as f:
            for logLine in f.readlines():
                if logLine.__contains__("/upgrade?") == False:
                    continue
                requestParameter = logLine.split("/upgrade?")[1]
                if requestParameter.__contains__("appkey=") == False:
                    continue
                appkeyStart = requestParameter.index("appkey=") + 7
                appkey = requestParameter[appkeyStart::].split("&")[0]
                productId = appkey[2:5]
                if productIdDict.get(productId) == None:
                    productIdDict[productId] = 1
                else:
                    productIdDict[productId] = productIdDict.get(productId) + 1
        print("结束处理", nginxFileName)
    print("开始写入")
    writeFileName = "productIdList_" + (datetime.now() - timedelta(days=1)).strftime('%Y%m%d') + ".txt"
    writeFile = open(writeFileName, "a")
    for key, value in productIdDict.items():
        writeFile.write(key + "=" + str(value) + "\n")
    print("结束写入")
    print("开始删除")
    # removeAllFilesUsed("/letv/shell/", "nginx_api_log_*")
    # removeAllFilesUsed("", fileName)
    print("结束删除")