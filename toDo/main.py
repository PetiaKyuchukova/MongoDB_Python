import pymongo

def insertOne(name,time):
  mydict = { "name": name, "time": time }
  x = mycol.insert_one(mydict)
  
def findAllTasks():
  for x in mycol.find({},{ "_id": 0, "name": 1, "time": 1 }):
        print(x)

def findOneTaskByName(name):
  myquery = { "name": name }
  mydoc = mycol.find(myquery)
  for x in mydoc:
    print(x)

def findOneTaskByTime(time):
  myquery = { "time": time }
  mydoc = mycol.find(myquery)
  for x in mydoc:
    print(x)

def deleteOne(name):
    myquery = { "name": name }
    mycol.delete_one(myquery)

def sortTasksAscending(time):
  mydoc = mycol.find().sort("time",1)
  for x in mydoc:
    print(x)

def sortTasksDescending(time):
  mydoc = mycol.find().sort("time",-1)
  for x in mydoc:
    print(x)

def updateName():
  print("Wich document you want to update")
  print("The name of task is ")
  name = input()
  print("The time of task is ")
  time = input()
  mydict = { "name": name, "time": time }
  print("new name is")
  name = input()
  newValues = { "$set": { "name": name } }
  mycol.update_one(mydict, newValues)

def updateTime():
  print("Wich document you want to update")
  print("The name of task is ")
  name = input()
  print("The time of task is ")
  time = input()
  mydict = { "name": name, "time": time }
  print("new time is")
  time = input()
  newValues = { "$set": { "time": time } }
  mycol.update_one(mydict, newValues)

def welcome():
  print("Welcome to your task manager!")
  print("If you want to ADD a task, key down a!")
  print("If you want to SEE all tasks, key down s!")
  print("If you want to SEARCH by NAME, key down sn!")
  print("If you want to SEARCH by TIME, key down st!")
  print("If you want to UPDATE a task`s NAME, key down un!")
  print("If you want to UPDATE a task`s TIME, key down ut!")
  print("If you want to DELETE a task, key down d!")
  input1 = input()

  if input1 == "close":
    print("bye bye")
  else: 
    if(input1 == "a"):
      print("Please, insert info about your task!")
      name = input()
      time = input()
      insertOne(name,time)
    elif(input1 == "s"):
      findAllTasks()
    elif(input1 == "sn"):
      print("Please, insert name!")
      name = input()
      findOneTaskByName(name)
    
    elif(input1 == "st"):
      print("Please, insert time!")
      time = input()
      findOneTaskByTime(time)
    
    elif(input1 == "d"):
      name = input()
      deleteOne(name)
    
    elif(input1 == "un"):
      updateName()
    
           
    elif (input1 == "ut"):
      updateTime

  welcome()  


client = pymongo.MongoClient('mongodb+srv://PetyaKyuchukova:471219011@cluster0.fgpsp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
mydb = client['taskMenager']

dblist = client.list_database_names()
if "taskMenager" in dblist:
  print("The database exists.")

mycol = mydb["task"]


welcome()







