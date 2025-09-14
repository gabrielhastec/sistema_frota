"""Módulo para gerenciamento de viagens.

Este módulo define a classe Viagem, que representa uma viagem realizada por um motorista
em um veículo, incluindo informações como origem, destino, datas e quilometragem.
Fornece métodos para finalizar a viagem e consultar suas informações.
"""

from datetime import datetime

class Viagem:
    """Representa uma viagem com informações de motorista, veículo, trajeto e quilometragem.

    Atributos:
        viagem_id (int): Identificador único da viagem.
        motorista_id (int): Identificador do motorista associado à viagem.
        veiculo_id (int): Identificador do veículo associado à viagem.
        origem (str): Local de origem da viagem.
        destino (str): Local de destino da viagem.
        data_inicio (datetime): Data e hora de início da viagem.
        data_fim (datetime, opcional): Data e hora de término da viagem.
        km_inicial (float): Quilometragem inicial do veículo.
        km_final (float): Quilometragem final do veículo.
    """

    def __init__(self, viagem_id: int, motorista_id: int, veiculo_id: int, origem: str, destino: str,
                 data_inicio: datetime, data_fim: datetime = None, km_inicial: float = 0, km_final: float = 0):
        """Inicializa uma nova instância da classe Viagem.

        Args:
            viagem_id (int): Identificador único da viagem.
            motorista_id (int): Identificador do motorista.
            veiculo_id (int): Identificador do veículo.
            origem (str): Local de origem da viagem.
            destino (str): Local de destino da viagem.
            data_inicio (datetime): Data e hora de início da viagem.
            data_fim (datetime, opcional): Data e hora de término da viagem. Padrão é None.
            km_inicial (float, opcional): Quilometragem inicial do veículo. Padrão é 0.
            km_final (float, opcional): Quilometragem final do veículo. Padrão é 0.

        Raises:
            ValueError: Se viagem_id, motorista_id ou veiculo_id forem negativos,
                        origem ou destino forem vazios, data_inicio não for datetime,
                        ou km_inicial ou km_final forem negativos.
            TypeError: Se data_inicio ou data_fim (quando fornecido) não forem objetos datetime.
        """
        if viagem_id < 0:
            raise ValueError("O ID da viagem não pode ser negativo.")
        if motorista_id < 0:
            raise ValueError("O ID do motorista não pode ser negativo.")
        if veiculo_id < 0:
            raise ValueError("O ID do veículo não pode ser negativo.")
        if not origem.strip():
            raise ValueError("A origem da viagem não pode ser vazia.")
        if not destino.strip():
            raise ValueError("O destino da viagem não pode ser vazio.")
        if not isinstance(data_inicio, datetime):
            raise TypeError("A data de início deve ser um objeto datetime.")
        if data_fim is not None and not isinstance(data_fim, datetime):
            raise TypeError("A data de fim deve ser um objeto datetime.")
        if km_inicial < 0:
            raise ValueError("A quilometragem inicial não pode ser negativa.")
        if km_final < 0:
            raise ValueError("A quilometragem final não pode ser negativa.")

        self.viagem_id = viagem_id
        self.motorista_id = motorista_id
        self.veiculo_id = veiculo_id
        self.origem = origem
        self.destino = destino
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.km_inicial = km_inicial
        self.km_final = km_final

    def finalizar_viagem(self, data_fim: datetime, km_final: float):
        """Finaliza a viagem, definindo a data de término e a quilometragem final.

        Args:
            data_fim (datetime): Data e hora de término da viagem.
            km_final (float): Quilometragem final do veículo.

        Raises:
            TypeError: Se data_fim não for um objeto datetime.
            ValueError: Se km_final for negativo ou menor que km_inicial,
                        ou se data_fim for anterior à data_inicio.

        Returns:
            None
        """
        if not isinstance(data_fim, datetime):
            raise TypeError("A data de fim deve ser um objeto datetime.")
        if km_final < 0:
            raise ValueError("A quilometragem final não pode ser negativa.")
        if km_final < self.km_inicial:
            raise ValueError("A quilometragem final não pode ser menor que a inicial.")
        if data_fim < self.data_inicio:
            raise ValueError("A data de fim não pode ser anterior à data de início.")

        self.data_fim = data_fim
        self.km_final = km_final

    def obter_informacoes(self):
        """Retorna as informações da viagem em formato de dicionário.

        Returns:
            dict: Dicionário contendo viagem_id, motorista_id, veiculo_id, origem,
                  destino, data_inicio, data_fim, km_inicial e km_final.
        """
        return {
            "viagem_id": self.viagem_id,
            "motorista_id": self.motorista_id,
            "veiculo_id": self.veiculo_id,
            "origem": self.origem,
            "destino": self.destino,
            "data_inicio": self.data_inicio,
            "data_fim": self.data_fim,
            "km_inicial": self.km_inicial,
            "km_final": self.km_final
        }
