# O render renderiza a mensagem para html a sua mensagem
# Incluído a importação do HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

# Criei o método hello que recebe como parâmetro o request, que a requisição dos dados que são enviadas
def hello(request, nome, idade):
    # Retornará a mensagem abaixo usanto o interpretador 'HttpResponse' interpretar a imagem para http
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos<h1>')
