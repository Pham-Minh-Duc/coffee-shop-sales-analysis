import os
import urllib.parse
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

def get_db_engine(db_type):
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    safe_password = urllib.parse.quote_plus(password)
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    database = os.getenv('DB_NAME')

    if db_type == 'raw':
        database = os.getenv('DB_DL')
    else:
        database = os.getenv('DB_DWH')

    connection_string = f"mysql+pymysql://{username}:{safe_password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)

    return engine
