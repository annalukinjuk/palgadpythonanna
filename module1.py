def add_person():

def delete_person():
    palgad,inimesed=lists()
    nimi=input("siseta nimi - ")
    if nimi not in inimesed:
        print("lisame inimene ja tema palk?  ")
        p=input("1 - lisame, 2 - ei lisa  ")
        if p.upper=="1":

def biggest_salary():
    """calculating suurem palk
    """
    palgad=[]
    with open("palgad.txt", "r") as f1:
        for stro in f1:
            palgad.append