from django.urls import path
from . import views

urlpatterns = [
    path('', views.interview, name='interview'),
    path('cakeboy', views.cakeboy, name='cakeboy'),
    path('jeembo', views.jeembo, name='jeembo')
]

