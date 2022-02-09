from sqlalchemy import create_engine
import pandas as pd
import psycopg2





class Database:
    def __init__(self,db):
        """
        :param db: name of a database to connect
        """
        self.db = db
        self.engine = create_engine(f'postgresql+psycopg2://user:password@host/{self.db}')
        self.connection = self.engine.connect()

    def queryData(self, query):
        """
        :param query(string): postgres query
        :return: this functions returns a string of pandas dataframe result of postgres query
        """
        df= pd.read_sql(query,self.connection)
        print(df.head(20).to_string())

    def createTable(self,df,name):
        """
        :param df(string): dataframe to convert
        :param name(string): name of the table to be created
        :return: this function return a new table if {name} not exists, or insert row in the table  if exists
        """
        df.to_sql(name,schema='public', con=self.engine,index=False,if_exists='append')






