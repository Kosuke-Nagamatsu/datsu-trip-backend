from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud, models, schemas, seed
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS:リクエストを許可するorigin
origins = [
    "https://kosuke-nagamatsu.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=origins,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello！"}


@app.get("/regions", response_model=List[schemas.Region])
def read_regions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_regions = crud.get_regions(db, skip=skip, limit=limit)
    return db_regions


@app.get("/regions/", response_model=schemas.Region)
def read_region(x: str, y: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  x=float(x)
  y=float(y)
  db_region=crud.get_region_by_position(db, x=x, y=y)
  if db_region is None:
    raise HTTPException(status_code=404, detail="Region not found")
  return db_region


# seedデータ用
@app.post("/seed")
def create_seed_data(db: Session = Depends(get_db)):
    seed.create(db)
    return {"message": "Seed data created."}