import pandas as pd

def obter_casos_covid(url: str) -> pd.DataFrame:
    df = pd.read_html(url)
    df = df[0]
    df.columns = ["Data", "Casos confirmados totais", "Óbitos totais", "Casos confirmados novos", "Óbitos novos"]
    return df