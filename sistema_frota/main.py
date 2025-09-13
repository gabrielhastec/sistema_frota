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
            motoristas.cadastrar()
        elif opcao == "3":
            veiculos.listar()
        elif opcao == "4":
            motoristas.listar()
        elif opcao == "5":
            viagens.cadastrar()
        elif opcao == "6":
            viagens.listar()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
