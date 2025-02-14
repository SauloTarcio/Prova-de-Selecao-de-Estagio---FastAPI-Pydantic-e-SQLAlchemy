from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/empresa/", response_model=schemas.Empresa)
def criar_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    return crud.criar_empresa(db, empresa)

@app.get("/empresas/", response_model=list[schemas.Empresa])
def listar_empresas(db: Session = Depends(get_db)):
    return crud.obter_empresas(db)

@app.post("/empresas/{empresa_id}/obrigacoes/", response_model=schemas.ObrigacaoAcessoria)
def adicionar_obrigacao(empresa_id: int, obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    return crud.criar_obrigacao(db, obrigacao, empresa_id)