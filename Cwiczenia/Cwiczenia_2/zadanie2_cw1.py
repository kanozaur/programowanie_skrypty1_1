wiek1=input("Wpisz wiek pierwszego studenta: ")
wiek1=int(wiek1)

with open ("wiek_drugiego_studenta.txt", 'r') as plik1:
    wiek2=plik1.readlines()

wiek2=int(wiek2[0])

a=(wiek2-wiek1)
a=str(a)
tekst=("Pierwszy student jest mlodszy od drugiego o "+ a + " lat(a)")
if wiek2>wiek1:
    print(tekst)

with open('wiek2.txt', 'w') as plik2:
    plik2.write(tekst)
