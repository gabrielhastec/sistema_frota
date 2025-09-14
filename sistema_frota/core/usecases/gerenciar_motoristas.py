"""Módulo para gerenciamento de motoristas no sistema de frota.

Este módulo define a classe GerenciarMotoristas, responsável por operações de
cadastro, listagem, ativação e desativação de motoristas, utilizando um repositório
para interação com os dados.
"""

from sistema_frota.core.entities.motorista import Motorista

class GerenciarMotoristas:
    """Gerencia operações relacionadas a motoristas no sistema de frota.

    Atributos:
        repo: Repositório responsável por interagir com os dados dos motoristas.
    """

    def __init__(self, repo):
        """Inicializa uma nova instância da classe GerenciarMotoristas.

        Args:
            repo: Repositório que gerencia a persistência dos dados dos motoristas.

        Raises:
            TypeError: Se o repositório fornecido for None.
        """
        if repo is None:
            raise TypeError("O repositório não pode ser None.")
        self.repo = repo

    def cadastrar_motorista(self, nome: str, cnh: str):
        """Cadastra um novo motorista no sistema.

        Args:
            nome (str): Nome completo do motorista.
            cnh (str): Número da Carteira Nacional de Habilitação.

        Returns:
            Motorista: Instância do motorista criado.

        Raises:
            ValueError: Se nome ou cnh forem vazios.
        """
        if not nome.strip():
            raise ValueError("O nome do motorista não pode ser vazio.")
        if not cnh.strip():
            raise ValueError("A CNH do motorista não pode ser vazia.")
        return self.repo.criar(nome, cnh)

    def listar_motoristas(self):
        """Retorna uma lista de todos os motoristas cadastrados.

        Returns:
            list: Lista de instâncias de Motorista.
        """
        return self.repo.listar()

    def ativar_motorista(self, motorista_id: int):
        """Ativa um motorista com base no seu ID.

        Args:
            motorista_id (int): Identificador único do motorista.

        Returns:
            Motorista: Instância do motorista ativado.

        Raises:
            ValueError: Se motorista_id for negativo.
        """
        if motorista_id < 0:
            raise ValueError("O ID do motorista não pode ser negativo.")
        return self.repo.ativar(motorista_id)

    def desativar_motorista(self, motorista_id: int):
        """Desativa um motorista com base no seu ID.

        Args:
            motorista_id (int): Identificador único do motorista.

        Returns:
            Motorista: Instância do motorista desativado.

        Raises:
            ValueError: Se motorista_id for negativo.
        """
        if motorista_id < 0:
            raise ValueError("O ID do motorista não pode ser negativo.")
        return self.repo.desativar(motorista_id)
