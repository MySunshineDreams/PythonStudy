#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Get Online Service Device Count'
import urllib.request
import json

address = "http://10.11.144.68:48080/engine/usrmgr/query/devnum"
request = urllib.request.urlopen(address)
response_data = request.read()
print(response_data)
response_data = response_data.decode("utf-8").replace(" ", "").replace("\n", "")
jsonArray = json.loads(response_data)
print(jsonArray["date"], jsonArray["time"], jsonArray["count"])
