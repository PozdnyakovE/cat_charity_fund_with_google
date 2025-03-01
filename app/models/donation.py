from sqlalchemy import Column, ForeignKey, Integer, Text

from app.core.db import DonationsBase


class Donation(DonationsBase):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
