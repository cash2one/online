# -*- coding:utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField("昵称", max_length=50, default="")
    birthday = models.DateField("生日", null=True, blank=True)
    gender = models.CharField("性别", max_length=5, choices=(("male", "男"), ("female", "女")), default="female")
    address = models.CharField("地址", max_length=100, default="")
    mobile = models.CharField("手机号", max_length=11, null=True, blank=True)
    image = models.ImageField("头像", upload_to="images/%Y/%m", default="images/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField("验证码", max_length=20)
    email = models.EmailField("邮箱", max_length=50)
    send_type = models.CharField(max_length=10, choices=(("register", "注册"), ("forget", "找回密码")))
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField("标题", max_length=100)
    image = models.ImageField("轮播图", upload_to="banner/%Y/%m", max_length=100)
    url = models.URLField("访问地址", max_length=200)
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
