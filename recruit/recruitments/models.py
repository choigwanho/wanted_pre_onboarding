from django.db import models
from recruit.users import models as user_model


# Create your models here.
class TimeStampModel(models.Model): # 생성 및 수정 날짜
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Recruitment(TimeStampModel): # 채용공고를 관리하는 모델
    rc_author = models.ForeignKey(
        user_model.User, 
        null=True, 
        on_delete=models.CASCADE, 
        related_name='rc_author'
        )
    rc_content = models.TextField(blank=True)
    rc_position = models.CharField(blank=True, max_length=255) 
    rc_reward = models.CharField(blank=True, max_length=255)
    rc_skill = models.CharField(blank=True, max_length=255)
    cp_id = models.CharField(blank=True, max_length=255)
    

