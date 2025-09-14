"""Módulo de testes unitários para o repositório de viagens do sistema de frota.

Este módulo contém testes para a classe `ViagemRepositorySQLite`, verificando as
operações de criação, finalização e listagem de viagens no banco de dados SQLite.
Os testes utilizam um banco de dados em memória para garantir isolamento e
independência, criando registros de motoristas e veículos quando necessário para
satisfazer as restrições de chaves estrangeiras.
"""

import unittest
import sqlite3
from datetime import datetime
from sistema_frota.infrastructure.db.schema import criar_tabelas
from sistema_frota.infrastructure.repositories.motorista_repo import MotoristaRepositorySQLite
from sistema_frota.infrastructure.repositories.veiculo_repo import VeiculoRepositorySQLite
from sistema_frota.infrastructure.repositories.viagem_repo import ViagemRepositorySQLite
from sistema_frota.core.entities.viagem import Viagem

class TestViagemRepositorySQLite(unittest.TestCase):
    """Classe de testes para o ViagemRepositorySQLite.

    Testa as operações de persistência de viagens, incluindo criação, finalização
    e listagem, utilizando um banco de dados SQLite em memória.
    """

    def setUp(self) -> None:
        """Configura o ambiente de teste antes de cada método de teste.

        Cria um banco de dados SQLite em memória, inicializa o esquema das tabelas,
        instancia os repositórios de motoristas, veículos e viagens, e cria um motorista
        e um veículo para satisfazer as restrições de chaves estrangeiras.
        """
        self.conn = sqlite3.connect(":memory:")
        criar_tabelas()  # Inicializa o esquema do banco de dados
        self.motorista_repo = MotoristaRepositorySQLite()
        self.veiculo_repo = VeiculoRepositorySQLite()
        self.viagem_repo = ViagemRepositorySQLite()
        
        # Cria um motorista e um veículo para os testes
        self.motorista_repo.criar("João Silva", "12345678901")
        self.veiculo_repo.criar("ABC1234", "Fiat Uno", 2020, 10000.0)

    def tearDown(self) -> None:
        """Limpa o ambiente de teste após cada método de teste.

        Fecha a conexão com o banco de dados em memória.
        """
        self.conn.close()

    def test_criar_viagem(self) -> None:
        """Testa a criação de uma viagem no banco de dados.

        Verifica se uma viagem é criada corretamente e pode ser recuperada da
        lista de viagens.
        """
        viagem = self.viagem_repo.criar(1, 1, "São Paulo", "Rio de Janeiro", 50000.0)
        viagens = self.viagem_repo.listar()
        self.assertEqual(len(viagens), 1)
        self.assertEqual(viagens[0].viagem_id, 1)
        self.assertEqual(viagens[0].motorista_id, 1)
        self.assertEqual(viagens[0].veiculo_id, 1)
        self.assertEqual(viagens[0].origem, "São Paulo")
        self.assertEqual(viagens[0].destino, "Rio de Janeiro")
        self.assertEqual(viagens[0].km_inicial, 50000.0)
        self.assertIsNone(viagens[0].km_final)
        self.assertIsNone(viagens[0].data_fim)

    def test_listar_viagens_vazio(self) -> None:
        """Testa a listagem de viagens quando o banco de dados está vazio.

        Verifica se a lista retornada é vazia quando nenhuma viagem foi criada.
        """
        viagens = self.viagem_repo.listar()
        self.assertEqual(len(viagens), 0)

    def test_finalizar_viagem(self) -> None:
        """Testa a finalização de uma viagem.

        Cria uma viagem, finaliza-a com uma quilometragem final e verifica se os
        campos `km_final` e `data_fim` são atualizados corretamente.
        """
        self.viagem_repo.criar(1, 1, "São Paulo", "Rio de Janeiro", 50000.0)
        viagem = self.viagem_repo.finalizar(1, 51000.0)
        self.assertEqual(viagem.viagem_id, 1)
        self.assertEqual(viagem.km_final, 51000.0)
        self.assertIsNotNone(viagem.data_fim)
        viagens = self.viagem_repo.listar()
        self.assertEqual(len(viagens), 1)
        self.assertEqual(viagens[0].km_final, 51000.0)
        self.assertIsNotNone(viagens[0].data_fim)

    def test_criar_multiplas_viagens(self) -> None:
        """Testa a criação de múltiplas viagens.

        Cria várias viagens e verifica se todas são registradas corretamente.
        """
        self.viagem_repo.criar(1, 1, "São Paulo", "Rio de Janeiro", 50000.0)
        self.viagem_repo.criar(1, 1, "Belo Horizonte", "Salvador", 60000.0)
        viagens = self.viagem_repo.listar()
        self.assertEqual(len(viagens), 2)
        self.assertEqual(viagens[0].origem, "São Paulo")
        self.assertEqual(viagens[1].origem, "Belo Horizonte")

    def test_finalizar_viagem_inexistente(self) -> None:
        """Testa a finalização de uma viagem inexistente.

        Verifica se uma exceção é levantada ao tentar finalizar uma viagem com ID
        inválido.
        """
        with self.assertRaises(ValueError) as context:
            self.viagem_repo.finalizar(999, 51000.0)
        self.assertEqual(str(context.exception), "Viagem com ID 999 não encontrada.")

if __name__ == "__main__":
    unittest.main()
