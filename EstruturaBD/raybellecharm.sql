-- criando o banco de dados
CREATE DATABASE raybellecharm
-- usando o banco de dados
USE raybellecharm;

-- criação da tabela tb_cliente e seus atributos
CREATE TABLE tb_cliente(
	nome VARCHAR (100) NOT NULL,
    cpf NUMERIC PRIMARY KEY,
    email VARCHAR (100) NOT NULL,
    telefone NUMERIC NOT NULL,
    senha VARCHAR (100) NOT NULL,
    endereco_rua VARCHAR (100) NOT NULL,
    endereco_numero NUMERIC NOT NULL,
    estado VARCHAR (50) NOT NULL,
    cidade VARCHAR (50) NOT NULL
);

-- criação da tabela tb_produto e seus atributos
CREATE TABLE tb_produto(
	cod_prod NUMERIC PRIMARY KEY,
    nome_prod VARCHAR (100) NOT NULL,
    preco FLOAT NOT NULL,
    foto VARCHAR (200) NOT NULL,
    descricao VARCHAR (200) NOT NULL
);


-- criação da tabela tb_carrinho e seus atributos
CREATE TABLE tb_carrinho(
    id_carrinho INT PRIMARY KEY AUTO_INCREMENT,
	quantidade NUMERIC NOT NULL,
    cpf_cliente NUMERIC NOT NULL,
    id_prod NUMERIC NOT NULL
);


-- criação da tabela tb_comentario e seus atributos
CREATE TABLE tb_comentario(
	cpf_cliente VARCHAR (200) NOT NULL,
    avaliacao VARCHAR (200) NOT NULL,
    cod_avaliacao NUMERIC PRIMARY KEY,
    id_produto NUMERIC NOT NULL
);

CREATE USER 'usuario_raybelle'@'%' IDENTIFIED BY 'raybelle';

GRANT ALL PRIVILEGES ON raybellecharm.* TO 'usuario_raybelle'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;