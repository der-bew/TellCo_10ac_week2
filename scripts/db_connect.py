import psycopg2
import pandas as pd
from sqlalchemy import create_engine

class PostgresDBConnector:
    def __init__(self, db_url):
        """
        Initializes the database connector with the provided database URL.
        
        :param db_url: The URL of the PostgreSQL database.
        """
        self.engine = create_engine(db_url)
        self.connection = self.engine.connect()

    def query_to_dataframe(self):
        """
        Executes a SQL query and returns the result as a pandas DataFrame.
        
        :return: A pandas DataFrame containing the query results.
        """
    
        return pd.read_sql_query("SELECT * FROM xdr_data", self.engine)

    def close_connection(self):
        """
        Closes the database connection.
        """
        self.connection.close()