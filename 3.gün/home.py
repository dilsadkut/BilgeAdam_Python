# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:42:16 2022

@author: lenovo
"""

import action as ac
import platform as plt
from settings import name
import datetime as dt
import math 
import json
import re
import camelcase
import fileUsing as fl

sm=ac.sum(100, 50)


mn= ac.minus(100, 50)
print(sm)
print(mn)


for city in ac.cities:
    print(city)

for city in ac.cityArr:
    print(city["no"],city["name"])
    
for city in ac.cityArr:
    print(city["no"],city["name"])

print(plt.system())
print(dir(ac))
print(dir(plt)) #platform özellikleri

print(name)

#datetime

print(dt.datetime.now())
print(dt.datetime.now())
print(dt.datetime.now())

date = dt.datetime.now()
#year
print(date.year)
#month
print(date.month)
#day
print(date.day)

now ="{}-{}-{}"
nowFormat = now.format(date.day,date.month,date.year)
print(nowFormat)

print("{} Ayındayız".format(ac.months[date.month-1]))

# Math

mx = max(30,50,66)
print(mx)
mn = min(30,50,66)
print(mn)

absVal = abs(-89.5)
print(absVal)

powVal = pow(5,3)
print(powVal)

sqr = math.sqrt(7)
print(sqr)

print(math.ceil(19.9))
print(math.floor(19.9))

print(math.ceil(19.1))
print(math.floor(19.1))

piVal = math.pi
print(piVal)

# json

stJson =  '{ "name":"John", "age":30, "city":"New York"}'
dic = json.loads(stJson)
print(dic["name"], dic["age"],dic["city"])

stArr = '[ { "type": "home", "number": "212 555-1234" }, { "type": "fax", "number": "646 555-4567" } ]'
arr = json.loads(stArr)
for item in arr:
    print(item["number"])

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

print(type(x))
jsondumps = json.dumps(x)
print(type(jsondumps))
print(jsondumps)

# regex

data = 'ali bu gün merhaba dedi'

status = re.search('.*bi',data)

if status:
    print("Koşullar sağlanıyor")
else:
    print("Koşullar sağlanmadı")

email ="ali@ali.com"

emailStatus = ac.emailValid(email)
print(emailStatus)

#pip example
camel = camelcase.CamelCase()
dataPip = "Python kolay bir dil"
upperCase = camel.hump(dataPip)
print(upperCase)

#try except
try:
    #xxx = 10
    #print(xxx.call())
    div = 1/0
    print("this line call",div)
except Exception as ex:
   print("Lütfen 0'dan büyük bir değer giriniz!",ex)

try:
    i=1/0
    print("this call - 1")
except Exception:
    print("error call - 2")
finally:
    print("this call - 3")

print("This line call")

#input
#emailVal = input("Lütfen E-mail giriniz:")
#print(emailVal)

#file using

#file create
fl.createFile()

#file write data
fl.fileWrite("İzmir")

# file read data
ls = fl.fileRead()





  




    




















