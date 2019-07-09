# from django.urls import path
# from django.conf.urls import *
from django.conf.urls import url

from .views import HomePageView, AboutUsPageView
from . import views

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^about/', views.about, name='about'),
    # path('', HomePageView.as_view(), name='home'),
    # path('about/', views.about, name='about'),
    # path('home/', HomePageView.as_view(), name='home'),
]


