from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

engine = create_engine('sqlite:///jcn.db')

Base = declarative_base()

conecta = engine.connect()

class Reunion(Base):
    __tablename__ = 'reunion'
    id = Column(Integer, primary_key=True)
    fecha = Column(String(8))

class Carrera(Base):
    __tablename__ = 'carrera'
    id = Column(Integer, primary_key=True)
    nroReunion = Column(Integer, ForeignKey='reunion.id')
    hora = Column(String(5))

class Remate(Base):
    __tablename__= 'remate'
    id = Column(Integer, primary_key=True)
    nroCarrera = Column(Integer, ForeignKey='carrera.id')

class Caballo(Base):
    __tablename__= 'caballo'
    id = Column(Integer, primary_key=True)
    monto = Column(Integer)
    nroCarrera = Column(Integer, ForeignKey='carrera.id')

