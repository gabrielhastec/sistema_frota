from db.database import get_connection

class ViagemManager:
    def cadastrar(self):
        conn = get_connection()
        cursor = conn.cursor()

        # listar veículos disponíveis
        cursor.execute("SELECT id, placa, modelo FROM veiculos")
        veiculos = cursor.fetchall()
        if not veiculos:
            print("❌ Nenhum veículo cadastrado.")
            conn.close()
            return

        print("\n--- Veículos ---")
        for v in veiculos:
            print(f"{v[0]} - {v[1]} ({v[2]})")

        veiculo_id = input("Escolha o ID do veículo: ")

        # listar motoristas disponíveis
        cursor.execute("SELECT id, nome, cnh FROM motoristas")
        motoristas = cursor.fetchall()
        if not motoristas:
            print("❌ Nenhum motorista cadastrado.")
            conn.close()
            return

        print("\n--- Motoristas ---")
        for m in motoristas:
            print(f"{m[0]} - {m[1]} (CNH: {m[2]})")

        motorista_id = input("Escolha o ID do motorista: ")

        destino = input("Destino: ")
        km_rodados = int(input("Km percorridos: "))

        try:
            cursor.execute("""
                INSERT INTO viagens (veiculo_id, motorista_id, destino, km_rodados)
                VALUES (?, ?, ?, ?)
            """, (veiculo_id, motorista_id, destino, km_rodados))

            # Atualiza quilometragem do veículo
            cursor.execute("""
                UPDATE veiculos
                SET km = km + ?
                WHERE id = ?
            """, (km_rodados, veiculo_id))

            conn.commit()
            print("✅ Viagem registrada com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT v.id, mot.nome, veic.placa, vi.destino, vi.km_rodados, vi.data
            FROM viagens vi
            JOIN motoristas mot ON vi.motorista_id = mot.id
            JOIN veiculos veic ON vi.veiculo_id = veic.id
            ORDER BY vi.data DESC
        """)
        viagens = cursor.fetchall()

        if not viagens:
            print("Nenhuma viagem registrada.")
        else:
            print("\n--- Viagens ---")
            for v in viagens:
                print(f"[{v[0]}] Motorista: {v[1]} | Veículo: {v[2]} | Destino: {v[3]} | "
                      f"Km: {v[4]} | Data: {v[5]}")

        conn.close()
