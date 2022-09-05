# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 09:43:25 2022

@author: lenovo
"""

import productService as pro
import datetime

#status = productSave("Tablet","Tablet Detail",6000)
#print(status)

start = datetime.datetime.now()
proList = pro.productList()
for item in proList:
    print(item[0], item[1], item[2], item[3], item[4])
end = datetime.datetime.now()
print(start)
print(end)

print("searchList===================")
searchList = pro.productSearch('69301')
for item in searchList:
    print(item)
    
print("updateStatus===================")
updateStatus = pro.productUpdate(2,'Fırın','Fırın detayı',15000)
print(updateStatus)

print("deleteStatus===================")
deleteStatus = pro.productDelete(2)
print(deleteStatus)











    

    

    



    

    
    
    
    
    



