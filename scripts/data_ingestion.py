import os
import logging
from sqlalchemy import create_engine
import config

# You can initialize the engine here if you plan to use the same connection string for all operations.
engine = create_engine(config.conn_str)

def insert_data_into_db(df, file):
    table_name = os.path.splitext(file)[0]
    try:
        df.to_sql(table_name, engine, index=False, if_exists='replace', schema='dbo')
        logging.info(f"Data successfully inserted into {table_name}.")
    except Exception as e:
        logging.error(f"Error inserting data into {table_name}: {e}")
