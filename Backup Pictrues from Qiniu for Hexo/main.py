import re
import os
import urllib
import urllib2

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
	urllib.urlretrieve(url, storePath)
	print "\n" + Add + "downloaded over"


r = re.compile(u"\(http://ofpsxx.qiniudn.com/.*?\)")
path = './_posts'
backupPath = './backupPic'


if not os.path.exists(backupPath):
	os.mkdir(backupPath)
for parent, dir, fileList in os.walk(path):
	for name in fileList:
		if(name[-3:] == '.md'):
			content = open(parent + "/" + name).read()
			add = r.findall(content)
			for Add in add:
				Add = Add[1:-1]
				downLoadAdd = backupPath + "/" + Add.split('/')[-1]
				if os.path.exists(downLoadAdd):
					if int(os.path.getsize(downLoadAdd)) != int(getFileSize(Add)):
						print os.path.getsize(downLoadAdd), getFileSize(Add)
						downLoadFile(Add, backupPath + "/" + Add.split('/')[-1])
				else:
					downLoadFile(Add, backupPath + "/" + Add.split('/')[-1])



