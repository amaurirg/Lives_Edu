from requests import get

get('http://google.com')

xpto = get('http://google.com')

print(xpto.status_code)		# status da resposta
print(xpto.reason)	 		# razão da resposta
print(xpto.headers)			# resposta do cabeçalho
print(xpto.text)			# texto html da página

