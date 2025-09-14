"""Módulo de inicialização do pacote de entidades do sistema de frota.

Este módulo define o pacote `entities`, que contém as classes de domínio do sistema,
representando as entidades principais como Motorista, Veículo e Viagem. Ele facilita
o acesso a essas classes por meio de importações diretas a partir do pacote.
"""

from .motorista import Motorista
from .veiculo import Veiculo
from .viagem import Viagem
