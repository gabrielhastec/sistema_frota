"""Módulo de testes unitários para o repositório de motoristas do sistema de frota.

Este módulo contém testes para a classe `MotoristaRepositorySQLite`, verificando as
operações de criação, listagem, ativação e desativação de motoristas no banco de dados
SQLite. Os testes utilizam um banco de dados em memória para garantir isolamento e
independência.
"""

import unittest
import sqlite3
from sistema_frota.infrastructure.db.schema import criar_tabelas
from sistema_frota.infrastructure.repositories.motorista_repo import MotoristaRepositorySQLite

class TestMotoristaRepositorySQLite(unittest.TestCase):
    """Classe de testes para o MotoristaRepositorySQLite.

    Testa as operações de persistência de motoristas, incluindo criação, listagem,
    ativação e desativação, utilizando um banco de dados SQLite em memória.
    """

    def setUp(self) -> None:
        """Configura o ambiente de teste antes de cada método de teste.

        Cria um banco de dados SQLite em memória, inicializa o esquema das tabelas
        e instancia o repositório de motoristas.
        """
        self.conn = sqlite3.connect(":memory:")
        criar_tabelas()  # Inicializa o esquema do banco de dados
        self.repo = MotoristaRepositorySQLite()

    def tearDown(self) -> None:
        """Limpa o ambiente de teste após cada método de teste.

        Fecha a conexão com o banco de dados em memória.
        """
        self.conn.close()

    def test_criar_motorista(self) -> None:
        """Testa a criação de um motorista no banco de dados.

        Verifica se um motorista é criado corretamente e pode ser recuperado da
        lista de motoristas.
        """
        self.repo.criar("João Silva", "12345678901")
        motoristas = self.repo.listar()
        self.assertEqual(len(motoristas), 1)
        self.assertEqual(motoristas[0], (1, "João Silva", "12345678901", 1))

    def test_listar_motoristas_vazio(self) -> None:
        """Testa a listagem de motoristas quando o banco de dados está vazio.

        Verifica se a lista retornada é vazia quando nenhum motorista foi criado.
        """
        motoristas = self.repo.listar()
        self.assertEqual(len(motoristas), 0)

    def test_ativar_motorista(self) -> None:
        """Testa a ativação de um motorista.

        Cria um motorista, desativa-o e depois o ativa, verificando se o status
        `ativo` é atualizado corretamente.
        """
        self.repo.criar("Maria Oliveira", "98765432109")
        self.repo.desativar(1)
        motoristas = self.repo.listar()
        self.assertEqual(motoristas[0][3], 0)  # Verifica se está desativado
        self.repo.ativar(1)
        motoristas = self.repo.listar()
        self.assertEqual(motoristas[0][3], 1)  # Verifica se está ativado

    def test_desativar_motorista(self) -> None:
        """Testa a desativação de um motorista.

        Cria um motorista e o desativa, verificando se o status `ativo` é atualizado
        corretamente.
        """
        self.repo.criar("Pedro Santos", "45678912345")
        self.repo.desativar(1)
        motoristas = self.repo.listar()
        self.assertEqual(motoristas[0][3], 0)  # Verifica se está desativado

    def test_criar_multiplos_motoristas(self) -> None:
        """Testa a criação de múltiplos motoristas.

        Cria vários motoristas e verifica se todos são registrados corretamente.
        """
        self.repo.criar("Ana Costa", "11122233344")
        self.repo.criar("Bruno Almeida", "55566677788")
        motoristas = self.repo.listar()
        self.assertEqual(len(motoristas), 2)
        self.assertEqual(motoristas[0][1], "Ana Costa")
        self.assertEqual(motoristas[1][1], "Bruno Almeida")

if __name__ == "__main__":
    unittest.main()
