from django.shortcuts import render
from django.views.generic import View

from utils.mixin import LoginRequiredMixin
from .models import Movie, MovieType, Movie
from django.contrib.auth import login

# Create your views here.


class Index(LoginRequiredMixin, View):
    def get(self, request):
        quanbu_info = Movie.objects.all()
        zainan = MovieType.objects.get(type_video='灾难')
        zainan_info = zainan.movie_set.all().order_by('-id')
        donghua = MovieType.objects.get(type_video='动画')
        donghua_info = donghua.movie_set.all().order_by('-id')
        kehuan = MovieType.objects.get(type_video='科幻')
        kehuan_info = kehuan.movie_set.all().order_by('-id')
        maoxian = MovieType.objects.get(type_video='冒险')
        maoxian_info = maoxian.movie_set.all().order_by('-id')
        xiju = MovieType.objects.get(type_video='喜剧')
        xiju_info = xiju.movie_set.all().order_by('-id')
        fanzui = MovieType.objects.get(type_video='犯罪')
        fanzui_info = fanzui.movie_set.all().order_by('-id')
        aiqing = MovieType.objects.get(type_video='爱情')
        aiqing_info = aiqing.movie_set.all().order_by('-id')
        wuxia = MovieType.objects.get(type_video='武侠')
        wuxua_info = wuxia.movie_set.all().order_by('-id')

        context = {
            'zainan_info': zainan_info,
            'donghua_info': donghua_info,
            'kehuan_info': kehuan_info,
            'maoxian_info': maoxian_info,
            'xiju_info': xiju_info,
            'fanzui_info': fanzui_info,
            'aiqing_info': aiqing_info,
            'wuxia_info': wuxua_info,
            'quanbu_info': quanbu_info,
        }
        return render(request, 'index.html', context)


class Video(LoginRequiredMixin, View):
    def get(self, request, num):
        movie_info = Movie.objects.get(video_name=num)
        return render(request, 'video.html', {'movie_info': movie_info})


# def video(request, num):
#     movie_info = Movie.objects.get(id=num)
#     return render(request, 'video.html', {'movie_info': movie_info})
