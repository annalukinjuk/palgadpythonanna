from module import*
from keyboard import*
palgad=loe_failist_listisse("palk.txt")
inimesed=loe_failist_listisse("inimesed.txt")

while 1:
    print("*"*100, "\nKeskmine - A\nMinimum - B\nMaksimum - C\n0tsing - G\nLisa - V")
    print("vajuta nuppu==>")

    if read_key()=="A":
        kesk_palk=round(keskmine(palgad,inimesed), 2)
        print("keskmine palk on ", kesk_palk)

    elif read_key()=="B":
        min_palk, kellel=minimum(palgad,inimesed)
        print("minimaalne palk ==> ", min_palk, " Kellel ==> ",kellel)

    elif read_key()=="C":
        max_palk, kellel=maksimum(palgad,inimesed)
        print("maksimaalne palk ==> ", max_palk, " Kellel ==> ",kellel)

    elif read_key()=="V":
        lisa(palgad,inimesed)
        print("siseta info  ", ans, "kellel==>")
