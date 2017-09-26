from requests import get
from bs4 import BeautifulSoup as bs


base_url = 'http://pyjobs.com.br/jobs/'
num_page = f'{base_url}?page='

page = get(base_url)
page_jobs = bs(page.text, 'html.parser')

links = page_jobs.find('ul', {'class': 'pagination'}).find_all('a')
last_page = int(max([link.get('href')[-1] for link in links]))
urls = ['{}{}'.format(num_page, n) for n in range(1, last_page+1)]


for cada_url in urls:
	page = get(cada_url)
	page_jobs = bs(page.text, 'html.parser')
	boxes = page_jobs.find_all('div', {'class': 'col-md-10'})
	for box in boxes:
		titulo = box.find('h3').text
		ps = box.find_all('p')
		empresa = ps[0].text
		tipo = ps[1].text
		local = ps[3].text
		print('\n', titulo, empresa, tipo, local, sep='\n', end='')
print()