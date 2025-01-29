
# Gerenciador de Assinaturas

**Gerenciador de Assinaturas** é uma aplicação para controle de assinaturas de serviços, permitindo o cadastro, pagamento e exclusão de assinaturas de maneira fácil e organizada. O projeto foi desenvolvido com **Python** e utiliza **SQLAlchemy** para gerenciar o banco de dados.

## Sumário

- [Descrição do Projeto](#descrição-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-Requisitos](#pré-requisitos)
- [Configuração do Ambiente](#configuração-do-ambiente)
  - [Linux](#linux)
  - [macOS](#macos)
  - [Windows](#windows)
- [Como Executar](#como-executar)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Contribuições](#contribuições)
- [Licença](#licença)

## Descrição do Projeto

O **Gerenciador de Assinaturas** permite que os usuários realizem os seguintes processos:

- Cadastro de novas assinaturas.
- Visualização das assinaturas ativas.
- Realização de pagamentos.
- Exclusão de assinaturas (inativação).
  
A aplicação é desenvolvida com o propósito de simplificar o controle financeiro das assinaturas de serviços.

## Funcionalidades

- Cadastro de assinatura.
- Pagamento de assinatura.
- Exclusão de assinaturas.
- Relatórios de pagamentos.
- Validação de pagamentos duplicados.

## Tecnologias Utilizadas

- **Python** 3.x
- **SQLAlchemy** - ORM para interação com o banco de dados.
- **SQLite** - Banco de dados.
- **Pydantic** - Validação de dados.
- **Click** - Interface de linha de comando.

## Pré-Requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas no seu sistema:

- Python 3.7 ou superior.
- Gerenciador de pacotes **pip**.
- Banco de dados **SQLite** (usado no projeto).

### Dependências

- Para instalar as dependências, utilize o comando abaixo:

```bash
pip install -r requirements.txt
```

## Configuração do Ambiente

### Linux

1. **Clone o repositório:**

```bash
git clone https://github.com/AndressaSilva0/gerenciador-de-assinaturas.git
cd gerenciador-de-assinaturas
```

2. **Crie e ative o ambiente virtual:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip3 install -r requirements.txt
```

4. **Configure as variáveis de ambiente (se necessário):**

```bash
export DATABASE_URL=sqlite:///db.sqlite3
```

### macOS

1. **Clone o repositório:**

```bash
git clone https://github.com/AndressaSilva0/gerenciador-de-assinaturas.git
cd gerenciador-de-assinaturas
```

2. **Crie e ative o ambiente virtual:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip3 install -r requirements.txt
```

4. **Configure as variáveis de ambiente (se necessário):**

```bash
export DATABASE_URL=sqlite:///db.sqlite3
```

### Windows

1. **Clone o repositório:**

```bash
git clone https://github.com/AndressaSilva0/gerenciador-de-assinaturas.git
cd gerenciador-de-assinaturas
```

2. **Crie e ative o ambiente virtual:**

```bash
python -m venv venv
venv\Scripts\activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente (se necessário):**

```bash
set DATABASE_URL=sqlite:///db.sqlite3
```

## Como Executar

Para rodar o sistema, você pode usar o seguinte comando:

```bash
python templates/app.py
python3 templates/app.py #Linux and MacOS
```

O aplicativo será iniciado no terminal e você poderá interagir com a interface para gerenciar suas assinaturas.



3. **Teste manualmente pela interface de linha de comando:**

- Cadastre assinaturas.
- Realize pagamentos.
- Exclua assinaturas (inative-as).

## Estrutura de Diretórios

```plaintext
gerenciador-de-assinaturas/
├── .git/               # Diretório do Git
├── gerenciador_de_assinaturas/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── model.py
│   ├── templates/
│   │   ├── __init__.py
│   │   ├── app.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── view.py
├── venv/               # Ambiente virtual Python
├── .gitignore          # Arquivo para ignorar arquivos no Git
├── database.db         # Banco de dados SQLite
├── README.md           # Documentação do projeto
├── requirements.txt    # Arquivo com as dependências do projeto

```

## Contribuições

Se você deseja contribuir para este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/nome-da-sua-feature`).
3. Faça as alterações necessárias.
4. Envie um pull request.

## Licença

Este projeto está licenciado sob a **MIT License**.

---

# Subscription Manager

**Subscription Manager** is an application for managing service subscriptions, allowing users to register, pay, and delete subscriptions in an easy and organized way. The project is developed in **Python** and uses **SQLAlchemy** for database management.

For instructions in English, please refer to the sections above and use a translation tool if necessary.

