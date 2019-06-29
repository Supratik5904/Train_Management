import sys
from colorama import init
from termcolor import colored
from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
mydb=client["Trains"] #creating the Trains database
trains=mydb.trains   #creating the collection named trains
Mydb=client["User"] #creating the Users database
users=Mydb.users     #creating the collection named users
i=1
while(i!=-1):
    print("1.Login as admin")
    print("2.Login as user")
    print("3.Sign up")
    k=int(input("Enter choice:"))
    if(k==1):
        n=input("Enter ID:")
        pasw=int(input("Enter Password:"))
        if(n=="admin" and pasw==1234):
            l=1
            while(l!=-1):
                print("1.Insert Trains")
                print("2.Update Trains")
                print("3.Delete Trains")
                print("4.Search Trains")
                print("5.Show Trains")
                j=int(input("Your choice:"))

                def insert():
                    r=int(input("Number of records"))
                    for i in range(0,r):
                        Trains=dict()
                        Trains["_id"]=input("Enter Train Number:")
                        Trains["Source"]=input("Input source:")
                        Trains["Destination"]=input("Input destination:")
                        Trains["Departure"]=input("Input departure time:")
                        Trains["Arrival"]=input("Input arrival time:")
                        mydb.trains.insert_one(Trains)

                def show():
                    for train in trains.find():
                        print(train)

                def search():
                    s=input("Enter Source Station:")
                    d=input("Enter Destintion Station:")
                    query={"Source":s,"Destination":d}
                    for train in trains.find(query):
                        print(train)

                def update():
                    
                    n=input("Enter number of the Train to be updated:")
                    query={"_id":n}
                    for train in trains.find(query):
                        print(train)
                    print("1.Update Source")
                    print("2.Update Destination")
                    print("3.Update Schedule")
                    ch=int(input("Enter your choice:"))
                    if(ch==1):
                        src=input("Enter new source station:")
                        _query={"_id":n}
                        newquery={"$set":{"Source":src}}
                        trains.update_many(_query,newquery)
                        print("updated")
                    if(ch==2):
                        des=input("Enter new destination station:")
                        _query={"_id":n}
                        newquery={"$set":{"Destination":des}}
                        trains.update_many(_query,newquery)
                        print("updated")
                    if(ch==3):
                        st=input("Enter new departure:")
                        av=input("Enter new arrival:")
                        _query={"_id":n}
                        newquery={"$set":{"Departure":st,"Arrival":av}}
                        trains.update_many(_query,newquery)
                        print("updated")

                def delete():
                    _id=input("Enter train number to be deleted:")
                    trains.delete_one({"_id":_id})
                    
                    
                if(j==1):
                    insert()

                if(j==5):
                    show()
                    
                if(j==4):
                    search()

                if(j==2):
                    update()

                if(j==3):
                    delete()

                l=int(input("Enter -1 to exit as an admin"))
                
        else:
            init() 
            print(colored('Invalid admin or password', 'red')) 

    elif(k==2):
        user_id=input("Enter user name:")
        passw=input("Enter password:")
        
        query={"_id":user_id}
        for user in users.find(query):
            
            if(passw==user["password"]):
                l=1
                while(l!=-1):
                    print("1.Show Trains")
                    print("2.Search Trains")
                    print("3.Book Tickets")
                    print("4.Show Bookings")
                    c=int(input("Enter your choice:"))
                    def show():
                        for train in trains.find():
                            print(train)

                    def search():
                        s=input("Enter Source Station:")
                        d=input("Enter Destintion Station:")
                        query={"Source":s,"Destination":d}
                        for train in trains.find(query):
                            print(train)

                    def book():
                        search()
                        try:
                            ID=input("Enter train number to be booked:")
                        except:
                            print("enter an train number")
                        try:
                            date=input("Enter Date:")
                        except:
                            print("enter a date")
                        query={"_id":ID}
                        for train in trains.find(query):
                            train['date']=date
                            _query={"_id":user_id}
                            newquery={"$set":{"status":train}}
                            users.update_many(_query,newquery)
                            init()
                            print(colored('Booked','green'))

                    def ticket():
                        query={"_id":user_id}
                        for user in users.find(query,{"password":0,"_id":0}):
                            print(user)

                    if(c==1):
                        show()
                    if(c==2):
                        search()
                    if(c==3):
                        book()
                    if(c==4):
                        ticket()

                    l=int(input("Enter -1 to exit as an user"))

            else:
                init()
                print(colored('Invalid password', 'red'))
        else:
            init()
            print(colored('Invalid User', 'red'))
                    

    elif(k==3):
        
        User=dict()
        User["_id"]=input("Enter user name:")
        User["password"]=input("Set password:")
        User["status"]=[]
        Mydb.users.insert_one(User)
                    
                
    i=int(input("Enter -1 to exit"))
            
        
    

    
