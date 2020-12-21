import requests
from config import URL_BASE_TOP_HEADLINES, API_KEY


def top_noticias(country):
    """
    Retorna as top noticias do site apinews.org
    :param country: passar o pais que deseja pesquisar
    :return: lista de noticias
    """
    url = f"{URL_BASE_TOP_HEADLINES}country={country}&apiKey={API_KEY}"

    # coletando dados no formato json
    resposta = requests.get(url).json()

    # filtrando para pegar apenas os artigos
    artigos = resposta['articles']

    # criando a lista de noticias
    noticias = []
    for artigo in artigos:
        noticias.append(f"{artigo['title']}, "
                        f"URL:{artigo['url']}, "
                        f"Publicado em:{artigo['publishedAt']}.")

    return noticias
