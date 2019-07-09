from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy 

from .forms import PostForm
from .models import Post


class HomePageView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'home.html'
    success_url = reverse_lazy('home')

class AboutUsPageView(CreateView):
    template_name = 'about.html'

def about(request):
   return render(request, "about.html")