"""
Aggregate de Viagem.

Encapsula a lógica de negócio relacionada a viagens, motoristas e veículos,
incluindo validações de regras de negócio e geração de eventos de domínio.
"""

from datetime import datetime
from typing import List
from app.domain.entities.viagem import Viagem
from app.domain.entities.motorista import Motorista
from app.domain.entities.veiculo import Veiculo
from app.domain.events import (
    BusinessRuleViolation,
    DomainEvent,
    ViagemIniciada,
    ViagemEncerrada,
)

class ViagemAggregate:
    """
    Aggregate responsável por coordenar as regras de negócio de uma viagem.

    Este aggregate garante a consistência entre viagem, motorista e veículo,
    aplicando validações e emitindo eventos de domínio quando necessário.
    """

    def __init__(
        self,
        viagem: Viagem,
        motorista: Motorista,
        veiculo: Veiculo,
    ) -> None:
        """
        Inicializa o aggregate de viagem.

        Args:
            viagem: Entidade Viagem associada.
            motorista: Motorista responsável pela viagem.
            veiculo: Veículo utilizado na viagem.
        """
        self.viagem = viagem
        self.motorista = motorista
        self.veiculo = veiculo
    
    def iniciar_viagem(self) -> List[DomainEvent]:
        """
        Valida e inicia a viagem.

        Realiza as validações de regras de negócio necessárias e, caso todas
        sejam atendidas, inicia a viagem e gera os eventos de domínio
        correspondentes.

        Raises:
            BusinessRuleViolation: Se o motorista estiver inativo ou o veículo
                indisponível.

        Returns:
            Lista de eventos de domínio gerados durante a operação.
        """
        eventos: List[DomainEvent] = []
        
        # Validações
        if not self.motorista.ativo:
            raise BusinessRuleViolation("Motorista inativo")
        
        if not self.veiculo.disponivel:
            raise BusinessRuleViolation("Veículo indisponível")
        
        # Marca veículo como em uso
        self.veiculo.em_uso = True

        # Gera evento de viagem iniciada
        eventos.append(
            ViagemIniciada(
                viagem_id=self.viagem.id,
                motorista_id=self.motorista.id,
                veiculo_id=self.veiculo.id,
                data_inicio=datetime.now()
            )   
        )
        
        return eventos

    def finalizar_viagem(self) -> List[DomainEvent]:
        """
        Finaliza a viagem.
        Marca o veículo como disponível novamente e registra a data de fim da viagem.
        
        Raises:
            BusinessRuleViolation: Se a viagem já estiver finalizada ou cancelada.
        
        Returns:
            Lista de eventos de domínio gerados durante a operação.
        """
        eventos: List[DomainEvent] = []

        # Marca veículo como disponível
        self.veiculo.em_uso = False
        self.viagem.data_fim = datetime.now()
        self.viagem.status = "finalizada"

        # Gera evento de viagem encerrada
        eventos.append(
            ViagemEncerrada(
                viagem_id=self.viagem.id,
                data_fim=self.viagem.data_fim
            )
        )

        return eventos

    def cancelar_viagem(self, motivo: str) -> List[DomainEvent]:
        """
        Cancela a viagem.

        Marca o veículo como disponível novamente e registra o motivo do cancelamento.

        Args:
            motivo: Motivo do cancelamento da viagem.
        """
        self.veiculo.em_uso = False
        self.viagem.status = "cancelada"
        self.viagem.motivo_cancelamento = motivo

        # Gera evento de viagem cancelada
        return [
            ViagemEncerrada(
                viagem_id=self.viagem.id,
                data_fim=datetime.now()
            )
        ]
