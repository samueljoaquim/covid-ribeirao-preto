from covid_cases import get_covid_cases_df
from covid_beds import get_covid_beds_df
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

URL_CASES="https://ciis.fmrp.usp.br/covid19//wp-content/insideSP/dadosRibeiraoPreto.html"
URL_BEDS="https://api.leitoscovid.org/dashboard?city=ribeirao-preto"


def plot_graphic(df, days, key):
    if days:
        idx = days*-1
        df = df[idx:]
    df.plot(0, key, 'line')
    plt.show()


def add_moving_avg(df, key, amount):
    df[f"{key} {amount}d"] = df[[key]].rolling(window=7).mean()

def prepare_tables():
    table_cases = get_covid_cases_df(URL_CASES)
    table_beds = get_covid_beds_df(URL_BEDS)
    return table_cases, table_beds

def get_consolidated_table(table_cases, table_beds):
    return pd.merge(how="left", left=table_cases, right=table_beds, left_on="Data", right_on="Data")

table_cases, table_beds = prepare_tables()
table_consolidated = get_consolidated_table(table_cases, table_beds)
print(f"""
    As seguintes variáveis estão disponíveis para análise:

    * table_cases: casos por dia
        colunas: {table_cases.columns}

    * table_beds: leitos ocupados por dia
        colunas: {table_beds.columns}
        
    * table_consolidated: casos e leitos consolidados
        colunas: {table_consolidated.columns}

    Operações:

    * plot_graphic(tabela, dias, nome_coluna)

    * add_moving_avg(tabela, nome_coluna, quantidade_dias)

""")