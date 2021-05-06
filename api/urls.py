from django.urls import path

from .api_views import (
    ApplicationsListApiView, 
    ApplicationDetailApiView
)


urlpatterns = [
    path('applications/', ApplicationsListApiView.as_view(), name='applications_api' ), 
    path('application/<int:pk>/', ApplicationDetailApiView.as_view(), name='application_detail_api')
]

