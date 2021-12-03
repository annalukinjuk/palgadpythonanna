def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    :rtype list loeme:
    :var stroka:
    """
    file=open(file,"r")
    liist=[]
    for stroka in file:
        liist.append(stroka.strip())
    file.close()
    return liist
def lisa(palgad, inimesed):
    """lisab inimene ja tema salary
    :rtype:list:
    :bool: palgad ja nimed
    """
    a=input("siseta nimi=>  ")
    b=int(input("siseta palk=>  "))
    inimesed.append(a)
    palgad.append(b)
    return palgad,inimesed

def otsing_nimi_jargi(inimesed:list,palk:list):
    """otsime inimesed ja nema palkad nimele listis
    :rtype:float:nimed:
    :bool: index
    """
    nimi=input("keda otsime?")
    for inimene in inimesed:
        if inimene.upper()==nimi.upper():
            n=inimesed.count(nimi)
            print("Inimene on olemas, selline nimi kohtume",n, "korda")
            b=0
            t=[]
            for i in range(n):
                k=inimesed.index(nimi, b)
                return inimene
def tulumaks():
    """otsime palk with tulumaks
    :rtype:float:palgad:
    :var: in nimed:
    """
    palgad=[]
    with open("palgad.txt", "r") as f1:
        for s in f1:
            palgad.append(s.strip())
    inimesed=[]
    with open("inimesed.txt", "r") as inimene:
        for q in inimene:
            inimesed.append(q.strip())
    nimi=input("kelle palk arvutame?  ")
    if nimi in inimesed:
        a=inimesed.index(nimi)
        b=palgad[a]
        b=float(b)
        if b<=1200:
            h=b-500
            if h==0 or h<0:
                ans="tulumaks palk on" +str
                return ans
def suurim_(i:list,p:list):
    """Otsime suurim palk
    :rtype: str, str:
    :var kellel
    """
    suurim=max(p)
    print(suurim)
    b=p.index(suurim)
    kellel=i[b]
    print(kellel)
    return suurim, kellel

