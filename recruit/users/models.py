from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    cp_name = models.CharField(blank=True, max_length=255)
    cp_nation = models.CharField(blank=True, max_length=255)
    cp_city = models.CharField(blank=True, max_length=255) 


class User(AbstractUser): # 사용자를 관리하는 모델

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField(blank=True, max_length=255)
    cp = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

