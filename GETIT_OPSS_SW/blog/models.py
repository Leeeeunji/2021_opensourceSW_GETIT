from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class mentor(models.Model): #작성자, 생성날짜, 모집기간, 봉사기간, 봉사하는시간대, 활동요일, 모집인원, 봉사분야, 봉사자 유형, 모집기관, 등록기관(위치), 봉사장소, 봉사대상, 활동구분(온/오프라인), 첨부파일
    title = models.CharField(max_length=100, verbose_name='글 제목')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자') #related_name 필드?
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='생성날짜') #자동으로 글 올린 날짜 저장. 수정불가
    recruit_startDate = models.DateField(dafault=timezone.now, verbose_name='모집시작일') 
    recruit_endDate = models.DateField(default=timezone.now, verbose_name='모집종료일') 
    volun_startDate = models.DateField(default=timezone.now, verbose_name='봉사시작일') 
    volun_endDate = models.DateField(default=timezone.now, verbose_name='봉사종료일') 
    volun_times = models.TextField(blank=True, verbose_name='봉사 시간대') 
    volun_day = models.TextField(blank=True, verbose_name='봉사요일') #그냥 입력하게 하도록
    recruit_number = models.IntegerField(blank=True, verbose_name='모집정원')
    #아래부터는 자세한사항 미정이므로 TextField로 임시설정
    volun_field = models.TextField(blank=True, verbose_name='봉사 분야') 
    recruit_center = models.TextField(blank=True, verbose_name='모집기관')
    volun_place = models.TextField(blank=True, verbose_name='봉사장소')
    volun_for = models.TextField(blank=True, verbose_name='봉사대상')
    volun_type = models.TextField(blank=True, verbose_name='봉사 형식(온/오프라인)')
    files = models.FileField(null=True, blank=True, verbose_name='첨부파일', upload_to="")
    
    def __str__(self):
        return "{self.id}: {self.title}"




