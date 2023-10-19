from sqlalchemy import (
    Boolean,
    Column,
    create_engine,
    DateTime,
    delete,
    Float,
    ForeignKey,
    Integer,
    select,
    String,
    Time)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    Session,
    sessionmaker)
from typing import List, Optional


print('Declarando e definindo models')


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=True)
    salary: Mapped[float] = mapped_column(Float, nullable=True)
    phones: Mapped[List["Telephone"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r})"


class Telephone(Base):
    __tablename__ = "telephone"

    id: Mapped[int] = mapped_column("id", Integer, primary_key=True, nullable=False, autoincrement=True)
    country_code: Mapped[str] = mapped_column(String(6), nullable=True)
    local_code: Mapped[str] = mapped_column(String(6), nullable=False)
    number: Mapped[str] = mapped_column(String(32), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="phones")

    def __repr__(self):
        cc = '' if self.country_code is None or len(self.country_code) == 0 else self.country_code
        return f"({self.id}) {cc} ({self.local_code}) {self.number}"


print('Criando a base')
engine = create_engine("sqlite:///users", echo=True)
Base.metadata.create_all(engine)


print('Limpando as tabelas de teste')
with Session(engine) as session_0:
    print('Truncando a tabela Telephone')
    stmt_d_1 = delete(Telephone)
    session_0.execute(stmt_d_1)

    print('Truncando a tabela User')
    stmt_d_2 = delete(User)
    session_0.execute(stmt_d_2)


# Registrando 2 novos usuários

# Forma 1
print('Abrindo conexão com o banco na forma 1 - Parte 1')
with Session(engine) as session_1:
    print('Verificando se já existe usuário Anselmo')
    stmt_a = select(User).filter_by(name='Anselmo Lira')
    anselmo = session_1.scalars(stmt_a).first()
    print('Retorno da query:')
    print(anselmo)

    if anselmo is None:
        print('Criando usuário Anselmo')
        anselmo = User(
            name="Anselmo Lira",
            age=36,
            salary=7600.00
        )
        print('Usuário Anselmo não existe. Criando...')
        session_1.add(anselmo)
    else:
        print('Usuário Anselmo já existe no banco')
        print(f'\t- Anselmo possui {len(anselmo.phones)} telefones')

        print('Removendo as demais duplicatas de Anselmo')
        print(f'ID do usuário Anselmo achado anteriormente: {anselmo.id}')

        lista_anselmo_old = session_1.query(User).filter(User.name == 'Anselmo Lira', User.id != anselmo.id).all()
        #stmt_a_2 = select(User).filter_by(id != anselmo.id, name = 'Anselmo Lira')
        #lista_anselmo_old = session_1.scalars(stmt_a_2).all()
        print(f'Temos {len(lista_anselmo_old)} registros a remover')

        for ar in lista_anselmo_old:
            print(f'Apagando usuário {ar.id}')
            session_1.delete(ar)

    print('Verificando se já existe usuário Jorge')
    stmt_j = select(User).filter_by(name='Jorge Lira')
    jorge = session_1.scalars(stmt_j).first()
    if jorge is None:
        print('Criando usuário Jorge')
        jorge = User(
            name="Jorge Lira",
            age=60,
            salary=13400.00
        )
        print('Usuário Jorge não existe. Criando...')
        session_1.add(jorge)
    else:
        print('Usuário Jorge já existe no banco')
        print(f'\t- Jorge possui {len(jorge.phones)} telefones')

        print('Removendo as demais duplicatas de Jorge')
        print(f'ID do usuário Jorge achado anteriormente: {jorge.id}')

        lista_jorge_old = session_1.query(User).filter(User.name == 'Jorge Lira', User.id != jorge.id).all()
        print(f'Temos {len(lista_jorge_old)} registros a remover')

        for jr in lista_jorge_old:
            print(f'Apagando usuário {jr.id}')
            session_1.delete(jr)

    print('Criando telefone para usuário Anselmo')
    ta_1 = Telephone(country_code="55", local_code="11", number="96485-3026", user=anselmo)
    print('Criando telefone para usuário Jorge')
    tj_1 = Telephone(country_code="55", local_code="21", number="991636967", user=jorge)

    print('Adicionando telefones ao banco')
    session_1.add(ta_1)
    session_1.add(tj_1)
    # session.add_all([ta_1, tj_1])

    print('Fazendo o commit das alterações')
    session_1.commit()


print('Abrindo conexão com o banco na forma 1 - Parte 2')
with Session(engine) as session_2:
    print('Localizando usuário Jorge para adicionar novo telefone')
    stmt = select(User).filter_by(name='Jorge Lira')
    user_obj = session_2.scalars(stmt).first()

    print('Usuário localizado:')
    print(user_obj)

    print('Adicionando novo telefone ao usuário Jorge')
    telefone_novo = Telephone(
        country_code='55',
        local_code='21',
        number='98148-7636',
        user=user_obj)
    session_2.add(telefone_novo)
    print('Fazendo commit no banco')
    session_2.commit()


# Forma 2
'''
print('Abrindo conexão com o banco na forma 2')
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
db = session()

print('Criando usuário Anselmo')
anselmo = User(
    name='Anselmo Lira',
    age=36,
    salary=2600.00)
print('Criando usuário Jorge')
jorge = User(
    name='Jorge Lira',
    age=60,
    salary=13400.00)

print('Adicionando usuários ao banco')
db.add(anselmo)
db.add(jorge)

print('Criando telefones')
ta_1 = Telephone(
    country_code='55',
    local_code='11',
    number='96485-3026',
    user=anselmo)
tj_1 = Telephone(
    country_code='55',
    local_code='21',
    number='99163-6967',
    user=jorge)

print('Adicionando telefones ao banco')
db.add(ta_1)
db.add(tj_1)

print('Fazendo commit das mudanças')
db.commit()
'''