from app.domain.value_objects.tipo_cnh import TipoCNH

class Motorista:
    def __init__(self, nome: str, cnh: str, tipo_cnh: TipoCNH):
        if not nome:
            raise ValueError("Nome do motorista é obrigatório")

        self.nome = nome
        self.cnh = cnh
        self.tipo_cnh = tipo_cnh
        self.ativo = True

    def atualizar_nome(self, novo_nome: str):
        if not novo_nome:
            raise ValueError("Nome inválido")
        self.nome = novo_nome

    def desativar(self):
        """Regra de negócio: motorista não é apagado, apenas desativado"""
        self.ativo = False
