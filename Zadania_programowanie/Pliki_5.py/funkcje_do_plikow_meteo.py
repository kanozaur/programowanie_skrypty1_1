import csv
import numpy as np
import os

#podprogram do generowania listy plikow w dowolnym katalogu
def utworz_lista_plikow(moj_folder):
    lista_plikow=os.listdir(katalog)
    return lista_plikow

#podprogram do czytania jednego pliku z danymi meteo
def czytaj_jeden_plik(sciezka_i_plik):
    pola=[]
    lista=[]
    with open(sciezka_i_plik,"r",encoding="utf8") as plikcsv:
    csvreader=csv.reader(plikcsv)
    pola=next(csvreader)
    for wiersz in csvreader:
        lista.append(wiersz)
    tablica=np.array(lista)
    return tablica

#podprogram do oblicznaia minimalnej temp ze wsyzstkich stacji w jednym pomiarz

def oblicz_min_temp(tablica_meteo):
    temperatura=[]
    for i in range(0,len(tablica_meteo[:,4])):
        temperatura.append(float(tablica_meteo,[i,4]))
    temperatura=np.array(temperatura)
    min_temp=min(temperatura)
    return min_temp
    