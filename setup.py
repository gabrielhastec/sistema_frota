from setuptools import setup, find_packages

setup(
    name="sistema_frota",
    version="0.1.0",
    description="Framework simples para gerenciamento de frota",
    author="Gabriel Rodrigues",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "sistema-frota=sistema_frota.main:main",
        ],
    },
)
