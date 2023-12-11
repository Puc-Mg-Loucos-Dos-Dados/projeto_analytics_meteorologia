from db_models import (
    SA_D_Data,
    SA_D_DiaNoite,
    SA_D_EstacaoAno,
    SA_D_Hora,
    SA_F_Tempo,
    SQLA_Base)
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


print('Criando a base')
engine = create_engine(f'mysql+pymysql://app:app123@127.0.0.1:3306/analytics_weather_db', echo=True)
SQLA_Base.metadata.create_all(engine)


print('Limpando as tabelas do banco')
with Session(engine) as session_0:
    print('Limpando a tabela F_Tempo')
    lst_f_tempo = session_0.query(SA_F_Tempo).all()
    for i1 in lst_f_tempo:
        session_0.delete(i1)

    print('Limpando a tabela D_Hora')
    lst_d_hora = session_0.query(SA_D_Hora).all()
    for i2 in lst_d_hora:
        session_0.delete(i2)

    print('Limpando a tabela D_DiaNoite')
    lst_d_dia_noite = session_0.query(SA_D_DiaNoite).all()
    for i3 in lst_d_dia_noite:
        session_0.delete(i3)

    print('Limpando a tabela D_EstacaoAno')
    lst_d_estacao_ano = session_0.query(SA_D_EstacaoAno).all()
    for i4 in lst_d_estacao_ano:
        session_0.delete(i4)

    print('Limpando a tabela D_Data')
    lst_d_data = session_0.query(SA_D_Data).all()
    for i5 in lst_d_data:
        session_0.delete(i5)

    session_0.commit()


print('Registrando as estações do ano')
with Session(engine) as session_1:
    print('Verificando se já existe estação Primavera')
    stmt_a = select(SA_D_EstacaoAno).filter_by(nome_estacao='Primavera')
    primavera = session_1.scalars(stmt_a).first()

    if primavera is None:
        primavera = SA_D_EstacaoAno(nome_estacao='Primavera')
        session_1.add(primavera)
    else:
        lista_primavera_old = session_1.query(SA_D_EstacaoAno).filter(SA_D_EstacaoAno.nome_estacao == 'Primavera', SA_D_EstacaoAno.id != primavera.id).all()
        for p_old in lista_primavera_old:
            session_1.delete(p_old)

    print('Verificando se já existe estação Verão')
    stmt_b = select(SA_D_EstacaoAno).filter_by(nome_estacao='Verão')
    verao = session_1.scalars(stmt_b).first()

    if verao is None:
        verao = SA_D_EstacaoAno(nome_estacao='Verão')
        session_1.add(verao)
    else:
        lista_verao_old = session_1.query(SA_D_EstacaoAno).filter(SA_D_EstacaoAno.nome_estacao == 'Verão', SA_D_EstacaoAno.id != verao.id).all()
        for v_old in lista_verao_old:
            session_1.delete(v_old)

    print('Verificando se já existe estação Outono')
    stmt_c = select(SA_D_EstacaoAno).filter_by(nome_estacao='Outono')
    outono = session_1.scalars(stmt_c).first()

    if outono is None:
        outono = SA_D_EstacaoAno(nome_estacao='Outono')
        session_1.add(outono)
    else:
        lista_outono_old = session_1.query(SA_D_EstacaoAno).filter(SA_D_EstacaoAno.nome_estacao == 'Outono', SA_D_EstacaoAno.id != outono.id).all()
        for o_old in lista_outono_old:
            session_1.delete(o_old)

    print('Verificando se já existe estação Inverno')
    stmt_d = select(SA_D_EstacaoAno).filter_by(nome_estacao='Inverno')
    inverno = session_1.scalars(stmt_d).first()

    if inverno is None:
        inverno = SA_D_EstacaoAno(nome_estacao='Inverno')
        session_1.add(inverno)
    else:
        lista_inverno_old = session_1.query(SA_D_EstacaoAno).filter(SA_D_EstacaoAno.nome_estacao == 'Inverno', SA_D_EstacaoAno.id != inverno.id).all()
        for i_old in lista_inverno_old:
            session_1.delete(i_old)

    print('Fazendo o commit das alterações')
    session_1.commit()
