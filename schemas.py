from pydantic import BaseModel, Field
from typing import List

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    pass

class ObrigacaoAcessoria(ObrigacaoAcessoriaBase):
    id: int
    empresa_id: int
    
    class config:
        from_attributes = True

class EmpresaBase(BaseModel):
    nome: str
    cpnj: str = Field(..., min_length=14, max_length=14, pattern=r"^\d{14}$")
    endereco: str
    email: str
    telefone: str

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int
    obrigacoes: List["ObrigacaoAcessoria"] = []

    class config:
        from_attributes = True