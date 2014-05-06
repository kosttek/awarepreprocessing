__author__ = 'kosttek'
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
import datetime
import json


class DatabaseAccess():
    Base = declarative_base()
    def init_mysql(self,username,password,databasename):
        self.engine = create_engine('mysql://'+username+':'+password+'@localhost/'+databasename, echo=True)
        self._init()

    def init_sqlite(self,filename):
        self.engine = create_engine('sqlite:///'+filename)
        self._init()

    def _init(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.Base.metadata.create_all(self.engine)

        self.meta = MetaData()

    def getTables(self,tablelist):
        result = list()
        for tablename in tablelist:
            table = Table(tablename, self.meta, autoload=True, autoload_with=self.engine)
            result.append(table)
        return  result

    def queryAllFromTable(self,table):
        return self.session.query(table).all()