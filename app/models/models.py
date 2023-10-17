from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry


DATABASE_URL = "postgresql://admin:admin@db:5432/admin"

engine = create_engine(DATABASE_URL)

Base = declarative_base()


class Apartments(Base):
    __tablename__ = "apartments"

    id = Column(Integer, primary_key=True, index=True)
    geopos = Column(Geometry('Point', srid=4326))
    apartments = Column(Integer)
    price = Column(Integer)
    year = Column(Integer)


class Hex(Base):
    __tablename__ = "hex"

    id = Column(Integer, primary_key=True, index=True)
    hex = Column(String)


Base.metadata.create_all(bind=engine)
