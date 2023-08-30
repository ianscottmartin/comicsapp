# from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# from sqlalchemy import ForeignKey, Table
# from sqlalchemy.orm import relationship


# Base = declarative_base()

#comic_user = Table(
  #  "comic_user",
  #  Base.metadata,
   # Column("id", Integer, primary_key=True),
   # Column("comic_id", ForeignKey("comic.id")),
   # Column("user_id", ForeignKey("user.id")),
#)

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     username = Column(String, unique=True)
#     email = Column(String)

# #comics = relationship("Comic", secondary="comic_user")   
# comics= relationship("Comic", backref="owner")  
    
 
# class Comic(Base):
#     __tablename__ = 'comics'

#     id = Column(Integer, primary_key=True)
#     title = Column(String, unique=True)
#     issue_number = Column(Integer)
#     publisher = Column(String)   
    
# #users = relationship("User", secondary="comic_user")
# user_id = Column(Integer, ForeignKey("users.id"))

# print(User)

from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserComicAssociation(Base):
    __tablename__ = 'user_comic_association'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    comic_id = Column(Integer, ForeignKey('comics.id'), primary_key=True)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    comics = relationship("Comic", secondary="user_comic_association")

class Comic(Base):
    __tablename__ = 'comics'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    publisher = Column(String)
    users = relationship("User", secondary="user_comic_association")

