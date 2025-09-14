"""Módulo de inicialização do pacote de testes do sistema de frota.

Este módulo define o pacote `tests`, que agrupa os módulos de testes unitários
para as funcionalidades do sistema, incluindo `test_motorista`, `test_veiculos` e
`test_viagens`. Esses módulos contêm testes para os repositórios de motoristas,
veículos e viagens, respectivamente. Este pacote facilita a execução e organização
dos testes por meio de importações diretas.
"""

from . import test_motorista
from . import test_veiculos
from . import test_viagens
