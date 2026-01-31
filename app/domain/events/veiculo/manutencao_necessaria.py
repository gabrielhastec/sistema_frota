"""
Módulo de Eventos de Manutenção de Veículos.

Define os eventos de domínio relacionados à manutenção de veículos,
utilizados para sinalizar a necessidade de ações preventivas ou
corretivas com base em quilometragem, tempo ou condição de uso.
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from enum import Enum

class TipoManutencao(Enum):
    """
    Enumeração que representa os tipos de manutenção
    que podem gerar eventos no sistema.
    """

    PREVENTIVA = "preventiva"
    CORRETIVA = "corretiva"
    TROCA_OLEO = "troca_oleo"
    REVISAO_PERIODICA = "revisao_periodica"

@dataclass
class ManutencaoNecessaria:
    """
    Evento de domínio disparado quando um veículo
    necessita de manutenção.

    Este evento deve ser publicado sempre que uma regra
    de negócio identificar que o veículo atingiu um ponto
    crítico de manutenção.
    """
    veiculo_id: UUID                  # Identificador único do veículo associado ao evento
    km_atual: float                   # Quilometragem atual do veículo
    km_ultima_manutencao: float       # Quilometragem registrada na última manutenção
    km_proxima_manutencao: float      # Quilometragem prevista para a próxima manutenção
    data_alerta: datetime             # Data e hora em que o evento foi gerado
    tipo_manutencao: TipoManutencao   # Tipo de manutenção que motivou o evento
    criticidade: str                  # Nível de criticidade do evento: "baixa", "media" ou "alta"
    descricao: str                    # Descrição detalhada do motivo da geração do evento
