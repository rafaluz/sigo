from django.shortcuts import render
from .models import *    
from sishe.accounts.forms import CreateUserForm    
from django.urls import reverse_lazy    
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, FormMixin    
    
class UserCreate(CreateView):
    model = User
    template_name = 'user/add.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('accounts:login')
    # success_url = reverse_lazy('core:index')