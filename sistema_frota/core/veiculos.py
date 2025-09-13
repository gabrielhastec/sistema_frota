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

        cursor.execute("SELECT placa, modelo, ano, km FROM veiculos")
        veiculos = cursor.fetchall()

        if not veiculos:
            print("Nenhum veículo cadastrado.")
        else:
            print("\n--- Veículos ---")
            for v in veiculos:
                print(f"{v[0]} - {v[1]} ({v[2]}) - {v[3]} km")

        conn.close()
