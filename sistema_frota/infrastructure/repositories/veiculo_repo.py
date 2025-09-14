"""Módulo para gerenciamento de veículos no banco de dados SQLite do sistema de frota.

Este módulo define a classe `VeiculoRepositorySQLite`, que encapsula operações de
persistência para veículos, incluindo criação, listagem, ativação e desativação.
As operações são realizadas utilizando a conexão com o banco de dados SQLite fornecida
pelo módulo `database`.
"""

from sistema_frota.infrastructure.db.database import get_connection
from typing import List, Tuple

class VeiculoRepositorySQLite:
    """Repositório para gerenciamento de veículos no banco de dados SQLite.

    Fornece métodos para criar, listar, ativar e desativar veículos, interagindo
    diretamente com a tabela `veiculos` no banco de dados SQLite.
    """

    def criar(self, placa: str, modelo: str, ano: int, km: float = 0.0) -> None:
        """Cria um novo veículo no banco de dados.

        Insere um novo registro na tabela `veiculos` com a placa, modelo, ano e
        quilometragem inicial fornecidos. O campo `ativo` é definido como 1 por padrão.

        Args:
            placa (str): Placa do veículo.
            modelo (str): Modelo do veículo.
            ano (int): Ano de fabricação do veículo.
            km (float, optional): Quilometragem inicial do veículo. Padrão é 0.0.

        Raises:
            sqlite3.Error: Se houver falha na execução da query, como problemas de
                conexão ou violação de restrições do banco de dados.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO veiculos (placa, modelo, ano, km) VALUES (?, ?, ?, ?)",
            (placa, modelo, ano, km)
        )
        conn.commit()
        conn.close()

    def listar(self) -> List[Tuple[int, str, str, int, float, int]]:
        """Lista todos os veículos registrados no banco de dados.

        Recupera todos os registros da tabela `veiculos`, incluindo ID, placa, modelo,
        ano, quilometragem e status de ativação.

        Returns:
            List[Tuple[int, str, str, int, float, int]]: Lista de tuplas contendo os
                dados dos veículos (veiculo_id, placa, modelo, ano, km, ativo).

        Raises:
            sqlite3.Error: Se houver falha na execução da query, como problemas de
                conexão com o banco de dados.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT veiculo_id, placa, modelo, ano, km, ativo FROM veiculos")
        veiculos = cursor.fetchall()
        conn.close()
        return veiculos

    def ativar(self, veiculo_id: int) -> None:
        """Ativa um veículo no sistema.

        Atualiza o campo `ativo` para 1 na tabela `veiculos` para o veículo
        especificado pelo ID.

        Args:
            veiculo_id (int): Identificador único do veículo.

        Raises:
            sqlite3.Error: Se houver falha na execução da query, como problemas de
                conexão ou veiculo_id inexistente.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE veiculos SET ativo = 1 WHERE veiculo_id = ?", (veiculo_id,))
        conn.commit()
        conn.close()

    def desativar(self, veiculo_id: int) -> None:
        """Desativa um veículo no sistema.

        Atualiza o campo `ativo` para 0 na tabela `veiculos` para o veículo
        especificado pelo ID.

        Args:
            veiculo_id (int): Identificador único do veículo.

        Raises:
            sqlite3.Error: Se houver falha na execução da query, como problemas de
                conexão ou veiculo_id inexistente.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE veiculos SET ativo = 0 WHERE veiculo_id = ?", (veiculo_id,))
        conn.commit()
        conn.close()
