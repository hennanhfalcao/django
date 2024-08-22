from django.views.generic.edit import FormView
from .forms import PessoaForm
from django.urls import reverse_lazy
from .models import Pessoa


class PessoaFormView(FormView):
    template_name= 'teste.html'
    form_class = PessoaForm
    model = Pessoa
    success_url = reverse_lazy('/')

# Create your views here.
# APAGA O BANCO DE DDOS ANTIGO E MAKEMIGRATIONS E MIGRATE