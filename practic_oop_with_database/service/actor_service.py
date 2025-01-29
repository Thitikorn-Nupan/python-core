from mysql.connector.aio import MySQLConnectionAbstract
from mysql.connector.aio.abstracts import MySQLCursorAbstract

from practic_oop_with_database.configuration.connect_database import ConnectDatabase
from practic_oop_with_database.entity.actor import Actor
from practic_oop_with_database.log.log_application import LogApplication


class ActorService :

    __connectDatabase : ConnectDatabase
    __actors : list[Actor]
    __logApplication : LogApplication

    def __init__(self):
        self.__connectDatabase = ConnectDatabase()
        # self.__actors : list[Actor] = list() # way to initial and specify type
        self.__actors  = list()
        self.__logApplication = LogApplication(__file__)
        self.__logApplication.log.info("ActorService class is initial")


    def getAllActors(self):
        cursor = self.__connectDatabase.connect.cursor()
        cursor.execute("SELECT * FROM actors;")
        # If you are only interested in one row, you can use the fetchone() method.
        rows = cursor.fetchall()
        cursor.close()
        index = 0
        for columns in rows:
            # print(x) # (5, 'Dwayne Johnson', 199999900)
            # id = int(columns[0]) # get colum 1
            # name = str(columns[1]) # get colum 2
            # following = float(columns[2]) # get colum 3
            actor = self.convertSetToActor(columns[0],columns[1],columns[2])
            index = index+1
            self.__actors.insert(index,actor)
        return self.__actors

    def getActorById(self,id):
        cursor = self.__connectDatabase.connect.cursor()
        # ** Escape query values by using the placholder %s method:
        sql = "SELECT * FROM actors where actor_id = %s;"
        value = tuple((id,)) # have to be tuple type!!
        cursor.execute(sql,value) # dynamic values mark by %s
        row = cursor.fetchone() # If you are only interested in one row, you can use the fetchone() method.
        cursor.close()
        actor = self.convertSetToActor(row[0],row[1],row[2])
        # self.__logApplication.log.debug(actor)
        return actor

    # when we do something to database , do not forget commit()
    def removeActorById(self, id):
        # if you wanna know all methods , you should specify type
        connect : MySQLConnectionAbstract  = self.__connectDatabase.connect
        cursor : MySQLCursorAbstract = connect.cursor()
        sql = "delete from actors where actor_id = %s;"
        value = tuple((id,))  # have to be tuple type!!
        cursor.execute(sql, value)  # dynamic values mark by %s
        row = cursor.rowcount # 1 means present in the table and 0 means deleted
        connect.commit() # ***
        connect.close()
        cursor.close()
        # self.__logApplication.log.debug(actor)
        return row == 1


    def convertSetToActor(self, colum0, column1, column2):
        id = int(colum0)
        name = str(column1)
        following = float(column2)
        return Actor(id, name, following)




"""       
# Reads
for actor in ActorService().getAllActors() :
    print(actor)

# Read
print(ActorService().getActorById(1))    

# Delete
print(ActorService().removeActorById(8))


"""

