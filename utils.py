from sqlalchemy import engine


from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

def bd():
    engine = create_engine('sqlite:///jcn.db')
    conecta = engine.connect()
    Session = sessionmaker(bind=conecta)
    sess = Session()
    return sess