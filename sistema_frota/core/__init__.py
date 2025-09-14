"""Módulo de inicialização do pacote principal do sistema de frota.

Este módulo define o pacote `core`, que agrupa os submódulos `entities` e `usecases`.
O submódulo `entities` contém as classes de domínio (Motorista, Veículo, Viagem),
enquanto o submódulo `usecases` contém as classes de gerenciamento da lógica de negócios
(GerenciarMotoristas, GerenciarVeículos, GerenciarViagens). Este pacote facilita o
acesso a essas funcionalidades por meio de importações diretas.
"""

from . import entities
from . import usecases
