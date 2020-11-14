a=21.3
if isinstance(a,str)==True:
     print("Typ zmiennej: lancuch.")
if isinstance(a,str)==False:
     print("Typ zmiennej: liczba")

if isinstance(a,int)==True:
    print("Typ zmiennej: calkowita.")
    print("Zmienna jest wartoscia calkowita.")

if isinstance(a,float)==True:
    print("Typ zmiennej: rzeczywista.")
    if a.is_integer()==True:
        print("Wartosc zmiennej: calkowita.")
    if a.is_integer()==False:
        print("Wartosc zmiennej: rzeczywista.")
