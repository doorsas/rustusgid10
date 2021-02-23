from django.urls import path

from .views import HomePageView, AboutPageView,PugosPageView, HomeView, ArticleDetailView, AddPostView,UpdatePostView, DeletePostView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('pugos/', PugosPageView.as_view(), name='pugos'),
    path('blogas/', HomeView.as_view(), name='blogas'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete-post')
]
