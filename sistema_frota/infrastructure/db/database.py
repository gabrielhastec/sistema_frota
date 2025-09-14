"""Módulo de gerenciamento de conexão com o banco de dados do sistema de frota.

Este módulo fornece funcionalidades para estabelecer conexão com o banco de dados
SQLite utilizado pelo sistema de frota. A conexão é gerenciada de forma centralizada,
garantindo consistência e reutilização em outras partes do sistema.
"""

import sqlite3

# Nome do arquivo do banco de dados SQLite
DB_NAME = "sistema_frota.db"

def get_connection() -> sqlite3.Connection:
    """Estabelece uma conexão com o banco de dados SQLite.

    Cria e retorna uma conexão com o banco de dados especificado pela constante
    DB_NAME. A conexão é configurada para uso em operações de leitura e escrita.

    Returns:
        sqlite3.Connection: Objeto de conexão com o banco de dados SQLite.

    Raises:
        sqlite3.Error: Se houver falha ao conectar ao banco de dados, como
            permissões insuficientes ou arquivo de banco corrompido.
    """
    return sqlite3.connect(DB_NAME)
