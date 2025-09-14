"""Módulo de utilitários para validação de dados no sistema de frota.

Este módulo fornece funções para validar os dados de entrada usados nas operações
de motoristas, veículos e viagens, garantindo que os valores atendam aos requisitos
do sistema, como formatos corretos, intervalos válidos e restrições de negócio.
"""

from typing import Optional

def validar_nome(nome: str) -> None:
    """Valida o nome de um motorista.

    Verifica se o nome é uma string não vazia e contém apenas caracteres válidos
    (letras, espaços e hífens). Remove espaços extras e verifica o comprimento.

    Args:
        nome (str): Nome do motorista a ser validado.

    Raises:
        ValueError: Se o nome for vazio, muito longo (>100 caracteres) ou contiver
            caracteres inválidos.
        TypeError: Se o nome não for uma string.
    """
    if not isinstance(nome, str):
        raise TypeError("O nome deve ser uma string.")
    nome = nome.strip()
    if not nome:
        raise ValueError("O nome não pode ser vazio.")
    if len(nome) > 100:
        raise ValueError("O nome não pode exceder 100 caracteres.")
    if not all(c.isalpha() or c.isspace() or c == '-' for c in nome):
        raise ValueError("O nome deve conter apenas letras, espaços ou hífens.")

def validar_cnh(cnh: str) -> None:
    """Valida o número da CNH de um motorista.

    Verifica se a CNH é uma string com 11 dígitos numéricos.

    Args:
        cnh (str): Número da CNH a ser validado.

    Raises:
        ValueError: Se a CNH não tiver 11 dígitos ou contiver caracteres não numéricos.
        TypeError: Se a CNH não for uma string.
    """
    if not isinstance(cnh, str):
        raise TypeError("A CNH deve ser uma string.")
    cnh = cnh.strip()
    if len(cnh) != 11:
        raise ValueError("A CNH deve ter exatamente 11 dígitos.")
    if not cnh.isdigit():
        raise ValueError("A CNH deve conter apenas dígitos numéricos.")

def validar_placa(placa: str) -> None:
    """Valida a placa de um veículo.

    Verifica se a placa segue o formato brasileiro (ex.: ABC-1234 ou ABC1D23 para
    padrão Mercosul) ou outro formato válido com até 8 caracteres.

    Args:
        placa (str): Placa do veículo a ser validada.

    Raises:
        ValueError: Se a placa for vazia, muito longa (>8 caracteres) ou não seguir
            um formato válido.
        TypeError: Se a placa não for uma string.
    """
    if not isinstance(placa, str):
        raise TypeError("A placa deve ser uma string.")
    placa = placa.strip().replace('-', '').upper()
    if not placa:
        raise ValueError("A placa não pode ser vazia.")
    if len(placa) > 8:
        raise ValueError("A placa não pode exceder 8 caracteres.")
    
    # Validação simplificada para formatos brasileiros (ex.: ABC1234 ou ABC1D23)
    if len(placa) == 7 and not (
        (placa[:3].isalpha() and placa[3:].isdigit()) or
        (placa[:3].isalpha() and placa[3:4].isdigit() and placa[4:5].isalpha() and placa[5:].isdigit())
    ):
        raise ValueError("A placa deve seguir o formato ABC1234 ou ABC1D23.")

def validar_ano(ano: int) -> None:
    """Valida o ano de fabricação de um veículo.

    Verifica se o ano é um número inteiro entre 1900 e o ano atual + 1.

    Args:
        ano (int): Ano de fabricação do veículo.

    Raises:
        ValueError: Se o ano estiver fora do intervalo válido.
        TypeError: Se o ano não for um inteiro.
    """
    from datetime import datetime
    ano_atual = datetime.now().year
    if not isinstance(ano, int):
        raise TypeError("O ano deve ser um número inteiro.")
    if ano < 1900 or ano > ano_atual + 1:
        raise ValueError(f"O ano deve estar entre 1900 e {ano_atual + 1}.")

def validar_km(km: float) -> None:
    """Valida a quilometragem de um veículo ou viagem.

    Verifica se a quilometragem é um número não negativo.

    Args:
        km (float): Quilometragem a ser validada.

    Raises:
        ValueError: Se a quilometragem for negativa.
        TypeError: Se a quilometragem não for um número (float ou int).
    """
    if not isinstance(km, (float, int)):
        raise TypeError("A quilometragem deve ser um número.")
    if km < 0:
        raise ValueError("A quilometragem não pode ser negativa.")

def validar_local(local: str) -> None:
    """Valida o local de origem ou destino de uma viagem.

    Verifica se o local é uma string não vazia com até 100 caracteres.

    Args:
        local (str): Local (origem ou destino) a ser validado.

    Raises:
        ValueError: Se o local for vazio ou exceder 100 caracteres.
        TypeError: Se o local não for uma string.
    """
    if not isinstance(local, str):
        raise TypeError("O local deve ser uma string.")
    local = local.strip()
    if not local:
        raise ValueError("O local não pode ser vazio.")
    if len(local) > 100:
        raise ValueError("O local não pode exceder 100 caracteres.")
