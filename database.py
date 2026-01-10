from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


dp_url = "postgresql://postgres:NewStrongPassword123@localhost:5432/Rajat"
engine = create_engine(dp_url)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)