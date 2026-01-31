"""
Módulo de entidade Viagem.

Define a entidade Viagem, responsável por representar uma viagem realizada,
contendo informações sobre o veículo, o motorista e o status da viagem.
"""

from datetime import datetime
from app.domain.entities.motorista import Motorista
from app.domain.entities.veiculo import Veiculo

class Viagem:
    """
    Representa uma viagem realizada.

    A entidade Viagem armazena os dados da viagem, como o motorista,
    o veículo utilizado, o momento de início e fim, e o status da viagem.

    Attributes:
        motorista (Motorista): Motorista que realizou a viagem.
        veiculo (Veiculo): Veículo utilizado na viagem.
        data_inicio (datetime): Data e hora de início da viagem.
        data_fim (datetime): Data e hora de fim da viagem.
        status (str): Status da viagem (iniciada, em andamento, concluída).
    """

    # Métodos para manipulação da viagem
    def __init__(self, motorista: Motorista, veiculo: Veiculo):
        """
        Inicializa uma nova viagem.

        Args:
            motorista (Motorista): Motorista que realiza a viagem.
            veiculo (Veiculo): Veículo utilizado na viagem.
        """
        self.motorista = motorista
        self.veiculo = veiculo
        self.data_inicio = None
        self.data_fim = None
        self.status = "não iniciada"

    # Método para iniciar a viagem
    def iniciar(self):
        """Inicia a viagem, registrando o momento de início e alterando o status."""
        if self.status != "não iniciada":
            raise ValueError("Viagem já foi iniciada ou concluída")
        self.data_inicio = datetime.now()
        self.status = "iniciada"

    # Método para finalizar a viagem
    def finalizar(self):
        """Finaliza a viagem, registrando o momento de término e alterando o status."""
        if self.status != "iniciada":
            raise ValueError("Viagem não foi iniciada ou já foi concluída")
        self.data_fim = datetime.now()
        self.status = "concluída"
