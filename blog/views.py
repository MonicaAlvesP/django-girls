from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def sala(request):
    return render(request, 'blog/sala.html', {})

def sala2(request):
    return HttpResponse("Entre em nossa sala de aula 2!")