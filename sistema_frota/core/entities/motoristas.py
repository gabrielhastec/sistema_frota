"""Módulo para gerenciamento de motoristas.

Este módulo define a classe Motorista, que representa um motorista com informações
básicas como identificador, nome, CNH e status de ativação. Ele fornece métodos
para ativar e desativar o motorista, além de consultar suas informações.
"""

class Motorista:
    """Representa um motorista com informações básicas e status de ativação.

    Atributos:
        motorista_id (int): Identificador único do motorista.
        nome (str): Nome completo do motorista.
        cnh (str): Número da Carteira Nacional de Habilitação.
        ativo (bool): Indica se o motorista está ativo (padrão: True).
    """

    def __init__(self, motorista_id: int, nome: str, cnh: str, ativo: bool = True):
        """Inicializa uma nova instância da classe Motorista.

        Args:
            motorista_id (int): Identificador único do motorista.
            nome (str): Nome completo do motorista.
            cnh (str): Número da Carteira Nacional de Habilitação.
            ativo (bool, opcional): Status de ativação do motorista. Padrão é True.

        Raises:
            ValueError: Se motorista_id for negativo ou se nome ou cnh forem vazios.
        """
        if motorista_id < 0:
            raise ValueError("O ID do motorista não pode ser negativo.")
        if not nome.strip():
            raise ValueError("O nome do motorista não pode ser vazio.")
        if not cnh.strip():
            raise ValueError("A CNH do motorista não pode ser vazia.")

        self.motorista_id = motorista_id
        self.nome = nome
        self.cnh = cnh
        self.ativo = ativo

    def desativar(self):
        """Desativa o motorista, alterando seu status para inativo.

        Returns:
            None
        """
        self.ativo = False

    def ativar(self):
        """Ativa o motorista, alterando seu status para ativo.

        Returns:
            None
        """
        self.ativo = True

    def obter_informacoes(self):
        """Retorna as informações do motorista em formato de dicionário.

        Returns:
            dict: Dicionário contendo motorista_id, nome, cnh e status ativo.
        """
        return {
            "motorista_id": self.motorista_id,
            "nome": self.nome,
            "cnh": self.cnh,
            "ativo": self.ativo
        }
