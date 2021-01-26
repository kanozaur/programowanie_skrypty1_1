#zad1
import csv
import numpy as np
plikcsv='C:/Users/Karolina/Documents/programowanie_skrypty/Zadania_programowanie/Cwiczenia_4/meteo.csv'
lista=[]
with open(plikcsv,'r') as plik:
    zmienna=csv.reader(plik)
    naglowki=next(zmienna)
    print(naglowki)
    lista.append(next(zmienna))
    lista.append(next(zmienna))
    lista.append(next(zmienna))
    lista.append(next(zmienna))
    lista.append(next(zmienna))
    print(lista[0])
tablica=np.array(lista)
print(tablica)
print(tablica[3])
# Czestochowa

#zad2
#wszystkie wiersze, kolumna
#sr.temp
print(tablica[:,4].astype(float))
print(np.mean(tablica[:,4].astype(float)))
#sr.wilg
print(tablica[:,7].astype(float))
print(np.mean(tablica[:,7].astype(float)))
#sr.cis
print(tablica[:,-1].astype(float))
print(np.mean(tablica[:,-1].astype(float)))