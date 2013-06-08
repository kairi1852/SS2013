import sys
import re

filePath=sys.argv[1]
f=open(filePath)
s = f.read()
f.close()
s_sub=re.sub(re.compile("[^A-Za-z]")," ",s.lower())

words = s_sub.split()

d = {}

for w in words: 
    if d.has_key(w):
        d[w] += 1
    else: 
        d[w] = 1


sored_keys = sorted(d.keys(), key = lambda x: d[x], reverse = True)
print "all: %d" % len(d)

i = 0
for k in sored_keys:
    if i == 20:
        break
    print k, ": ", d[k]
    i += 1
