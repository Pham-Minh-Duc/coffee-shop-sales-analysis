import pandas as pd
from .db import get_db_engine

def extract_data(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        df = pd.read_json(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        df = pd.read_excel(file_path)
    
    return df

def extract_data_from_db(table_name, db_type, query=None):
    if db_type is None:
        engine = get_db_engine('raw')
    else:
        engine = get_db_engine(db_type)

    if query is None:
        query = f"SELECT * FROM {table_name}"
    
    df = pd.read_sql(query, con=engine)
    return df


def transform_data():
    return

def load_data(df, table_name, db_type, if_exists='replace'):
    engine = get_db_engine(db_type=db_type)
    df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)

    