create database if not exists "analytics-weather-db";
use "analytics-weather-db";

create table D_EstacaoAno (
    id int not null auto_increment primary key,
    nome_estacao varchar(20) not null
);

create table D_Data(
    id int not null auto_increment primary key,
    data date not null,
    dia_semana varchar(30) not null,
    criado_em datetime not null default CURRENT_TIMESTAMP
);

create table D_Hora(
    id int not null auto_increment primary key,
    id_data int not null,
    hora time not null,
    criado_em datetime not null default CURRENT_TIMESTAMP,
    foreign key (id_data) references D_Data(id) on update cascade on delete cascade
);

create table D_DiaNoite(
    id int not null auto_increment primary key,
    momento_dia varchar(10) not null
);

create table F_Tempo(
    id bigint not null primary key auto_increment,
    id_estacao_ano int not null,
    id_data int not null,
    id_hora int not null,
    id_dia_noite int not null,
    temperatura decimal(5, 2) not null,
    umidade decimal(5, 2) not null,
    pressao_atmosferica decimal(7, 2) default null,
    visibilidade decimal(5, 2) default null,
    vento decimal(5, 2) default null,
    hora_coleta datetime default CURRENT_TIMESTAMP,
    foreign key (id_estacao_ano) references D_EstacaoAno(id) on update cascade on delete cascade,
    foreign key (id_data) references D_Data(id) on update cascade on delete cascade,
    foreign key (id_hora) references D_Hora(id) on update cascade on delete cascade,
    foreign key (id_dia_noite) references D_DiaNoite(id) on update cascade on delete cascade
);