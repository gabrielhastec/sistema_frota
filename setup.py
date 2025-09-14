"""
Script de configuração para instalação e distribuição do pacote sistema_frota.

Este script utiliza setuptools para definir os metadados do projeto, dependências
e estrutura do pacote, permitindo a instalação via pip. O pacote sistema_frota
contém funcionalidades para gerenciamento de motoristas, veículos e viagens, com
persistência em banco de dados SQLite e testes unitários.
"""

import os
from setuptools import setup, find_packages

# Carregar README.md como long_description
def readme():
    if os.path.exists("README.md"):
        with open("README.md", encoding="utf-8") as f:
            return f.read()
    return ""

setup(
    name="sistema_frota",
    version="1.0.0",
    author="Gabriel Hastec",
    author_email="gabrielhastec.dev@gmail.com",
    description="Sistema para gerenciamento de frota com motoristas, veículos e viagens.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/gabrielhastec/sistema_frota",
    packages=find_packages(exclude=["tests", "tests.*", "examples"]),
    include_package_data=True,
    install_requires=[
        # Nenhuma dependência externa necessária, usa apenas biblioteca padrão
    ],
    extras_require={
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
        "dev": [
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "sistema-frota=examples.main:main",  # Executar direto no terminal
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Database :: Front-Ends",
        "Topic :: Utilities",
        "Environment :: Console",
    ],
    keywords="frota motoristas veículos viagens sqlite gerenciamento",
    project_urls={
        "Bug Tracker": "https://github.com/gabrielhastec/sistema_frota/issues",
        "Source Code": "https://github.com/gabrielhastec/sistema_frota",
    },
    python_requires=">=3.8",
)
