from django.db import models

# Create your models here.


class MovieType(models.Model):
    type_video = models.CharField(max_length=5, verbose_name='种类')  # 电影种类

    def __str__(self):
        return self.type_video

    class Meta:
        db_table = 'MovieType'
        verbose_name = '电影种类'
        verbose_name_plural = verbose_name


class Movie(models.Model):
    """ 视频 URL 存数据库 """
    type_foreignkey = models.ForeignKey('MovieType', on_delete=models.CASCADE, verbose_name='种类')  # 外键
    video_name = models.CharField(max_length=20, verbose_name='电影名')    # 电影名字
    movie = models.FileField(max_length=100, verbose_name='url地址')    # 电影的URL地址
    video_img_path = models.ImageField(upload_to='type', default=None)  # 电影封面地址

    def __str__(self):
        return '%s   |   %s   |   %s' % (self.video_name, self.movie, self.type_foreignkey)

    class Meta:
        db_table = 'Movie'
        verbose_name = '电影信息'
        verbose_name_plural = verbose_name
