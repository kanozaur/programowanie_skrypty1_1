import csv
import os
cwd=os.get.cwd()
files=os.listdir(cwd)
print("Files in %r:%s")
with open('datafile.txt', newline='') as csvfile:
    rows=csv.reader(csvfile,delimeter=',')
    data={}
    for row in rows:
        data[row[0]]=row[1:]

for key in data:
    print(data[key])

#dictionary uses key:value
#key=email adress
#value=list containining [firstmname, lastname, nickname]
#print(data[xde@gmail.com])
#>>["rest of data"]
#print(data[xde@gmail.com][0])
#>>"xde"