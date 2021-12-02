def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    """
    file=open(file,"r")
    list_=[]
    for stroka in file:
        list_.append(stroke.strip())
    file.close()
    return list_
def lise(palk, inimene):
    """lisab inimene ja tema salary
    """
    a=input("siseta nimi=>")
    inimesed.appeand(b)
    return palk,inimesed

def otsing nimi_jargi(inimesed:list,palk:list):
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
def 