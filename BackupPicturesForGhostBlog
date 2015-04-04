# coding: utf-8
import sys
import re  
import os  
import urllib  
import urllib2
import collections


def getFileSize(url):  
    opener = urllib2.build_opener()
    request = urllib2.Request(url)
    request.get_method = lambda: 'HEAD'
    try:
        response = opener.open(request)
        response.read()
    except Exception, e:
        print '%s %s', (url, e)
    else:
        return dict(response.headers).get('content-length', 0)

def downLoadFile(url, storePath):  
    try:
        urllib.urlretrieve(url, storePath)
    except Exception, e:
        print '%s', e
    finally:
        print "\n" + url + "  downloaded over"

prefix = "http://ofpsxx.com/content/images/"
r = re.compile(u"/content/images/([0-9]+)/([0-9]+)/([a-zA-Z0-9-_]+)\.(jpg|png|bmp)")
reload(sys)
sys.setdefaultencoding("utf-8")
f = open("h.json").read()
result = set(r.findall(f))

downloadFiles = 0
passFiles = 0
totalFiles = len(result)

for x in result:
    dirs = os.path.abspath('.') + "\\" + x[0] + "\\" + x[1];
    webAddress = prefix + x[0] + "/" + x[1] + "/" + x[2] + "." + x[3]
    localAddress = os.path.abspath('.') + "\\" + x[0] + "\\" + x[1] + "\\" + x[2] + "." + x[3]
    if os.path.exists(dirs) == False:
        os.makedirs(dirs)
    if os.path.exists(localAddress):
        if int(os.path.getsize(localAddress)) != int(getFileSize(webAddress)):
            downLoadFile(webAddress, localAddress)
            downloadFiles += 1
        else:
            print webAddress, "pass" 
            passFiles += 1
    else:
        downLoadFile(webAddress, localAddress)
        downloadFiles += 1
    print str(passFiles) + " files passed ", str(downloadFiles) + " files downloaded ", " TotalFiles:" + str(totalFiles)

