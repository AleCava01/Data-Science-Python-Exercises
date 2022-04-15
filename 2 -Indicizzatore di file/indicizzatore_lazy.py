import glob
import re

path = "directory"
d=dict()
for filename in glob.glob(path+'/*.*'):
    try:
        with open(filename, mode='r') as f:
            data = f.read()
            words = [x.lower() for x in re.findall(r"\w+",data)]
            for word in words:
                
                
                d[word]=[]
    except Exception as e:
        print(e)
        print('impossibile aprire il file')
for filename in glob.glob(path+'/*.*'):
    try:
        with open(filename, mode='r') as f:
            data = f.read()
            words = [x.lower() for x in re.findall(r"\w+",data)]
            for word in words:
                
                
                d[word].append(filename)
    except Exception as e:
        print(e)
        print('impossibile aprire il file')
for key in d.keys():
    print(key,d[key])