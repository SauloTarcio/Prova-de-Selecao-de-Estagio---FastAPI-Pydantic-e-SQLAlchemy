from sqlalchemy.orm import Session
import models, schemas

def create_empresa(db: Session, empresa: schemas.EmpresaCreate):
    db_empresa = models.Empresa(nome=empresa.nome, cnpj=empresa.cnpj, 
                                endereco=empresa.endereco, email=empresa.email, telefone=empresa.telefone)
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def obter_empresa(db: Session):
    return db.query(models.Empresa).all()

def obter_empresa_por_id(db: Session, empresa_id: int):
    return db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()

def update_empresa(db: Session, empresa_id: int, empresa: schemas.EmpresaCreate):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if db_empresa:
        db_empresa.nome = empresa.nome
        db_empresa.cnpj = empresa.cnpj
        db_empresa.endereco = empresa.endereco
        db_empresa.email = empresa.email
        db_empresa.telefone = empresa.telefone
        db.commit()
        db.refresh(db_empresa)
        return db_empresa
    return None
    
def delete_empresa(db: Session, empresa_id: int):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if db_empresa:
        db.delete(db_empresa)
        db.commit()
        return db_empresa
    return None

def create_obrigacao(db: Session, obrigacao: schemas.ObrigacaoAcessoriaCreate, empresa_id: int):
    db_obrigacao = models.ObrigacaoAcessoria(**obrigacao.model_dump(), empresa_id=empresa_id)
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

def obter_obrigacoes(db: Session, empresa_id: int):
    return db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.empresa_id == empresa_id).all()

def obter_obrigacao_por_id(db: Session, obrigacao_id: int):
    return db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()

def update_obrigacao(db: Session, obrigacao_id: int, obrigacao: schemas.ObrigacaoAcessoriaCreate):
    db_obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if db_obrigacao:
        db_obrigacao.nome = obrigacao.nome
        db_obrigacao.periodicidade = obrigacao.periodicidade
        db.commit()
        db.refresh(db_obrigacao)
        return db_obrigacao
    return None

def delete_obrigacao(db: Session, obrigacao_id: int):
    db_obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if db_obrigacao:
        db.delete(db_obrigacao)
        db.commit()
        return db_obrigacao
    return None