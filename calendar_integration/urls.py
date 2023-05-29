
from django.urls import path
from . import views

app_name = 'calendar_integration'

urlpatterns = [
    path('init/', views.GoogleCalendarInitView, name='init'),
    path('redirect/', views.GoogleCalendarRedirectView, name='redirect'),
]
