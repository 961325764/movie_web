from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser, models.Model):

    def __str__(self):
        return '%s | %s' % (self.username, self.is_active)

    class Meta:
        db_table = 'user'
        verbose_name = '用户名及密码信息表'
        verbose_name_plural = verbose_name

