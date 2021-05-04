import requests
import pandas as pd
from datetime import datetime
from functools import reduce



def get_covid_beds_df(url):
    response = requests.get(url)
    data = response.json()
    historical = [
        [
          datetime.fromisoformat(k).strftime("%Y-%m-%d"),
          *reduce(lambda a, b : (a[0]+b[0], a[1]+b[1], f"{(a[1]+b[1])/(a[0]+b[0]):.2%}"), 
          [
              (
                  i["intensive_care_unit"]["covid"]["total"], i["intensive_care_unit"]["covid"]["busy"]
              ) for i in v["beds"]
          ]
          )
        ]
        for (k,v) in data["historical"].items()
    ]

    df = pd.DataFrame(historical)
    df.columns = ["Data", "Total de leitos", "Leitos ocupados", "Porcentagem ocupada"]
    return df
