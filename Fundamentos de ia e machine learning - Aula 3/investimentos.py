def calcular_retorno_investimento(valor_investido: float, valor_resgatado: float) -> float:
    """
    Calcula o retorno percentual de um investimento com base no valor investido e no valor resgatado.

    Fórmula:
        Retorno (%) = ((Valor Resgatado - Valor Investido) / Valor Investido) * 100

    Args:
        valor_investido (float): O valor inicial investido.
        valor_resgatado (float): O valor final resgatado após o período de investimento.

    Returns:
        float: O retorno percentual do investimento.
    """

    retorno_percentual = ((valor_resgatado - valor_investido) / valor_investido) * 100
    return retorno_percentual

def calcular_juros_compostos(capital_inicial: float, taxa_juros_anual: float, periodo: int) -> float:
    """
    Calcula o valor final de um investimento com base na fórmula de juros compostos.

    Fórmula:
        Valor Final = Capital Inicial * (1 + Taxa de Juros Decimal) ^ Número de Períodos

    Args:
        capital_inicial (float): O valor inicial investido.
        taxa_juros_anual (float): A taxa de juros anual em porcentagem (ex.: 5 para 5%).
        periodos (int): O número de períodos (ex.: anos) de aplicação.

    Returns:
        float: O valor final do investimento após o período especificado.
    """
    taxa_juros_decimal = taxa_juros_anual / 100
    valor_final = capital_inicial * (1 + taxa_juros_decimal) ** periodo
    return valor_final

def converter_taxa_anual_para_mensal(taxa_juros_anual: float) -> float:
    """
    Converte uma taxa de juros anual para mensal utilizando a fórmula de equivalência de taxas.

    Fórmula:
        Taxa Mensal = (1 + Taxa Anual)^(1/12) - 1

    Args:
        taxa_juros_anual (float): A taxa de juros anual em porcentagem (ex.: 5 para 5%).

    Returns:
        float: A taxa de juros mensal em porcentagem.
    """
    taxa_juros_decimal = taxa_juros_anual / 100
    taxa_mensal_decimal = (1 + taxa_juros_decimal) ** (1/12) - 1
    return taxa_mensal_decimal * 100

def calcular_cagr(valor_investido: float, valor_resgatado: float, anos: int) -> float:
    """
    Calcula a taxa de crescimento anual composta (CAGR) de um investimento.

    Fórmula:
        CAGR = ((Valor Final / Valor Inicial) ^ (1 / Número de Anos)) - 1

    Args:
        valor_investido (float): O valor inicial investido.
        valor_resgatado (float): O valor final resgatado após o período de investimento.
        anos (int): O número de anos do investimento.

    Returns:
        float: A taxa de crescimento anual composta em porcentagem.
    """
    cagr = ((valor_resgatado / valor_investido) ** (1 / anos)) - 1
    return cagr * 100