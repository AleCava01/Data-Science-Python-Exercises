import glob
import re

path = "directory"
content = []
filenames = glob.glob(path+'/*.*')
for filename in filenames:
    try:
        with open(filename, mode='r') as f:
            data = f.read()
            words = [x.lower() for x in re.findall(r"\w+",data)]
            content.append(words)
    except Exception as e:
        print(e)
        print('impossibile aprire il file')
keys=set()
d=dict()
values=[]
for x in content:
    for y in x:
        keys.add(y)
for key in keys:
    d[key]=[]
    for i in range(0,len(content)):
        if key in content[i]:
            d[key].append(filenames[i])
    
    
for key in d.keys():
    print(key,d[key])