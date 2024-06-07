-- criando o banco de dados
CREATE DATABASE raybellecharm;
-- usando o banco de dados
USE raybellecharm;

-- criação da tabela tb_cliente e seus atributos
CREATE TABLE tb_cliente(
	nome VARCHAR (100) NOT NULL,
    cpf VARCHAR(11) PRIMARY KEY,
    email VARCHAR (100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    senha VARCHAR (100) NOT NULL,
    endereco_rua VARCHAR (100) NOT NULL,
    endereco_numero VARCHAR(200) NOT NULL,
    estado VARCHAR (50) NOT NULL,
    cidade VARCHAR (50) NOT NULL
);

-- criação da tabela tb_produto e seus atributos
CREATE TABLE tb_produto(
	cod_prod VARCHAR(200) PRIMARY KEY,
    nome_prod VARCHAR (100) NOT NULL,
    preco FLOAT NOT NULL,
    foto VARCHAR (255) NOT NULL,
    descricao VARCHAR (200) NOT NULL,
    categoria VARCHAR (200) NOT NULL
);
-- criação da tabela tb_carrinho e seus atributos
CREATE TABLE tb_carrinho(
    id_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    id_prod VARCHAR(200),
	quantidade INT NOT NULL,
    cpf_cliente VARCHAR(11) NOT NULL
);

-- criação da tabela tb_comentario e seus atributos
CREATE TABLE tb_comentario(
	cod_avaliacao INT AUTO_INCREMENT PRIMARY KEY,
	cpf_cliente VARCHAR (11) NOT NULL,
    avaliacao VARCHAR (200) NOT NULL
);

CREATE USER 'usuario_raybelle'@'%' IDENTIFIED BY 'raybelle';

GRANT ALL PRIVILEGES ON raybellecharm.* TO 'usuario_raybelle'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

SELECT * FROM tb_produto p
INNER JOIN tb_carrinho c
ON p.cod_prod = c.id_prod;

INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('0', 'anel-ouro', '150.00', '/static/img/produtos-ouro/anel-ouro.jpg', 'Anel Rika', 'ouro');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('1', 'anel-ouro2', '350.00', '/static/img/produtos-ouro/anel-ouro2.jpg', 'Anel Vitória', 'ouro');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('2', 'anel-ouro3', '500.00', '/static/img/produtos-ouro/anel-ouro3.jpg', 'Anel Realeza', 'ouro');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('3', 'bracelete-ouro', '250.00', '/static/img/produtos-ouro/bracelete-ouro.jpg', 'Bracelete Prego', 'ouro');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('4', 'bracelete-ouro2', '300.00', '/static/img/produtos-ouro/bracelete-ouro2.jpg', 'Bracelete Noiva Bella', 'ouro');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('5', 'brinco-cravejado', '99.90', '/static/img/produtos-ouro/brinco-ouro.jpg', 'Brinco Pricilla', 'ouro');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('6', 'colar-ouro', '80.50', '/static/img/produtos-ouro/colar-ouro2.jpg', 'Colar Raio de Sol', 'ouro');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('7', 'colar-ouro2', '310.00', '/static/img/produtos-ouro/colar-ouro3.jpg', 'Colar Vestígios do Campo', 'ouro');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('8', 'conjunto-ouro', '460.00', '/static/img/produtos-ouro/conjunto-ouro.jpg', 'Conjunto Apaixonada', 'ouro');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('9', 'gargantilha-ouro', '1000.00', '/static/img/produtos-ouro/gargantilha-ouro.jpg', 'Gargantilha Autoestima', 'ouro');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('10', 'anel-prata', '3500.00', '/static/img/produtos-prata/anel-prata2.jpg', 'Anel Isadora', 'prata');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('11', 'anel-prata2', '5500.00', '/static/img/produtos-prata/anel-prata3.jpg', 'Anel Isabelle', 'prata');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('12', 'bracelete-prata', '150.00', '/static/img/produtos-prata/bracelete-prata.jpg', 'Bracelete Ísis', 'prata');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('13', 'bracelete-prata2', '150.00', '/static/img/produtos-prata/bracelete-prata2.jpg', 'Bracelete Débora', 'prata');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('14', 'brinco-prata', '55.50', '/static/img/produtos-prata/Brinco-prata.jpg', 'Brinco Diamante', 'prata');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('15', 'brinco-prata2', '150.50', '/static/img/produtos-prata/brinco-prata2.jpg', 'Brinco Rayane', 'prata');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('16', 'colar-prata', '100.99', '/static/img/produtos-prata/colar-prata.jpg', 'Colar Coração de Mãe', 'prata');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('17', 'conjunto-prata', '500.00', '/static/img/produtos-prata/conjunto-prata.jpg', 'Conjunto Mulher de Fases', 'prata');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('18', 'conjunto-prata2', '350.00', '/static/img/produtos-prata/conjunto-prata2.jpg', 'Conjunto Jupter e Saturno', 'prata');
INSERT INTO `raybellecharm`.`tb_produto` (`cod_prod`, `nome_prod`, `preco`, `foto`, `descricao`, `categoria`) VALUES ('19', 'kit-prata', '550.99', '/static/img/produtos-prata/kit-prata.jpg', 'Kit Outono', 'prata');