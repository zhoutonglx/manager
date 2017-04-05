from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    """用户附加信息"""
    user = models.ForeignKey(User, unique=True)
    real_name = models.CharField(max_length=32, null=True, default='')
    sex = models.IntegerField()
    id_num = models.CharField(max_length=32)

    def __str__(self):
        return self.real_name

    class Meta:
        db_table = 'account_profile'


class Carousel(models.Model):
    """轮播图片"""
    title = models.CharField(max_length=64, null=True, default='')
    path = models.CharField(max_length=128, null=True, default='')
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'carousel'


class Supervision(models.Model):
    """监督"""
    title = models.CharField(max_length=64, null=True, default='')
    # path = models.CharField(max_length=128, null=True, default='')
    content = models.TextField(null=True)
    user = models.ForeignKey(User)
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'supervision'


class Comment(models.Model):
    """评论"""
    supervision = models.ForeignKey(Supervision)
    content = models.TextField(max_length=1024)
    ctime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    class Meta:
        db_table = 'comment'


class Image(models.Model):
    """用户监督时上传图片"""
    img = models.ImageField()
    ctime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    supervision = models.ForeignKey(Supervision)
