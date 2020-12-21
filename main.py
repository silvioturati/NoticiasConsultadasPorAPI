from config import COUNTRY
from helpers import top_noticias


if __name__ == '__main__':
    noticias = top_noticias(COUNTRY)

    for numero in range(len(noticias)):
        print(f"{numero + 1} - {noticias[numero]}")
