from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            """
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
                VALUES (p_nome, p_data_nascimento, p_salario, p_observacoes, p_nome_mae, p_nome_pai, p_cpf);
                SET p_id_pessoa = LAST_INSERT_ID();
                SELECT p_id_pessoa AS id_pessoa;
            END;
            """
        ),
        migrations.RunSQL(
            """
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
            END;
            """
        ),
        migrations.RunSQL(
            """
            CREATE PROCEDURE deletar_pessoa (
                IN p_id_pessoa INT
            )
            BEGIN
                DELETE FROM api_rest_pessoas
                WHERE id_pessoa = p_id_pessoa;
                SELECT 'OK' AS status;
            END;
            """
        ),
        migrations.RunSQL(
            """
            CREATE PROCEDURE selecionar_tudo ()
            BEGIN
                SELECT * FROM api_rest_pessoas;
            END;
            """
        ),
        migrations.RunSQL(
            """
            CREATE PROCEDURE selecionar_pessoa (
                IN p_id_pessoa INT
            )
            BEGIN
                SELECT * FROM api_rest_pessoas
                WHERE id_pessoa = p_id_pessoa;
            END;
            """
        )
    ]