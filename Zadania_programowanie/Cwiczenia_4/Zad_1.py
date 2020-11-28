#zad1
import csv
plik='meteo.csv'
with open('C:/Users/Karolina/Documents/programowanie_skrypty/Zadania_programowanie/Cwiczenia_4/meteo.csv','r') as plik:
    zmienna=plik.readline()
    lista=[zmienna]
    print(lista)
    wiersz2=plik.readlines(2)
    wiersz3=plik.readlines(3)
    wiersz4=plik.readlines(4)
    wiersz5=plik.readlines(5)
    wiersz6=plik.readlines(6)
    print(wiersz2)
    print(wiersz3)
    print(wiersz4)
    print(wiersz5)
    print(wiersz6)

import numpy as np
lista=[plik]
tablica=np.array(lista)
print(tablica)
#dane meteo dla 4 wiersza?
print(wiersz4)
#Dane meteorologiczne dla czwartego wiersza dotyczą Chojnic.

#zad2
#srednia temp
srednia_t=[zmienna]
print(srednia_t[3])
#srednia wilg
#srednie cisnienie
