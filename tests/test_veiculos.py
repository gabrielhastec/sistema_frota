"""Módulo de testes unitários para o repositório de veículos do sistema de frota.

Este módulo contém testes para a classe `VeiculoRepositorySQLite`, verificando as
operações de criação, listagem, ativação e desativação de veículos no banco de dados
SQLite. Os testes utilizam um banco de dados em memória para garantir isolamento e
independência.
"""

import unittest
import sqlite3
from sistema_frota.infrastructure.db.schema import criar_tabelas
from sistema_frota.infrastructure.repositories.veiculo_repo import VeiculoRepositorySQLite

class TestVeiculoRepositorySQLite(unittest.TestCase):
    """Classe de testes para o VeiculoRepositorySQLite.

    Testa as operações de persistência de veículos, incluindo criação, listagem,
    ativação e desativação, utilizando um banco de dados SQLite em memória.
    """

    def setUp(self) -> None:
        """Configura o ambiente de teste antes de cada método de teste.

        Cria um banco de dados SQLite em memória, inicializa o esquema das tabelas
        e instancia o repositório de veículos.
        """
        self.conn = sqlite3.connect(":memory:")
        criar_tabelas()  # Inicializa o esquema do banco de dados
        self.repo = VeiculoRepositorySQLite()

    def tearDown(self) -> None:
        """Limpa o ambiente de teste após cada método de teste.

        Fecha a conexão com o banco de dados em memória.
        """
        self.conn.close()

    def test_criar_veiculo(self) -> None:
        """Testa a criação de um veículo no banco de dados.

        Verifica se um veículo é criado corretamente e pode ser recuperado da
        lista de veículos.
        """
        self.repo.criar("ABC1234", "Fiat Uno", 2020, 10000.0)
        veiculos = self.repo.listar()
        self.assertEqual(len(veiculos), 1)
        self.assertEqual(veiculos[0], (1, "ABC1234", "Fiat Uno", 2020, 10000.0, 1))

    def test_listar_veiculos_vazio(self) -> None:
        """Testa a listagem de veículos quando o banco de dados está vazio.

        Verifica se a lista retornada é vazia quando nenhum veículo foi criado.
        """
        veiculos = self.repo.listar()
        self.assertEqual(len(veiculos), 0)

    def test_ativar_veiculo(self) -> None:
        """Testa a ativação de um veículo.

        Cria um veículo, desativa-o e depois o ativa, verificando se o status
        `ativo` é atualizado corretamente.
        """
        self.repo.criar("XYZ5678", "Honda Civic", 2018, 20000.0)
        self.repo.desativar(1)
        veiculos = self.repo.listar()
        self.assertEqual(veiculos[0][5], 0)  # Verifica se está desativado
        self.repo.ativar(1)
        veiculos = self.repo.listar()
        self.assertEqual(veiculos[0][5], 1)  # Verifica se está ativado

    def test_desativar_veiculo(self) -> None:
        """Testa a desativação de um veículo.

        Cria um veículo e o desativa, verificando se o status `ativo` é atualizado
        corretamente.
        """
        self.repo.criar("DEF9012", "Toyota Corolla", 2021, 15000.0)
        self.repo.desativar(1)
        veiculos = self.repo.listar()
        self.assertEqual(veiculos[0][5], 0)  # Verifica se está desativado

    def test_criar_multiplos_veiculos(self) -> None:
        """Testa a criação de múltiplos veículos.

        Cria vários veículos e verifica se todos são registrados corretamente.
        """
        self.repo.criar("GHI3456", "Volkswagen Gol", 2019, 30000.0)
        self.repo.criar("JKL7890", "Chevrolet Onix", 2022, 5000.0)
        veiculos = self.repo.listar()
        self.assertEqual(len(veiculos), 2)
        self.assertEqual(veiculos[0][1], "GHI3456")
        self.assertEqual(veiculos[1][1], "JKL7890")

if __name__ == "__main__":
    unittest.main()
