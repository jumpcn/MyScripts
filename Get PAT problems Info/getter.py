from bs4 import BeautifulSoup
import urllib
import re
oURL = "http://www.patest.cn/contests/pat-a-practise/"

findMS = re.compile(r'[0-9]+\sms')
findByte = re.compile(r'[0-9]+\sB')
findMem = re.compile(r'[0-9]+\skB')
File = open(r'result.txt', 'w')
for x in xrange(86):
	url = oURL + str(1000 + x + 1)
	html = urllib.urlopen(url).read()
	bs = BeautifulSoup(html)
	k = bs.find_all(attrs={"class":"value"})
	MS = findMS.findall(str(k[0]))
	Mem = findMem.findall(str(k[1]))
	Byte = findByte.findall(str(k[2]))
	result = str(x + 1000 + 1) + " " + str(MS) + " " + str(Mem) + " " + str(Byte) + "\n"
	File.write(result)
	print result
File.close()