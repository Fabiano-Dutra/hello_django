"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Django_e_Python.hello_django.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluí um novo caminho hello/ com seus parâmetros
    path('hello/<nome>/<int:idade>/', views.hello),
    # Exercício: criando 3 rotas/caminhos que fazer 4 operaçõs básicas
    path('soma/<int:n1>/<int:n2>/', views.soma),
    path('subtração/<int:n1/<int:n2>', views.subtrai),
    path('multiplicação/<n1>/<n2>/', views.multiplica),
    path('divisão/<n1>/<n2>/', views.divide)
]
