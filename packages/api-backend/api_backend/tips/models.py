from sqlalchemy import  Column, Integer, String
from db_config import Base


class Tip(Base):
    __tablename__ ="tips"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)