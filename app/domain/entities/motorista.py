"""
Módulo de entidade Motorista.

Define a entidade Motorista, responsável por representar um motorista
no domínio da aplicação, incluindo seus dados de identificação, tipo de habilitação
e status de atividade. A entidade Motorista também lida com a validação da CNH
e restrições associadas ao motorista.
"""

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List
from uuid import UUID, uuid4

from app.domain.value_objects.motorista.cpf import CPF
from app.domain.value_objects.motorista.tipo_cnh import TipoCNH
from app.domain.value_objects.veiculo.tipo_veiculo import TipoVeiculo

@dataclass
class Motorista:
    """Entidade Motorista.

    Representa um motorista no domínio, contendo informações
    como nome, CPF, CNH, tipos de CNH, restrições e status de atividade.

    Attributes:
        id (UUID): Identificador único do motorista.
        nome (str): Nome completo do motorista.
        cpf (CPF): CPF do motorista.
        cnh_numero (str): Número da CNH do motorista.
        tipos_cnh (List[TipoCNH]): Lista de tipos de CNH que o motorista possui.
        data_validade_cnh (date): Data de validade da CNH do motorista.
        data_emissao_cnh (date): Data de emissão da CNH.
        ativo (bool): Indica se o motorista está ativo ou desativado.
        restricoes (List[str]): Lista de restrições associadas à CNH do motorista.
        data_criacao (datetime): Data e hora de criação do motorista.
        data_atualizacao (datetime): Data e hora da última atualização do motorista.
    """
    id: UUID = field(default_factory=uuid4)
    nome: str = ''
    cpf: CPF = None
    cnh_numero: str = ''
    tipos_cnh: List[TipoCNH] = field(default_factory=list)
    data_validade_cnh: date = None
    data_emissao_cnh: date = None
    ativo: bool = True
    restricoes: List[str] = field(default_factory=list)  # Ex: ["lentes", "aparelho auditivo"]
    data_criacao: datetime = field(default_factory=datetime.now)
    data_atualizacao: datetime = field(default_factory=datetime.now)

    def __init__(
        self,
        id: UUID,
        nome: str,
        cpf: CPF,
        cnh_numero: str,
        tipos_cnh: List[TipoCNH],
        data_validade_cnh: date,
        data_emissao_cnh: date,
    ) -> None:
        """Inicializa a entidade Motorista.

        Args:
            id (UUID): Identificador único do motorista.
            nome (str): Nome completo do motorista.
            cpf (CPF): CPF do motorista.
            cnh_numero (str): Número da CNH do motorista.
            tipos_cnh (List[TipoCNH]): Lista de tipos de CNH do motorista.
            data_validade_cnh (date): Data de validade da CNH.
            data_emissao_cnh (date): Data de emissão da CNH.

        Raises:
            ValueError: Se o nome do motorista não for informado.
        """
        if not nome:
            raise ValueError("Nome do motorista é obrigatório")

        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.cnh_numero = cnh_numero
        self.tipos_cnh = tipos_cnh
        self.data_validade_cnh = data_validade_cnh
        self.data_emissao_cnh = data_emissao_cnh
        self.ativo = True
        self.restricoes = []
        self.data_criacao = datetime.now()
        self.data_atualizacao = datetime.now()

    # Atualiza o nome do motorista
    def atualizar_nome(self, novo_nome: str) -> None:
        """Atualiza o nome do motorista.

        Regra de negócio: O nome do motorista deve ser válido
        para que a atualização seja realizada.

        Args:
            novo_nome (str): Novo nome do motorista.

        Raises:
            ValueError: Se o novo nome for inválido (vazio).
        """
        
        # Validação do novo nome
        if not novo_nome:
            raise ValueError("Nome inválido")
        
        self.nome = novo_nome
        self.data_atualizacao = datetime.now()

    # Adiciona um tipo de CNH ao motorista
    def adicionar_tipo_cnh(self, tipo: TipoCNH) -> None:
        """Adiciona um tipo de CNH ao motorista.

        Regra de negócio: Não adicionar tipos duplicados.

        Args:
            tipo (TipoCNH): Tipo de CNH a ser adicionado.
        """
        if tipo not in self.tipos_cnh:
            self.tipos_cnh.append(tipo)
            self.data_atualizacao = datetime.now()

    # Verifica se o motorista pode dirigir um tipo de veículo
    def pode_dirigir_veiculo(self, veiculo_tipo: TipoVeiculo) -> bool:
        """Verifica se o motorista pode dirigir o tipo de veículo especificado.

        Args:
            veiculo_tipo (TipoVeiculo): Tipo de veículo a ser verificado.

        Returns:
            bool: Retorna True se o motorista pode dirigir o veículo, False caso contrário.
        """
        for tipo in self.tipos_cnh:
            if tipo.pode_dirigir(veiculo_tipo):
                return True
        return False
        
    # Verifica se a CNH está vencida
    def cnh_vencida(self) -> bool:
        """Verifica se a CNH está vencida.

        Returns:
            bool: Retorna True se a CNH está vencida, False caso contrário.
        """
        if not self.data_validade_cnh:
            return False
        return self.data_validade_cnh < date.today()
    
    # Verifica se a CNH está próxima de vencer
    def cnh_proxima_vencer(self, dias_antecedencia: int = 30) -> bool:
        """Verifica se a CNH está próxima de vencer.

        Args:
            dias_antecedencia (int): Número de dias de antecedência para verificar se a CNH vai vencer.

        Returns:
            bool: Retorna True se a CNH está próxima de vencer, False caso contrário.
        """
        if not self.data_validade_cnh:
            return False
        
        dias_para_vencer = (self.data_validade_cnh - date.today()).days
        return 0 < dias_para_vencer <= dias_antecedencia
    
    # Adiciona uma restrição à CNH do motorista
    def adicionar_restricao(self, restricao: str):
        """Adiciona uma restrição à CNH do motorista.

        Regra de negócio: Não adicionar restrições duplicadas.

        Args:
            restricao (str): Descrição da restrição a ser adicionada.
        """
        if restricao not in self.restricoes:
            self.restricoes.append(restricao)
            self.data_atualizacao = datetime.now()
    
    # Desativa o motorista
    def desativar(self):
        """Desativa o motorista.

        Regra de negócio: O motorista não é removido do sistema,
        apenas é marcado como inativo.
        """
        self.ativo = False
        self.data_atualizacao = datetime.now()
