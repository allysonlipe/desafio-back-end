# desafio-dev-backend

## Descrição

Estou criando esse repositório para um teste técnico para uma vaga de Beck-end, tendo como objetivo: 
```
"Criar uma aplicação CRUD básica com banco de dados e API em Python..." 
```
## Resultados Esperados

```
"Ao final deste desafio, deve existir uma aplicação backend capaz de criar , atualizar , remover e selecionar dados de um banco de dados."
```


## Funcionalidades

Liste as principais funcionalidades do projeto:

- Criar dados em um banco de dados;
- Atualizar dados em um banco de dados;
- Remover dados em um banco de dados;
- Selecionar dados em um banco de dados.

## Tecnologias Utilizadas

Mencione as principais tecnologias, bibliotecas e frameworks utilizados no projeto.

- Python (Framework Django)
- MYSQL

## Requisitos

Liste os pré-requisitos necessários para configurar e executar o projeto.

- Python 3.x
- Django 5.x
- MySQL 8.x

## Instalação

Passo a passo de como configurar o ambiente de desenvolvimento e instalar as dependências.

1. Clone o repositório:
   ```bash
   git clone https://github.com/allysonlipe/desafio-DEV-BackEnd.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd api
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # No Windows: myenv\Scripts\activate
   ```
   Caso encontre o seguinte erro:
   ```
   não pode ser carregado porque a execução de scripts foi desabilitada neste sistema.     
   Para obter mais informações, consulte about_Execution_Policies em 
   https://go.microsoft.com/fwlink/?LinkID=135170.
   No linha:1 caractere:3
   ```
   1. **Abra o PowerShell como Administrador;**
   &nbsp;
   2. **Verifique a política atual (opcional):**
      ```
      Get-ExecutionPolicy
      ```
   3. **Altere a política de execução para permitir scripts:**
      ```
      Set-ExecutionPolicy RemoteSigned
      ```
   4. **Confirme a alteração:**
         Quando solicitado, pressione Y e depois Enter para confirmar a alteração.
   5. **Tente ativar o ambiente virtual novamente:**
         ```
         source myenv/bin/activate  # No Windows: myenv\Scripts\activate
         ```


4. Pressione `Ctrl` + `Shift` + `P`, e ao abrir a janela abaixo, digite `Python: Select Interpreter` e selecione a opção marcada como na imagem abaixo: 
   <img src="assets/img/print1.png">

5. Agora, selecione a segunda opção da imagem, `Enter interpreter path`:
   <img src="assets/img/print2.png">
6. Agora, clique em `Find...`
   <img src="assets/img/print3.png">
7. O passo anterior irá abrir uma janela de gerenciador de arquivos, nessa janela, você vai selecionar o caminho da sua `env\scripts`:
   <img src="assets/img/print5.png">

8. E selecionar o arquivo `python`:
   <img src="assets/img/print4.png">
9. Para instalar todas as dependências, execute:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração

Explique como configurar as variáveis de ambiente e outras configurações necessárias.

1. Dentro do seu projeto, há um arquivo chamado settings.py, procure por **DATABASES** e faça sua configuração, se você utilizar meus scripts SQLS a configuração será:

   ```env
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'desafio',
        'USER':'root',
        'PASSWORD':'admin',
        'HOST': 'localhost',
        'PORT':'3306',
    }
      ```

## Uso

Instruções sobre como executar o projeto.

1. Inicie o servidor:
   ```bash
      VER DEPOIS
   ```

2. Acesse a aplicação em `http://localhost:8000`.

## Licença

This project is under MIT license. See the [LICENSE](LICENSE.md) for more details.