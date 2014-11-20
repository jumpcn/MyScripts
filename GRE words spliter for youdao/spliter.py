# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import random
s = map(lambda x: str(x).encode('utf-8'), open('gre2.xml', 'r').readlines())[1:-1]
k = [[s[i * 4 + j] for j in xrange(4)] for i in xrange(len(s)/4)]
random.shuffle(k)
div = 150
f = None
for i in xrange(len(k)):
	if(i % div == 0):
		if(f != None): f.write('</wordbook>')
		f = open('day' + str(i / div) + '.xml', 'w')
		f.write('<wordbook>')
	for j in xrange(4):
		f.write(k[i][j])
f.write('</wordbook>')
f.close()