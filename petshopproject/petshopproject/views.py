from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('olá')

def pagina(request):
    nome = {'times':{'equipe': 'flamengo', 'equipe': 'corinthians'} }
    servicos_oferecidos = {'serviços': {'serviço':'limpeza', 'serviço': 'tosa', 'serviço': 'venda de ração'}}

    return render(request, 'index.html')

def paginamae(request):
    return render(request)






