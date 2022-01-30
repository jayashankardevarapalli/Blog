from django.contrib import admin
from django.urls import path,include
from .views import index,post,category,about


urlpatterns = [
    path('', index),
    path('blog/<slug:url>', post),
    path('category/<slug:url>', category),
    path('about/', about)
]