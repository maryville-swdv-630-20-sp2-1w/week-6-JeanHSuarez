import unittest
from datetime import datetime
from datetime import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect
from week6 import Person
from week6 import Base
#from week6 import Duration


class DatabaseTests(unittest.TestCase):
    #Test for Database setup and teardown.
    
    def setUp(self):
        
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
                        
    def tearDown(self):
        try:
            Person.__table__.drop(self.engine)

        except:
            pass
    #Test if database exist or not. table/s will be inside the list. Additional tables will be added in the
    #list in a stack manner.
    def test_check_created_tables(self):
        ins = inspect(self.engine)
        self.assertEqual(ins.get_table_names(),['persons'])
        
      
      #test for storing and retrieving objects in the database
        
class UserTableTests(unittest.TestCase):
    
    def setUp(self):
        
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
                              
    def tearDown(self):
        try:
            Person.__table__.drop(self.engine)
#            Duration.__table__.drop(self.engine)

        except:
            pass
        
    def test_input_data(self):
        
        person_one = Person("Jean", "Suarez", "123001234", datetime.fromisoformat('1980-12-10'))
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.add(person_one)
        
        
        person = session.query(Person).filter(Person.firstname =='Jean').filter(Person.birthdate == datetime.fromisoformat('1980-12-10')).all()
        
        self.assertTrue(person[0].firstname == "Jean")
        
        
        
        
"""
This test is in prep for Week 8. Please ignore this block. This is not a working code yet. 

        duration_one = Duration("", datetime.fromisoformat('1980-12-10'), time(8,10,10), time(9,20,10))
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.add(duration_one)
        
        
        duration = session.query(Duration).filter(Duration.date == datetime.fromisoformat('1980-12-10')).all()
        
        self.assertTrue(duration[0].firstname == 1)
"""        
               
if  __name__=='__main__':
    unittest.main()