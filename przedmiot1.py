przedmiot = input ("Wpisz nazwe przedmiotu:")
print("Uczeszczam na nastepujacy kurs: ", przedmiot)
#print(przedmiot)
plik=open("text.txt")
print(plik)
tresc=plik.read()
print(tresc)
with open("values.txt") as plik:zawartosc=plik.readlines()
with open("values.txt") as plik:zawartosc=plik.read().splitlines()
with open("values.txt") as plik:zawartosc=[]
for wiersz in plik:zawartosc.append(float(wiersz))

a=12
b=24
print(b-a)
print("Hello, world!")

test=input("Wpisz nazwe tgodnia:")
test

