# -*- coding: utf-8 -*-

class py2Mongo(object):
    """Class to create MongoDB code for inserting basic key-value entries"""
    def __init__(self, db):
        self.db_name = db
        self.j = 1
        self.ini_dict = {}
        
    @staticmethod    
    def nested_lists():
        """method to create list of nested lists to store k:v pairs"""
        count = -1
        while count <=0:
            try:
                print("\nEnter the number of desired key-value pairs for this entry: ")
                count = int(input())
            except ValueError:
                stars = "*" * 10
                print("\n" + stars + "Invalid input!" + stars + "\n"\
                      + "Please Enter a positive integer.\n")
        nested_L = [ [] for i in range (count)]
        return nested_L

    def set_db(self, d):
        """method to take string to set db_name"""
        self.db_name = d
        
    def get_current_dict(self):
        """method to return the current dictionary entries"""
        return str(self.ini_dict)
        
    def add_entries(self):
        """method to add entries to ini_dict,
        k:v pairs are stored in a nested list, 
        nested lists are the value for a numbered key"""
        L = py2Mongo.nested_lists()
        for i in range(1, len(L)+1):
            print("\nEnter a key for this pair: ")
            key = input()
            print("\nEnter a value for this pair: ")
            value=input()
            L[i-1] = [key, value]
            if i == len(L):
                self.ini_dict[self.j] = L
                self.j += 1
                print("\nPairs added: " + str(L))
                print("\nEntries so far: " + str(self.ini_dict))
                
    def make_inserts(self):
        """take dictionary and store pairs as a string
        then write it to a text file"""
        inserts = "use " + self.db_name + ";\nvar in = [ \n"
        for x in range(1, len(self.ini_dict) + 1):
            inserts += "{"
            c=1
            for i in self.ini_dict[x]:
                if (c != len(self.ini_dict[x])):
                    inserts += '"' + str(i[0]) +'"' + ":" +\
                    '"' + str(i[1]) + '"' + ", "
                else:
                    if x != len(self.ini_dict):
                        inserts += '"' + str(i[0]) + '"' + ":" +\
                        '"' + str(i[1]) + '"' + "},\n"
                    else:
                        inserts += '"' + str(i[0]) + '"' + ":" +\
                        '"' + str(i[1]) + '"' + "}\n];"
                c+=1
        inserts += "\ndb." + self.db_name + ".insert(in);"
        script_file = open("MongoInserts.txt", "w+")
        script_file.write(inserts)
        script_file.close()
        print("\n" + inserts)    