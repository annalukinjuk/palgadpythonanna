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
    nimi=input("keda otsime")