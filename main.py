import pandas as pd
from database import Base, engine
from crud import add_dataframe
import typer


def create_db(file_path:str="./data/descs.csv", textcol:str="text"):
    Base.metadata.create_all(bind=engine)
    descs = pd.read_csv(file_path)
    descs.columns = ['text']
    add_dataframe(descs)
    print("Create Database Success")
    
    
if __name__ == "__main__":
    typer.run(create_db)