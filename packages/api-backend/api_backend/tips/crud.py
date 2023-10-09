from sqlalchemy.orm import Session
from tips.models import Tip


def get_all_tips(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Tip).offset(skip).limit(limit).all()


def get_tip_by_id(db: Session, tip_id: int):
    return db.query(Tip).filter(Tip.id == tip_id).first()
