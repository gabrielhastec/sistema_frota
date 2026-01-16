"""
Módulo de serviço de validação de viagem.

Contém regras de validação relacionadas à disponibilidade de motoristas,
veículos e compatibilidade de licenças para realização de viagens.
"""

from datetime import datetime
from uuid import UUID
from app.domain.entities.motorista import Motorista
from app.domain.entities.veiculo import Veiculo

class ValidacaoViagemService:
    """
    Serviço responsável por validar regras de negócio para viagens.
    """

    def validar_disponibilidade_motorista(
        self,
        motorista_id: UUID,
        data_inicio: datetime,
        data_fim: datetime,
    ) -> bool:
        """
        Verifica se o motorista está disponível no período informado.

        A validação deve considerar viagens já agendadas ou em andamento
        associadas ao motorista.

        Args:
            motorista_id (UUID): Identificador único do motorista.
            data_inicio (datetime): Data e hora de início do período.
            data_fim (datetime): Data e hora de fim do período.

        Returns:
            bool: True se o motorista estiver disponível, False caso contrário.
        """
        # Implementar lógica utilizando repositório de viagens
        raise NotImplementedError(
            "Validação de disponibilidade do motorista não implementada."
        )
    
    def validar_disponibilidade_veiculo(
        self,
        veiculo_id: UUID,
        data_inicio: datetime,
        data_fim: datetime,
    ) -> bool:
        """
        Verifica se o veículo está disponível no período informado.

        A validação deve considerar manutenções programadas ou viagens
        já associadas ao veículo.

        Args:
            veiculo_id (UUID): Identificador único do veículo.
            data_inicio (datetime): Data e hora de início do período.
            data_fim (datetime): Data e hora de fim do período.

        Returns:
            bool: True se o veículo estiver disponível, False caso contrário.
        """
       
       # Implementar lógica utilizando repositório de viagens/manutenções
        raise NotImplementedError(
            "Validação de disponibilidade do veículo não implementada."
        )
    
    def validar_licencas(
        self, 
        motorista: Motorista, 
        veiculo: Veiculo
    ) -> bool:
        """
        Valida se o motorista possui habilitação compatível com o veículo.

        Args:
            motorista (Motorista): Motorista a ser validado.
            veiculo (Veiculo): Veículo que será conduzido.

        Returns:
            bool: True se o motorista estiver habilitado, False caso contrário.
        """
        return veiculo.tipo in motorista.tipos_cnh_habilitados
