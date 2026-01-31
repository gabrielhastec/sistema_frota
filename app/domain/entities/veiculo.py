"""
Módulo de entidade Veículo.

Define a entidade Veiculo, responsável por representar um veículo,
seu hodômetro atual e o histórico de manutenções realizadas.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict
from uuid import UUID, uuid4

from ..value_objects.veiculo.manutencao import Manutencao
from ..value_objects.veiculo.placa import Placa
from ..value_objects.veiculo.tipo_combustivel import TipoCombustivel
from ..value_objects.veiculo.tipo_veiculo import TipoVeiculo
from ..events.veiculo.manutencao_necessaria import ManutencaoNecessaria, TipoManutencao

class Veiculo:
    """
    Representa um veículo e seu histórico de manutenções.

    Attributes:
        km_atual (float): Quilometragem atual do veículo.
        manutencoes (List[Manutencao]): Lista de manutenções registradas.
    """
    def __init__(self, km_atual: float):
        """
        Inicializa uma instância de Veiculo.

        Args:
            km_atual (float): Quilometragem atual do veículo.
        """
        self.km_atual: float = km_atual
        self.manutencoes: List[Manutencao] = []
    
    # Adiciona manutenção ao veículo
    def adicionar_manutencao(self, manutencao: Manutencao):
        """
        Registra uma nova manutenção no histórico do veículo.

        Args:
            manutencao (Manutencao): Objeto de manutenção a ser registrado.
        """
        self.manutencoes.append(manutencao)
    
    # Calcula próximo KM para manutenção
    def proxima_manutencao_km(self, intervalo_km: float) -> float:
        """
        Calcula a quilometragem prevista para a próxima manutenção.

        Caso não exista manutenção registrada, considera a quilometragem
        atual do veículo como base.

        Args:
            intervalo_km (float): Intervalo de quilometragem entre manutenções.

        Returns:
            float: Quilometragem estimada para a próxima manutenção.
        """
        if not self.manutencoes:
            return self.km_atual + intervalo_km
        
        ultima_km = max(m.km_veiculo for m in self.manutencoes)
        return ultima_km + intervalo_km
    