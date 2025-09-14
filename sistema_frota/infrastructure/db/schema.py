"""Módulo para inicialização do esquema do banco de dados do sistema de frota.

Este módulo define a função para criar as tabelas necessárias no banco de dados
SQLite, incluindo as tabelas de motoristas, veículos e viagens, com suas respectivas
chaves primárias, chaves estrangeiras e restrições. A criação é realizada de forma
idempotente, garantindo que as tabelas só sejam criadas se ainda não existirem.
"""

from sistema_frota.infrastructure.db.database import get_connection

def criar_tabelas() -> None:
    """Cria as tabelas necessárias no banco de dados SQLite.

    Inicializa as tabelas 'motoristas', 'veiculos' e 'viagens' com suas respectivas
    colunas e restrições, utilizando a conexão fornecida pelo módulo de banco de dados.
    A operação é idempotente, utilizando 'CREATE TABLE IF NOT EXISTS' para evitar
    erros caso as tabelas já existam.

    Tabelas criadas:
        - motoristas: Armazena informações dos motoristas (ID, nome, CNH, status ativo).
        - veiculos: Armazena informações dos veículos (ID, placa, modelo, ano, km, status ativo).
        - viagens: Registra viagens com detalhes como motorista, veículo, origem, destino,
          datas e quilometragens, com chaves estrangeiras para motoristas e veículos.

    Returns:
        None: A função não retorna valores, apenas executa a criação das tabelas.

    Raises:
        sqlite3.Error: Se houver falha na execução das queries, como problemas de
            conexão ou permissões no banco de dados.
    """
    
    # Estabelece conexão com o banco de dados
    conn = get_connection()
    cursor = conn.cursor()

    # Criação da tabela motoristas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS motoristas (
        motorista_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cnh TEXT NOT NULL,
        ativo INTEGER DEFAULT 1
    )
    """)

    # Criação da tabela veiculos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS veiculos (
        veiculo_id INTEGER PRIMARY KEY AUTOINCREMENT,
        placa TEXT NOT NULL,
        modelo TEXT NOT NULL,
        ano INTEGER NOT NULL,
        km REAL DEFAULT 0,
        ativo INTEGER DEFAULT 1
    )
    """)

    # Criação da tabela viagens com chaves estrangeiras
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS viagens (
        viagem_id INTEGER PRIMARY KEY AUTOINCREMENT,
        motorista_id INTEGER NOT NULL,
        veiculo_id INTEGER NOT NULL,
        origem TEXT NOT NULL,
        destino TEXT NOT NULL,
        data_inicio TEXT NOT NULL,
        data_fim TEXT,
        km_inicial REAL,
        km_final REAL,
        FOREIGN KEY (motorista_id) REFERENCES motoristas(motorista_id),
        FOREIGN KEY (veiculo_id) REFERENCES veiculos(veiculo_id)
    )
    """)

    # Confirma as alterações no banco de dados
    conn.commit()

    # Fecha a conexão com o banco de dados
    conn.close()
