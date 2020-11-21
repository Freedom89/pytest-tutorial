from pydantic import BaseModel
from enum import Enum


class Category(str, Enum):
    A: str = "A"
    B: str = "B"
    C: str = "C"


class RawData(BaseModel):
    x: int
    y: int
    z: int
    category: Category


class IntFeat(BaseModel):
    x: int
    x_times_y: int
    y_div_z: float
    cat_in_AB: bool


class Response(Enum):
    value0: str = "value0"
    value1: str = "value1"
    value2: str = "value2"
    value3: str = "value3"
    value4: str = "value4"
