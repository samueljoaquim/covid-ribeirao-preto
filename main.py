from covid_cases import get_covid_cases_df
from covid_beds import get_covid_beds_df

import pandas as pd

URL_CASES="https://ciis.fmrp.usp.br/covid19//wp-content/insideSP/dadosRibeiraoPreto.html"
URL_BEDS="https://api.leitoscovid.org/dashboard?city=ribeirao-preto"


def plot_graphic(table):
    plt.figure()
    obitos=table[["Data","Óbitos novos"]].values
    plt.hist(obitos, bins=50)
    plt.title('Óbitos por dia')

    plt.show()

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

    * {__name__}.table_cases: casos por dia
        colunas: {table_cases.columns}

    * {__name__}.table_beds: leitos ocupados por dia
        colunas: {table_beds.columns}
        
    * {__name__}.table_consolidated: casos e leitos consolidados
        colunas: {table_consolidated.columns}
""")