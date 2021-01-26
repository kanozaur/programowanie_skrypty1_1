import csv
import numpy as np
import requests

url="https://danepubliczne.imgw.pl/api/data/synop/format/csv"

r=requests.get(url,allow_redirects=True)
dane_meteo=str(r.content,encoding='utf8')
dane_meteo=dane_meteo.split('\n')
#wyswietlic liste stacji synoptycznych wraz z identyfikatorami

dlugosc=len(dane_meteo)

for i in range(dlugosc):
    dane_meteo[i]=dane_meteo[i].split(',')

print(dane_meteo)

tablica_meteo=np.array(dane_meteo)
for i in range(len(tablica_meteo)-1):
    print(tablica_meteo[i][0],tablica_meteo[i][1])


#zadac od uzytkowanika wybrania 1 stacji poprzez wpisania jej kodu, podanie niewlasciwego kodu ma powodowac odpowiednia reakcje programu

liczba=int(input())
if liczba>20:
    print("Tak")
else:
        print("Nie")


