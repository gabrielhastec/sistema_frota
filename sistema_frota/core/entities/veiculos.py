"""Módulo para gerenciamento de veículos.

Este módulo define a classe Veiculo, que representa um veículo com informações
como identificador, placa, modelo, ano, quilometragem e status de ativação.
Fornece métodos para atualizar a quilometragem, ativar e desativar o veículo,
além de consultar suas informações.
"""

class Veiculo:
    """Representa um veículo com informações básicas e status de ativação.

    Atributos:
        veiculo_id (int): Identificador único do veículo.
        placa (str): Placa do veículo.
        modelo (str): Modelo do veículo.
        ano (int): Ano de fabricação do veículo.
        km (float): Quilometragem atual do veículo.
        ativo (bool): Indica se o veículo está ativo (padrão: True).
    """

    def __init__(self, veiculo_id: int, placa: str, modelo: str, ano: int, km: float = 0, ativo: bool = True):
        """Inicializa uma nova instância da classe Veiculo.

        Args:
            veiculo_id (int): Identificador único do veículo.
            placa (str): Placa do veículo.
            modelo (str): Modelo do veículo.
            ano (int): Ano de fabricação do veículo.
            km (float, opcional): Quilometragem inicial do veículo. Padrão é 0.
            ativo (bool, opcional): Status de ativação do veículo. Padrão é True.

        Raises:
            ValueError: Se veiculo_id for negativo, placa ou modelo forem vazios,
                        ano for inválido (menor que 1900 ou maior que o ano atual),
                        ou km for negativo.
        """
        from datetime import datetime
        current_year = datetime.now().year

        if veiculo_id < 0:
            raise ValueError("O ID do veículo não pode ser negativo.")
        if not placa.strip():
            raise ValueError("A placa do veículo não pode ser vazia.")
        if not modelo.strip():
            raise ValueError("O modelo do veículo não pode ser vazio.")
        if ano < 1900 or ano > current_year:
            raise ValueError(f"O ano deve estar entre 1900 e {current_year}.")
        if km < 0:
            raise ValueError("A quilometragem não pode ser negativa.")

        self.veiculo_id = veiculo_id
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.km = km
        self.ativo = ativo

    def atualizar_km(self, km: float):
        """Atualiza a quilometragem do veículo.

        Args:
            km (float): Nova quilometragem do veículo.

        Raises:
            ValueError: Se a quilometragem fornecida for negativa.

        Returns:
            None
        """
        if km < 0:
            raise ValueError("A quilometragem não pode ser negativa.")
        self.km = km

    def desativar(self):
        """Desativa o veículo, alterando seu status para inativo.

        Returns:
            None
        """
        self.ativo = False

    def ativar(self):
        """Ativa o veículo, alterando seu status para ativo.

        Returns:
            None
        """
        self.ativo = True

    def obter_informacoes(self):
        """Retorna as informações do veículo em formato de dicionário.

        Returns:
            dict: Dicionário contendo veiculo_id, placa, modelo, ano, km e status ativo.
        """
        return {
            "veiculo_id": self.veiculo_id,
            "placa": self.placa,
            "modelo": self.modelo,
            "ano": self.ano,
            "km": self.km,
            "ativo": self.ativo
        }
