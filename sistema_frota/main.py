from db.database import init_db
from utils.menus import menu_principal
from core.veiculos import VeiculoManager
from core.motoristas import MotoristaManager
from core.viagens import ViagemManager

def main():
    init_db()
    veiculos = VeiculoManager()
    motoristas = MotoristaManager()
    viagens = ViagemManager()

    while True:
        opcao = menu_principal()

        if opcao == "1":
            veiculos.cadastrar()
        elif opcao == "2":
            incluir_inativos = input("Incluir veículos inativos? (s/n): ").lower() == "s"
            veiculos.listar(incluir_inativos)
        elif opcao == "3":
            vid = int(input("ID do veículo a desativar: "))
            veiculos.desativar(vid)
        elif opcao == "4":
            vid = int(input("ID do veículo a reativar: "))
            veiculos.ativar(vid)
        elif opcao == "5":
            motoristas.cadastrar()
        elif opcao == "6":
            incluir_inativos = input("Incluir motoristas inativos? (s/n): ").lower() == "s"
            motoristas.listar(incluir_inativos)
        elif opcao == "7":
            mid = int(input("ID do motorista a desativar: "))
            motoristas.desativar(mid)
        elif opcao == "8":
            mid = int(input("ID do motorista a reativar: "))
            motoristas.ativar(mid)
        elif opcao == "9":
            viagens.cadastrar()
        elif opcao == "10":
            viagens.listar()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
