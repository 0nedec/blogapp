from django.shortcuts import render
from django.http import HttpResponse
from models import BlogArticle
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    blogs = BlogArticle.objects.all()
    if request.method == 'POST':
      usrname = request.POST.get('username', None)
      pwd = request.POST.get('password', None)
      user = authenticate(username = usrname, password = pwd)
      if user is not None:
        login(request, user)
        return render(request, "main.html", {'testvar': "Test STring 2!", 'blogs': blogs, 'user': user})
    return render(request, "main.html", {'testvar': "Test STring 2!", 'blogs': blogs, 'user': None})

def createBlog(request):
  newBlog = BlogArticle()
  newBlog.title = request.POST['title']
  newBlog.author = request.user
  newBlog.content = request.POST['blog_content']
  newBlog.save()
  blogs = BlogArticle.objects.all()
  return render(request, "main.html", {'testvar': "Test STring 2!", 'blogs': blogs, 'user': request.user})