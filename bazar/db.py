from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
Session = sessionmaker()

class User(Base):
    __tablename__ = 'users'
    name = Column(String, primary_key=True)
    password = Column(String)
    salt = Column(String)
    opt = Column(String)


def create_session(container, connection_string):
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)
    return Session(bind=engine)

# vim: sts=4 sw=4 et si
