import pandas as pd

def get_covid_cases_df(url):
    df = pd.read_html(url)
    df = df[0]
    df.columns = ["Data", "Casos confirmados totais", "Óbitos totais", "Casos confirmados novos", "Óbitos novos"]
    return df