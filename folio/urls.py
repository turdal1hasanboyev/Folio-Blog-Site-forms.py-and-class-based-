from django.urls import path

from .views import HomePageView, BlogsGridPageView, ArticleDetailPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blogs/', BlogsGridPageView.as_view(), name='blogs'),
    path('article-detail/<slug:slug>/', ArticleDetailPageView.as_view(), name='article-detail'),
]
