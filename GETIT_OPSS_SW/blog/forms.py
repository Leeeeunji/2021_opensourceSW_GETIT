#멘토 게시글 작성페이지용 
from django.forms import ModelForm

from .models import *

class MentoWrite(ModelForm):
    class Meta:
        model = mentor
        fields = ['title', 'user', 'pub_date']