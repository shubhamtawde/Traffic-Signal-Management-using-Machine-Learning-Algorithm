from django.urls import path
from . import views

urlpatterns = [
path('traffic', views.index, name='home'),
path('place', views.place, name='place'),
path('fetch', views.fetch, name='fetch'),
path('index.html', views.index, name='home'),
path('register', views.register, name='register'),
path('login', views.login, name='login'),
path('logout', views.logout, name='logout'),
path('stats', views.stats, name='stats'),
path('export', views.export, name='export')
]
