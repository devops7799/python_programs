#!/usr/bin/env python3
### Get all the pull requests from the github repo ###
import requests
import json

url = 'https://api.github.com/repos/kubernetes/kubernetes/pulls'
data = requests.get(url).json()
for i in range(len(data)):
    print ("Name: ", data[i]["user"]["login"])
