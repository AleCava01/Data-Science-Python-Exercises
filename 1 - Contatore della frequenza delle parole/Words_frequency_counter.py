import urllib.request
import re
from collections import Counter

#url = input("inserire l'indirizzo url della pagina richiesta: ")
url = "https://it.wikipedia.org/wiki/Physignathus_cocincinus"


try:
    with urllib.request.urlopen(url) as doc:
        html = doc.read().decode()
        data=re.findall(r"\w+",html)
        data=[x.lower() for x in data]
        cntr = Counter(data)
        cntrDict = dict(cntr.most_common(10))
        print(cntrDict)
except Exception as e:
    print(e)
    print("Could not open required page")