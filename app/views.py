from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Category


def index(request):
	blogs = Blog.objects.all()[:11]
	cats = Category.objects.all()

	data = {
		'blogs': blogs,
		'cats': cats		
	} 
	return render(request, 'index.html', data)

def post(request, url):
	post = Blog.objects.get(url=url)
	return render(request, 'blogs.html', {'post': post})

def category(request, url):
	cat = Category.objects.get(url=url)
	blogs = Blog.objects.filter(cat=cat)
	data = {
		'cat': cat,
		'blogs': blogs
	}
	return render(request, 'category.html', data)

def about(request):
	return render(request, 'about.html')