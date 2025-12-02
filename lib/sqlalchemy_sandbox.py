#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create the Base class for our ORM models
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f"<Student id={self.id} name={self.name}>"

# Run schema creation only when executed as a script
if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)
    print("students.db created with 'students' table.")
