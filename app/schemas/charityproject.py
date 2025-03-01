from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, validator
from pydantic.types import PositiveInt


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[PositiveInt]


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt = Field(...)


class CharityProjectDB(CharityProjectCreate):
    id: int
    fully_invested: bool
    invested_amount: int
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class CharityProjectUpdate(CharityProjectBase):

    class Config:
        extra = Extra.forbid

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Название не может быть пустым!')
        return value
