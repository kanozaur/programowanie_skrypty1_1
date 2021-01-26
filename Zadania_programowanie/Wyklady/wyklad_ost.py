import requests
url="https://danepubliczne.imgw.pl/api/data/synop/format/csv"
req=requests.get(url)
all_data=req.content
all_data=all_data.splitlines()
for r in range(0,len(all_data)):
    print(all_data[r])
import time
poczatek=time.localtime()
for i in range(0,1000):
    print(i)
koniec=time.localtime()
roznica=time.mktime(koniec)-time.mktime(poczatek)

print("poczatek: ",poczatek)
print("koniec: ",koniec)
print("roznica: ",roznica)



datetime=time.strptime("2021-01-18 10:02:21.3", "%Y-%m-%d %H:%M:%S.%f")
print(datetime)


print("Koniec")
datetime=time.strptime("2021-01-18 10:02:21.3", "%Y-%m-%d %H:%M:%S.%f")
datetime_str=time.strftime("%Y-%m-%d %H:%M:%S",datetime)
print(datetime_str)

print("uspiony czas")
time.sleep(5)
print("Test")

#for i in range(0,10):
	#time.sleep(3)
#	print(i)
#break
#problem z pip install
import schedule

def zadanie():
    print("Wykonaj moje zadanie...")

schedule.every(1).minutes.do(zadanie)
schedule.every().hour.do(zadanie)
schedule.every().day.at("12:15").do(zadanie)

while 1:
    schedule.run_pending()

~~~~~~
    import time
#data i czas
#zatrzymanie programu na jakis czas, po sekundzie i dwoch sekundach i dzialac na kilka krokow


#wykonanie dwoch funkcji jednoczesnie
print("start")
timer=time.time()
timer2=time.time()
while True:
    if time.time()-timer >1:
        print("test")
        timer=time.time()

    if time.time()-timer2>5:
        break

#do tego dodać jescze liste, stacje i bedzie sie pobeirac!
#za pomoca tego mozemy mierzyc dwa czasy na raz!