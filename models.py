from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
     __tablename__ = "empresas"

     id = Column(Integer, primary_key=True, index=True)
     nome = Column(String, index=True)
     cnpj = Column(String(14), unique=True, index=True)
     endereco = Column(String, index=True)
     email = Column(String, index=True)
     telefone = Column(String, index=True)

     obrigacoes = relationship("ObrigacaoAcessoria", back_populates="Empresa")

class ObrigacaoAcessoria(Base):
     __tablename__ = "obrigacoes_acessorias"

     id = Column(Integer, primary_key=True, index=True)
     nome = Column(String, index=True)
     periodicidade = Column(String, nullable=False)
     empresa_id = Column(Integer, ForeignKey("empresas.id"))

     empresa = relationship("Empresa", back_populates="obrigacoes")