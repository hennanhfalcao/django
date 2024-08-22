from django.urls import path
from .views import PessoaFormView

urlpatterns = [
   path('pessoa/', PessoaFormView.as_view(), name='pessoa')
]

#cria o arquivo urls.py no app e importa o path e o direciona pra home. > vai pras views