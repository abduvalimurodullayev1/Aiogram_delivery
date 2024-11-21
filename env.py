from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

# Fayldagi konfiguratsiyani yuklash
config = context.config
fileConfig(config.config_file_name)

# Bu yerda `Base`ni import qiling
from app.utils.db import Base  

target_metadata = Base.metadata

def run_migrations_online():
    """Online rejimda migratsiyalarni ishlatish."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
