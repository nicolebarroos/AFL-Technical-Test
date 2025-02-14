# 📌 FastAPI - Empresas e Contratos  

## 🎯 Objetivo  
Desenvolver uma aplicação que contenha **empresas e seus contratos**, permitindo a **criação, listagem, gerenciamento** dessas entidades e **métricas específicas**.  

---

## 🚀 Como Iniciar o Projeto  

### 🔹 Requisitos  
Antes de iniciar, certifique-se de ter os seguintes requisitos instalados:  
- **Python 3.10+**  
- **Poetry** (Gerenciador de dependências)  
- **Docker & Docker Compose**  

### 🔹 Clonando o Repositório  
```bash
git clone https://github.com/nicolebarroos/AFL-Technical-Test.git
cd seu-repo
```

### 🔹 Criando e Configurando o Ambiente  

#### **1. Configurar as Variáveis de Ambiente**  
```bash
cp .env.example .env
nano .env  # Edite com suas credenciais
```

#### **2. Gerar uma SECRET_KEY para autenticação JWT**  
Execute o seguinte comando no terminal:  
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
Copie a chave gerada e adicione ao arquivo `.env`:  
```ini
SECRET_KEY=chave-gerada-aqui
```

---

## 🚀 Rodando o Projeto  

### 🔹 Executar com Docker  
```bash
docker-compose up --build
```
Acesse a API em [`http://localhost:8008/docs`](http://localhost:8008/docs).  

---

## 🧪 Rodando os Testes  

### 🔹 Executar os testes dentro do contêiner  
Acesse o contêiner:  
```bash
docker exec -it fastapi_container bash
```
Dentro do contêiner, execute os testes com:  
```bash
poetry run pytest -v
```
Ou simplesmente:  
```bash
pytest
```

---

## 🏗 Arquitetura do Projeto  

A aplicação segue os princípios da **Arquitetura Limpa**, separando bem as responsabilidades em diferentes camadas:  

📂 **Camada de Aplicação (`app/use_cases`)**  
- Contém os **casos de uso** (use cases), que definem a lógica da aplicação sem depender da infraestrutura.  

📂 **Camada de Domínio (`app/domain`)**  
- Define as **entidades principais** do sistema e suas interfaces.  

📂 **Camada de Infraestrutura (`app/infrastructure`)**  
- Implementa os **repositórios** que interagem com o banco de dados.  

📂 **Camada de Interface (`app/interfaces`)**  
- Contém os **controllers** (responsáveis pelos endpoints) e **schemas** (validações de entrada e saída de dados).  

🔹 **Benefícios:**  
✅ **Baixo acoplamento**  
✅ **Alta coesão**  
✅ **Facilidade na manutenção e escalabilidade**  

