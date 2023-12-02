from django.shortcuts import render
from .models import Instalacao

# Create your views here.
def home(request):
    return render(request,'home.html')

def pedido_cadastrados(request):
    nova_instalacao = Instalacao()
    nova_instalacao.pedido = request.Post.get('pedido')
    nova_instalacao.vendedor = request.Post.get('vendedor')