from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra
from pydantic.types import PositiveInt


class DonationBase(BaseModel):
    comment: Optional[str]
    full_amount: PositiveInt

    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBase):
    pass


class UserDonationDB(DonationCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationDB(UserDonationDB):
    fully_invested: bool
    close_date: Optional[datetime]
    user_id: int
    invested_amount: int

    class Config:
        orm_mode = True
