"""Módulo para gerenciamento de motoristas no banco de dados SQLite do sistema de frota.

Este módulo define a classe `MotoristaRepositorySQLite`, que encapsula operações de
persistência para motoristas, incluindo criação, listagem, ativação e desativação.
As operações são realizadas utilizando a conexão com o banco de dados SQLite fornecida
pelo módulo `database`.
"""

from sistema_frota.infrastructure.db.database import get_connection
from typing import List, Tuple

class MotoristaRepositorySQLite:
    """Repositório para gerenciamento de motoristas no banco de dados SQLite.

    Fornece métodos para criar, listar, ativar e desativar motoristas, interagindo
    diretamente com a tabela `motoristas` no banco de dados SQLite.
    """

    def criar(self, nome: str, cnh: str) -> None:
        """Cria um novo motorista no banco de dados.

        Insere um novo registro na tabela `motoristas` com o nome e a CNH fornecidos.
        O campo `ativo` é definido como 1 por padrão.

        Args:
            nome (str): Nome do motorista.
            cnh (str): Número da Carteira Nacional de Habilitação do motorista.

        Raises:
            sqlite3.Error: Se houver falha na execução da query, como problemas de
                conexão ou violação de restrições do banco de dados.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO motoristas (nome, cnh) VALUES (?, ?)", (nome, cnh))
        conn.commit()
        conn.close()

    def listar(self) -> List[Tuple[int, str, str, int]]:
        """Lista todos os motoristas registrados no banco de dados.

        Recupera todos os registros da tabela `motoristas`, incluindo ID, nome, CNH
        e status de ativação.

        Returns:
            List[Tuple[int, str, str, int]]: Lista de tuplas contendo os dados dos
                motoristas (motorista_id, nome, cnh, ativo).

        Raises:
            sqlite3.Error: Se houver falha na execução da query, como problemas de
                conexão com o banco de dados.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT motorista_id, nome, cnh, ativo FROM motoristas")
        motoristas = cursor.fetchall()
        conn.close()
        return motoristas

    def ativar(self, motorista_id: int) -> None:
        """Ativa um motorista no sistema.

        Atualiza o campo `ativo` para 1 na tabela `motoristas` para o motorista
        especificado pelo ID.

        Args:
            motorista_id (int): Identificador único do motorista.

        Raises:
            sqlite3.Error: Se houver falha na execução da query, como problemas de
                conexão ou motorista_id inexistente.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE motoristas SET ativo = 1 WHERE motorista_id = ?", (motorista_id,))
        conn.commit()
        conn.close()

    def desativar(self, motorista_id: int) -> None:
        """Desativa um motorista no sistema.

        Atualiza o campo `ativo` para 0 na tabela `motoristas` para o motorista
        especificado pelo ID.

        Args:
            motorista_id (int): Identificador único do motorista.

        Raises:
            sqlite3.Error: Se houver falha na execução da query, como problemas de
                conexão ou motorista_id inexistente.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE motoristas SET ativo = 0 WHERE motorista_id = ?", (motorista_id,))
        conn.commit()
        conn.close()
