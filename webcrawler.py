import bs4
from urllib.request import urlopen as uReq #apelidinhos deixam as coisas mais faceis
from bs4 import BeautifulSoup as soup

#class MagicCard(object):
#	def __init__(self, Name, MinPrice):
#		self.Name = Name
#		self.MinPrice = MinPrice

filename = "deck.csv"
f = open(filename, "w")

headers = "qtd | nome | min prince | mid price | max price\n"

f.write(headers)

my_url= 'https://www.ligamagic.com.br/?view=decks/view&deck=647329'
uClient = uReq(my_url) #baixando a conexão com a pagina
page_html = uClient.read() #lendo a pagina e armazenando seu html em uma variavel
uClient.close() #fechando a conexão
page_soup = soup(page_html, "html.parser") #parsing do html 
containers = page_soup.findAll("div",{"class":"truncate170"}) #capturando os dados individuais das cartas

for container in containers: 
	cartinha = " "
	cartinha = container.a["onmouseover"]
	cartinha.replace(cartinha[:3], '')
	gambiflag = cartinha.split()
	#print(cartinha.split())
	gambiflag[-3] = gambiflag[-3][:-1]
	gambiflag[-2] = gambiflag[-2][:-1]
	gambiflag[-1] = gambiflag[-1][:-2]
	descricao = container.text.split()
	#print(descricao[0], container.a.text, gambiflag[-3], gambiflag[-2], gambiflag[-1])
	f.write(descricao[0] + "|" + container.a.text + "|" + gambiflag[-3] + "|" + gambiflag[-2] + "|" + gambiflag[-1] + "\n")
	#carta = MagicCard(gambiflag[2], gambiflag[3])

f.close()



