"""Módulo para interface de menu do sistema de frota.

Este módulo define a classe `Menu`, que fornece uma interface de linha de comando
interativa para gerenciar motoristas, veículos e viagens no sistema de frota.
A classe integra os casos de uso de gerenciamento, utilizando repositórios SQLite
para persistência de dados, e permite ao usuário navegar pelas opções disponíveis.
"""

from sistema_frota.core.usecases.gerenciar_motoristas import GerenciarMotoristas
from sistema_frota.core.usecases.gerenciar_veiculos import GerenciarVeiculos
from sistema_frota.core.usecases.gerenciar_viagens import GerenciarViagens
from sistema_frota.infrastructure.repositories.motorista_repo import MotoristaRepositorySQLite
from sistema_frota.infrastructure.repositories.veiculo_repo import VeiculoRepositorySQLite
from sistema_frota.infrastructure.repositories.viagem_repo import ViagemRepositorySQLite

class Menu:
    """Classe responsável por exibir e gerenciar o menu interativo do sistema de frota.

    Inicializa os casos de uso para motoristas, veículos e viagens, utilizando
    repositórios SQLite, e fornece uma interface de linha de comando para interação
    com o usuário.

    Attributes:
        motoristas (GerenciarMotoristas): Instância para gerenciar operações de motoristas.
        veiculos (GerenciarVeiculos): Instância para gerenciar operações de veículos.
        viagens (GerenciarViagens): Instância para gerenciar operações de viagens.
    """

    def __init__(self) -> None:
        """Inicializa a classe Menu com os casos de uso e repositórios necessários.

        Configura as instâncias de `GerenciarMotoristas`, `GerenciarVeiculos` e
        `GerenciarViagens`, conectando-as aos respectivos repositórios SQLite.
        """
        self.motoristas = GerenciarMotoristas(MotoristaRepositorySQLite())
        self.veiculos = GerenciarVeiculos(VeiculoRepositorySQLite())
        self.viagens = GerenciarViagens(ViagemRepositorySQLite())

    def exibir(self) -> None:
        """Exibe o menu interativo e gerencia as opções selecionadas pelo usuário.

        Apresenta um menu em loop com opções para gerenciar motoristas, veículos,
        viagens ou sair do sistema. Processa a entrada do usuário e chama os métodos
        apropriados dos casos de uso.

        Returns:
            None: A função não retorna valores, apenas gerencia a interação com o usuário.

        Raises:
            KeyboardInterrupt: Se o usuário interromper a execução (Ctrl+C).
            Exception: Para erros inesperados durante a interação com os repositórios.
        """
        while True:
            
            # Exibe o menu principal
            print("\n--- Sistema de Frota ---")
            print("1. Gerenciar Motoristas")
            print("2. Gerenciar Veículos")
            print("3. Gerenciar Viagens")
            print("0. Sair")

            # Captura a opção do usuário
            opcao = input("Escolha uma opção: ")

            # Processa a opção selecionada
            if opcao == "1":
                print(self.motoristas.listar_motoristas())
            elif opcao == "2":
                print(self.veiculos.listar_veiculos())
            elif opcao == "3":
                print(self.viagens.listar_viagens())
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")
