#import bibliotek
import csv
import numpy as np
import os
from funkcje_do_plikow_meteo import utworz_lista_plikow, czytaj_jeden_plik, oblicz_min_temp #wydaje mi sie ze tu czegoś brakuje?

#program do obliczania min temp w Pl w kolejnych momentach obserwacji
moj_folder="C:/Users/Karolina/Documents/programowanie_skrypty/Zadania_programowanie/Pliki_5.py/Cwiczenia_5/"

#utworz liste plikow z wykorzystaniem funkcji 'utworz_lista_plikow'
lista_plikow=utworz_lista_plikow(moj_folder)

min_temp_wektor=[]
#petla po plikach z listy - stosujemy funkcje "czytaj_jeden_plik" i "oblicz_min_temp"
for plik in lista_plikow:
    sciezka_i_plik=moj_folder+plik
    tablica_danych=czytaj_jeden_plik(sciezka_i_plik)
    minimalna_temperatura=oblicz_min_temp(tablica_danych)
    min_temp_wektor.append(minimalna_temperatura)

print(min_temp_wektor)