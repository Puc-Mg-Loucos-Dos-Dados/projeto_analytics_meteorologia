from .d_data import D_Data
from .db_base import SQLA_Base
from datetime import datetime, time
from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    Time)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship)
from sqlalchemy.sql import func
from typing import List


class SA_D_Hora(SQLA_Base):
    __tablename__ = 'd_hora'

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, nullable=False, autoincrement=True)
    id_data: Mapped[int] = mapped_column(ForeignKey('d_data.id'), nullable=False)
    hora: Mapped[time] = mapped_column(Time, nullable=False)
    criado_em: Mapped[datetime] = mapped_column(DateTime(timezone=False), server_default=func.now())
    medidas: Mapped[List["SA_F_Tempo"]] = relationship(back_populates="hora", cascade="all, delete-orphan")

    data: Mapped['SA_D_Data'] = relationship(back_populates="horas")


class D_Hora:
    def __init__(self, d_id: int, data: D_Data, hora: int, minuto: int):
        self.d_id = d_id
        self.data = data
        self.hora = hora
        self.minuto = minuto
