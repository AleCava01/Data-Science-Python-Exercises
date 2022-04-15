import glob
import re
import pickle


def savePickle(data):
    with open("data.pickle", "wb") as oFile:
        pickle.dump(data,oFile)

def openPickle():
    with open("data.pickle", "rb") as iFile:
        obj = pickle.load(iFile)
        for key in obj.keys():
            print(key,obj[key])
        
   

path = "directory"
content = []
keys=set()
filenames = glob.glob(path+'/*.*')
for filename in filenames:
    try:
        with open(filename, mode='r') as f:
            data = f.read()
            words = [x.lower() for x in re.findall(r"\w+",data)]
            content.append(words)
            for x in words:
                keys.add(x)
    except Exception as e:
        print(e)
        print('impossibile aprire il file')

d=dict()

for key in keys:
    d[key]=[]
    for i in range(0,len(content)):
        if key in content[i]:
            d[key].append(filenames[i])
    
savePickle(d)
openPickle()