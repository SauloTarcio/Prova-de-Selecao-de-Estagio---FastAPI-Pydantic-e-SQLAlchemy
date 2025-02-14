from sqlalchemy.orm import Session
import models, schemas

def create_empresas(db: Session, empresa: schemas.EmpresaCreate):
    db_empresa = models.Empresa(nome=empresa.nome, cnpj=empresa.cnpj, 
                                endereco=empresa.endereco, email=empresa.email, telefone=empresa.telefone)
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def obter_empresa(db: Session):
    return db.query(models.Empresa).all()

def create_obrigacao(db: Session, obrigacao: schemas.ObrigacaoAcessoriaCreate, empresa_id: int):
    db_obrigacao = models.ObrigacaoAcessoria(**obrigacao.model_dump(), empresa_id=empresa_id)
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao