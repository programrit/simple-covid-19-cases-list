import datetime
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="ENTER USERNAME",
    password="ENTER PASSWORD",
    database="covid_19"
)
mycursor=mydb.cursor()
now=datetime.datetime.now()
current_time=now.strftime("%T")
# mycursor.execute("create database covid_19")
# mycursor.execute("create table register(name varchar(30),username varchar(40),phoneno varchar(10),password varchar(500),cpassword varchar(500))")
print("\n\tCovid-19 Data Management System")
print("Welcome to user page")
def show():
    user=input("If you have already account (yes/no): ").lower()
    def user_register():
        # insert data into database.
        sql="insert into register(name,username,phoneno,password,cpassword) values(%s,%s,%s,%s,%s)"
        while True:
            name=input("enter your name: ")
            if len(name) < 3:
                print("\tYour name is less than 3.")
                print("\tPlease enter your correct name")
                continue
            else:    
                if not name.isalpha():
                    print("\tNot allowed,number and special charcters")
                    print("\tPlease enter your correct name")
                    continue
                else:
                    break
        while True: 
            username=input("Enter your username: ")
            if len(username)<3:
                print("\tYour username less than 3")
                print("\tPlease enter your correct name")
                continue
            else:
                break
        while True:
            try:
                phoneno=int(input("Enter your phoneno: "))
            except:
                print("\tplease enter number only!")
                continue
            if len(str(phoneno))==10:
                break
            else:
                print("\tPlease enter correct phoneno")
                continue
        while True:   
            password=input("enter your password: ")
            if len(password)<6:
                print("\tYour password length is less than 6 characters!")
                continue
            else:
                break
        while True:
            cpassword=input("enter your confirm password: ") 
            if password!=cpassword:
                print("\tpassword doesn't match") 
                continue            
            else:
                break
        # check the username already exists or not.
        sql2=("select * from register where username=%s")
        mycursor.execute(sql2,[(username)])
        result=mycursor.fetchall()
        if result: 
            print("\tusername already exists")
            print("\tPlease use another username")
            user_register()
        else:        
            val=(name,username,phoneno,password,password) 
            mycursor.execute(sql,val)  
            mydb.commit()
            print("\n\tRegister Successfully") 
    def user_login():
        while True:
            username=input("Enter your username: ")
            password=input("Enter your password: ")
            # check the username and password in the db.
            sql2=("select * from register where username=%s and password=%s")
            mycursor.execute(sql2,[(username),(password)])
            result=mycursor.fetchall()
            if result:
                print("\n\tWelcome",username)
                break
            else:
                print("\tIncorrect username and password") 
                user=input("If you have already account (yes/no): ").lower()
                if user=="yes":
                    user_login()
                elif user=="no":
                    user_register()
                else:
                    print("\tEnter only yes or no!")
    if user=="yes":
        user_login()
    elif user=="no":
        user_register()
        user_login()
    else:
        print("\tEnter only yes or no!")
        show()
show()        
def show1():
    print("Covid positive list: ")  
    print("Covid recovery list: ")
    print("Covid death list: ")
# mycursor.execute("create table covid_positive(state varchar(50),district varchar(50),no_of_case int(50))")
    user1=input("Enter your choose (1,2,3): ")
    if user1=="1": # I have already insert the data about covid positive list
        print("\tCovid_19 positive list")
        mycursor.execute("select * from covid_positive")
        result1=mycursor.fetchall()
        for row in result1:
            f=open("covid_19.txt","w")
            f.write(f"current time is:{current_time}\n{result1}")
            f.close()
            print(row)                 
#  mycursor.execute("create table covid_recovery_list(state varchar(50),district varchar(50),no_of_death int(50))")
    elif user1=="2":# I have already insert the data about covid recovery list
        print("\tCovid_19 recovery list")
        mycursor.execute("select * from covid_recovery_list")
        result1=mycursor.fetchall()
        for row in result1:
            f=open("covid_19.txt","w")
            f.write(f"\n\ncurrent time is:{current_time}\n{result1}")
            f.close()
            print(row)           
# mycursor.execute("create table covid_death_list(state varchar(50),district varchar(50),no_of_death int(50))")
    elif user1=="3": # I have already insert the data about covid death list
        print("\tCovid_19 death list")
        mycursor.execute("select * from covid_death_list")
        result1=mycursor.fetchall()
        for row in result1:
            f=open("covid_19.txt","w")
            f.write(f"\n\ncurrent time is:{current_time}\n{result1}")
            f.close()
            print(row)
    else:
        print("\tPlease enter correct number") 
        show1()
show1()       
while True:
    con=input("Do you want to contine(yes/no): ").lower()
    if con=="yes":
        show1()
    elif con=="no":
        print("\n\tSTAY SAFE AND STAY HOME :)")
        break
    else:
        print("\tInvalid input")
        print("\tPlease enter only yes or no!") 
        continue



        


    



