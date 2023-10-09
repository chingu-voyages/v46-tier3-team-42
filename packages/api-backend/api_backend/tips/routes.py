from fastapi import APIRouter, HTTPException, Depends
from tips.schemas import EnergySavingTip
from db_config import SessionLocal
from sqlalchemy.orm import Session
from typing import List
from tips import crud


tip_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@tip_router.get("/tip", response_model=EnergySavingTip)
def get_energy_saving_tip(tip_id: int, db: Session = Depends(get_db)):
    result = crud.get_tip_by_id(db, tip_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Tip not found")
    return EnergySavingTip(tip_id=result.id, title=result.title, description=result.description)


@tip_router.get("/tips", response_model=List[EnergySavingTip])
async def get_energy_saving_tips(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    result = crud.get_all_tips(db, skip, limit)
    return [{"tip_id": tip.id, "title": tip.title, "description": tip.description} for tip in result]


# TODO complete funcion
# @tip_router.get("/user/{user_id}/personalized_tips", response_model=List[EnergySavingTip])
# def get_personalized_energy_saving_tips(user_id: int):
#     # Fetch user's utility bill data from the database
#     user_bills = get_user_utility_bills(user_id)

#     # Analyze the data and generate personalized tips
#     personalized_tips = analyze_user_data(user_bills)

#     return personalized_tips
