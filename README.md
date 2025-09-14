# 🚚 Sistema de Frota

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![Tests](https://img.shields.io/badge/tests-pytest-blueviolet)](./tests)
[![Coverage](https://img.shields.io/badge/coverage-in%20progress-yellowgreen)](#)
[![Status](https://img.shields.io/badge/status-em%20evolução-orange)](#)
[![Contributions](https://img.shields.io/badge/contributions-welcome-success)](#)

---

## 📖 Sobre o Projeto

O **Sistema de Frota** é um projeto em **Python puro**, desenvolvido com foco em **boas práticas de arquitetura**, organização em **camadas** e **testabilidade**.

Seu objetivo principal é gerenciar **motoristas, veículos e viagens**, permitindo evoluir gradualmente até se tornar uma base sólida para projetos maiores.  
Atualmente o projeto está em **fase de estudo e evolução**, servindo como prática para desenvolvimento de **frameworks próprios**, organização de código e controle de versões.

---

## 🛠 Estrutura do Projeto

````bash
sistema_frota/
├── examples/
│      └── main.py               # Exemplo de uso do sistema
│
├── sistema_frota/
│      ├── core/
│      │   ├── entities/         # Classes de domínio (Motorista, Veiculo, Viagem)
│      │   │   ├── __init__.py
│      │   │   ├── motorista.py
│      │   │   ├── veículos.py
│      │   │   └── viagens.py
│      │   ├── usecases/         # Lógica de negócios (GerenciarMotoristas, Veiculos, Viagens)
│      │   │   ├── __init__.py
│      │   │   ├── gerenciar_motorista.py
│      │   │   ├── gerenciar_veículos.py
│      │   │   └── gerenciar_viagens.py
│      │   └── __init__.py
│      │
│      ├── infrastructure/
│      │   ├── db/               # Conexão e esquema do banco de dados SQLite
│      │   │   ├── __init__.py
│      │   │   ├── database.py
│      │   │   └── schema.py
│      │   ├── repositories/     # Repositórios para persistência (Motorista, Veiculo, Viagem)
│      │   │   ├── __init__.py
│      │   │   ├── motorista_repo.py
│      │   │   ├── veículos_repo.py
│      │   │   └── viagens_repo.py
│      │   └── __init__.py
│      │
│      ├── interface/             # Interface de linha de comando (Menu)
│      │   ├── __init__.py
│      │   └── menu.py
│      │
│      ├── utils/                 # Funções utilitárias (validações, helpers)
│      │   ├── __init__.py
│      │   └── validators.py
│      │
│      └── __init.py
│
├── tests/                        # Testes unitários
│      ├── __init__.py
│      ├── test_motorista.py
│      ├── test_veículos.py
│      └── test_viagens.py
│
├── setup.py                    # Configuração clássica para instalação
├── pyproject.toml              # Configuração moderna do projeto (PEP 621)
└── README.md                   # Documentação do projeto

---

## 🚀 Instalação

Clone o repositório e instale as dependências (caso opte por rodar os testes):

```bash
git clone https://github.com/gabrielhastec/sistema_frota.git
cd sistema_frota
pip install -e ".[test]"
````

---

## 📦 Uso

Exemplo básico de utilização:

```python
from core.entities.motorista import Motorista
from core.entities.veiculo import Veiculo
from core.entities.viagem import Viagem

# Criando entidades
motorista = Motorista(nome="João Silva", cnh="123456789")
veiculo = Veiculo(placa="ABC-1234", modelo="Caminhão", capacidade=10000)
viagem = Viagem(motorista=motorista, veiculo=veiculo, origem="Recife", destino="Natal")

print(viagem)
```

Mais exemplos práticos estão disponíveis em [📂 examples](./examples).

---

## ✅ Testes

Os testes são implementados em **pytest**.

Rodar todos os testes:

```bash
pytest
```

Rodar com relatório de cobertura:

```bash
pytest --cov=core --cov-report=term-missing
```

---

## 🗺 Roadmap / Próximas Atualizações

- [ ] Adicionar relatórios de viagens detalhados
- [ ] Criar repositórios de persistência com SQLite
- [ ] Interface de linha de comando (CLI) para interação
- [ ] Melhorar cobertura de testes automatizados
- [ ] Gerar relatórios em PDF/CSV
- [ ] Integração futura com APIs de geolocalização

---

## 🤝 Contribuições

Este projeto é de caráter **educacional** e está aberto para sugestões, correções e melhorias.
Para contribuir:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b minha-feature`)
3. Commit suas alterações (`git commit -m 'Adiciona minha feature'`)
4. Faça push para sua branch (`git push origin minha-feature`)
5. Abra um Pull Request

---

## 📌 Status do Projeto

Atualmente em **fase de aprendizado e evolução**.
No futuro, será adicionada uma licença (provavelmente MIT) conforme necessidade.

---

## 🔗 Links Úteis

- [📂 Exemplos](./examples)
- [🧪 Testes](./tests)
- [📑 Issues](https://github.com/gabrielhastec/sistema_frota/issues)
- [📦 PyPI (futuro)](#)

---

> 💡 **Nota:** Este projeto é voltado para **aprendizado**. O código e a arquitetura podem sofrer mudanças constantes até atingir uma versão estável.
