


from enum import Enum
from typing import List

from app.domain.value_objects.veiculo.tipo_veiculo import TipoVeiculo

class TipoCNH(Enum):
    """Tipos de Carteira Nacional de Habilitação"""
    A = "A"  # Motos
    B = "B"  # Carros
    C = "C"  # Caminhões
    D = "D"  # Ônibus
    E = "E"  # Carreta/Combinações
    
    def pode_dirigir(self, tipo_veiculo: 'TipoVeiculo') -> bool:
        """Verifica se esta CNH permite dirigir o tipo de veículo"""
        cnhs_aceitas = TipoVeiculo.get_cnh_requerida(tipo_veiculo)
        return self in cnhs_aceitas
    
    @classmethod
    def get_hierarquia(cls, tipo_cnh: 'TipoCNH') -> List['TipoCNH']:
        """Retorna hierarquia de CNHs (CNHs superiores podem conduzir inferiores)"""
        hierarquia = {
            cls.A: [cls.A],
            cls.B: [cls.A, cls.B],
            cls.C: [cls.B, cls.C],
            cls.D: [cls.B, cls.D],
            cls.E: [cls.B, cls.C, cls.D, cls.E],
        }
        return hierarquia.get(tipo_cnh, [])
    