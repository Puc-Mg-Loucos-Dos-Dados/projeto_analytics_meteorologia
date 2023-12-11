from .d_data import D_Data
from .d_dia_noite import D_DiaNoite
from .d_estacao_ano import D_EstacaoAno
from .d_hora import D_Hora
from .db_base import SQLA_Base
from datetime import datetime
from sqlalchemy import (
    DateTime,
    Float,
    Integer,
    String,
    ForeignKey)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship)
from sqlalchemy.sql import func


class SA_F_Tempo(SQLA_Base):
    __tablename__ = 'f_tempo'

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, nullable=False, autoincrement=True)
    id_estacao_ano: Mapped[int] = mapped_column(ForeignKey("d_estacao_ano.id"), nullable=True)
    id_data: Mapped[int] = mapped_column(ForeignKey("d_data.id"), nullable=False)
    id_hora: Mapped[int] = mapped_column(ForeignKey("d_hora.id"), nullable=False)
    id_dia_noite: Mapped[int] = mapped_column(ForeignKey("d_dia_noite.id"), nullable=True)
    temperatura: Mapped[float] = mapped_column(Float, nullable=False)
    umidade: Mapped[float] = mapped_column(Float, nullable=True)
    pressao_atmosferica: Mapped[float] = mapped_column(Float, nullable=True)
    visibilidade: Mapped[float] = mapped_column(Float, nullable=True)
    vento: Mapped[float] = mapped_column(Float, nullable=True)
    criado_em: Mapped[datetime] = mapped_column(DateTime(timezone=False), server_default=func.now())

    estacao_ano: Mapped["SA_D_EstacaoAno"] = relationship(back_populates='medidas')
    data: Mapped["SA_D_Data"] = relationship(back_populates='medidas')
    hora: Mapped["SA_D_Hora"] = relationship(back_populates='medidas')
    dia_noite: Mapped['SA_D_DiaNoite'] = relationship(back_populates='medidas')



class F_Tempo:
    def __init__(self, data: D_Data, hora: D_Hora,
                 dia_noite: D_DiaNoite, estacao_ano: D_EstacaoAno):
        self.data = data
        self.hora = hora
        self.dia_noite = dia_noite
        self.estacao_ano = estacao_ano

    def to_json(self):
        pass
