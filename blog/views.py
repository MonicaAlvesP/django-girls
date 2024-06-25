from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {"posts": posts})

# def sala(request):
#     return render(request, 'blog/sala.html', {})

# def sala2(request):
#     return HttpResponse("Entre em nossa sala de aula 2!")