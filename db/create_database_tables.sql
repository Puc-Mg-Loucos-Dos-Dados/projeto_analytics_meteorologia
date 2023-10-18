create database if not exists "analytics-weather-db";
use "analytics-weather-db";

create table D_EstacaoAno (
    d_id int not null auto_increment primary key,
    nome_estacao varchar(20) not null
);

create table D_Data(
    d_id int not null auto_increment primary key,
    ano int not null,
    mes int not null,
    dia int not null
);

create table D_Hora(
    d_id int not null auto_increment primary key,
    id_data int not null,
    hora int not null,
    minuto int not null,
    foreign key (id_data) references D_Data(d_id) on update cascade on delete cascade
);

create table D_DiaNoite(
    d_id int not null auto_increment primary key,
    momento_dia varchar(10) not null
);

create table F_Tempo(
    d_estacao_ano int not null,
    d_data int not null,
    d_hora int not null,
    d_dia_noite int not null,
    temperatura decimal(5, 2) not null,
    umidade decimal(5, 2) not null,
    pressao_atmosferica decimal(7, 2) default null,
    visibilidade decimal(5, 2) default null,
    hora_coleta datetime default CURRENT_TIMESTAMP,
    primary key (d_estacao_ano, d_data, d_hora, d_dia_noite),
    foreign key (d_estacao_ano) references D_EstacaoAno(d_id) on update cascade on delete cascade,
    foreign key (d_data) references D_Data(d_id) on update cascade on delete cascade,
    foreign key (d_hora) references D_Hora(d_id) on update cascade on delete cascade,
    foreign key (d_dia_noite) references D_DiaNoite(d_id) on update cascade on delete cascade
);