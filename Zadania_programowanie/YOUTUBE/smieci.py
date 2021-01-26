import datetime

teraz=datetime.datetime.now()
print(teraz.strftime("%H:%Y %d.%m.%Y"))

#data i godzina dzialania programu 
import time
print("start")
timer=time.time()
timer2=time.time()
while True:
    if time.time()-timer >1:
        print("test")
        timer=time.time()

    if time.time()-timer2>5:
        break

#przyszla data pobierania danych
datetime=time.strptime("2021-01-26 10:02:21.3", "%Y-%m-%d %H:%M:%S.%f")
datetime_str=time.strftime("%Y-%m-%d %H:%M:%S",datetime)
print(datetime_str)
~~~~
a="6" 
b=0

try:
    wynik=a/b
except ZeroDivisionError:
    print("dzielenie przez 0")
except:
    print("blad niezidentyfikowany")
else:
    print(wynik)
#wsystkie bledy bedzie zapisywal do liku, info o tej godzinie nie bylo int i sie nie wykonalo
#uodpornienie by program sie nie przerywal, aby skrypt dalej dzialal
finally: #dzieja sie zasze czy zdarzyl sie wyjatek czy nie
    print("koniec pracy")

#nie dziala jesli mamy string

Jeśli bedzie problem, program nie przstanie działać. 

#obsluga wyjatkow
try:
    print(text)
except:
    print("Wyjątek")
    
try:
    print("Moj napis")
except:
    print("Error")
else:
    print("ok")
#w przeciwnym wypadku niz except :)


a=6
b=0

try:
    wynik=a/b
except:
    print("cos poszlo nie tak")
else:
    print(wynik)
#wsystkie bledy bedzie zapisywal do liku, info o tej godzinie nie bylo int i sie nie wykonalo
#uodpornienie by program sie nie przerywal, aby skrypt dalej dzialal
finally: #dzieja sie zasze czy zdarzyl sie wyjatek czy nie
    print("koniec pracy")





czas_gromadzenia_plikow=input("Podaj id stacji: ")
nazwa_stacji=""
while i in range(dlugosc):
    if(numer_stacji == tablica_meteo[i][0]):
        nazwa_stacji = tablica_meteo[i][1]
        print(str("Dane synoptyczne zawieraja informacje o stacji " + nazwa_stacji))
        break
else:
    print("Brak stacji o podanym id.")
    przyszly_czas=input("Podaj date ")
    przyszly_czas=strptime("2021-01-26 10:02:21.3", "%Y-%m-%d %H:%M:%S.%f")
datetime_str=time.strftime("%Y-%m-%d %H:%M:%S",przyszly_czas)
print(przyszly_czas)

