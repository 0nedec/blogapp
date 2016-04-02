from django.shortcuts import render
from django.http import HttpResponse
from models import BlogArticle

# Create your views here.
def index(request):
    blogs = BlogArticle.objects.all()
    return render(request, "main.html", {'testvar': "Test STring 2!", 'blogs': blogs})
