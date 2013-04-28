import hashlib

#A file for making a database of users and passwords.

class log(object):
    login = 0
    def addUser(self, username, password): #Method that writes a users name and password into a text file. At a later point, I may add an option for different databases.
        with open('C:/DATABASE/file.txt', "a") as myfile:
            if self.findUser(username) != "None": #Checks to see if the username is taken or not.
                hashpswd = hashlib.sha224(password).hexdigest() #Hashes password.
                myfile.write(username + "   " + hashpswd + "\n")
                myfile.close()
            else:
                print "Sorry, that username is taken."
            
    def findUser(self, username): #Method that searches through the text file for a username, and then returns the users name and password.
        fob = open("C:/DATABASE/file.txt", "r")
        lines = fob.readlines()
        num = len(username)
        for line in lines:
            if line[:num].upper() == username.upper():
                return line[:-2]
            else:
                pass
        fob.close()
                    
    def delUser(self, username, password): #Function for deleting user.
        userid=len(username)
        passid=len(password)
        if self.findUser(username) != "None":
            fob = open("C:/DATABASE/file.txt", "r")
            lines = fob.readlines()
            fob.close()
            fob = open("C:/DATABASE/file.txt", "w")
            for line in lines:
                if((line[:userid] == username) and (line[passid-1:] == password)):
                    fob.write(line)
                else:
                    pass
            fob.close()
        else:
            print "User not found."
        fob.close()

    def login(self, username, password):
        line = self.findUser(username)
        passid = len(password)
        userid = len(username)
        
        if((line[:userid] == username) and (line[passid-1:] == password)):
            print "Login successful."
            self.login = 1
        else:
            print "Invalid username or password."
        
a=log()
