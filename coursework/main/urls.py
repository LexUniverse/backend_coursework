from django.urls import path, include
from . import views

urlpatterns = [
    path('news/', include('news.urls'), name='news'),
    path('contacts', views.contacts, name='contacts'),
    path('interview/', include('interviews.urls'), name='interview'),
    path('gallery', views.gallery, name='gallery'),
    path('confpolicy', views.confpolicy, name='confpolicy'),
    path('swyaz', views.swyaz, name='swyaz'),
    path('', views.RegisterUser.as_view(), name='reg'),
    path('login', views.LoginUser.as_view(), name='log'),
    path('logout', views.logout_user, name='logout'),
    path('profille', views.profile, name='profile'),
    path('admpanel', views.admpanel, name='admpanel'),
]

