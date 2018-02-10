
from django.urls import path

from . import views

urlpatterns = [

    path('', views.ArticleListView.as_view(), name='home' ),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_page' ),
]
