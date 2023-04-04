from sqlalchemy.orm import Session

import models, schemas


def get_regions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Region).offset(skip).limit(limit).all()


def get_region_by_position(db: Session, x: float, y: float):
    region = db.query(models.Region).filter(models.Region.min_x_position <= x, models.Region.max_x_position >= x, models.Region.min_y_position <= y, models.Region.max_y_position >= y).first()
    return region