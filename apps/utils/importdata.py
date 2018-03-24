# _*_coding:utf-8_*_

import json

def importdatabase(name):
    with open(name, 'r') as f:
        data = json.load(f)
        print data[0]
    return data
