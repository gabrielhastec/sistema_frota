"""Módulo para gerenciamento de viagens no banco de dados SQLite do sistema de frota.

Este módulo define a classe `ViagemRepositorySQLite`, que encapsula operações de
persistência para viagens, incluindo criação, finalização e listagem. As operações
são realizadas utilizando a conexão com o banco de dados SQLite fornecida pelo
módulo `database`.
"""

from sistema_frota.infrastructure.db.database import get_connection
from sistema_frota.core.entities.viagem import Viagem
from datetime import datetime
from typing import List, Tuple

class ViagemRepositorySQLite:
    """Repositório para gerenciamento de viagens no banco de dados SQLite.

    Fornece métodos para criar, finalizar e listar viagens, interagindo diretamente
    com a tabela `viagens` no banco de dados SQLite.
    """

    def criar(self, motorista_id: int, veiculo_id: int, origem: str, destino: str, km_inicial: float) -> Viagem:
        """Cria uma nova viagem no banco de dados.

        Insere um novo registro na tabela `viagens` com os dados fornecidos e a data
        de início definida como o momento atual. O campo `data_fim` e `km_final`
        são inicialmente nulos.

        Args:
            motorista_id (int): Identificador único do motorista.
            veiculo_id (int): Identificador único do veículo.
            origem (str): Local de origem da viagem.
            destino (str): Local de destino da viagem.
            km_inicial (float): Quilometragem inicial do veículo.

        Returns:
            Viagem: Objeto representando a viagem recém-criada.

        Raises:
            sqlite3.Error: Se houver falha na execução da query, como problemas de
                conexão, violação de chaves estrangeiras ou parâmetros inválidos.
        """
        conn = get_connection()
        cursor = conn.cursor()
        data_inicio = datetime.now().isoformat()
        cursor.execute(
            """
            INSERT INTO viagens (motorista_id, veiculo_id, origem, destino, data_inicio, km_inicial)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (motorista_id, veiculo_id, origem, destino, data_inicio, km_inicial)
        )
        viagem_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return Viagem(
            viagem_id=viagem_id,
            motorista_id=motorista_id,
            veiculo_id=veiculo_id,
            origem=origem,
            destino=destino,
            data_inicio=data_inicio,
            km_inicial=km_inicial
        )

    def finalizar(self, viagem_id: int, km_final: float) -> Viagem:
        """Finaliza uma viagem existente no banco de dados.

        Atualiza o registro da viagem com o ID fornecido, definindo a quilometragem
        final e a data de término como o momento atual.

        Args:
            viagem_id (int): Identificador único da viagem.
            km_final (float): Quilometragem final do veículo.

        Returns:
            Viagem: Objeto representando a viagem atualizada.

        Raises:
            sqlite3.Error: Se houver falha na execução da query, como problemas de
                conexão ou viagem_id inexistente.
            ValueError: Se km_final for menor que km_inicial da viagem.
        """
        conn = get_connection()
        cursor = conn.cursor()
        data_fim = datetime.now().isoformat()
        cursor.execute(
            "UPDATE viagens SET km_final = ?, data_fim = ? WHERE viagem_id = ?",
            (km_final, data_fim, viagem_id)
        )
        cursor.execute(
            "SELECT motorista_id, veiculo_id, origem, destino, data_inicio, km_inicial FROM viagens WHERE viagem_id = ?",
            (viagem_id,)
        )
        result = cursor.fetchone()
        conn.commit()
        conn.close()
        if not result:
            raise ValueError(f"Viagem com ID {viagem_id} não encontrada.")
        motorista_id, veiculo_id, origem, destino, data_inicio, km_inicial = result
        return Viagem(
            viagem_id=viagem_id,
            motorista_id=motorista_id,
            veiculo_id=veiculo_id,
            origem=origem,
            destino=destino,
            data_inicio=data_inicio,
            data_fim=data_fim,
            km_inicial=km_inicial,
            km_final=km_final
        )

    def listar(self) -> List[Viagem]:
        """Lista todas as viagens registradas no banco de dados.

        Recupera todos os registros da tabela `viagens`, retornando uma lista de
        objetos Viagem com os dados correspondentes.

        Returns:
            List[Viagem]: Lista de objetos Viagem representando todas as viagens.

        Raises:
            sqlite3.Error: Se houver falha na execução da query, como problemas de
                conexão com o banco de dados.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT viagem_id, motorista_id, veiculo_id, origem, destino, data_inicio,
                   data_fim, km_inicial, km_final FROM viagens
            """
        )
        viagens = cursor.fetchall()
        conn.close()
        return [
            Viagem(
                viagem_id=row[0],
                motorista_id=row[1],
                veiculo_id=row[2],
                origem=row[3],
                destino=row[4],
                data_inicio=row[5],
                data_fim=row[6],
                km_inicial=row[7],
                km_final=row[8]
            ) for row in viagens
        ]
