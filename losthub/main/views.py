from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import NormalUserForm
from .models import StudentForm
from django.contrib.auth.models import User


# 渲染home
def home(request):
    return render(request, "home.html")


# 渲染lost
def lost(request):
    return render(request, "lost.html")


# 渲染found
def found(request):
    return render(request, "found.html")


# 渲染register
def register(request):
    # 若已登录的用户通过链接进入此页，则登出该用户以便注册
    if request.user.is_authenticated:
        logout(request)
    # 流程：
    # ① 若用户在register页面输入了格式正确的注册信息，则登陆此用户并返回主页
    # ② 若用户输入了错误的信息或通过链接访问此页面，则直接返回空的注册页面
    if request.method == "POST":
        reg_form = NormalUserForm(request.POST)  # 使用用户填写的信息创建一个新表单
        if reg_form.is_valid():  # 若表单无误
            reg_form.save()
            new_user = authenticate(username=reg_form.cleaned_data["username"], password=reg_form.cleaned_data["password1"])  # 注意NormalUserForm中password1为第一次输入的密码，password2为确认密码
            new_user.email = reg_form.cleaned_data["email"]
            StudentForm(user=new_user, StudentID=reg_form.cleaned_data["StudentID"], Phone=reg_form.cleaned_data["Phone"], Gender=reg_form.cleaned_data["Gender"]).save()
            login(request, new_user)
            return redirect("main:home")
    # 直接跳转至注册页时
    else:
        reg_form = NormalUserForm()  # 创建一个空的注册表单

    # 到达这里的情况：①直接跳转至注册页时；②注册表单中有错误时。
    content = {"reg_form": reg_form}
    return render(request, "register.html", content)  # 返回至注册页以显示


# log_in页的登录功能
def log_in(request):
    if request.method == "POST":
        # 若是POST请求，则由request中的信息创建一个user对象
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            # 若不存在此用户，则返回登录页
            return render(request, "log_in.html", {"error": "用户名或密码错误！"})
        else:
            login(request, user)
            return redirect("main:home")
    else:
        return render(request, "log_in.html")


# 登出功能
def log_out(request):
    logout(request)
    return redirect("main:home")


# 个人中心
def user_center(request):
    if request.user.is_authenticated:
        content = {"user": request.user}
        return render(request, "user_center.html", content)
    else:
        return redirect("main:log_in")


# 修改个人信息
def info_edit(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            return redirect("main:user_center")
        else:
            return render(request, "info_edit.html")
    else:
        return redirect("main:log_in")


# 修改密码
def change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            return redirect("main:user_center")
        else:
            return render(request, "info_edit.html")
    else:
        return redirect("main:log_in")


# 渲染passage_manage
def passage_manage(request):
    return render(request, "passage_manage.html")


# 渲染publish_lost
def publish_lost(request):
    if request.user.is_authenticated:
        return render(request, "publish_lost.html")
    else:
        return redirect("main:log_in")


# 渲染publish_found
def publish_found(request):
    if request.user.is_authenticated:
        return render(request, "publish_found.html")
    else:
        return redirect("main:log_in")

