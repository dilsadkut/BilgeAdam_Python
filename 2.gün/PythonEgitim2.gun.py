print("Hello")

dic = {"title":"TV","Price":1000}
dic["detail"] = "TV Detail"
dic

 keys = dic.keys()
 values= dic.values()
 keys, values

 for key,val in dic.items():
    print(key,val)

dic.pop("detail")

dic

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

keys = myfamily.keys()
keys 

for key in keys:
    child = myfamily[key]
    print( child["name"], child["year"])

num1=10
num2=11

if num1 == num2:
    print("sayılar eşit")
else:
    print("Sayılar eşit değil")

name=""
surname=""
email=""
password=""

if name == "" or surname == "" or email == "" or password == "":
    print("Bazı alanlar boş")

if name == "":
    print("Name empty!")
elif surname =="":
    print("Surname empty!")
elif email =="":
    print("Email empty!")
elif password =="":
    print("Password empty!")
else:
    print("Form Send..")

name="Erkan"
surname=""
email="erkan@mail.com"
password=""

name="Erkan"
surname="Bilmem"
email="erkan@mail.com"
password="12345"

if num1>10 or num2>10:
    print("Koşullar sağlanıyor")
else:
    print("Koşullar sağlanmıyor")

if num1>9 and num2==10:
    print("Koşullar sağlanıyor")
else:
    print("Koşullar sağlanmıyor")

data=""
if num1>9 : 
    data ="9'dan Büyük"
    data

x=0
while x<10:
    print("While Call")
    x = x+1


x=0
while x<10:
    print("While Call:",x)
    x = x+1


y=0
while y<10:
    print("While Call",y)
    y=y+1
    if y==5:
        break

city ="İstanbul"

for char in city:
    print(char)

for x in range(6):
    print(x)

for i in range(10):
    print("For",i)

for i in range(5,15,2):
    print("For Range",i)

def noParams():
    print("noParams Call")

noParams()


def sum(n1,n2):
    sm = n1+n2
    print("Sum:", sm)

sum(100,500)
sum(343,565)

smx = sum(100,3453)
print(smx)

def returnSum(n1,n2):
    sm = n1+n2
    return sm

smy = returnSum(234,4564)
print("sum:",smy)

def arrFnc(*arr):
    print(arr[1])
listx = ["ali","veli","hasan"]
arrFnc("ali","veli","hasan")

def fncDic(**dic):
    print(dic["name"])


fncDic( name ="Zehra", surname = "Bilmem")

def fncDefaultValue(yas = 0, boy=0):
    end = yas/boy
    print(end)

fncDefaultValue(35, 170)
fncDefaultValue(50)


def fncDefaultValue(yas = 1, boy=1):
    end = yas/boy
    print(end)

fncDefaultValue(35)
fncDefaultValue(35,180)

listx = ["İstanbul","İzmir","Samsun","Adana","Ankara"]

def fncList(arr):
    for item in arr:
        print(item)

fncList(listx)

def faktoriyel(n):
    
    if n == 0:
        return 1
    else:
   
        return n * faktoriyel(n-1)

faktoriyel(4)


def recursive (n):
    if n==0:
        return 1
    else:
     sayi3= n* recursive(n-1)
     print(sayi3)
     return sayi3

recursive(3)

#lambda

sumLambda = lambda a,b : a+b 

sumz = sumLambda(40,55)
sumz

class Action:
    name = "Ali"
    surname = "Bilmem"
    age = 30

obj1 = Action()
type(obj1)

print( obj1.name, obj1.surname,obj1.age)

class Settings:
    num1 = 20
    def fncAction():
        return num1*num1

objSet = Settings()

end = objSet.fncAction()
end

objSet =  Settings()
objSet.fncAction()

class Settings:
    num1 = 20
    def fncAction(self):
        return self.num1*self.num1
        
objSet =  Settings()
objSet.fncAction()

objSet.num1 = 30
objSet.fncAction()

#Constructor (Değerlerin zorunlu tutulması)
class Customer:
    def __init__(self, name, surname, email, age ):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age

customer = Customer("Serkan","Bilmem","serkan@mail",40)

print(customer.name,customer.surname,customer.email,customer.age)

customerx= Customer() #bu şekilde çağırınca hata alıyoruz.

del customer
print(customer) #hata verir.

#-----------------------------------

class Student(Customer):
    def fncName(self):
        print(self.name, self.surname)


std = Student("Mehmet","Bilsin","mehmet@mail",40)
std.fncName()

lst = ["Mehmet","Ayşe","Suna","Ali","Kemal"]

for item in lst:
    print(item)

for item in lst:
    print(item)

itr1 = iter(lst)
print(type(itr1))

print( next(itr1))
print( next(itr1))
print( next(itr1))
print( next(itr1))
print( next(itr1))
print( next(itr1))

itr1 = iter(lst)
itr1.__sizeof__

for item in lst:
    print(next(itr1))

for item in lst:
    print(next(itr1))

objTuple = ("Adana","Antalya","Mersin")
print(type(objTuple))

itr2 = iter(objTuple)

print(next(itr2))

def fncSet():
    cityName = "İzmir"

fncSet()

print(cityName)

def fncSet():
    global cityName
    cityName = "İzmir"

fncSet()

print(cityName)

customerName = ""
customerName = "Kemal"

def fncCustomerName():
    customerName = "Ecem"

print(customerName)

fncCustomerName()

print(customerName)

def fncCustomerName(self):
    self.customerName = "Ecem"

fncCustomerName()

