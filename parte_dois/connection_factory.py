import mysql.connector


from settings import *

class ConnectionFactory:
    @staticmethod
    def get_connection():
        connection = mysql.connector.connect(
            host=HOST,
            database=DATABASE,
            user=USER,
            password=PASSWORD
        )
        return connection
