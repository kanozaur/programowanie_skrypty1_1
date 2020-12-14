import os
import csv
import numpy as np
moj_folder="C:/Users/Karolina/Documents/programowanie_skrypty/Zadania_programowanie/Pliki_5.py/Cwiczenia_5"
lista_1=os.listdir(moj_folder)
print(lista_1)
liczba_elementow=len(lista_1)
lista=[]

for i in lista_1:
    with open (os.path.join(moj_folder,i),'r',encoding='utf8') as plikcsv:
        zmienna=csv.reader(plikcsv)
        naglowki=next(zmienna)
        for row in zmienna:
            lista.append(row)
print(lista)
tablica=np.array(lista)
print(tablica)

temp=tablica[:,4].astype(float)
min_temp=min(temp)
min_temp_index=np.where(temp==min_temp)

max_temp=max(temp)
max_temp_index=np.where(temp==max_temp)

lokalizacja1=tablica[min_temp_index,1]
godzina1=tablica[min_temp_index,3]
lokalizacja2=tablica[max_temp_index,1]
godzina2=tablica[max_temp_index,3]

print("Najnizsza temperatura zostala zaobserowana na stacji ",(lokalizacja1),"o godzinie ",(godzina1))
print("Najwyższa temperatura zostala zaobserowana na stacji ",(lokalizacja2),"o godzinie ",(godzina2))


opad=tablica[:,8].astype(float)

dlugosc=len(tablica)
b=0
for a in range(0,dlugosc):
    c=float(tablica[a,8])
    if (b<c):
        print("Opad wystapil na stacji ",(tablica[a,1])," o godzinie ",(tablica[a,3]),".")
    