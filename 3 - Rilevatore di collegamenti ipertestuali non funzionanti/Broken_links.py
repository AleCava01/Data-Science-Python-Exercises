from bs4 import BeautifulSoup as bts
from collections import Counter
import re
from urllib.request import urlopen
import progressbar


url=input("url address (with http/https included): ")
print("Analyzing "+url+" ...")

try:
    soup = bts(urlopen(url), "html5lib")
    links = soup.find_all("a")
    error_raisers=[]
    errors = []
    n_errors = 0
    
    bar = progressbar.ProgressBar(maxval=len(links), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    
    
    for i in range (0, len(links)):
        if re.match(r'^http', str(links[i].get("href"))):
            links[i]=str(links[i].get("href"))
        else:
            links[i]=url+str(links[i].get("href"))
        try:
            urlopen(links[i])
            error_raisers.append(" ")
        except Exception as e:
            error_raisers.append(links[i])
            errors.append(str(e))
        bar.update(i+1)
            
    bar.finish()
    print("----------------------------")
    print("Not working urls:\n")
    for url in error_raisers:
        if(url!=" "):
            print(url)
    print("----------------------------")
    print("Statistiche \n")
    for key, value in Counter(errors).items():
        print(str(key)+": ", value)
        n_errors+=value
    print("\nNot working total: "+str(n_errors)+"/"+str(len(links)))
    print("Not working percentage: "+ str(round((n_errors/len(links)*100),2))+ "%")
    bye = input("\n\npress any key to kill")
    
except Exception:
    print("Unable to open requested url, error: \n"+str(Exception))

