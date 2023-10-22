from .db_base import SQLA_Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class SA_D_DiaNoite(SQLA_Base):
    __tablename__ = 'd_dia_noite'

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, nullable=False, autoincrement=True)
    momento_dia: Mapped[str] = mapped_column(String(10), nullable=False)
    medidas: Mapped[List['SA_F_Tempo']] = relationship(back_populates="dia_noite", cascade="all, delete-orphan")

    def __repr__(self):
        return f'({self.id}) {self.momento_dia}'


class D_DiaNoite:
    def __init__(self, d_id: int, momento_dia: str):
        self.d_id = d_id
        self.momento_dia = momento_dia
