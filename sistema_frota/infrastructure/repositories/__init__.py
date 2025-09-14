"""Módulo de inicialização do pacote de repositórios do sistema de frota.

Este módulo define o pacote `repositories`, que agrupa os módulos de repositórios
para gerenciamento de dados no banco de dados SQLite. Os módulos `motorista_repo`,
`veiculo_repo` e `viagem_repo` fornecem operações de persistência para motoristas,
veículos e viagens, respectivamente. Este pacote facilita o acesso a essas
funcionalidades por meio de importações diretas.
"""

from . import motorista_repo
from . import veiculo_repo
from . import viagem_repo
