import os
import mysql.connector as mysql


def cwd():
    cwd= os.getcwd()
    return cwd


#Checks and reads login.txt, if login.txt doesn't exist it creates one with your credentials you input
def login():
    path= f"{cwd()}\\login.txt"
    if not os.path.isfile(path):
        print("login.txt not found \nlogin.txt will be created")
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


def folder_create():
    path= f"{cwd()}\\graphs"
    if not os.path.exists(path):
        os.makedirs(path)


def graph_open():
    path= f"{cwd()}\\graphs"
    for file in os.listdir(path):
        os.system(f"{path}\\{file}")