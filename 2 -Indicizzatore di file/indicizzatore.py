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
values=[]
for x in content:
    for y in x:
        keys.add(y)

for key in keys:
    value = []
    index=0
    for x in content:
        for y in x:
            if y==key:
                value.append(filenames[index])
        index=index+1
    values.append(value)
d=dict(zip(keys,values))
for key in d.keys():
    print(key,d[key])