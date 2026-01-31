"""
Módulo de entidade Manutenção.

Define a entidade Manutenção, responsável por registrar os serviços realizados
em um veículo, incluindo a quilometragem, data e tipo de serviço.
"""

from datetime import datetime

class Manutencao:
    """
    Representa uma manutenção realizada em um veículo.

    A entidade Manutencao armazena os detalhes de uma manutenção, incluindo
    o tipo de serviço, a quilometragem do veículo no momento da manutenção
    e a data em que o serviço foi realizado.

    Attributes:
        km_veiculo (float): Quilometragem do veículo no momento da manutenção.
        tipo_servico (str): Tipo de serviço realizado (troca de óleo, revisão, etc.).
        data (datetime): Data da manutenção.
        custo (float): Custo da manutenção.
    """

    # Métodos para manipulação da manutenção
    def __init__(self, km_veiculo: float, tipo_servico: str, custo: float):
        """
        Inicializa um novo registro de manutenção.

        Args:
            km_veiculo (float): Quilometragem do veículo no momento da manutenção.
            tipo_servico (str): Tipo de serviço realizado na manutenção.
            custo (float): Custo total da manutenção.
        """
        self.km_veiculo = km_veiculo
        self.tipo_servico = tipo_servico
        self.data = datetime.now()
        self.custo = custo
