from fastapi import APIRouter, HTTPException
from api_backend.schemas.tips import EnergySavingTip
from typing import Any, List
from api_backend.models.tips import Tip
from api_backend.deps.db import CurrentAsyncSession
from api_backend.deps.users import CurrentUser
from sqlalchemy import func

router = APIRouter()


@router.get("/tip", response_model=EnergySavingTip)
async def get_energy_saving_tip_by_id(
    tip_id: int,
    session: CurrentAsyncSession,
    user: CurrentUser,
    ) -> Any:
    result = session.query(Tip).filter(Tip.id == tip_id).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Tip not found")
    return EnergySavingTip(tip_id=result.id, title=result.title, description=result.description)


@router.get("/all_tips", response_model=List[EnergySavingTip])
async def get_all_energy_saving_tips(
    session: CurrentAsyncSession,
    user: CurrentUser,
    skip: int = 0,
    limit: int = 100,
    ) -> Any:
    result = session.query(Tip).offset(skip).limit(limit).all()
    return [{"tip_id": tip.id, "title": tip.title, "description": tip.description} for tip in result]


# FIXME 
@router.get("/personalized_tips", response_model=List[EnergySavingTip])
async def get_personalized_energy_saving_tips(
    user_id: int,
    session: CurrentAsyncSession,
    user: CurrentUser,
    ) -> Any:

    total = session.query(func.count()).select_from(Tip).scalar()
    import random
    personalized_tips = get_energy_saving_tip_by_id(random.randint(0, total), session, user)

    # TODO
    # Fetch user's utility bill data from the database
    # Analyze the data and generate personalized tips

    return personalized_tips
