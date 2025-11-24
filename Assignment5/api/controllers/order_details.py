from sqlalchemy.orm import Session
from fastapi import Response, status
from api.models import models, schemas


def create(db: Session, od: schemas.OrderDetailCreate):
    db_od = models.OrderDetail(
        order_id=od.order_id,
        sandwich_id=od.sandwich_id,
        amount=od.amount,
    )
    db.add(db_od)
    db.commit()
    db.refresh(db_od)
    return db_od


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, od_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == od_id).first()


def update(db: Session, od_id: int, od: schemas.OrderDetailUpdate):
    db_od = db.query(models.OrderDetail).filter(models.OrderDetail.id == od_id)
    update_data = od.dict(exclude_unset=True)
    db_od.update(update_data, synchronize_session=False)
    db.commit()
    return db_od.first()


def delete(db: Session, od_id: int):
    db_od = db.query(models.OrderDetail).filter(models.OrderDetail.id == od_id)
    db_od.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
