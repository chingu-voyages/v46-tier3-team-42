from pydantic import BaseModel


class UtilityBill(BaseModel):
    user_id: int
    month: str
    electricity_usage: float
    energ_cost: float


class EnergySavingTip(BaseModel):
    tip_id: int
    title: str
    description: str
