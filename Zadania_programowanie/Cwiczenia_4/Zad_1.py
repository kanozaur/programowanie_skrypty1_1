#zad1
import csv
import numpy as np
plik='meteo.csv'
with open('C:/Users/Karolina/Documents/programowanie_skrypty/Zadania_programowanie/Cwiczenia_4/meteo.csv','r') as plik:
    zmienna=plik.readline()
    lista=[zmienna]
    zmienna=np.array(lista)
    for row in zmienna:
        lista.append(row)
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
lista=[plik]
tablica=np.array(lista)
print(tablica)
#dane meteo dla 4 wiersza?
print(wiersz4)
#Dane meteorologiczne dla czwartego wiersza dotyczą Chojnic.
#zad2
import statistics
import math
t_bialyst=float(tablica[1][5])
t_bielsko=float(tablica[2][5])
t_chojn=float(tablica[3][5])
t_czesto=float(tablica[4][5])
t_elb=float(tablica[5][5])
srednia_t=((t_bialyst+t_bielsko+t_chojn+t_czesto+t_elb)/5)
print(srednia_t)
#srednia wilg
#w_bialyst=
#w_bielsko=
#w_chojn=
#w_czesto=
#w_elb=
#srednia_w=
#srednie cisnienie