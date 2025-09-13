import sqlite3

DB_NAME = "frota.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Criação das tabelas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS veiculos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        placa TEXT UNIQUE NOT NULL,
        modelo TEXT NOT NULL,
        ano INTEGER NOT NULL,
        km INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS motoristas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cnh TEXT UNIQUE NOT NULL,
        telefone TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS viagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        veiculo_id INTEGER NOT NULL,
        motorista_id INTEGER NOT NULL,
        destino TEXT NOT NULL,
        km_rodados INTEGER NOT NULL,
        data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (veiculo_id) REFERENCES veiculos (id),
        FOREIGN KEY (motorista_id) REFERENCES motoristas (id)
    )
    """)

    conn.commit()
    conn.close()
