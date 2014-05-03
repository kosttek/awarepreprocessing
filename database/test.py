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

Base = declarative_base()
#example
# class RawLog(Base):
#     __tablename__ = 'rawlogs'
#     id = Column(Integer,Sequence("rawlog_id_seq"), primary_key=True)
#     log = Column(String, nullable=False)
#     date = Column(DateTime, nullable=False)
#     clog_id = Column(Integer, ForeignKey('compressedlogs.id'))


if __name__  == "__main__":
    #its only for test purpose
    #dialect+driver://username:password@host:port/database
    engine = create_engine('mysql://aware:awarepass@localhost/aware', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    meta = MetaData()
    Network = Table('network', meta, autoload=True, autoload_with=engine)

    print Network.name
    print [c.name for c in Network.columns]

    i = 0

    for nw in  session.query(Network).all():
        i+=1
        print type(nw)
        print(datetime.datetime.fromtimestamp(int(nw.timestamp/1000)).strftime('%Y-%m-%d %H:%M:%S'))
        if i > 30 : break

    print type(session.query(Network).first())
