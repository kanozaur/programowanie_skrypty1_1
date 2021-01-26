import csv
import io
import numpy as np
import os
import requests

moj_folder="C:/Users/Karolina/Documents/programowanie_skrypty/Zadania_programowanie/Cwiczenia_ostatnie/stacje"
lista_stacji=os.listdir(moj_folder)
print(lista_stacji)
liczba_elementow=len(lista_stacji)
lista=[]
for i in lista_stacji:
    with open (os.path.join(moj_folder,i),'r',encoding='utf8') as plikcsv:
        zmienna=csv.reader(plikcsv)
        for row in zmienna:
            lista.append(row)
print(lista)
tablica=np.array(lista)
print(tablica)

id_stacji=str(tablica[:,0])
print(id_stacji)
stacja=str(tablica[:,1])
print(stacja)

#co mamy, jakie problemy, z czym pomoc, by zaprezentowac liste, to co wyswietlamy, zebysmy mieli juz cos konkretnego
