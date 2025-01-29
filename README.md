# 📌 FastAPI - Empresas - Contratos

## 🎯 Objetivo
Desenvolver uma aplicação que contenha **empresas e seus contratos**, permitindo a criação, listagem, gerenciamento dessas entidades e métricas específicas.

---

## 🚀 **1. Como Iniciar o Projeto**

### 🔹 **1.1 Requisitos**
Antes de iniciar, certifique-se de ter os seguintes requisitos instalados:
- **Python 3.10+**
- **Poetry** (Gerenciador de dependências)
- **Docker & Docker Compose**

### 🔹 **1.2 Clonando o Repositório**
```bash
git clone https://github.com/nicolebarroos/AFL-Technical-Test.git
cd seu-repo
```

### 🔹 **1.3 Criando e Configurando o Ambiente**
**Configure as variáveis de ambiente**
   ```bash
   cp .env.example .env
   nano .env  #Edite com suas credenciais
   ```
**Gerando uma SECRET_KEY para autenticação JWT**
   Para gerar uma chave secreta segura para JWT, execute o seguinte comando no terminal:
   ```bash
   openssl rand -hex 32
   ```
   Copie a chave gerada e adicione ao arquivo `.env`:
   ```ini
   SECRET_KEY=chave-gerada-aqui
   ```

### 🔹 **1.4 Rodando o Projeto**

#### 🔹 **Executar com Docker**
```bash
docker-compose up --build
```
Acesse a API em [`http://localhost:8008/docs`](http://localhost:8008/docs)

---

## 🌐 2. Deploy da Aplicação
A aplicação foi implantada em uma instância EC2 da AWS, e o banco de dados está hospedado no RDS. Você pode acessar a API diretamente através do seguinte endereço:

http://18.204.211.139:8008/docs/
