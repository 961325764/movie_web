from django.shortcuts import render, reverse, redirect
from django.views.generic import View
from .models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


class Login(View):  # user/login
    def get(self, request):
        logout(request)
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''
        return render(request, 'user_login.html', {'username': username,
                                                   'checked': checked})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password, is_active=False)
        if user is not None:
            if user.is_active:
                login(request, user)
                next_url = request.GET.get('next', reverse('movie:index'))
                response = redirect(next_url)
                # 判断是否需要记住用户名
                remember = request.POST.get('remember')
                if remember == 'on':
                    response.set_cookie('username', username, max_age=7 * 24 * 3600)
                else:
                    response.delete_cookie('username')
                return response
            else:
                return render(request, 'user_login.html', {'errmsg': '请联系管理员激活账户'})
        else:
            return render(request, 'user_login.html', {'errmsg': '用户名或密码不正确'})


class LogoutView(View):
    """退出登录"""
    def get(self, request):
        # 退出登录清除用户session信息
        logout(request)
        # 返回登录页面
        return redirect(reverse('user:login'))


class Register(View):  # user/register
    """注册"""
    def get(self, request):
        """显示注册页面"""
        return render(request, 'user_regist.html')

    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')
        if not all([username, password]):
            return render(request, 'user_regist.html', {'errmsg': '数据不完整，请重新输入'})
        else:
            try:
                user_dec = User.objects.get(username=username)
            except User.DoesNotExist:
                user_dec = None
            if user_dec:
                return render(request, 'user_regist.html', {'errmsg': '用户名已存在'})

            User.objects.create_user(username, email=None, password=password, is_active=False)
            return redirect(reverse('user:login'))

# def register(request):
#     """注册"""
#     if request.method == 'GET':
#         return render(request, 'user_regist.html')
#     else:
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         if not all([username, password]):
#             return render(request, 'user_regist.html', {'errmsg': '数据不完整，请重新输入'})
#         else:
#             try:
#                 user_dec = User.objects.get(username=username)
#             except User.DoesNotExist:
#                 user_dec = None
#             if user_dec:
#                 return render(request, 'user_regist.html', {'errmsg': '用户名已存在'})
#
#             User.objects.create_user(username, email=None, password=password)
#             return HttpResponse('注册成功')
