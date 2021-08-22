from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.deletion import CASCADE

# Create your models here.
class mentor(models.Model): 
    #작성자, 생성날짜, 모집기간, 봉사기간, 봉사하는시간대, 활동요일, 모집인원, 봉사분야, 봉사자 유형,
    # 모집기관, 등록기관(위치), 봉사장소, 봉사대상, 활동구분(온/오프라인), 첨부파일
    title = models.CharField(max_length=100) #글 제목
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #related_name 필드?
    pub_date = models.DateTimeField(auto_now_add=True) #자동으로 글 올린 날짜 저장. 수정불가 #생성날짜
    # recruit_startdate = models.DateField(null=True, default=timezone.now) #모집시작일
    recruit_startdate = models.DateField(blank=True)
    recruit_endDate = models.DateField(blank=True) #모집종료일
   
    volun_startDate = models.DateField(blank=True) #봉사시작일
    volun_endDate = models.DateField(blank=True) #봉사종료일
   
    volun_times = models.TextField(blank=True) #봉사시간대
    volun_day = models.TextField(blank=True) #그냥 입력하게 하도록 #봉사요일
   
    recruit_number = models.IntegerField(default=0, blank=True) #모집정원
    volunType_Choices = (('Onine', '온라인'), ('Offline', '오프라인'))
    volunType = models.CharField(null=True, max_length=10, choices=volunType_Choices)  

    #아래부터는 자세한사항 미정이므로 TextField로 임시설정, verbose_name='봉사 분야') #봉사 분야
    recruit_center = models.TextField(blank=True) #모집기관
    center_latitude = models.FloatField(default=0.0) #모집기관 위도
    center_longitude = models.FloatField(default=0.0) #모집기관 경도
    volun_place = models.TextField(blank=True)# 봉사장소
    volun_for = models.TextField(blank=True)#봉사대상
    files = models.FileField(null=True, blank=True, upload_to="")#첨부파일

    def __str__(self):
        return "멘토 " + str(self.id) + "번 : " + str(self.title)

class mentee(models.Model): 
    # 작성자, 원하는 학습 분야, 개인/단체, 성별, 나이, 원하는 멘토링 시간대
    title = models.CharField(max_length=100) #글 제목
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #related_name 필드?
    pub_date = models.DateTimeField(auto_now_add=True) #자동으로 글 올린 날짜 저장. 수정불가 #생성날짜
    # mentoringStart_times = models.DateField(null=True, default=timezone.now)    #원하는 멘토링 시작 시각
    # mentoringEnd_times = models.DateField(null=True, default=timezone.now)      #원하는 멘토링 종료 시각
    study_times = models.TextField(blank=True) #교육을 원하는 시간대
    mentoringType_Choices = (('Onine', '온라인'), ('Offline', '오프라인'))
    mentoringType = models.CharField(max_length=10, choices=mentoringType_Choices)
    partMentor_Chocies = (('Study', '학업'), ('Digital', '디지털'))
    partMentor = models.CharField(max_length=10, choices=partMentor_Chocies)

    
    #아래부터는 자세한사항 미정이므로 TextField로 임시설정, verbose_name='봉사 분야') #봉사 분야
    recruit_center = models.TextField(blank=True) #모집기관
    
    center_latitude = models.FloatField(default=0.0) #모집기관 위도
    center_longitude = models.FloatField(default=0.0) #모집기관 경도

    volun_place = models.TextField(blank=True)# 봉사장소
    files = models.FileField(null=True, blank=True, upload_to="")#첨부파일

    def __str__(self):
        return "멘티 " + str(self.id) + "번 : " + str(self.title)
