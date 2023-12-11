import requests
import mysql.connector
from datetime import datetime, timedelta

# Dados de acesso ao banco de dados
user = 'admin'
password = 'Samoht123.'
host = 'pucminas.cz1qlmufl8xa.sa-east-1.rds.amazonaws.com'
#database = 'dw_salao_de_beleza' 
port = '3306' 

# Criando o banco de dados 

# Conectar ao banco de dados
db_connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
   #database=database,
    port=port
)
cursor = db_connection.cursor()

create_database_query = "CREATE DATABASE IF NOT EXISTS dw_salao_de_beleza;"
cursor.execute(create_database_query)
print("Criado com sucesso")

use_database_query = "USE dw_salao_de_beleza;"
cursor.execute(use_database_query)
print("Acessando o banco")

# Inserindo a query de criação do DB
insert_query_data = """ -- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: dw_salao_de_beleza
-- ------------------------------------------------------
-- Server version	8.0.34

--
-- Table structure for table `d_agenda`
--
-- Drop table if exists d_agenda;
DROP TABLE IF EXISTS d_agenda;

-- Create table if not exists d_agenda;
CREATE TABLE IF NOT EXISTS d_agenda (
    data_id DATE NOT NULL PRIMARY KEY,
    dia INT DEFAULT NULL,
    UNIQUE(data_id)	
);

-- Drop table if exists d_clima;
DROP TABLE IF EXISTS d_clima;

-- Create table if not exists d_clima;
CREATE TABLE IF NOT EXISTS d_clima (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    temperatura_min DOUBLE DEFAULT NULL,
    temperatura_max DOUBLE DEFAULT NULL,
    temperatura_tarde DOUBLE DEFAULT NULL,
    temperatura_noite DOUBLE DEFAULT NULL,
    temperatura_manha DOUBLE DEFAULT NULL,
    dia DATE NOT NULL,
    data_atual DATE NOT NULL,
    FOREIGN KEY (dia) REFERENCES d_agenda(data_id),
    UNIQUE (dia)
);


DROP TABLE IF EXISTS d_cliente;
create table if not exists d_cliente (
    id int unsigned not null  auto_increment,
    nome varchar(120) not null primary key,
    telefone varchar(45) default null
);

DROP TABLE IF EXISTS d_funcionario;
create table if not exists d_funcionario (
    id int unsigned primary key not null auto_increment,
    nome varchar(120) not null,
    cargo varchar(64) default null,
    telefone varchar(20) default null
);

drop table if exists d_servico;
CREATE TABLE d_servico (
    id int unsigned not null primary key auto_increment,
    nome varchar(120) not null,
    valor int DEFAULT 0
);

drop table if exists fato_pagamento;
create table if not exists fato_pagamento (
    id_cliente int unsigned not null,
    data_id date not null,
    id_funcionario int unsigned not null,
    id_servico int unsigned not null,
    valor_pago float default 0,
    primary key (id_cliente, data_id, id_funcionario, id_servico),
    foreign key FK_FatoPagamento_Cliente(id_cliente) references d_cliente(id),
    foreign key FK_FatoPagamento_Agenda(data_id) references d_agenda(data_id),
    foreign key FK_FatoPagamento_Funcionario(id_funcionario) references d_funcionario(id),
    foreign key FK_FatoPagamento_Servico(id_servico) references d_servico(id)
); """

print("Banco criado com sucesso!")

# Execute todas as consultas pendentes e recupere os resultados
cursor.fetchall()

# Faça o commit das alterações
db_connection.commit()

# Agora você pode executar um novo comando
cursor.execute(insert_query_data)
db_connection.commit()
