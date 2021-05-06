from django.shortcuts import render
from django.template import loader
from django.contrib.auth import authenticate, login, logout 
# Creat
from django.http import HttpResponse
from .forms import LoginForm, ApplicationForm
from django.http import Http404
from django import http
from django.urls import reverse_lazy, reverse

from samplesite.settings import EMAIL_SMTP_SERVER
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import Applications, Clients, ItPerson, Dept
from django.views.generic import View, TemplateView, CreateView


class HomaPageTemplateView(TemplateView):
    template_name = 'bboards/home.html' 

   
class ApplicationCreateView(CreateView):
    model = Applications
    fields = ['theme', 'desc', 'priority', 'type_app']

    def get_success_url(self): 
        return reverse('bboard:home')


class LogInTemplateView(View):

    template_name = 'account/login.html'

    def get(self, request):        
        form = LoginForm()
        return  render(request, self.template_name, {'form':form})
        

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])            
            if user is not None:
                if user.is_active :
                    login(request, user)                    
                    next = request.POST.get('next', '/')
                    if next and next != '': 
                        return http.HttpResponseRedirect(next)                                            
                    else: 
                        return http.HttpResponseRedirect(reverse('bboard:home'))                                            
                else:
                    return http.HttpResponse('Disabled account')
            else:
                return http.HttpResponse('Invalid login')
        else:
            return http.HttpResponse('Invalid login')

    
class LogOutTemplateView(TemplateView):
    template_name = 'bboards/home.html'

    def get(self, request):
        logout(request)
        return render(request, template_name)
