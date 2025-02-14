from enum import Enum
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from schemas import PeriodicidadeEnum

class Empresa(Base):
     __tablename__ = "Empresas"

     id = Column(Integer, primary_key=True, index=True)
     nome = Column(String, index=True)
     cnpj = Column(String(14), unique=True, index=True)
     endereco = Column(String, index=True)
     email = Column(String, index=True)
     telefone = Column(String, index=True)

     obrigacoes = relationship("ObrigacaoAcessoria", back_populates="Empresas")

class ObrigacaoAcessoria(Base):
     __tablename__ = "obrigacoes_acessorias"

     id = Column(Integer, primary_key=True, index=True)
     nome = Column(String, index=True)
     peridiciosidade = Column(Enum(PeriodicidadeEnum), nullable=False)
     empresa_id = Column(Integer, ForeignKey("empresa.id"))

     empresa = relationship("Empresa", back_populates="obrigacoes")