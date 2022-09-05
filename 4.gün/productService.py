# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:49:10 2022

@author: lenovo
"""
import db
from db import database


# product insert
def productSave(title,detail,price):
    cursor = database.cursor()
    sql ='insert into product values(null, %s, %s, %s, now() )'
    val = (title, detail, price)
    cursor.execute(sql,val)
    db.database.commit()
    return cursor.rowcount

# product list
def productList():
    cursor = database.cursor()
    sql = 'select * from product'
    cursor.execute(sql)
    return cursor.fetchall()

    
# product search
def productSearch(data):
    cursor = database.cursor()
    sql = 'SELECT * FROM product WHERE title LIKE %s OR detail LIKE %s OR price LIKE %s'
    data = "%{0}%".format(data)
    val = (data,data,data)
    cursor.execute(sql,val)
    return cursor.fetchall()

# product update
def productUpdate(pid, title, detail, price):
    cursor = database.cursor()
    sql = 'update product set title = %s, detail = %s, price = %s where pid = %s'
    val = (title,detail, price, pid)
    cursor.execute(sql,val)
    db.database.commit()
    return cursor.rowcount

# product delete
def productDelete(pid):
    cursor = database.cursor()
    sql ='delete from product where pid = %s'
    val = (pid,)
    cursor.execute(sql,val)
    db.database.commit()
    return cursor.rowcount




    
    
    







    
    
    


