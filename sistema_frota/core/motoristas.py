from db.database import get_connection

class MotoristaManager:
    def cadastrar(self):
        nome = input("Nome: ")
        cnh = input("CNH: ")
        telefone = input("Telefone: ")

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO motoristas (nome, cnh, telefone) VALUES (?, ?, ?)",
                (nome, cnh, telefone),
            )
            conn.commit()
            print(f"✅ Motorista {nome} cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT nome, cnh, telefone FROM motoristas")
        motoristas = cursor.fetchall()

        if not motoristas:
            print("Nenhum motorista cadastrado.")
        else:
            print("\n--- Motoristas ---")
            for m in motoristas:
                print(f"{m[0]} - CNH: {m[1]} - Tel: {m[2]}")

        conn.close()
