from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='config.env')
if os.getenv("TEST_MODE") == "true":
    database_url = os.getenv("DATABASE_TEST_URL")
else:
    database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise ValueError("A variável DATABASE_URL não está definida no ambiente!")

engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Função para recriar o banco de dados no modo de teste
def recreate_db():
    if os.getenv("TEST_MODE") == "true":
        print("Modo de teste ativo. Recriando o banco de dados...")

        # Dropa todas as tabelas
        Base.metadata.drop_all(bind=engine)

        # Cria novamente todas as tabelas
        Base.metadata.create_all(bind=engine)

# Chama a função para recriar o banco de dados ao iniciar o código
recreate_db()