from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *
import psycopg2
from psycopg2 import OperationalError

connection_url = 'postgresql://admin:1234@localhost:5433/suspicious_emails_db'
engine = create_engine(connection_url)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def init_db():
    import models
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


init_db()
