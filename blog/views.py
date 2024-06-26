from django.shortcuts import render
from .models import Blog
# Create your views here.
def blog_list(requiest):
  blog_list = Blog.objects.all().order_by('-publication_date')
  return render(requiest, 'blog/blog_list.html', {'blog_list': blog_list})