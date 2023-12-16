import pandas as pd

from sqlalchemy import create_engine

def get_connections(host, user, password, database, port = None):
    connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)
    try:
        connection = engine.connect()
        print("connection successful to mysql database")
        connection.close()
    except Exception as e:
        print(f"Error connecting: {e}")
    return engine

def ingest_to_database(conn, table_name):
    file_path = "data/london_smart_meters/weather_daily_darksky.csv"
    df_itr = pd.read_csv(file_path, iterator=True, chunksize=10000)
    df = next(df_itr)
    df.head(0).to_sql(name=table_name, con=conn, if_exists="replace")
    print("Header Inserted")
    df.to_sql(name=table_name, if_exists="append", con=conn)
    print("First Itration Inserted")

    try:
        while True:
            df = next(df_itr)
            # df = df[~(df["LCLid"] == "LCLid")]
            df.to_sql(name=table_name, if_exists="append", con=conn)
            print("Chunck inserted")
    except StopIteration as e:
        print(f"All itrations inserted so {e} in place ")