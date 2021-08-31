from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from django.db.models.deletion import CASCADE

class User(AbstractUser):
    name = models.TextField(max_length=200, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.TextField(max_length=200, blank=True)
    phone = models.TextField(max_length=200, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True) # 현 계정의 사용자를 가져올 수 있음.
   # nickname = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True) #자기소개
    foundation = models.TextField(blank=True) #소속
    profile_photo = models.ImageField(upload_to='profile/',blank=True)          # 값을 채워넣지 않아도 되는 속성.
