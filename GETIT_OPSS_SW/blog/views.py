from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .models import mentor, mentee

def main(request):
    return render(request, 'main.html')

def mentor_post(request):
    return render(request, 'mentor_post.html')

def mentor_list(request):
    return render(request, 'mentor_list.html')

#def mentor_detail(request, id):
def mentor_detail(request, id):
    blog = get_object_or_404(mentor, pk =id)
    person = get_object_or_404(get_user_model(), username=request.user)
    context = {
        'blog' : blog,
        'person' : person
    }
    return render(request, 'mentor_detail.html', context)

def mentor_board(request):
    mentors = mentor.objects.all()
    return render(request, 'mentor_board.html', {'mentors':mentors})

def mentee_post(request):
    return render(request, 'mentee_post.html')

def mentee_list(request):
    return render(request, 'mentee_list.html')

    #def mentee_detail(request, id):
def mentee_detail(request):
    blog = get_object_or_404(mentee, pk = id)
    person = get_object_or_404(get_user_model(), username=request.user)
    context = {
        'blog' : blog,
        'person' : person
    }
    return render(request, 'mentee_detail.html', context)

def mentee_board(request):
    mentees = mentee.objects.all()
    return render(request, 'mentee_board.html', {'mentees':mentees})

def base(request):
    return render(request, 'base.html')

def support(request):
    return render(request, 'support.html')

def create(request):
    mentor_blog = mentor()
    mentor_blog.title = request.POST['title']
    mentor_blog.user = request.user
    mentor_blog.recruit_startdate = request.POST['recruit_startdate']
    mentor_blog.recruit_endDate = request.POST['recruit_endDate']

    mentor_blog.volun_startDate = request.POST['volun_startDate']
    mentor_blog.volun_endDate = request.POST['volun_endDate']

    mentor_blog.volun_times = request.POST['volun_times']
    mentor_blog.volun_day = request.POST['volun_day']
    mentor_blog.recruit_number = request.POST['recruit_number']
    # mentor_blog.detail=request.POST['detail']
    mentor_blog.save()
    return redirect('main')

def create2(request):
    mentee_blog = mentee()
    mentee_blog.title = request.POST['title']
    mentee_blog.user = request.user
    mentee_blog.study_times = request.POST['study_times']
    mentee_blog.mentoringType = request.POST['mentoringType']
    mentee_blog.partMentor = request.POST['partMentor']
    mentee_blog.save()
    return redirect('main')

def mypage(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    return render(request, 'mypage.html', {'user':user})
