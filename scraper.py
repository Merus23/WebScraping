from typing import Text
from bs4 import BeautifulSoup
import requests
from requests.models import Response

class scraper():

    def __init__(self, produto_nome):
        self.base = 'https://lista.mercadolivre.com.br/'
        self.produto_nome  = produto_nome
        self.titulo = None
        self.link = None
        self.preco = None
        #Requisição do produto e conversão com bs4
        produtos = requests.get(self.base + self.produto_nome)
        produtos = produtos.text
        produtos = BeautifulSoup(produtos, 'html.parser')
        todos_produtos = produtos.findAll('div', attrs={'class':'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

        for produto in todos_produtos:
            titulo = produto.find('h2', attrs={'class':'ui-search-item__title'})
            titulo = titulo.text
            print("Título :", titulo)
            
            link = produto.find('a', attrs={'class':'ui-search-link'})
            print("link :", link['href'])

            real = produto.find('span', attrs={'class':'price-tag-fraction'})
            centavos = produto.find('span', attrs={'class':'price-tag-cents'})
            if(centavos):
                centavos = float(centavos.text)
                preco = float(real.text) + centavos/100
                print("Preço :", preco)            
            else:
                preco = float(real.text)
                print("Preço :", preco)

            print("\n")


if __name__ == "__main__":
    s = scraper("mi band 5")