wiek=input("Pierwszy student jest starszy i ma ")
print("Wiek pierwzego studenta")
a=input("25")
print("Wiek drugiego studenta")
b=input("22")
if a>b:
    print("pierwszy student jest starszy i ma "+a+"lata")

#wiek drugiego studenta
plik=open("wiek_drugiego_studenta.txt")
print(plik)
tresc=(plik.read)
print(tresc)
with open("wiek_drugiego_studenta.txt") as plik:
    zawartosc=plik.readlines()
with open("wiek_drugiego_studenta.txt") as plik:
    zawartosc=plik.read().splitlines()
with open("wiek_drugiego_studenta.txt") as plik:
    zawartosc=[]
    for wiersz in plik:
        zawartosc.append(wiersz)
        zawartosc.append(float(wiersz))

str(a-b)
print(a-b)
int(wiek)
with_open('moj_plik.txt') as plik:
plik.write(Pierwszy student jest starszy i ma 25 lat)
