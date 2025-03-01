from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession
    ) -> list[dict[str, str]]:
        charity_projects = await session.execute(
            select(
                [
                    CharityProject.name,
                    (func.julianday(CharityProject.close_date) -
                     func.julianday(CharityProject.create_date)
                     ).label('days_before_closed'),
                    CharityProject.description
                ]
                ).where(CharityProject.fully_invested).order_by(
                    'days_before_closed')
        )
        return charity_projects


charity_project_crud = CRUDCharityProject(CharityProject)
