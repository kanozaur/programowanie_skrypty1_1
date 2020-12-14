moj_folder="C:/Users/Karolina/Documents/programowanie_skrypty/Zadania_programowanie/Cwiczenia_5"
import os
import csv
import numpy as np

lista_1=os.listdir(moj_folder)
liczba_elementow=len(lista_1)

lista=[]
for i in range(0,liczba_elementow):
    j=lista_1[i]
    with open (j,'r',encoding='utf8') as plik:
        zmienna=csv.reader(plik,delimeter=',')
        naglowki=next(zmienna)
        for row in zmienna:
            lista.append(row)

tablica=np.array(lista)
temp=tablica[:,4].astype(float)
min_temp=min(temp)
min_temp_index=np.where(temp==min_temp)

max_temp=max(temp)
max_temp_index=np.where(temp==max_temp)

lokalizacja1=tablica[min_temp_index,1]
godzina1=tablica[min_temp_index,3]

lokalizacja2=tablica[max_temp_index,1]
godzina2=tablica[max_temp_index,3]
print("Najnizsza temperatura zostala zaobserowana na stacji "+str(lokalizacja1)+"o godzinie ",+(godzina1))
print("Najwyższa temperatura zostala zaobserowana na stacji "+str(lokalizacja2)+"o godzinie ",+(godzina2))

dlugosc=len(tablica)
a=0

for a in range(0,dlugosc):
    b=float(tablica[a,8])
    godzina=tablica([a,3])
    if (b<c):
        print("Opad wystapil na stacji"+str(tablica[a,1])+"o godzinie "+ str(godzina))