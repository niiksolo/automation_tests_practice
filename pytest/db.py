from sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from configuration import Connection_row

Model - declarative_base(name='Model')

engine = create_engine(
    Connection_row
)

session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False
)

session = Session
