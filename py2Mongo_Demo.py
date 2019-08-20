# -*- coding: utf-8 -*-
from py2Mongo import py2Mongo as p2m

def display_menu():
    print("\nEnter 1 to add entries to the db"\
          "\n\nEnter 2 to change the database name"\
          "\n\nEnter 3 to view the current database entries"\
          "\n\nEnter 4 to make MongoDB code and create the " \
          "MongoInserts.txt file"\
          "\n\nEnter 0 to exit and complete the program")
    try:
        return int(input())
    except ValueError:
        print("\n*" * 10 +"Invalid Input" + "*" * 10 + \
              "\nPlease enter an integer correspondinng to your choice.")

def displ_ch(x):
    print("\nChoice: " + str(x))

print("Enter a DB Name: ")
user_db = input()
db_obj = p2m(user_db)
user_ch = -1
while user_ch != 0:
    user_ch = display_menu()
    if user_ch == 1:
        displ_ch(user_ch)
        db_obj.add_entries()
    elif user_ch == 2:
        displ_ch(user_ch)
        print("\nPlease enter a new name for the database: ")
        user_db = input()
        db_obj.set_db(user_db)
    elif user_ch == 3:
        displ_ch(user_ch)
        print("\nCurrent Entries:")
        print(db_obj.ini_dict)
    elif user_ch == 4:
        displ_ch(user_ch)
        db_obj.make_inserts()
    elif user_ch == 0:
        displ_ch(user_ch)
        print("\nProgram will now terminate. Thank you for using py2Mongo.")
    else:
        print("\nPlease enter a number corresponding to one of the menu options")