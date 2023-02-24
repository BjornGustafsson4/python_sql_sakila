import os
import mysql.connector as mysql


#Checks and reads login.txt, if login.txt doesn't exist it creates one with your credentials you input
def login():
    cwd= os.getcwd()
    path= f"{cwd}\\login.txt"
    if not os.path.isfile(path):
        print("login.txt not found \n login.txt will be created")
        username= input("please enter your MySQL username: ")
        password= input("please enter your MySQL password: ")
        lines= str.encode(f"username {username} \npassword {password}")
        log= os.open("login.txt", os.O_RDWR|os.O_CREAT)
        os.write(log, lines)
        os.close(log)
    d= {}
    with open("login.txt") as txt:
        for line in txt:
            key, val = line.split()
            d[key]= val
    return d


#For this version database will always be sakila
def sql_connect(login_d):
    mydb = mysql.connect(
        host= "localhost",
        user= login_d["username"],
        password= login_d["password"],
        database= "sakila")
    return mydb