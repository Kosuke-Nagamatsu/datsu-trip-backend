from pydantic import BaseModel


class Island(BaseModel):
    id: int
    name: str
    region_id: int

    class Config:
        orm_mode = True


class Region(BaseModel):
    id: int
    name:str
    min_x_position: int
    max_x_position: int
    min_y_position: int
    max_y_position: int
    islands: list[Island] = []

    class Config:
        orm_mode = True