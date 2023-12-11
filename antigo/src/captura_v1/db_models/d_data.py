from .db_base import SQLA_Base
from datetime import date, datetime
from sqlalchemy import (
    Date,
    DateTime,
    Integer,
    String,
    Time)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship)
from sqlalchemy.sql import func
from typing import List, Optional


class SA_D_Data(SQLA_Base):
    __tablename__ = 'd_data'

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, nullable=False, autoincrement=True)
    data: Mapped[date] = mapped_column(Date, nullable=False)
    dia_semana: Mapped[str] = mapped_column(String(30), nullable=True)
    criado_em: Mapped[datetime] = mapped_column(DateTime(timezone=False), server_default=func.now())
    medidas: Mapped[List["SA_F_Tempo"]] = relationship(back_populates="data", cascade="all, delete-orphan")
    horas: Mapped[List["SA_D_Hora"]] = relationship(back_populates="data", cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.id} {self.data.strftime("%d/%m/%Y")}'


class D_Data:
    def __init__(self, id: int, data: date, dia_semana: str):
        self.id = id
        self.data = data
        self.dia_semana = dia_semana
