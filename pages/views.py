from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import PostForm, EditForm
from .models import Post


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'pages/update_post.html'
    # fields = ['title', 'title_tag', 'body' ]
    form_class = EditForm

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/add_post.html'
    # fields = '__all__'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'pages/delete_post.html'
    success_url = reverse_lazy('blogas')

class HomeView(ListView):
    model = Post
    template_name = 'pages/blogas.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'pages/article_details.html'




class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class PugosPageView(TemplateView):
    template_name = 'pages/pugos.html'