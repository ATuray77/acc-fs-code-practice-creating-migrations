from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String(55))
    
    def __repr__(self):
        return f"\n<User" \
            + f"id={self.id}, " \
            + f"username={self.username}, " \
            + f"email={self.emal}," \
            + ">"