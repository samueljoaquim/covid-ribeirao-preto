from covid_casos import obter_casos_covid
from covid_leitos import obter_leitos_covid
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

from config import URL_CASOS, URL_LEITOS


def plotar_grafico(tabela: pd.DataFrame, dias: int, colunas: list):
    if dias:
        idx = dias*-1
        tabela = tabela[idx:]
    tabela.plot(0, colunas, 'line')
    plt.show()


def adicionar_media_movel(tabela: pd.DataFrame, dias: int, coluna: str):
    tabela[f"{coluna} M{dias}d"] = tabela[[coluna]].rolling(window=dias).mean()


def inicializar_tabelas() -> tuple:
    tabela_casos = obter_casos_covid(URL_CASOS)
    tabela_leitos = obter_leitos_covid(URL_LEITOS)
    return tabela_casos, tabela_leitos


def tabela_consolidada(tabela_casos: pd.DataFrame, tabela_leitos: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(how="left", left=tabela_casos, right=tabela_leitos, left_on="Data", right_on="Data")


# Executado quando carregando as tabelas
casos, leitos = inicializar_tabelas()
consolidada = tabela_consolidada(casos, leitos)
print(f"""
    As seguintes variáveis estão disponíveis para análise:

    * casos: casos por dia
        colunas: {casos.columns}

    * leitos: leitos ocupados por dia
        colunas: {leitos.columns}
        
    * consolidada: casos e leitos consolidados
        colunas: {consolidada.columns}

    Operações:

    * plotar_grafico(tabela, dias, [nome_coluna, nome_outra_coluna, ...])
        exibe o gráfico da(s) coluna(s) especificada(s) a partir da data
        mais recente para trás até a quantidade de dias especificada.

    * adicionar_media_movel(tabela, quantidade_dias, nome_coluna)
        adiciona à tabela a média móvel da coluna especificada, calculada
        na quantidade de dias especificada

""")