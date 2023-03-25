from django.shortcuts import render
from django.shortcuts import get_object_or_404
# funções que serão chamadas por nossas rotas pra então abrir os templetes para visualização
from django.http import HttpResponse
from django.template import loader
from .models import Produto1

def index(request):
    produtos = Produto1.objects.all()


    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa',
        'produtos': produtos
    }
    return render (request, 'index.html', context)

def contato(request):
    return render( request, 'contato.html')

def produto(request, id):
    #prod = Produto1.objects.get(id=id)
    prod = get_object_or_404(Produto1, id=id)
    
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content = template.render(), content_type='text/html; charsert=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')    
    return HttpResponse(context=template.render(), content_type='text/html; charset=utf8', status=500)


