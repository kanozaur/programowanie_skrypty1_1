import csv
import numpy as np
import glob
import os

list_1=[]
np.array(list_1)
#tworze pusta liste i wyswietlam moj folder i pliki w nim zawarrte
moj_folder="C:/Users/Karolina/Documents/programowanie_skrypty/Zadania_programowanie/Cwiczenia_5"
lista_plikow=os.listdir(moj_folder)
for i in lista_plikow:
    print(os.path.join(moj_folder,i))
#do czego sluzy ta funkcja?
print(moj_folder)
print(lista_plikow)
#powielone? wystarczy jedno? bo moj folder zawiera to samo co lista plikow

#otwieram plik csv
#A=(str.encode(encoding="utf-8",errors="strict"))
with open("C:/Users/Karolina/Documents/programowanie_skrypty/Zadania_programowanie/Cwiczenia_5/synop_20201206_1400.csv", "r") as csvfile:
    dane=csv.reader(csvfile, delimiter=",")

    lista=[]
    print(lista)
# kiedy i w jaki sposob moge zrobic utf-8??

tablica=np.array(list_1)
temperatura=tablica[].astype(float)
min_temp=min(temperatura)
min_temp_index=np.where(temperatura==min_temp)
print(tablica[])
print(tablica[min_temp_index])
max_temp=max(temperatura)
max_temp_index=np.where(temperatura==min_temp)


#with open("synop_20201206_1400.csv,"rb") as csvfile:
   # csv reader=csv.reader(csvfile,delimeter=",")

  #  for row in csvreader:
   #     row=[entry.decode("utf8") for entry in row]
   #     print(":".join(now))




#otwieranie plikow/czytanie w petli wraz z UTF8 
#encoding="utf8"

