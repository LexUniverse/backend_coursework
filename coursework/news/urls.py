from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import moderator_required

urlpatterns = [
    path('', views.news, name='news'),
    path('create', views.create_news, name='create'),
    path('check', moderator_required(views.check_suggested_news), name='check'),
    path('<int:pk>', login_required(views.NewsDetailView.as_view()), name='news-detail'),
    path('<int:pk>/update', moderator_required(views.NewsUpdateView.as_view()), name='news-update'),
    path('<int:pk>/delete', moderator_required(views.NewsDeleteView.as_view()), name='news-delete'),
    path('check/<int:pk>/update', moderator_required(views.CheckNewsUpdateView.as_view()), name='check-news-update'),
    path('check/<int:pk>/check-delete-confirm', moderator_required(views.CheckNewsDeleteView.as_view()), name='check-delete-confirm'),
]

