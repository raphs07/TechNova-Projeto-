# TechNova-Projeto-

# Sistema de Gestão Comercial - TechNova Informática

## Descrição do Projeto

O **Sistema de Gestão Comercial (SGC)** da TechNova Informática foi desenvolvido para gerenciar as operações de uma loja de produtos e serviços de tecnologia. A aplicação permite o controle completo de clientes, produtos, vendas e relatórios, garantindo organização, segurança e eficiência no processo comercial.

O sistema segue uma arquitetura em camadas, com API REST e interface web integrada, proporcionando escalabilidade e facilidade de manutenção.

---

## Objetivos do Sistema

* Automatizar o controle de vendas e estoque
* Gerenciar clientes de forma segura
* Garantir integridade dos dados
* Facilitar a geração de relatórios
* Oferecer uma interface simples e funcional

---

## Arquitetura

O sistema foi desenvolvido utilizando **arquitetura em camadas**, dividida em:

* **Camada de Apresentação:** Interface Web (Django)
* **Camada de Aplicação:** API REST
* **Camada de Negócio:** Regras de negócio e validações
* **Camada de Dados:** Banco de dados relacional

---

## Tecnologias Utilizadas

* Python
* Django
* Django REST Framework
* SQLite / PostgreSQL
* Git e GitHub
* JWT (JSON Web Token)

---

## Segurança

* Autenticação via Token (JWT)
* Proteção de rotas
* Controle de acesso por perfil:

  * ADMIN
  * FUNCIONÁRIO

---

##Funcionalidades

### Gestão de Clientes

* Cadastro, edição e listagem
* Validação de CPF único
* Validação de email
* Restrição de exclusão com vendas vinculadas

### Gestão de Produtos

* Cadastro e controle de estoque
* Validação de preço
* Controle de estoque mínimo
* Bloqueio de vendas sem estoque

### Registro de Vendas

* Registro com múltiplos itens
* Cálculo automático do valor total
* Atualização automática do estoque
* Associação com cliente e usuário

### Relatórios

* Vendas por período
* Vendas por cliente
* Relatório gráfico anual

---

## API REST (Exemplos)

**Autenticação**

```
POST /auth/login
```

**Clientes**

```
GET /clientes
POST /clientes
```

**Produtos**

```
GET /produtos
POST /produtos
```

**Vendas**

```
GET /vendas
POST /vendas
```

Todas as respostas são retornadas no formato **JSON**.

---

## Banco de Dados

Tabelas principais:

* usuarios
* clientes
* produtos
* vendas
* itens_venda

Inclui:

* Script SQL de criação
* Diagrama lógico do banco

---

## Diagramas

O projeto contém os seguintes diagramas:

* Diagrama de Casos de Uso
* Diagrama de Classes
* Diagrama de Domínio
* Diagrama Lógico do Banco de Dados

---

## Como Executar o Projeto

### Pré-requisitos

* Python instalado
* Git instalado

### Passos

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Acessar a pasta
cd seu-repositorio

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Rodar migrações
python manage.py migrate

# Executar servidor
python manage.py runserver
```

---

## Equipe

* Anna Beatriz
* Elaine
* Raphaela
* Vitória

---

## Licença

Este projeto é acadêmico e foi desenvolvido para fins educacionais.
