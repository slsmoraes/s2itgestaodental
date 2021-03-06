"""s2itgestaodental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import RedirectView

from paciente import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/paciente/')),
    path('paciente/', views.lista_pacientes),
    path('paciente/cadastro/', views.cadastro_paciente),
    path('paciente/cadastro/submit', views.submit_paciente),
    path('paciente/cadastro/delete/<int:id_paciente>/', views.delete_paciente),

    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),

]
