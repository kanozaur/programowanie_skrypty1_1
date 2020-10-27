#wiek=input("Wiek pierwszego sudenta: ")
#wiek1_1=float(wiek)
#wiek1_1=str(int(wiek))

#with open("wiek_drugiego_studenta.txt") as plik:
   # wiek2=plik.readlines()
   # print(wiek2)

wiek1=input("Wpisz wiek pierwszego studenta: ")
wiek1=float(wiek1)
wiek1_1=str(int(wiek1))

with open ("wiek_drugiego_studenta.txt") as plik2:
    wiek2=plik2.readlines()
    print(wiek2)

#with open("wiek_drugiego_studenta.txt") as plik:zawartosc=plik.readlines()
#with open("wiek_drugiego_studenta.txt") as plik:zawartosc=plik.read().splitlines()
#with open("wiek_drugiego_studenta.txt") as plik:zawartosc=[]
#for wiersz in plik:zawartosc.append(float(wiersz))
