# -*- coding: utf-8 -*-
import json
import urllib2
import sys
import os

def getdata(id):
    name = ""
    try:
        if (id == 847334708):
            name = "meipai"
            f = open("meipai.txt", mode="w+")
        elif (id == 738897668):
            name = "xiaoying"
            f = open("xiaoying.txt", mode="w+")
        elif (id == 955253735):
            name = "faceu"
            f = open("faceu.txt", mode="w+")

        for page in range(1, 6):
            url = "https://itunes.apple.com/rss/customerreviews/page=" + str(page) + "/id=" + str(id) + "/sortby=mostrecent/json?l=en&&cc=cn"
            response = urllib2.urlopen(url)
            print "================================" + name + " : " + str(page) + "===================================================="
            jsonObj = json.loads(response.read())
            for i in jsonObj["feed"]["entry"][1:]:
                res = i["content"]["label"] + ";" + i["im:rating"]["label"] + ";" + i["im:version"]["label"]
                f.write(res+'\n')
    except Exception as e:
        raise
    finally:
        f.close()

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    getdata(847334708) # meipai
    getdata(738897668) # xiaoying
    getdata(955253735) # faceu
