"""Módulo de inicialização do pacote de infraestrutura de banco de dados do sistema de frota.

Este módulo define o pacote `db`, que agrupa os módulos `database` e `schema`.
O módulo `database` fornece funcionalidades para conexão com o banco de dados SQLite,
enquanto o módulo `schema` define a estrutura das tabelas do sistema. Este pacote
facilita o acesso a essas funcionalidades por meio de importações diretas.
"""

from . import database
from . import schema
