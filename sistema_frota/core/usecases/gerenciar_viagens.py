"""Módulo para gerenciamento de viagens no sistema de frota.

Este módulo define a classe `GerenciarViagens`, que encapsula a lógica de negócios
para registro, finalização e listagem de viagens. A classe utiliza um repositório
para operações de persistência de dados, garantindo modularidade e separação de
responsabilidades.
"""

from sistema_frota.core.entities.viagem import Viagem
from datetime import datetime

class GerenciarViagens:
    """Classe para gerenciamento de operações relacionadas a viagens no sistema.

    Responsável por coordenar o registro, finalização e consulta de viagens,
    utilizando um repositório para acesso a dados. Garante a integridade das
    operações e fornece uma interface clara para interação com o sistema.

    Attributes:
        repo: Repositório de viagens que implementa operações de persistência.
    """

    def __init__(self, repo):
        """Inicializa a classe com um repositório de viagens.

        Args:
            repo: Instância do repositório de viagens para operações de dados.
        """
        self.repo = repo

    def registrar_viagem(self, motorista_id: int, veiculo_id: int, origem: str, destino: str, km_inicial: float) -> Viagem:
        """Registra uma nova viagem no sistema.

        Cria uma nova entrada de viagem com base nos parâmetros fornecidos,
        delegando a persistência ao repositório.

        Args:
            motorista_id (int): Identificador único do motorista.
            veiculo_id (int): Identificador único do veículo.
            origem (str): Local de origem da viagem.
            destino (str): Local de destino da viagem.
            km_inicial (float): Quilometragem inicial do veículo.

        Returns:
            Viagem: Objeto representando a viagem recém-criada.

        Raises:
            ValueError: Se os parâmetros forem inválidos (ex.: km_inicial negativo).
            TypeError: Se os tipos dos parâmetros não corresponderem aos esperados.
        """
        return self.repo.criar(motorista_id, veiculo_id, origem, destino, km_inicial)

    def finalizar_viagem(self, viagem_id: int, km_final: float) -> Viagem:
        """Finaliza uma viagem existente com a quilometragem final.

        Atualiza a viagem especificada com a quilometragem final, marcando-a como
        concluída no repositório.

        Args:
            viagem_id (int): Identificador único da viagem.
            km_final (float): Quilometragem final do veículo.

        Returns:
            Viagem: Objeto da viagem atualizado após a finalização.

        Raises:
            ValueError: Se o viagem_id não existir ou km_final for inválido.
            TypeError: Se os tipos dos parâmetros não corresponderem aos esperados.
        """
        return self.repo.finalizar(viagem_id, km_final)

    def listar_viagens(self) -> list[Viagem]:
        """Recupera a lista de todas as viagens registradas.

        Consulta o repositório para obter todas as viagens armazenadas.

        Returns:
            list[Viagem]: Lista contendo todos os objetos Viagem registrados.
        """
        return self.repo.listar()
