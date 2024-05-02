from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey,Boolean
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy.orm import declarative_base

datebase='credit_score'
engine = create_engine(f'postgresql+psycopg2://postgres:root@localhost/{datebase}')
if not database_exists(engine.url):
    with create_engine(f'postgresql+psycopg2://postgres:root@localhost').connect() as conn:
        
        conn.execute(Text("ALTER DATABASE template1 REFRESH COLLATION VERSION;"))
        # Do not substitute user-supplied database names here.
        conn.execute(f"CREATE DATABASE {datebase}")

print(database_exists(engine.url))
conn = engine.connect()



Base = declarative_base()


class PeopleInfo(Base):
    __tablename__ = 'PeopleInfo'
    id = Column(Integer, primary_key=True)
    fio = Column(String, nullable=False)
    active_credit_size = Column(Integer)
    co_borrower_size = Column(Integer)
    co_credit_peoples = Column(Integer)
    poruch = Column(Boolean)
    children_count = Column(Integer)
    children_aliment_count = Column(Integer)
    marriage = Column(Boolean)
    creditInfo = Column(Integer, ForeignKey('CreditInfo.id'),nullable=False)
    salary= Column(Integer, ForeignKey('Salary.id'), nullable=False)


class Salary(Base):
    __tablename__ = 'Salary'

    id = Column(Integer, primary_key=True)
    sallary= Column(Integer)
    clear_sallary= Column(Integer)

class CreditStatus(Base):
    __tablename__ = 'CreditStatus'

    id = Column(Integer, primary_key=True)
    status = Column(String, nullable=False)

class CreditInfo(Base):
    __tablename__ = 'CreditInfo'
    id = Column(Integer, primary_key=True)
    credit_size= Column(Integer)
    period = Column(Integer)
    max_size = Column(Integer)
    status = Column(Integer, ForeignKey('CreditStatus.id'),nullable=False)