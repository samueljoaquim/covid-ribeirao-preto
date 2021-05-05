# covid

## Sobre
Este projeto provê algumas ferramentas para análise diária dos casos de coronavírus na cidade de Ribeirão Preto. Ele utiliza como fonte dados provenientes do [Portal COVID-19 Brasil|https://ciis.fmrp.usp.br/covid19/monitoramento-ribeirao-preto/] da Faculdade de Medicina da USP Ribeirão Preto e também o portal [leitoscovid.org|https://leitoscovid.org/sp/ribeirao-preto].

## Detalhes
Este projeto utiliza a biblioteca Pandas do Python para fazer análises estatísticas, cruzamentos de dados e geração de gráficos personalizados em cima dos dados diários da Covid no município.

A fonte de dados diários de óbitos e casos provém do **Portal COVID-19**, e está disposto numa tabela HTML, que é carregada e transformada em um DataFrame. Ela contém os dados históricos desde o começo da pandemia no Brasil. Já os dados de leitos de UTI ocupados e totais vem do portal **leitoscovid.org**, e é disponibilizada em formato JSON. Esse JSON possui dados detalhados por hospital na cidade, e por isso é transformado para representar uma tabela com os totais de leitos ocupados, disponíveis e a porcentagem de ocupados, de forma a também ser transformado em um DataFrame.