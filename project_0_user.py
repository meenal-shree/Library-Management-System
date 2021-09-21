import pymongo
from os import system
Client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
library = Client['library']
user = library.users
books = library.books
current_user = ""

def print_books(x): 
    print("title:- ",x['title'])
    print("author:- ",x['author'])
    print("year:- ",x['pub_year'])
    print("isbn:- ",x['isbn']+'\n')
        
    

def borrow_book():
    book_isbn = input('Enter the ISBN of the book you wnat to borrow:- ')
    req_book = books.find({'isbn': book_isbn})
    if(bool(req_book)):
        if(req_book['status'] == 'A'):
            books.update_one({'isbn': book_isbn},{'$set':{'statue':'B','issuer':current_user}})
            print('Book issued!')
        elif(req_book['status'] == 'B'):
            print("Book already borrowed by ", req_book['issuer'])
    else:
        print("Book not found! Please Try again....")
        system('cls')
        borrow_book()

def user_list_books():
    print("\nlist of books\n")
    for x in books.find({}):
        print_books(x)
    input("press enter to continue")
    system("cls")

def list_br_books():
    print("\nlist of borrowed books\n")
    for x in books.find({'issuer':  current_user}):
        print_books(x)
    input("press enter to continue")
    system("cls")

def return_book():
    book_isbn = input('Enter the ISBN of the book:- ')
    req_book = books.find({'isbn': book_isbn})
    if(bool(req_book)):
        if(req_book['issuer'] == current_user and req_book['status'] == 'B'):
            books.update_one({'isbn': book_isbn},{'$set':{'statue':'A','issuer': 'NULL'}})
            print('Book Returned!')
        else:
            input("Book not issued by you or already returned\nPress enter to continue")
            system('cls')
    else:
        print("Book not found! Please Try again....")
        system('cls')
        return_book()

def user_login():
    print('-------- USER MENU--------')
    print('1.Borrow Book\n2.List all books\n3.List borrowed books\n4.Return book')
    choice = int(input('Enter your choice:- '))
    if(choice == 1):
        borrow_book()
    elif(choice == 2):
        user_list_books()
    elif(choice == 3):
        list_br_books()
    elif(choice == 4):
        return_book()
    else:
        try:
            assert False
        except:
            print('Exiting....')