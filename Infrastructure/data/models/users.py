from sqlalchemy import Column, Integer, String, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users( Base ):
    __tablename__ = 'users'
    
    id = Column( 'id', Integer, primary_key=True, unique=True )
    email_user = Column( String(40), nullable=False )
    name_user = Column( String(40), nullable=False )
    password_user = Column( String(255), nullable=False )
    url_photo_user = Column( String(255), nullable=False )

    @property
    def name(self):
        return self.__tablename__

    def __repr__(self) -> str:
        return '<User {}>'.format( self.name )