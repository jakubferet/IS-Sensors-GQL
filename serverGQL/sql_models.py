import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Text, BigInteger, Integer, DateTime, ForeignKey, Sequence, Table

from connection import engine


BaseModel = declarative_base()

unitedSequence = Sequence('all_id_seq')

ProductionModel = Table('production', BaseModel.metadata,
        Column('id', BigInteger, Sequence('all_id_seq'), primary_key=True),
        Column('manufacturer_id', ForeignKey('manufacturers.id'), primary_key=True),
        Column('category_id', ForeignKey('categories.id'), primary_key=True)
)

class SensorModel(BaseModel):
    __tablename__ = 'sensors'
    
    id = Column(BigInteger, Sequence('all_id_seq'), primary_key=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(Text)
    lastchange = Column(DateTime, default=datetime.datetime.now)

    manufacturer_id = Column(ForeignKey('manufacturers.id'))
    manufacturer = relationship('ManufacturerModel', back_populates='sensors')

    category_id = Column(ForeignKey('categories.id'))
    category = relationship('CategoryModel', back_populates='sensors')
        
class ManufacturerModel(BaseModel):
    __tablename__ = 'manufacturers'
    
    id = Column(BigInteger, Sequence('all_id_seq'), primary_key=True)
    name = Column(String)
    description = Column(Text)
    lastchange = Column(DateTime, default=datetime.datetime.now)

    sensors = relationship('SensorModel', back_populates='manufacturer')
    categories = relationship('CategoryModel', secondary=ProductionModel, back_populates='manufacturers')

class CategoryModel(BaseModel):
    __tablename__ = 'categories'
    
    id = Column(BigInteger, Sequence('all_id_seq'), primary_key=True)
    name = Column(String)
    lastchange = Column(DateTime, default=datetime.datetime.now)

    sensors = relationship('SensorModel', back_populates='category')
    manufacturers = relationship('ManufacturerModel', secondary=ProductionModel, back_populates='categories')

#BaseModel.metadata.drop_all(engine)
BaseModel.metadata.create_all(engine)