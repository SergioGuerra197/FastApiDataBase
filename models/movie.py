from config.database import Base
from sqlalchemy import Column, Integer,String,Float

#Hereda de Base, se le indica que es un modelo de la base de datos
class Movie(Base):

    __tablename__ = 'movies'

    id = Column(Integer, primary_key = True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)