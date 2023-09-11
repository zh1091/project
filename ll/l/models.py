from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=24, verbose_name='用户名')
    password = models.CharField(max_length=24, verbose_name='密码')
    phone = models.CharField(max_length=15, verbose_name='手机号码')
    email = models.CharField(max_length=50, verbose_name='邮箱')

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname


class Admin(models.Model):
    username = models.CharField(max_length=10, verbose_name='用户名')
    password = models.CharField(max_length=10, verbose_name='密码')
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'admin'
        verbose_name = '管理员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname


class answer(models.Model):
    message = models.CharField(max_length=50, verbose_name='关键词')
    photo = models.ImageField(verbose_name='图片')
    link = models.CharField(max_length=200, verbose_name='链接')

    class Meta:
        db_table = 'answer'
        verbose_name = '回复'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname


class login(models.Model):
    time = models.TimeField(verbose_name='时间')
    id = models.AutoField(primary_key=True)
    class Meta:
        db_table = 'login'
        verbose_name = '登录信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname

