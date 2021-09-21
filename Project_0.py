from re import search
import pymongo
import time
from os import system
client=pymongo.MongoClient('mongodb://127.0.0.1:27017')
library=client['library']
table1=library.books

def print_fun(value):
    print("\nlist of books\n")
    for x in value: #value contains list of dict. so we r iterarting for that
        print("title:- ",x['title'])
        print("author:- ",x['author'])
        print("year:- ",x['pub_year'])
        print("isbn:- ",x['isbn']+'\n')
        
    input("press enter to continue")


    system("cls")

def menu():#main function from wher execution starts in this module
    system("cls")
    while (True):#we will run the whiile loop infinitely till break statement
        print("Library Management System")
        print("1.add new book\n2.search book \n3.list books\n4.update book\n5.delete book\n6.exit")
        choice=int(input("enter your choice"))
        if(choice==1):
            createbook()
        elif(choice==2):
            search_book()
        elif(choice==3):
            list_book()
        elif(choice==4):
            update_book()
        elif(choice==5):
            lib_del()
        elif(choice==6):
            system("cls")
            print("Books Are Uniquely Portable Magic!!!")
            time.sleep(3)
            break
        else:
            input("invalid input.press enter to start again") #waiting for user interaction
            system("cls")
            menu()

def  createbook():
    title =input("enter the title:- ")
    author =input("enter the author:- ")
    pub_year =input("enter the year:- ")
    isbn =input("enter the isbn:- ")
    records={ #creating dict wid input data
        'title':title,
        'author':author,
        'pub_year': pub_year,
        'isbn':isbn,
        'status': 'A',
        'issuer':'NULL'
    }
    table1.insert_one(records)
    print("book added")
    input("press enter to continue")
    system("cls")


def list_book():
    cursor=table1.find({}) # cursor is having all documents from collection
    print_fun(cursor)
    
        



def update_book():
    cursor=table1.find({})
    inp=input("enter the isbn:- ")
    for x in cursor:
        if(x['isbn']==inp):
            ch=int(input("1. Title\n2.author\n3.year\nenter your choice:- "))
            if(ch==1):
                re=input("enter new title:- ")
                table1.update_one({'isbn':inp},{'$set':{'title':re}})
            elif(ch==2):
                re=input("enter new author:- ")
                table1.update_one({'isbn':inp},{'$set':{'author':re}})
                
                
            elif(ch==3):
                re=input("enter new Year:- ")
                table1.update_one({'isbn':inp},{'$set':{'year':re}})
            else:
                input("invalid input, press enter to continue")
                update_book()
        else:
            input("book not found,press enter to continue")
            update_book()
    print("book updated!")
    input("press enter to continue")
    system("cls")                





def lib_del():
    isbnval=input("enter the isbn")
    cur=table1.find({'isbn':isbnval})
    for x in cur:
        if(x['isbn'] == isbnval):
            result=table1.delete_one({
                'isbn':isbnval
            })
            input("book deleted.press enter to continue")
            system("cls")
    else:
        input("Book doesn't exists! Press enter to continue")
        system('cls')



def search_book():
    choice= int(input("How do u want to search??\n1. By Title\n2. By Author \n3. By Year \n4. By ISBN \n Enter your choice!!!"))
    if (choice == 1):
        search_title= input("Enter the Title\n")
        cursor=table1.find({"title":{"$regex":search_title}})
        print_fun(cursor)
    elif(choice==2):
        search_author= input("Enter the Author\n")
        cursor=table1.find({"author":{"$regex":search_author}})
        print_fun(cursor)
    elif(choice==3):
        search_year= input("Enter the Year\n")
        cursor=table1.find({"pub_year":search_year})
        print_fun(cursor)
    elif(choice==4):
        search_isbn= input("Enter the ISBN\n")
        cursor=table1.find({"isbn":search_isbn})
        print_fun(cursor)
        








