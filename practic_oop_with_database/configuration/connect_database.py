# from <path to file import> import <name class>
import mysql.connector as mysql
## *** Note when this file work on anther file
## *** import like => import info_connect as database <= won work. it's nesty folder
# import info_connect as database
## *** You should do like below!
from practic_oop_with_database.configuration.info_connect import infoConnect

from mysql.connector.aio import MySQLConnectionAbstract
from practic_oop_with_database.log.log_application import LogApplication



class ConnectDatabase:

    ## it's private attribute (__**)
    __logApplication: LogApplication

    # pip install mysql-connector-python
    connect: MySQLConnectionAbstract

    def __init__(self):
        self.__logApplication = LogApplication(__file__)
        self.__logApplication.log.info("ConnectDatabase class is initial")
        self.__initialConnect()

    def __initialConnect(self):
        self.connect = mysql.connect(
            host = infoConnect["host"],
            database = infoConnect["database"],
            user = infoConnect["user"],
            password = infoConnect["password"],
            port = infoConnect["port"]
        )

    # end setCursor()

    """
    def testCon(self):
        with mysql.connect(
                host='localhost',
                database='filmcompany',
                user='ttknp',
                password='12345',
                port=3306
        ) as connect:
            # # cursor object
            with connect.cursor() as cursor:
                # fetching all the tables
                cursor.execute("show tables;")
                # printing all the tables
                for table in cursor:
                    self.__logApplication.log.debug(table)
                # finally closing the database connection
                cursor.close()
    """

"""
connectDatabase = ConnectDatabase()
cr : MySQLConnectionAbstract = connectDatabase.connect.cursor()
cr.execute("show tables;")
for table in cr:
    print(table)
cr.close()
"""
