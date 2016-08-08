#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Nginx日志聚合'

from _datetime import datetime, timedelta
import os
import pymysql

allProductIdListFileName = "/letv/data/allProductIdList_" + (datetime.now() - timedelta(days=1)).strftime('%Y%m%d') + ".txt"
nginxMapResultFileName = "/letv/data/productIdList_" + (datetime.now() - timedelta(days=1)).strftime('%Y%m%d') + ".txt"
writeFileName = "/letv/data/allProductIdCount_" + (datetime.now() - timedelta(days=1)).strftime('%Y%m%d') + ".txt"
containerOne = "="
allProductCount = {}
dataProductList = {}
mysqlConfig = {
    "host":"10.100.100.246",
    "port":3322,
    "user":"taps_w",
    "password":"dut8WKdyubplYnB6XdBT",
    "db":"taps",
    'charset':'utf8mb4'
}
queryProductSQL = "SELECT PRO_CODE, PRO_NAME FROM PS_PRODUCT"

serverList = ["10.100.54.57", "10.100.54.58", "10.110.122.107", "10.110.122.80", "10.130.208.25", "10.130.208.33",
              "10.181.117.41", "10.181.117.81", "10.183.222.107", "10.183.222.135"]

if __name__ == "__main__":
    # Copy the productIdList from all servers
    for server in serverList:
        os.system("ssh root@" + server + " 'cat /letv/data/productIdList.txt' >> " + allProductIdListFileName)
    # Open the file and statistics the total number
    with open(allProductIdListFileName, "r") as allProductIdFile:
        for line in allProductIdFile.readlines():
            if line.__contains__(containerOne) == False:
                continue
            productId = line.split(containerOne)[0]
            productCount = line.split(containerOne)[1]
            allProductCount[productId] = allProductCount.get(productId, 0) + int(productCount)
    connection = pymysql.connect(**mysqlConfig)
    cursor = connection.cursor()
    cursor.execute(queryProductSQL)
    for dataLine in cursor:
        dataProductList[dataLine[0]] = dataLine[1]
    writeFile = open(writeFileName, "a")
    for key, value in allProductCount.items():
        if dataProductList.__contains__(key) == False:
            continue
        writeFile.write(dataProductList[key] + " " + str(value) + "\n")