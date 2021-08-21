from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .models import mentor
from .models import mentee

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

<<<<<<< HEAD

def create(request):
    mentor_blog = mentor()
    person=get_object_or_404(get_user_model(), username=request.user)
    mentor_blog.title = request.POST['title']
    mentor_blog.user = request.user
    # mentor_blog.pub_date = request.POST['pub_date']
    mentor_blog.recruit_startdate = request.POST['recruit_startdate']
    mentor_blog.recruit_endDate = request.POST['recruit_endDate']
    mentor_blog.volun_startDate = request.POST['volun_startDate']
    mentor_blog.volun_endDate = request.POST['volun_endDate']
    mentor_blog.volun_times = request.POST['volun_times']
    mentor_blog.volun_day = request.POST['volun_day']
    mentor_blog.recruit_number = request.POST['request_number']
    


    mentor_blog.save()
    return redirect('mentor_list')
=======
def mypage(request):
    return render(request, 'mypage.html')
>>>>>>> fd1652b96b49b6f73c8b411457773db493059ee3
