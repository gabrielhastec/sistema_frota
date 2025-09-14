from db.database import get_connection

class VeiculoManager:

    def cadastrar(self):
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        ano = input("Ano: ")
        km = input("Quilometragem inicial: ")

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO veiculos (placa, modelo, ano, km) VALUES (?, ?, ?, ?)",
                (placa, modelo, ano, km),
            )
            conn.commit()
            print(f"✅ Veículo {placa} cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()

        if incluir_inativos:
            cursor.execute("SELECT placa, modelo, ano, km, ativo FROM veiculos")
        else:
            cursor.execute("SELECT placa, modelo, ano, km FROM veiculos WHERE ativo = 1")
        veiculos = cursor.fetchall()
        conn.close()

        if not veiculos:
            print("Nenhum veículo cadastrado.")
        else:
            print("\n--- Veículos ---")
            for v in veiculos:
                status = "Ativo" if v[5] == 1 else "Inativo"
                print(f"[{v[0]}] {v[1]} - {v[2]} ({v[3]}) - {v[4]} km ({status})")

        conn.close()

    def desativar(self, veiculo_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE veiculos SET ativo = 0 WHERE id = ?", (veiculo_id,))
        conn.commit()
        conn.close()
        print(f"🚫 Veículo ID {veiculo_id} desativado.")

    def ativar(self, veiculo_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE veiculos SET ativo = 1 WHERE id = ?", (veiculo_id,))
        conn.commit()
        conn.close()
        print(f"✅ Veículo ID {veiculo_id} reativado.")
        