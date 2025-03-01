from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.donation import Donation
from app.models.user import User


class CRUDDonation(CRUDBase):
    async def get_by_user(
            self,
            user: User,
            session: AsyncSession
    ) -> list[Donation]:
        all_user_donations = select(Donation).where(
            Donation.user_id == user.id
        )
        donations = await session.execute(all_user_donations)
        donations = donations.scalars().all()
        return donations


donation_crud = CRUDDonation(Donation)
