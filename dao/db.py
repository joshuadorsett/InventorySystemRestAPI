from sqlalchemy import create_engine, MetaData


class DB:
    def __init__(self):
        # choose which db to use, using sql_lite for easier testing
        PG_DATABASE_URI = 'postgres+psycopg2://joshuadorsett:password@localhost:5432/InventorySystemDB'
        SQL_LITE_URI = 'sqlite:///InventorySystemDB.db'
        self.connection = create_engine(SQL_LITE_URI)
        self.meta = MetaData()
