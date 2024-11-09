import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(
    DATABASE_URL,
    pool_size=10,              # Tamaño máximo del pool de conexiones
    max_overflow=20,           # Número de conexiones adicionales si el pool está lleno
    pool_timeout=30,           # Tiempo máximo de espera para obtener una conexión antes de fallar
    pool_recycle=1800,         # Tiempo para reciclar conexiones viejas
    pool_pre_ping=True,        # Esta opción puede ayudar a detectar conexiones rotas antes de usarlas
    echo=False                # Cambiar a True para habilitar logs detallados de SQL
      
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    from app.models import user, transaction
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def get_db():
#     db = SessionLocal()
#     logger.debug("Session opened: %s", db)
#     try:
#         yield db
#     finally:
#         logger.debug("Session closed: %s", db)
#         db.close()