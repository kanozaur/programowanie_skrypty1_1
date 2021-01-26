import csv
import numpy as np
import os
katalog="C:/Users/Karolina/Documents/programowanie_skrypty/Zadania_programowanie/Pliki_5.py/Cwiczenia_5/"
#podprogram do generowania listy plikow w dowolnym katalogu
def utworz_lista_plikow(katalog):
    lista_plikow=os.listdir(katalog)
    return lista_plikow
#podprogram do czytania jednego pliku z danymi meteo
def czytaj_jeden_plik(sciezka_i_plik):
    pola=[]
    lista=[]
    with open(sciezka_i_plik,'r',encoding="utf8") as plikcsv:
        csvreader=csv.reader(plikcsv)
        pola=next(csvreader)
        for wiersz in csvreader:
            lista.append(wiersz)
    tablica=np.array(lista)
    return tablica 
#podprogram do obliczenia min temp ze wsyztskich stacji w jendym pom
def oblicz_min_temp(tablica_meteo):
    temperatura=[]
    for i in range(0,len(tablica_meteo[:,4])):
        temperatura.append(float(tablica_meteo[i,4]))
    temperatura=np.array(temperatura)
    min_temp=min(temperatura)
    return min_temp

#program do oblciania min temp w Pl w kolenych momentach obserwacji
moj_folder="C:/Users/Karolina/Documents/programowanie_skrypty/Zadania_programowanie/Pliki_5.py/Cwiczenia_5/"

# utworz liste plikow z wykorzystywaniem funkcji "utwrz_lista_plikow"
lista_plikow=utworz_lista_plikow(moj_folder)

min_temp_wektor=[]

#petla po plikach z listy - stosujemy funkcje 'czytaj_jeden_plik' i "oblicz_min_temp"
for plik in lista_plikow:
    sciezka_i_plik=moj_folder+plik
    tablica_danych=czytaj_jeden_plik(sciezka_i_plik)
    minimalna_temperatura=oblicz_min_temp(tablica_danych)
    min_temp_wektor.append(minimalna_temperatura)
print(min_temp_wektor)