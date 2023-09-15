#!/usr/bin/python3
"""
Class definition of a State with inheritance from Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """
    State Class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    # One-to-many relationship
    cities = relationship("City", backref="states", cascade="delete")
