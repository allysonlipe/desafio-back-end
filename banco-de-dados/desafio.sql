-- Objetivo : Criar estruturas de tabelas e procedures no banco de dados.
CREATE DATABASE IF NOT EXISTS desafio; 
USE desafio;

-- Criar script para criação da tabela Pessoas:
CREATE TABLE IF NOT EXISTS api_rest_pessoas (
    id_pessoa INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    observacoes TEXT
);

-- Criar script para alteração da tabela Pessoas:
ALTER TABLE api_rest_pessoas
ADD COLUMN nome_mae VARCHAR(100),
ADD COLUMN nome_pai VARCHAR(100),
ADD COLUMN cpf VARCHAR(11);

-- Criar um script para adicionar índices de pesquisa a tabela Pessoas (nome e data_nascimento):
CREATE INDEX idx_nome ON api_rest_pessoas (nome);
CREATE INDEX idx_data_nascimento ON api_rest_pessoas (data_nascimento);

-- Criar um script para adicionar indice/chave única a tabela Pessoas: Chave Única:cpf
ALTER TABLE api_rest_pessoas
ADD CONSTRAINT unique_cpf UNIQUE (cpf);

/* Criar um script para criar uma procedure de inserção de registros:   
Procedure deverá receber como parâmetros os campos da tabela Pessoas 
Procedure deverá retomar para a API o valor do campo id_pessoa. */

DELIMITER $$

CREATE PROCEDURE inserir_pessoa (
	
    IN p_nome VARCHAR(100),
	IN p_data_nascimento DATE,
	IN p_salario DECIMAL(10,2),
	IN p_observacoes TEXT,
	IN p_nome_mae VARCHAR(100),
	IN p_nome_pai VARCHAR(100),
	IN p_cpf VARCHAR(11),
	OUT p_id_pessoa INT

)

BEGIN
	INSERT INTO api_rest_pessoas (nome, data_nascimento, salario, observacoes, nome_mae, nome_pai, cpf)
	VALUES (p_nome, p_data_nascimento, p_salario, p_observacoes, p_nome_mae, p_nome_pai, p_cpf );
    SET p_id_pessoa = LAST_INSERT_ID();
    SELECT p_id_pessoa AS id_pessoa;
END $$

DELIMITER ;

/*
Criar um script para criar uma procedure de atualização de registros:
Procedure deverá receber como parâmetros os campos da tabela Pessoas .
Procedure deverá retomnar para a API o valor OK
*/

DELIMITER $$

CREATE PROCEDURE atualizar_pessoa (
    IN p_id_pessoa INT,
    IN p_nome VARCHAR(100),
    IN p_data_nascimento DATE,
    IN p_salario DECIMAL(10, 2),
    IN p_observacoes TEXT,
    IN p_nome_mae VARCHAR(100),
    IN p_nome_pai VARCHAR(100),
    IN p_cpf VARCHAR(11)
)
BEGIN
    UPDATE api_rest_pessoas
    SET 
        nome = p_nome,
        data_nascimento = p_data_nascimento,
        salario = p_salario,
        observacoes = p_observacoes,
        nome_mae = p_nome_mae,
        nome_pai = p_nome_pai,
        cpf = p_cpf
    WHERE id_pessoa = p_id_pessoa;

    SELECT 'OK' AS status;
END $$

DELIMITER ;

/* Criar um script para criar uma procedure de remoção de registros:
Procedure deverá receber como parâmetros o idPessoa a ser removido da tabela de Pessoas .
Procedure deverá retornar para a API o valor OK */

DELIMITER $$

CREATE PROCEDURE deletar_pessoa (
    IN p_id_pessoa INT
)
BEGIN
    DELETE FROM api_rest_pessoas
    WHERE id_pessoa = p_id_pessoa;

    SELECT 'OK' AS status;
END $$

DELIMITER ;


/* Criar um script para criar uma procedure de seleção de todos os registros:
Procedure deverá retornar todos os registros existentes na tabela de Pessoas */

DELIMITER $$

CREATE PROCEDURE selecionar_tudo (

)
BEGIN
	SELECT * FROM api_rest_pessoas;
END $$

DELIMITER ;

/* Criar um script para criar uma procedure de obter um registro:
Procedure deverá receber como parâmetros o id_pessoa a ser selecionado na tabela. */

DELIMITER $$

CREATE PROCEDURE selecionar_pessoa(
IN p_id_pessoa INT
)

BEGIN
	SELECT * FROM api_rest_pessoas
    WHERE id_pessoa = p_id_pessoa;
END $$

DELIMITER ;

SET @id_pessoa = LAST_INSERT_ID();

/*Criar um script para inserir dados na tabela de Pessoas através da procedure de inserção .*/
CALL inserir_pessoa('João da Silva','1990-05-15',2500.00,'esse é o João','Maria da Silva','José da Silva','12345678906',@id_pessoa);

/*Criar um script para atualizar dados na tabela de Pessoas através da procedure de atualização*/
call desafio.atualizar_pessoa(@id_pessoa, 'José da Silva Júnior', '2002-12-02', 800.00, 'esse agora é o Filho do José', 'Francisca da Silva', 'José da Silva', '12345678902');

/*Criar um script para remover dados na tabela de Pessoas através da procedure de remoção . */
call desafio.deletar_pessoa(@id_pessoa);

/*Criar um script para selecionar registros na tabela de Pessoas através da procedure de seleção de todos os registros.*/
call desafio.selecionar_tudo();

/*Criar um script para selecionar um registro na tabela de Pessoas através da procedure de seleção de um registro.*/
call desafio.selecionar_pessoa(@id_pessoa);

