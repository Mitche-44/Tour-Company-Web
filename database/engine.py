from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///tour_company.db"

engine = create_engine(DATABASE_URL, echo=True)

# create a Session class
Session = sessionmaker(bind=engine)
Base = declarative_base()