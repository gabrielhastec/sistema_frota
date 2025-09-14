"""Módulo principal para inicialização do sistema de frota.

Este módulo serve como ponto de entrada do sistema, inicializando o esquema do banco
de dados e exibindo o menu interativo para o usuário. Ele integra os componentes de
infraestrutura e interface para proporcionar a funcionalidade completa do sistema.
"""

from sistema_frota.infrastructure.db.schema import criar_tabelas
from sistema_frota.interface.menu import Menu

def main() -> None:
    """Função principal para execução do sistema de frota.

    Inicializa o esquema do banco de dados chamando a função `criar_tabelas` e
    instancia o menu interativo, chamando o método `exibir` para começar a interação
    com o usuário.

    Returns:
        None: A função não retorna valores, apenas executa a inicialização e exibição
            do menu.

    Raises:
        sqlite3.Error: Se houver falha na criação das tabelas do banco de dados.
        KeyboardInterrupt: Se o usuário interromper a execução (Ctrl+C).
        Exception: Para erros inesperados durante a inicialização ou execução do menu.
    """
    # Inicializa o esquema do banco de dados
    criar_tabelas()

    # Cria uma instância do menu interativo
    menu = Menu()

    # Exibe o menu para interação com o usuário
    menu.exibir()

if __name__ == "__main__":
    main()
