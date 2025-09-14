"""Módulo de inicialização do pacote de infraestrutura do sistema de frota.

Este módulo define o pacote `infrastructure`, que agrupa os submódulos `db` e
`repositories`. O submódulo `db` contém funcionalidades para conexão e definição
do esquema do banco de dados SQLite, enquanto o submódulo `repositories` contém
os repositórios para gerenciamento de dados de motoristas, veículos e viagens.
Este pacote facilita o acesso a essas funcionalidades por meio de importações diretas.
"""

from . import db
from . import repositories
