import mysql.connector


class MyDatabase:
    def __init__(self, myDb):
        mydb = mysql.connector.connect(
            host="sql6.freesqldatabase.com",
            user="sql6635850",
            password="WWhxxlLRHb",
            database="sql6635850",
        )
