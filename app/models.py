from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Region(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    min_x_position = Column(Integer, index=True)
    max_x_position = Column(Integer, index=True)
    min_y_position = Column(Integer, index=True)
    max_y_position = Column(Integer, index=True)

    islands = relationship("Island", back_populates="region")


class Island(Base):
    __tablename__ = "islands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"))

    region = relationship("Region", back_populates="islands")