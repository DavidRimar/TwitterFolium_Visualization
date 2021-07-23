from sqlalchemy.types import ARRAY, Float, JSON, Text, TEXT
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, NUMERIC
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


class STDBSCAN_02_10800_3_SEM(Base):
    __tablename__ = 'stdbscan_02_10800_3_sem'
    id = Column(Integer, primary_key=True)  # Auto-generated ID
    stdbscan_id = Column(Integer, nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    convexhull = Column(Geometry('POLYGON'), nullable=True)
    st_asgeojson = Column(JSON, nullable=True)
    bristol_textclassifier_70_volumes = Column(Integer, nullable=True)
    all_volumes = Column(Integer, nullable=True)
    normalized_volumes = Column(NUMERIC(21, 19), nullable=True)
    scaled_vol_06 = Column(NUMERIC(21, 19), nullable=True)
    span_day = Column(Integer, nullable=True)
    span_hour = Column(Integer, nullable=True)
    scaled_vol_1 = Column(NUMERIC(21, 19), nullable=True)
    tfidf_bigrams = Column(JSON, nullable=True)
    tfidf_unigrams = Column(JSON, nullable=True)

    # Constructor

    def __repr__(self):
        return "<Tweet(stdbscan_id='{}', start_date='{}', end_date={}, convexhull={}, st_asgeojson={}, bristol_textclassifier_70_volumes={}, all_volumes={}, normalized_volumes{}, scaled_vol_06={}, span_day={}, span_hour={}, scaled_vol_1={}, tfidf_bigrams={}, tfidf_unigrams={})>".format(self.stdbscan_id, self.start_date, self.end_date, self.convexhull, self.st_asgeojson, self.bristol_textclassifier_70_volumes, self.all_volumes, self.normalized_volumes, self.scaled_vol_06, self.span_day, self.span_hour, self.scaled_vol_1, self.tfidf_bigrams, self.tfidf_unigrams)

    def as_dict(self):

        as_dict = {'stdbscan_id': self.stdbscan_id,
                   'start_date': self.start_date,
                   'end_date': self.end_date,
                   'convexhull': self.convexhull,
                   'st_asgeojson': self.st_asgeojson,
                   'bristol_textclassifier_70_volumes': self.bristol_textclassifier_70_volumes,
                   'all_volumes': self.all_volumes,
                   'normalized_volumes': self.normalized_volumes,
                   'scaled_vol_06': self.scaled_vol_06,
                   'span_day': self.span_day,
                   'span_hour': self.span_hour,
                   'scaled_vol_1': self.scaled_vol_1,
                   'tfidf_bigrams': self.tfidf_bigrams,
                   'tfidf_unigrams': self.tfidf_unigrams

                   }

        return as_dict


class COPY_OF_TXT(Base):
    __tablename__ = 'copy_of_txt'
    id = Column(Integer, primary_key=True)  # Auto-generated ID
    stdbscan_id = Column(Integer, nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    st_asgeojson = Column(JSON, nullable=True)
    scaled_vol_1 = Column(NUMERIC, nullable=True)
    span_day = Column(Integer)
    span_hour = Column(Integer, nullable=True)
    tfidf_bigrams = Column(JSON, nullable=True)
    tfidf_unigrams = Column(JSON, nullable=True)

    # Constructor

    def __repr__(self):
        return "<Tweet(stdbscan_id='{}', start_date='{}', end_date={}, st_asgeojson={}, scaled_vol_1={}, span_day={}, span_hour={}, tfidf_bigrams={}, tfidf_unigrams={})>".format(self.stdbscan_id, self.start_date, self.end_date, self.st_asgeojson, self.scaled_vol_1, self.span_day, self.span_hour, self.tfidf_bigrams, self.tfidf_unigrams)

    def as_dict(self):

        as_dict = {'stdbscan_id': self.stdbscan_id,
                   'start_date': self.start_date,
                   'end_date': self.end_date,
                   'st_asgeojson': self.st_asgeojson,
                   'scaled_vol_1': self.scaled_vol_1,
                   'span_day': self.span_day,
                   'span_hour': self.span_hours,
                   'tfidf_bigrams': self.tfidf_bigrams,
                   'tfidf_unigrams': self.tfidf_unigrams

                   }

        return as_dict
