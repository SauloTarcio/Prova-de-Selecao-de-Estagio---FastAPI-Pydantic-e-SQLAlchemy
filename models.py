from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
     __tablename__ = "Empresas"

     id = Column(Integer, primary_key=True, index=True)
     nome = Column(String, index=True)
     cnpj = Column(String(14), unique=True, index=True)
     endereço = Column(String, index=True)
     email = Column(String, index=True)
     telefone = Column(String, index=True)

     obrigações = relationship("ObrigacaoAcessoria", back_populates="Empresas")

class ObrigacaoAcessoria(Base):
     __tablename__ = "obrigacoes_acessorias"

     id = Column(Integer, primary_key=True, index=True)
     nome = Column(String, index=True)
     peridiciosidade = Column(String)
     empresa_id = Column(Integer, ForeignKey("empresa.id"))

     empresa = relationship("Empresa", back_populates="obrigacoes")