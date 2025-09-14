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

    def listar(self, incluir_inativos=False):
        conn = get_connection()
        cursor = conn.cursor()

        if incluir_inativos:
            cursor.execute("SELECT nome, cnh, telefone, ativo FROM motoristas")
        else:
            cursor.execute("SELECT nome, cnh, telefone FROM motoristas WHERE ativo = 1")
        motoristas = cursor.fetchall()
        conn.close()

        if not motoristas:
            print("Nenhum motorista cadastrado.")
        else:
            print("\n--- Motoristas ---")
            for m in motoristas:
                status = "Ativo" if m[4] == 1 else "Inativo"
                print(f"[{m[0]}] {m[1]} - CNH: {m[2]} - Tel: {m[3]} - Status: {status}")

        conn.close()

    def desativar(self, motorista_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE motoristas SET ativo = 0 WHERE id = ?", (motorista_id,))
        conn.commit()
        conn.close()
        print(f"🚫 Motorista ID {motorista_id} desativado.")

    def ativar(self, motorista_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE motoristas SET ativo = 1 WHERE id = ?", (motorista_id,))
        conn.commit()
        conn.close()
        print(f"✅ Motorista ID {motorista_id} reativado.")

    def editar(self, motorista_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT nome, cnh, telefone FROM motoristas WHERE id = ?", (motorista_id,))
        motorista = cursor.fetchone()
        if not motorista:
            print("❌ Motorista não encontrado.")
            conn.close()
            return

        print(f"Editando Motorista ID {motorista_id}:")
        novo_nome = input(f"Nome ({motorista[0]}): ") or motorista[0]
        nova_cnh = input(f"CNH ({motorista[1]}): ") or motorista[1]
        novo_telefone = input(f"Telefone ({motorista[2]}): ") or motorista[2]

        try:
            cursor.execute("""
                UPDATE motoristas
                SET nome = ?, cnh = ?, telefone = ?
                WHERE id = ?
            """, (novo_nome, nova_cnh, novo_telefone, motorista_id))
            conn.commit()
            print("✅ Motorista atualizado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            conn.close()
