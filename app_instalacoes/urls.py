from django.urls import path
from app_instalacoes import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cadastros/', views.pedido_cadastrados, name='pedido_cadastrados'),
    path('cadastro_confirmados/', views.salvar_cadastro, name='cadastro_confirmados'),
    path('excel_page', views.gerar_excel, name='gerar_excel'),
]