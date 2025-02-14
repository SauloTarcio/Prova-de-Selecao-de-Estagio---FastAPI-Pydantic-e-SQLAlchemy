from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional

class Peridiciosidade(str, Enum):
    mensal = "Mensal"
    trimestral = "Trimestral"
    anual = "Anual"

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    peridiciosidade: Peridiciosidade

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    pass

class ObrigacaoAcessoria(ObrigacaoAcessoriaBase):
    id: int
    empresa_id: int
    
    class config:
        from_attributes = True

class EmpresaBase(BaseModel):
    nome: str
    cpnj: str = Field(..., min_length=14, max_length=14, regex="^\d{14}$")
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