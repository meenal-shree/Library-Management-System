import pymongo
from os import system
from time import sleep
import Project_0
import project_0_user
import stdiomask as s # for entering passwoerd to a stdio terminal and displying a #### mask
client=pymongo.MongoClient("mongodb://127.0.0.1:27017")
library=client['library']
user=library.users
use={} # to store userdata globally
count=0


def check_pass():
    global count
    while(count<3):
        pas=s.getpass(prompt="enter your password:-\n",mask="#")
        if (len(pas)<5 or len(pas)>15):
            input("password too long or too short")
            count +=1
            check_pass()
            
        elif (pas.isalnum()==False):
            input("password should be alpha numeric")
            count +=1
            check_pass()
            
        elif(use['password']==pas): # comparing the input password with the global user data
            return True
        else:
            input('Password is wrong!')
            
            count +=1
            check_pass()
    input("maximum tries reched....Going back to login menu.")
    system('cls')
    count = 0
    login_menu()
    
def check_user():
    username=input("enter your username\n")
    global use
    for x in user.find({'username': username}):
        use=x # storing data of the user in the global vaiable when it matches with input username.
        return True
    else:
        input("user does not exist\n")
        check_user()
    


def login_menu():
    system('cls')
    choice=int(input('1.Login\n2.Exit\nEnter Your Choice:-\n'))
    if (choice==1):
        username,password=False,False #initializing  username and password  to False
        username=check_user() 
        password=check_pass()
        global use
        
        if (username==True): # Proceed further if username exists
            if(password == True): # Proceed if the password match
                if(use['isAdmin'] == True):
                    Project_0.menu() # To open the menu in the Project_0 Module
                else:
                    project_0_user.user_login()
            else:
                input("password wrong")
                login_menu()
        else:
            input("user does not exist")
            login_menu()
    else:
        try:
            assert False
        except:
            print("Execution Stopped!!")


            
login_menu()



