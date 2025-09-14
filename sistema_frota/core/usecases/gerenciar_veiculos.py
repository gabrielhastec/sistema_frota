"""Módulo para gerenciamento de veículos no sistema de frota.

Este módulo define a classe GerenciarVeiculos, responsável por operações de
cadastro, listagem, ativação e desativação de veículos, utilizando um repositório
para interação com os dados.
"""

from sistema_frota.core.entities.veiculo import Veiculo
from datetime import datetime

class GerenciarVeiculos:
    """Gerencia operações relacionadas a veículos no sistema de frota.

    Atributos:
        repo: Repositório responsável por interagir com os dados dos veículos.
    """

    def __init__(self, repo):
        """Inicializa uma nova instância da classe GerenciarVeiculos.

        Args:
            repo: Repositório que gerencia a persistência dos dados dos veículos.

        Raises:
            TypeError: Se o repositório fornecido for None.
        """
        if repo is None:
            raise TypeError("O repositório não pode ser None.")
        self.repo = repo

    def cadastrar_veiculo(self, placa: str, modelo: str, ano: int):
        """Cadastra um novo veículo no sistema.

        Args:
            placa (str): Placa do veículo.
            modelo (str): Modelo do veículo.
            ano (int): Ano de fabricação do veículo.

        Returns:
            Veiculo: Instância do veículo criado.

        Raises:
            ValueError: Se placa ou modelo forem vazios, ou se o ano for inválido
                        (menor que 1900 ou maior que o ano atual).
        """
        current_year = datetime.now().year
        if not placa.strip():
            raise ValueError("A placa do veículo não pode ser vazia.")
        if not modelo.strip():
            raise ValueError("O modelo do veículo não pode ser vazio.")
        if ano < 1900 or ano > current_year:
            raise ValueError(f"O ano deve estar entre 1900 e {current_year}.")
        return self.repo.criar(placa, modelo, ano)

    def listar_veiculos(self):
        """Retorna uma lista de todos os veículos cadastrados.

        Returns:
            list: Lista de instâncias de Veiculo.
        """
        return self.repo.listar()

    def ativar_veiculo(self, veiculo_id: int):
        """Ativa um veículo com base no seu ID.

        Args:
            veiculo_id (int): Identificador único do veículo.

        Returns:
            Veiculo: Instância do veículo ativado.

        Raises:
            ValueError: Se veiculo_id for negativo.
        """
        if veiculo_id < 0:
            raise ValueError("O ID do veículo não pode ser negativo.")
        return self.repo.ativar(veiculo_id)

    def desativar_veiculo(self, veiculo_id: int):
        """Desativa um veículo com base no seu ID.

        Args:
            veiculo_id (int): Identificador único do veículo.

        Returns:
            Veiculo: Instância do veículo desativado.

        Raises:
            ValueError: Se veiculo_id for negativo.
        """
        if veiculo_id < 0:
            raise ValueError("O ID do veículo não pode ser negativo.")
        return self.repo.desativar(veiculo_id)
