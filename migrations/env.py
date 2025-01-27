import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Se quiser carregar .env
from dotenv import load_dotenv
load_dotenv()

# Importando seu Base
from src.infrastructure.database import Base
from src.domain.entities.user import User  # Forçar import
# Este é o objeto de configuração do Alembic
config = context.config

# (Opcional) Se quiser injetar a URL do banco via env:
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Leitura do arquivo de config para logging
fileConfig(config.config_file_name)
print(">>> Tabelas registradas no Base:", Base.metadata.tables.keys())

# Definindo quais metadados o Alembic deve rastrear
target_metadata = Base.metadata

def run_migrations_offline():
    """Executa as migrações em modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"}
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Executa as migrações em modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

def run_migrations():
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()

run_migrations()
