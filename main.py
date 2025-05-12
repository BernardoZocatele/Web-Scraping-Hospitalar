import requests
import re
from bs4 import BeautifulSoup

last_price = 0
price = 0

last_product = ""

# URL da página que você quer pegar os preços
url = "https://www.cfcarehospitalar.com.br/materiais-hospitalares/luva-de-latex"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Com a análise no html fonte, montamos um "alvo" para pegar
all_products = soup.find_all("div", class_="product")

for titulo in all_products:
    name = titulo.find('h2', class_="product__name")
    product = titulo.find('script', type="application/ld+json")
    
    
    for linha in product.string.splitlines():
        if 'price": ' in linha:
            numero_linha = re.search(r"\d+\.\d+", linha)
            price = float(numero_linha.group())
            
            print(name.text.strip(), price)