from django.shortcuts import render, redirect, get_object_or_404
from .models import mentor, mentee

def main(request):
    return render(request, 'main.html')

def mentor_post(request):
    return render(request, 'mentor_post.html')

def mentor_list(request):
    return render(request, 'mentor_list.html')

def mentor_detail(request):
    return render(request, 'mentor_detail.html')

def mentee_post(request):
    return render(request, 'mentee_post.html')

def mentee_list(request):
    return render(request, 'mentee_list.html')

def base(request):
    return render(request, 'base.html')

def mypage(request):
    return render(request, 'mypage.html')