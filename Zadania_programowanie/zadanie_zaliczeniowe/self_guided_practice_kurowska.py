import csv
import numpy as np
import requests 
import time
from datetime import datetime

URL = "https://danepubliczne.imgw.pl/api/data/synop/format/csv"

#pobieranie danych z URL
def get_data():
    r=requests.get(URL,allow_redirects=True) #funkcja do requestu z url zdefiniowanego wyżej
    dane_meteo=str(r.content,encoding='utf8') #kontent pobrany jest definiowany jako zestaw ascii w utf-8
    dane_meteo=dane_meteo.split('\n') #rozdzielenie danych \n

    #wyswietlia liste stacji synoptycznych wraz z identyfikatorami

    dlugosc=len(dane_meteo)

    for i in range(dlugosc):  
        dane_meteo[i]=dane_meteo[i].split(',')

    tablica_meteo = np.array(dane_meteo) #definiowanie wartosici w tablicy przez np.array
    return tablica_meteo
# zwraca tablice dwuwymiarowa jako np.array

#znajduje nazwe stcji po id_stacji    
def get_station_from_user():
    tablica_meteo = get_data()

    nazwa_stacji = None #wyczyszczanie stringu do pustego none 

    while not nazwa_stacji:
        for i in range(len(tablica_meteo)-1):
            print(tablica_meteo[i][0],tablica_meteo[i][1])
        numer_stacji = input("Podaj id stacji: ") #podaj id_stacji
        nazwa_stacji = check_station_exist(tablica_meteo, numer_stacji) #sprawdza czy podany numer stacji istnieje

    return (numer_stacji, nazwa_stacji)

# Zwraca numer_stacji jesli istnieje, jesli jej nie ma, stacja nie istnieje i kaze ponownie wprowadzic id stacji

def check_station_exist(tablica_meteo, numer_stacji):
    dlugosc = len(tablica_meteo)
    for i in range(dlugosc):
        if numer_stacji == tablica_meteo[i][0]:
            nazwa_stacji = tablica_meteo[i][1]
            print(str("Dane synoptyczne zawieraja informacje o stacji: " + nazwa_stacji))
            return numer_stacji
    print('Stacja nie istnieje. Wpisz ponownie ID stacji.')
    return None #stacja nie istnieje, zwroc none, wpisz ponownie id stacji


def get_time_from_user():
    date = input('Podaj date oraz godzine YYYY-MM-DD-HH')
    
    year, month, day, hour = [int(x) for x in date.split('-')] 
#You can loop over the list you get from date.split() and convert each entry to an int.
    end_date = datetime(year, month, day, hour)

    return end_date #zwraca okreslona koncowa date


def get_pomiary(id_stacja, godzina_pomiaru):
    url = f'https://danepubliczne.imgw.pl/api/data/synop/id/{id_stacja}/format/csv' 
    r = requests.get(url, allow_redirects=True) #allow_redirects pozwala na przekierowanie na nowa domene, w przypadku zmiany adresu
    dane_meteo=str(r.content,encoding='utf8')
    
    dane = dane_meteo.split('\n')[1].split(',')
    
    godzina = dane[3]
    temperatura = dane[4]
    return (godzina, temperatura)

#modul programu, glowny program
def main():
    godzina_pomiaru = None
    temperatury = []
    numer_stacji, nazwa_stacji = get_station_from_user()
    
    if not nazwa_stacji:
        return
    
    end_date = get_time_from_user()
    print(end_date)

    now = datetime.now() # pobiera aktualny czas
    if end_date < now: # sprawdzenie czy end_date jest mniejszy/pozniejszy od terazniejszosci
        print('Data dotyczy przeszłości. Spróbuj ponownie.')
        return
     
    while True:
        HOUR = 3600 # 60*60
        FIVE_MINUTES = 300 #5 minut =60*5=300

        seconds = HOUR # zdefiniowanie godziny w sekundach
       
        godzina, temperatura = get_pomiary(numer_stacji, godzina_pomiaru)

        if godzina == godzina_pomiaru:
            print('Pomiar został już zrobiony!')
            seconds = FIVE_MINUTES

        else:
            godzina_pomiaru = godzina
            temperatury.append(float(temperatura))

        print(godzina_pomiaru, temperatury)
        
        if end_date < datetime.now():
            print('Koniec pomiarow.')
            break
        time.sleep(seconds)

    srednia_temperatura = sum(temperatury) / len(temperatury)
    with open('srednia-temperatura.txt', 'w') as f:
        f.write(str(srednia_temperatura)) 

if __name__ == "__main__":
    main()

"""


""" #zakończenie wszystkich funkcji 