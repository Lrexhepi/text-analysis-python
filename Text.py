import statistics

def öffnen(text):
    return open(text, "r")


def lesen(text): 
    return text.read()

def summe(text): 
    anzahl = 0 
    wörter = text.split()

    if wörter == []: 
        return 0 

    for x in wörter: 
        anzahl += 1
    
    return anzahl


def amwenigsten(text):
    dic = {}
    wörter = text.split()

    for x in wörter:  
        if x  not in dic:
            dic[x] = 1
        else: 
            dic[x] += 1
    
    return {k:v for k,v in dic.items() if v == 1}


def top10(text): 
    dic = {}
    wörter = text.split()

    for x in wörter:  
        if x not in dic:
            dic[x] = 1
        else: 
            dic[x] += 1

    sortiert = sorted(dic.items(), key=lambda item: item[1], reverse=True)

    top_10 = sortiert[:10]

    return dict(top_10)

def maximum(text):
    top = top10(inhalt)
    maxi = max(top, key=top.get)
    return maxi 

import statistics

def durchschnitt(text):
    dic = {}
    wörter = text.split()

    for x in wörter:
        dic[x] = dic.get(x, 0) + 1

    werte = dic.values()
    return round(statistics.mean(werte), 2)







    











datei = öffnen("read.txt")
inhalt = lesen(datei)
print(inhalt)

print(summe(inhalt))
print("")
print(amwenigsten(inhalt))
print(" ")
print(top10(inhalt))
print("")
print(maximum(inhalt))
print("")
print(durchschnitt(inhalt))
datei.close()
