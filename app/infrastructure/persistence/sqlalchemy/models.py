
from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, 
    ForeignKey, Float, Date, Enum, Text, JSON
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
import enum

from .database import Base

# ================ ENUMS ================
class TipoCNH(str, enum.Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"

class TipoCombustivel(str, enum.Enum):
    GASOLINA = "gasolina"
    DIESEL = "diesel"
    ETANOL = "etanol"
    FLEX = "flex"
    ELETRICO = "eletrico"
    GNV = "gnv"

class TipoVeiculo(str, enum.Enum):
    CARRO = "carro"
    CAMINHAO = "caminhao"
    VAN = "van"
    ONIBUS = "onibus"
    CAMINHONETE = "caminhonete"
    MOTO = "moto"
    UTILITARIO = "utilitario"

class StatusVeiculo(str, enum.Enum):
    DISPONIVEL = "disponivel"
    EM_USO = "em_uso"
    EM_MANUTENCAO = "em_manutencao"
    INDISPONIVEL = "indisponivel"

class StatusViagem(str, enum.Enum):
    AGENDADA = "agendada"
    EM_ANDAMENTO = "em_andamento"
    CONCLUIDA = "concluida"
    CANCELADA = "cancelada"

class TipoManutencao(str, enum.Enum):
    PREVENTIVA = "preventiva"
    CORRETIVA = "corretiva"
    TROCA_OLEO = "troca_oleo"
    REVISAO = "revisao"
    PNEUS = "pneus"

# ================ MODELOS PRINCIPAIS ================
class Usuario(Base):
    """Modelo de usuários do sistema (login)"""
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    senha_hash = Column(String(255), nullable=False)
    ativo = Column(Boolean, default=True)
    perfil = Column(String(20), default="operador")  # admin, gestor, operador
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos
    criador_motoristas = relationship("Motorista", back_populates="criador")
    criador_veiculos = relationship("Veiculo", back_populates="criador")
    criador_viagens = relationship("Viagem", back_populates="criador")

class Motorista(Base):
    """Modelo de motoristas da frota"""
    __tablename__ = "motoristas"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False, index=True)
    cnh_numero = Column(String(20), unique=True, nullable=False)
    cnh_categoria = Column(Enum(TipoCNH), nullable=False)
    cnh_validade = Column(Date, nullable=False)
    cnh_emissao = Column(Date, nullable=False)
    telefone = Column(String(20))
    email = Column(String(100))
    endereco = Column(Text)
    data_nascimento = Column(Date)
    ativo = Column(Boolean, default=True)
    observacoes = Column(Text)
    
    # Campos de controle
    criado_por = Column(Integer, ForeignKey("usuarios.id"))
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos
    criador = relationship("Usuario", back_populates="criador_motoristas")
    viagens = relationship("Viagem", back_populates="motorista")
    documentos = relationship("DocumentoMotorista", back_populates="motorista", cascade="all, delete-orphan")

class Veiculo(Base):
    """Modelo de veículos da frota"""
    __tablename__ = "veiculos"
    
    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(7), unique=True, nullable=False, index=True)
    chassi = Column(String(17), unique=True)
    renavam = Column(String(11), unique=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    ano_fabricacao = Column(Integer, nullable=False)
    ano_modelo = Column(Integer, nullable=False)
    cor = Column(String(30))
    tipo_veiculo = Column(Enum(TipoVeiculo), nullable=False)
    tipo_combustivel = Column(Enum(TipoCombustivel), nullable=False)
    capacidade_tanque = Column(Float)  # em litros
    consumo_medio = Column(Float)  # km/l
    quilometragem_atual = Column(Float, default=0.0)
    status = Column(Enum(StatusVeiculo), default=StatusVeiculo.DISPONIVEL)
    
    # Dados de aquisição
    data_aquisicao = Column(Date)
    valor_aquisicao = Column(Float)
    seguradora = Column(String(100))
    apolice_seguro = Column(String(50))
    vencimento_seguro = Column(Date)
    
    # Campos de controle
    criado_por = Column(Integer, ForeignKey("usuarios.id"))
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos
    criador = relationship("Usuario", back_populates="criador_veiculos")
    viagens = relationship("Viagem", back_populates="veiculo")
    manutencoes = relationship("Manutencao", back_populates="veiculo", cascade="all, delete-orphan")
    documentos = relationship("DocumentoVeiculo", back_populates="veiculo", cascade="all, delete-orphan")

class Cliente(Base):
    """Modelo de clientes/transportadoras"""
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    tipo = Column(String(20))  # empresa, pessoa_fisica
    cnpj_cpf = Column(String(14), unique=True, index=True)
    inscricao_estadual = Column(String(20))
    telefone = Column(String(20))
    email = Column(String(100))
    endereco = Column(Text)
    cidade = Column(String(50))
    estado = Column(String(2))
    cep = Column(String(8))
    ativo = Column(Boolean, default=True)
    observacoes = Column(Text)
    
    # Campos de controle
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos
    viagens = relationship("Viagem", back_populates="cliente")

class Viagem(Base):
    """Modelo de viagens/transportes"""
    __tablename__ = "viagens"
    
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), unique=True, nullable=False, index=True)
    
    # Relacionamentos com outras tabelas
    motorista_id = Column(Integer, ForeignKey("motoristas.id"), nullable=False)
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"), nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    
    # Dados da viagem
    origem = Column(String(100), nullable=False)
    destino = Column(String(100), nullable=False)
    data_saida_prevista = Column(DateTime, nullable=False)
    data_chegada_prevista = Column(DateTime)
    data_saida_real = Column(DateTime)
    data_chegada_real = Column(DateTime)
    
    # Quilometragem
    km_inicial = Column(Float)
    km_final = Column(Float)
    km_total = Column(Float)
    
    # Consumo
    combustivel_inicial = Column(Float)  # litros
    combustivel_final = Column(Float)    # litros
    combustivel_consumido = Column(Float)
    custo_combustivel = Column(Float)
    
    # Custos adicionais
    pedagio = Column(Float, default=0.0)
    alimentacao = Column(Float, default=0.0)
    hospedagem = Column(Float, default=0.0)
    outros_custos = Column(Float, default=0.0)
    custo_total = Column(Float)
    
    # Status
    status = Column(Enum(StatusViagem), default=StatusViagem.AGENDADA)
    tipo_carga = Column(String(50))
    peso_carga = Column(Float)
    valor_frete = Column(Float)
    
    # Observações
    observacoes = Column(Text)
    motivo_cancelamento = Column(Text)
    
    # Campos de controle
    criado_por = Column(Integer, ForeignKey("usuarios.id"))
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos
    motorista = relationship("Motorista", back_populates="viagens")
    veiculo = relationship("Veiculo", back_populates="viagens")
    cliente = relationship("Cliente", back_populates="viagens")
    criador = relationship("Usuario", back_populates="criador_viagens")

# ================ MODELOS DE SUPORTE ================
class Manutencao(Base):
    """Modelo de manutenções dos veículos"""
    __tablename__ = "manutencoes"
    
    id = Column(Integer, primary_key=True, index=True)
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"), nullable=False)
    
    # Dados da manutenção
    tipo = Column(Enum(TipoManutencao), nullable=False)
    descricao = Column(Text, nullable=False)
    quilometragem = Column(Float, nullable=False)
    data_manutencao = Column(Date, nullable=False)
    data_proxima = Column(Date)
    quilometragem_proxima = Column(Float)
    
    # Custos
    custo_pecas = Column(Float, default=0.0)
    custo_mao_obra = Column(Float, default=0.0)
    custo_total = Column(Float, nullable=False)
    
    # Dados do fornecedor
    fornecedor = Column(String(100))
    nota_fiscal = Column(String(50))
    
    # Status
    concluida = Column(Boolean, default=True)
    observacoes = Column(Text)
    
    # Campos de controle
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos
    veiculo = relationship("Veiculo", back_populates="manutencoes")

class DocumentoMotorista(Base):
    """Documentos do RH dos motoristas"""
    __tablename__ = "documentos_motoristas"
    
    id = Column(Integer, primary_key=True, index=True)
    motorista_id = Column(Integer, ForeignKey("motoristas.id"), nullable=False)
    
    tipo = Column(String(50), nullable=False)  # RG, CPF, CNH, Comprovante Residência, etc.
    numero = Column(String(50))
    orgao_emissor = Column(String(50))
    data_emissao = Column(Date)
    data_validade = Column(Date)
    
    # Arquivo digital
    arquivo_nome = Column(String(255))
    arquivo_path = Column(String(500))
    arquivo_tipo = Column(String(50))
    
    observacoes = Column(Text)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos
    motorista = relationship("Motorista", back_populates="documentos")

class DocumentoVeiculo(Base):
    """Documentação dos veículos"""
    __tablename__ = "documentos_veiculos"
    
    id = Column(Integer, primary_key=True, index=True)
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"), nullable=False)
    
    tipo = Column(String(50), nullable=False)  # CRLV, DUT, Seguro, IPVA, Licenciamento
    numero = Column(String(50))
    orgao_emissor = Column(String(50))
    data_emissao = Column(Date)
    data_validade = Column(Date)
    
    # Valores
    valor = Column(Float)
    
    # Arquivo digital
    arquivo_nome = Column(String(255))
    arquivo_path = Column(String(500))
    arquivo_tipo = Column(String(50))
    
    observacoes = Column(Text)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos
    veiculo = relationship("Veiculo", back_populates="documentos")

class Abastecimento(Base):
    """Registro de abastecimentos"""
    __tablename__ = "abastecimentos"
    
    id = Column(Integer, primary_key=True, index=True)
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"), nullable=False)
    motorista_id = Column(Integer, ForeignKey("motoristas.id"))
    
    data = Column(DateTime, nullable=False, default=func.now())
    quilometragem = Column(Float, nullable=False)
    litros = Column(Float, nullable=False)
    valor_litro = Column(Float, nullable=False)
    valor_total = Column(Float, nullable=False)
    tipo_combustivel = Column(Enum(TipoCombustivel))
    
    # Local
    posto = Column(String(100))
    cidade = Column(String(50))
    
    # Dados do pagamento
    forma_pagamento = Column(String(20))
    nota_fiscal = Column(String(50))
    
    observacoes = Column(Text)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relacionamentos
    veiculo = relationship("Veiculo")
    motorista = relationship("Motorista")

class ConfiguracaoSistema(Base):
    """Configurações do sistema"""
    __tablename__ = "configuracoes_sistema"
    
    id = Column(Integer, primary_key=True, index=True)
    chave = Column(String(50), unique=True, nullable=False, index=True)
    valor = Column(Text)
    tipo = Column(String(20))  # string, integer, float, boolean, json
    descricao = Column(Text)
    categoria = Column(String(50))
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
