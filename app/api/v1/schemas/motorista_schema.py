
from pydantic import BaseModel, validator
from datetime import date
from typing import Optional

class MotoristaCreate(BaseModel):
    nome: str
    cpf: str
    cnh_numero: str
    cnh_categoria: str
    cnh_validade: date
    
    @validator('cpf')
    def validate_cpf(cls, v):
        # Validação de CPF
        return v
    
    @validator('cnh_categoria')
    def validate_cnh_categoria(cls, v):
        categorias_validas = ['A', 'B', 'C', 'D', 'E']
        if v.upper() not in categorias_validas:
            raise ValueError('Categoria de CNH inválida')
        return v.upper()
    