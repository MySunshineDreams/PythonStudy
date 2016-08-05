#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Nginx日志聚合'

from _datetime import datetime, timedelta
import os

serverList = ["10.100.54.57", "10.100.54.58", "10.110.122.107", "10.110.122.80", "10.130.208.25", "10.130.208.33", "10.181.117.41", "10.181.117.81", "10.183.222.107", "10.183.222.135"]

if __name__ == "__main__":
    nginxMapResultFileName = "productIdList_" + (datetime.now() - timedelta(days=1)).strftime('%Y%m%d') + ".txt"
    os.system("ssh root@10.110.122.80 'cat /letv/shell/productIdList.txt' > /letv/data/allProductIdList.txt")
