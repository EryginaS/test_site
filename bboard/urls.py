from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import user_passes_test
from .views import (
    LogOutTemplateView, 
    LogInTemplateView, 
    HomaPageTemplateView, 
    ApplicationCreateView
)

app_name = 'bboard'
urlpatterns = [
  
    path('', HomaPageTemplateView.as_view(), name='home'),
    path('logout/', LogOutTemplateView.as_view(),  name='logout'),
    path('login/', LogInTemplateView.as_view(), name='login'),
    path('send-form/', ApplicationCreateView.as_view(),  name='send_form')
    
]
