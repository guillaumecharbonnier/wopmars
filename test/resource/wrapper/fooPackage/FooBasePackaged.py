"""
Example of module documentation which can be
multiple-lined
"""
from sqlalchemy import Column, Integer, String

from wopmars.framework.database.Base import Base


class FooBasePackaged(Base):
    """
    Documentation for the class
    """
    __tablename__ = "FooBasePackaged"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    def __repr__(self):
        s = ""
        s += "<FooBasePackaged (id: %s; name: %s)>" % (self.id, self.name)
        return s
