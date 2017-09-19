from selenium import webdriver
from bs4 import BeautifulSoup as bs


base_url = 'https://www.reclameaqui.com.br'
url_site = f'{base_url}/indices/lista_reclamacoes/?id=902&status=ALL'

ff = webdriver.Firefox()
ff.get(url_site)
bs_obj = bs(ff.page_source, 'html.parser')

boxes = bs_obj.find_all('div', {'class': 'complain-status-title'})

href_links = [box.find('a').get('href') for box in boxes]

page_links = [f'{base_url}{link}' for link in href_links]

for link in page_links:
	ff.get(link)
	bs_page = bs(ff.page_source, 'html.parser')
	title = bs_page.find('h1', {'class': 'ng-binding'}).text
	recla = bs_page.find('div', {'class': 'complain-body'}).text.strip()
	print(f'\nTítulo: {title}\n\n', f'\rReclamação: {recla} {link}\n\n')

ff.quit()