plikcsv_1='C:/Users/Karolina/Documents/programowanie_skrypty/Zadania_programowanie/Pliki_5.py/Cwiczenia_5/synop_20201206_1400.csv'
moj_folder="C:/Users/Karolina/Documents/programowanie_skrypty/Zadania_programowanie/Pliki_5.py/Cwiczenia_5"
import os
import csv
import numpy as np

lista_1=os.listdir(moj_folder)
liczba_elementow=len(lista_1)


lista=[]
for i in range(0,liczba_elementow):
    j=lista_1[i]
    with open ('synop_20201206_1400.csv','r',encoding='utf8') as plikcsv:
            zmienna=csv.reader(plikcsv,delimeter=',')
            naglowki=next(zmienna)

