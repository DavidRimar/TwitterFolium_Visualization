from sqlalchemy.types import ARRAY, Float, JSON, Text, TEXT
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.types import ARRAY, Float
from geoalchemy2 import Geometry

Base = declarative_base()

"""
Tweet Class (extends Base class)
Representation of the data schema of the tables related to
the 'Bristol riots' event in the PostgreSQL.
"""


class GRID_11_5(Base):
    __tablename__ = 'grid_uk'
    row = Column(Integer)
    col = Column(Integer)
    geom = Column(Geometry('POLYGON'))
    id = Column(Integer, primary_key=True)  # Auto-generated ID
    st_asgeojson = Column(JSON)

    # Constructor

    def __repr__(self):
        return "<Tweet(row='{}', col='{}', geom={}, id={}, st_asgeojson={})>".format(self.row, self.col, self.geom, self.id, self.st_asgeojson)

    def as_dict(self):

        as_dict = {'row': self.row,
                   'col': self.col,
                   'geom': self.geom,
                   'id': self.id,
                   'st_asgeojson': self.st_asgeojson}

        return as_dict
