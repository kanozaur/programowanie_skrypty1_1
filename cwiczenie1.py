wiek1=input("Wpisz wiek pierwszego sudenta ")
wiek2=input("Wpisz wiek drugiego studenta ")
wiek1=float(wiek1)
wiek2=float(wiek2)

wiek1_1=str(int(wiek1))
wiek1_2=str(int(wiek2))


if wiek1>wiek2:
    moj_tekst = "Pierwszy student jest starszy i ma " + str(int(wiek1)) + " lat(a)."
    print(moj_tekst)
with open('wiek1.txt','w') as plik:
    plik.write("Wiek pierwszego studenta "+wiek1_1+'\n'+
    "Wiek drugiego studenta "+wiek1_2+'\n'+
    "Pierwszy student jest starszy i ma " + wiek1_1+"lat(a)")
