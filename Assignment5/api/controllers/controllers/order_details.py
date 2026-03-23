from fastapi import Response, status
from sqlalchemy.orm import Session
from .. import models, schemas

def create(db: Session, order_detail: schemas.OrderDetailCreate):
    db_detail = models.OrderDetail(
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id,
        quantity=order_detail.quantity
    )
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail

def read_all(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id).first()

def update(db: Session, detail_id: int, order_detail: schemas.OrderDetailUpdate):
    db_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    update_data = order_detail.dict(exclude_unset=True)
    db_detail.update(update_data, synchronize_session=False)
    db.commit()
    return db_detail.first()

def delete(db: Session, detail_id: int):
    db_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    db_detail.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
