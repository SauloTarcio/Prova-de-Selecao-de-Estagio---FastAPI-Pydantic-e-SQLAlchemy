from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models, schemas, crud
import os

# Função para recriar o banco de dados no modo de teste
def recreate_db():
    if os.getenv("TEST_MODE") == "true":
        print("Modo de teste ativo. Recriando o banco de dados...")

        # Dropa todas as tabelas
        Base.metadata.drop_all(bind=engine)

        # Cria novamente todas as tabelas
        Base.metadata.create_all(bind=engine)

# Recriar o banco de dados (se necessário)
recreate_db()

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD de Empresas

@app.post("/empresa/", response_model=schemas.Empresa)
def create_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    return crud.create_empresa(db, empresa)

@app.get("/empresas/", response_model=list[schemas.Empresa])
def listar_empresas(db: Session = Depends(get_db)):
    return crud.obter_empresa(db)

@app.get("/empresas/{empresa_id}", response_model=schemas.Empresa)
def obter_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = crud.obter_empresa_por_id(db, empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

@app.put("/empresas/{empresa_id}", response_model=schemas.Empresa)
def update_empresa(empresa_id: int, empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = crud.update_empresa(db, empresa_id, empresa)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

@app.delete("/empresas/{empresa_id}", response_model=schemas.Empresa)
def delete_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = crud.delete_empresa(db, empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa


# CRUD de Obrigações

@app.post("/empresas/{empresa_id}/obrigacoes/", response_model=schemas.ObrigacaoAcessoria)
def adicionar_obrigacao(empresa_id: int, obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    return crud.create_obrigacao(db, obrigacao, empresa_id)

@app.get("/empresas/{empresa_id}/obrigacoes/", response_model=list[schemas.ObrigacaoAcessoria])
def listar_obrigacoes(empresa_id: int, db: Session = Depends(get_db)):
    return crud.obter_obrigacoes(db, empresa_id)

@app.get("/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria)
def obter_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = crud.obter_obrigacao_por_id(db, obrigacao_id)
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    return db_obrigacao

@app.put("/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria)
def update_obrigacao(obrigacao_id: int, obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = crud.update_obrigacao(db, obrigacao_id, obrigacao)
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    return db_obrigacao

@app.delete("/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria)
def delete_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = crud.delete_obrigacao(db, obrigacao_id)
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    return db_obrigacao