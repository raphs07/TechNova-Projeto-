# TechNova-Projeto
# Sistema de Gestão Comercial — TechNova Informática

## Descrição do Projeto

O Sistema de Gestão Comercial (SGC) da TechNova Informática foi desenvolvido para gerenciar as operações comerciais de uma loja de produtos e serviços de tecnologia.

A aplicação permite:

- Controle de clientes
- Controle de produtos
- Controle de estoque
- Registro de vendas
- Emissão de relatórios
- Controle de usuários e permissões

O sistema utiliza arquitetura em camadas com API REST e interface web integrada, garantindo:

- Escalabilidade
- Segurança
- Organização
- Facilidade de manutenção

---

# Objetivos do Sistema

- Automatizar processos comerciais
- Melhorar o controle de estoque
- Garantir integridade dos dados
- Facilitar geração de relatórios
- Centralizar informações
- Melhorar produtividade operacional
- Garantir segurança de acesso

---

# Arquitetura do Sistema

O sistema foi desenvolvido utilizando Arquitetura em Camadas.

## Camadas da Arquitetura

### Camada de Apresentação
Responsável pela interface do usuário.

Componentes:
- Django Templates
- Interface Web
- Formulários
- Relatórios

---

### Camada de Aplicação
Responsável pela comunicação entre front-end e back-end.

Componentes:
- API REST
- Serialização de dados
- Autenticação JWT
- Controle de permissões

---

### Camada de Negócio
Responsável pelas regras de negócio do sistema.

Funcionalidades:
- Validação de CPF
- Controle de estoque
- Cálculo de vendas
- Validação de preços
- Regras de acesso

---

### Camada de Dados
Responsável pelo armazenamento e persistência das informações.

Tecnologias:
- SQLite

---

# Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Desenvolvimento Back-end |
| Django | Framework Web |
| Django REST Framework | API REST |
| SQLite | Banco de dados local |
| JWT | Autenticação |
| Git | Controle de versão |
| GitHub | Hospedagem do repositório |

---

# Segurança

## Autenticação
- JWT (JSON Web Token)
- Rotas protegidas
- Controle de sessão
- Controle de permissões

---

## Controle de Acesso

### ADMIN
Permissões:
- Gerenciamento de usuários
- Gerenciamento de clientes
- Gerenciamento de produtos
- Gerenciamento de vendas
- Geração de relatórios

### FUNCIONÁRIO
Permissões:
- Registro de vendas
- Consulta de produtos
- Consulta de clientes

---

# Funcionalidades

## Gestão de Clientes
- Cadastro de clientes
- Edição de clientes
- Exclusão de clientes
- Consulta de clientes
- Validação de CPF único
- Validação de e-mail

---

## Gestão de Produtos
- Cadastro de produtos
- Controle de estoque
- Controle de estoque mínimo
- Validação de preço
- Bloqueio de venda sem estoque

---

## Gestão de Vendas
- Registro de vendas
- Vendas com múltiplos itens
- Cálculo automático do total
- Atualização automática do estoque

---

## Relatórios
- Relatório de vendas por período
- Relatório de vendas por cliente
- Relatório gráfico anual

---

# Estrutura de Pastas

```plaintext
technova_sgc/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── usuarios/
├── clientes/
├── produtos/
├── vendas/
├── relatorios/
│
├── templates/
├── static/
└── media/
```

---

# API REST

## Autenticação

```http
POST /auth/login
```

### Exemplo de Resposta

```json
{
  "access": "token_jwt",
  "refresh": "refresh_token"
}
```

---

# Clientes

## Listar Clientes

```http
GET /clientes
```

## Cadastrar Cliente

```http
POST /clientes
```

### Exemplo JSON

```json
{
  "nome": "João Silva",
  "cpf": "12345678900",
  "email": "joao@email.com"
}
```

---

# Produtos

## Listar Produtos

```http
GET /produtos
```

## Cadastrar Produto

```http
POST /produtos
```

---

# Vendas

## Registrar Venda

```http
POST /vendas
```

### Exemplo JSON

```json
{
  "cliente": 1,
  "itens": [
    {
      "produto": 1,
      "quantidade": 2
    }
  ]
}
```

---

# Banco de Dados

## Tabelas Principais

- usuarios
- clientes
- produtos
- vendas
- itens_venda

---

# Script SQL

```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    senha VARCHAR(255),
    perfil VARCHAR(20)
);

CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    cpf VARCHAR(14) UNIQUE,
    email VARCHAR(100),
    telefone VARCHAR(20)
);

CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    preco DECIMAL(10,2),
    estoque INTEGER,
    estoque_minimo INTEGER
);

CREATE TABLE vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    usuario_id INTEGER,
    total DECIMAL(10,2),
    data_venda DATETIME,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id),
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE itens_venda (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    venda_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    subtotal DECIMAL(10,2),
    FOREIGN KEY(venda_id) REFERENCES vendas(id),
    FOREIGN KEY(produto_id) REFERENCES produtos(id)
);
```

---

# Diagramas

## Diagrama de Casos de Uso

```plaintext
                +------------------+
                |      ADMIN       |
                +------------------+
                  |   |   |   |
                  |   |   |   |
      ----------------------------------------
      |          |          |                |
Gerenciar   Gerenciar   Gerenciar      Gerar
Clientes    Produtos     Vendas       Relatórios

                +------------------+
                |   FUNCIONÁRIO    |
                +------------------+
                      |       |
                      |       |
               Registrar   Consultar
                 Vendas     Produtos
```

---

## Diagrama de Classes

```plaintext
+----------------+
| Usuario        |
+----------------+
| id             |
| nome           |
| email          |
| senha          |
| perfil         |
+----------------+

+----------------+
| Cliente        |
+----------------+
| id             |
| nome           |
| cpf            |
| email          |
| telefone       |
+----------------+

+----------------+
| Produto        |
+----------------+
| id             |
| nome           |
| preco          |
| estoque        |
| estoqueMinimo  |
+----------------+

+----------------+
| Venda          |
+----------------+
| id             |
| total          |
| dataVenda      |
+----------------+

+----------------+
| ItemVenda      |
+----------------+
| id             |
| quantidade     |
| subtotal       |
+----------------+
```

---

## Diagrama de Domínio

```plaintext
Cliente ---- realiza ---- Venda
Venda ---- possui ---- ItemVenda
Produto ---- pertence ---- ItemVenda
Usuario ---- registra ---- Venda
```

---

## Diagrama Lógico do Banco

```plaintext
CLIENTES (1) -------- (N) VENDAS
USUARIOS (1) -------- (N) VENDAS
VENDAS (1) ---------- (N) ITENS_VENDA
PRODUTOS (1) -------- (N) ITENS_VENDA
```

---

# Como Executar o Projeto

## Pré-requisitos

- Python instalado
- Git instalado

---

## Instalação e Execução

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Entrar na pasta do projeto
cd seu-repositorio

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar migrações
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

---

# Considerações Finais

O Sistema de Gestão Comercial da TechNova Informática foi desenvolvido utilizando boas práticas de desenvolvimento, arquitetura escalável e autenticação segura, proporcionando uma solução eficiente para gerenciamento comercial.

O projeto utiliza Django e Django REST Framework para garantir organização, manutenção simplificada e integração entre API REST e interface web.

---

##PARTICIPANTES DO GRUPO:

Anna Beatriz Pereira da Silva

Elaine Barbosa da Silva

Raphaela Pereira de Sousa

Vitória de Sousa Melo

---

## Licença

Este projeto é acadêmico e foi desenvolvido para fins educacionais.

