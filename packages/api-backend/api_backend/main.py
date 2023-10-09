from fastapi import FastAPI
from db_config import Base, engine

from tips.routes import tip_router


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tip_router, prefix="", tags=["tips"])


@app.get("/")
def test():
    return {"Hello": "World"}