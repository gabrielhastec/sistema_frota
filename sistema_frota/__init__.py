"""Módulo de inicialização do pacote principal do sistema de frota.

Este módulo define o pacote `sistema_frota`, que agrupa os submódulos `core`,
`infrastructure`, `interface` e `utils`. O submódulo `core` contém as entidades e
casos de uso do sistema, `infrastructure` gerencia a conexão com o banco de dados
e repositórios, `interface` fornece a interação com o usuário, e `utils` contém
funcionalidades utilitárias como validação de dados. Este pacote facilita o acesso
a essas funcionalidades por meio de importações diretas.
"""

from . import core
from . import infrastructure
from . import interface
from . import utils
