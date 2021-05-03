from htmlparser import HTMLTableParser
import matplotlib.pyplot as plt

#URL_CIIS_FMRP="https://ciis.fmrp.usp.br/covid19/monitoramento-ribeirao-preto/"
URL_CIIS_FMRP="https://ciis.fmrp.usp.br/covid19//wp-content/insideSP/dadosRibeiraoPreto.html"

def get_table():
    hp = HTMLTableParser()
    table = hp.parse_url(URL_CIIS_FMRP)
    return table

def plot_graphic(table):
    plt.figure()
    avg=table[4].values
    plt.hist(table, bins = 50)
    plt.title('Óbitos por dia')


if __name__ == "__main__":
    table = get_table()
    plot_graphic(table)