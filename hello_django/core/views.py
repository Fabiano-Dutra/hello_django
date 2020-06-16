# O render renderiza a mensagem para html a sua mensagem
# Incluído a importação do HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

# Criei o método hello que recebe como parâmetro o request, que a requisição dos dados que são enviadas
def hello(request, nome, idade):
    # Retornará a mensagem abaixo usanto o interpretador 'HttpResponse' interpretar a imagem para http
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos<h1>')

# Criando método soma, que recebe 2 números e responde com sua soma
def soma(request, n1, n2):
    # Retornará o mensagem abaixo usando o interpretador 'HttpResponse'
    return  HttpResponse(f'<h1>Soma de {n1} + {n2} = {n1 + n2}<h1>')

def subtrai(request, n1, n2):
    return HttpResponse(f'<h1>Subtração de {n1} - {n2} = {n1 - n2}<h1>')

def multiplica(request, n1, n2):
    return HttpResponse(f'<h1>Multiplicação de {n1} x {n2} = {n1 * n2}')

def divide(request, n1, n2):
    return HttpResponse(f'Divisão de {n1} / {n2} = {n1 / n2}')
