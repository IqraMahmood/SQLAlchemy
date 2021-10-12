from sqlalchemy import create_engine
import pandas as pd


class SqlalchemyOop:
    def return_engine(self, connection_string):
        self.engine = create_engine(connection_string)
        return self.engine

    def database_connection(self):
        self.connection = self.engine.connect()

    def select_query(self, query):
        self.x = pd.read_sql(query, self.connection)
        return self.x

    def get_tables(self):
        return self.engine.table_names()

    def df(self):
        self.df = pd.DataFrame(self.x)
        return self.df

    def get_duplicates(self):
        z = self.df
        y = z.copy()
        analysis_abc = pd.concat([z, y])
        analysis_abc.to_sql('analysis_abc', con=self.engine)
        self.connection.close()
