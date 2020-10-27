wiek1=input("Wpisz wiek pierwszego sudenta")
wiek2=input("Wpisz wiek drugiego studenta")
wiek1=float(wiek1)
wiek2=float(wiek2)

if wiek1>wiek2:
    moj_tekst = "Pierwszy student jest starszy i ma " + str(int(wiek1)) + " lat(a)."
    print(moj_tekst)
with open("wiek_drugiego_studenta.txt") as plik:
    zawartosc=plik.readlines()
with_open("wiek_drugiego_studenta.txt","a") as plik:
    plik.write(moj_tekst)

#dosprawdzenia
#plik=open("wiek_drugiego_studenta.txt")
#print(plik)
#tresc=(plik.read)
#print(tresc)
#with open("wiek_drugiego_studenta.txt") as plik:
    #zawartosc=plik.readlines()
#with open("wiek_drugiego_studenta.txt") as plik:
    #zawartosc=plik.read().splitlines()
#with open("wiek_drugiego_studenta.txt") as plik:
    #zawartosc=[]
   # for wiersz in plik:
      #  zawartosc.append(wiersz)
        #zawartosc.append(float(wiersz))

#str(a-b)
#print(a-b)
#int(wiek)
#
#a="Pierwszy student jest starszy i ma "+