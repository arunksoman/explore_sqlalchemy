from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_URI = "mysql+pymysql://root:root@127.0.0.1/db_sqlalchemy_example"
engine = create_engine(
    DB_URI,
    encoding='utf-8'
)

db = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = db.query_property()
