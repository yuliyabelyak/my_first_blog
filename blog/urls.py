from django.urls import path
from . import views
urlpatterns = [
   		 path('', views.homework, name='homework'),
         path('register', views.register, name='register'),
   		 path('gallery', views.gallery, name='gallery'),
   		 path('news', views.news, name='news'),
   		 path('merch', views.merch, name='merch'),
]
