import psycopg2


class Connection:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="InventorySystemDB",
            user="joshua",
            password="password",
            host="localhost",
            port="5433"
        )

    def __del__(self):
        self.connection.close()

    def getConnection(self):
        return self.connection

    def getNewCursor(self):
        return self.connection.cursor()
