from datetime import datetime
from datetime import time
from sqlalchemy import inspect
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()

#There will be atleast three classes for my week 8 final project. This class will be among the classes for my week 8
#project

class Person(Base):
    
    def __init__(self, firstname, lastname, ssn, birthdate):
        self.firstname = firstname
        self.lastname = lastname
        self.ssn = ssn
        self.birthdate = birthdate
        
    
    __tablename__ = 'persons'
    
    id = Column(Integer, primary_key = True)
    firstname =  Column(String)
    lastname = Column(String)
    ssn = Column(String)
    birthdate = Column(DateTime) 
    
    def __repr__(self):
        return "<persons(firstname={0}, lastname={1}, ssn={2}, birthdate={3})>".format(self.firstname, self.lastname, self.ssn, self.birthdate)
    
"""
This is in prep for week 8. This is not working yet. Please ignore this block.

class Duration(Base):
    
    def __init__(self, memberId, date, signIn, signOut):
        self.memberID = memberId
        self.date = date
        self.signIn = signIn
        self.signOut = signOut
        
    __tablename__ = 'durations'
    
    id = Column(Integer, primary_key = True)
    memberId = Column(Integer, ForeignKey("persons.id"), nullable="False")
    date = Column(DateTime)
    signIn = Column(DateTime)
    signOut = Column(DateTime)
    
    dura_rel = relationship("Person", back_populates="durations")
    
    def __repr__(self):
        return "<duration(memberID={0}, date={1}, signIn={2}, signOut={3})>".format(self.memberId, self.date, self.signIn, self.signOut)
    
Person.durations = relationship(
    "Duration", back_populates="dura_rel")
    
"""

          
    
        
    
    
    
    

    
    

    
    
    