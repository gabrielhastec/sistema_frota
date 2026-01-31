"""Define os tipos de veículos conforme a legislação brasileira."""

from enum import Enum
from typing import Set

from app.domain.value_objects.motorista.tipo_cnh import TipoCNH

class TipoVeiculo(Enum):
    """Tipos de veículos baseados na legislação brasileira"""
    MOTOCICLETA = "motocicleta"      # Requer CNH A
    CARRO = "carro"                  # Requer CNH B
    CAMINHONETE = "caminhonete"      # Requer CNH B
    CAMINHAO = "caminhao"            # Requer CNH C
    ONIBUS = "onibus"                # Requer CNH D
    CAMINHAO_PESADO = "caminhao_pesado"  # Requer CNH E
    VAN = "van"                      # Requer CNH B ou D dependendo da capacidade
    UTILITARIO = "utilitario"        # Requer CNH B
    
    @classmethod
    def get_cnh_requerida(cls, tipo_veiculo: 'TipoVeiculo') -> Set['TipoCNH']:
        """Retorna os tipos de CNH que podem conduzir este veículo"""
        mapping = {
            cls.MOTOCICLETA: {TipoCNH.A},
            cls.CARRO: {TipoCNH.B},
            cls.CAMINHONETE: {TipoCNH.B},
            cls.VAN: {TipoCNH.B, TipoCNH.D},
            cls.UTILITARIO: {TipoCNH.B},
            cls.CAMINHAO: {TipoCNH.C},
            cls.ONIBUS: {TipoCNH.D},
            cls.CAMINHAO_PESADO: {TipoCNH.E},
        }
        return mapping.get(tipo_veiculo, set())
    