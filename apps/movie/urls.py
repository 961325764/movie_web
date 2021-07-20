from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    re_path(r'video_(.+)', views.Video.as_view(), name="video_"),
    path('', views.Index.as_view(), name='index'),
    # url(r'video(?P<num>(\d+))', views.video),

]
