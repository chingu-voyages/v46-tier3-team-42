from sqlalchemy import  Column, Integer, String
from api_backend.db import Base


class Tip(Base):
    __tablename__ ="tips"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)