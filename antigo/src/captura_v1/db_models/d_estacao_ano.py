from .db_base import SQLA_Base
from sqlalchemy import (
    Integer,
    String)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship)
from typing import List, Optional


class SA_D_EstacaoAno(SQLA_Base):
    __tablename__ = 'd_estacao_ano'

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, nullable=False, autoincrement=True)
    nome_estacao: Mapped[str] = mapped_column(String(20), nullable=False)
    medidas: Mapped[List["SA_F_Tempo"]] = relationship(back_populates="estacao_ano", cascade="all, delete-orphan")

    def __repr__(self):
        return f'({self.id}) {self.nome_estacao}'


class D_EstacaoAno:
    def __init__(self, id: int, nome_estacao: str):
        self.id = d_id
        self.nome_estacao = nome_estacao
