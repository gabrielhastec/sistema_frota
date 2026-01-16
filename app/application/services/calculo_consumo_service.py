"""
Módulo de serviço de cálculo de consumo.

Contém serviços responsáveis por cálculos relacionados ao consumo
de combustível e custos de viagem.
"""

from typing import Dict, Optional

class CalculoConsumoService:
    """
    Serviço responsável por cálculos de consumo e custo de viagem.
    """
    
    # Calcular o consumo médio
    def calcular_consumo_medio(
        self, 
        distancia_km: float, 
        combustivel_litros: float
    ) -> float:
        """
        Calcula o consumo médio do veículo em quilômetros por litro (km/l).

        Args:
            distancia_km (float): Distância percorrida em quilômetros.
            combustivel_litros (float): Quantidade de combustível consumido em litros.

        Returns:
            float: Consumo médio em km/l.

        Raises:
            ValueError: Se a quantidade de combustível for menor ou igual a zero.
        """

        if combustivel_litros <= 0:
            raise ValueError("Combustivel deve ser maior que zero")
        
        return distancia_km / combustivel_litros
    
    # Calcular o custo total da viagem
    def calcular_custo_viagem(
        self,
        combustivel_litros: float,
        preco_combustivel: float,
        custos_adicionais: dict = None
    ) -> float:
        """
        Calcula o custo total de uma viagem.

        O custo total considera o gasto com combustível e custos adicionais
        opcionais, como pedágios ou alimentação.

        Args:
            combustivel_litros (float): Quantidade de combustível utilizada.
            preco_combustivel (float): Preço do combustível por litro.
            custos_adicionais (Optional[Dict[str, float]]): Custos extras da viagem.

        Returns:
            float: Custo total da viagem.
        """

        custo_combustivel = combustivel_litros * preco_combustivel
        custos_extras = sum(custos_adicionais.values()) if custos_adicionais else 0

        return custo_combustivel + custos_extras
