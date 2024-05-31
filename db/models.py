from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Director(Base):
    __tablename__ = 'director'

    id = Column('id' ,Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    film = relationship('Film', back_populates='director', cascade='all, delete')


class Film(Base):
    id = Column('id' ,Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    director = relationship('Director', back_populates='film')
    director_id = ForeignKey('director.id')


