from django.shortcuts import render

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
    return render(request, "register.html")


# 渲染login
def login(request):
    return render(request, "login.html")


# 渲染user_center
def user_center(request):
    return render(request, "user_center.html")


# 渲染info_edit
def info_edit(request):
    return render(request, "info_edit.html")


# 渲染passage_manage
def passage_manage(request):
    return render(request, "passage_manage.html")


# 渲染publish_lost
def publish_lost(request):
    return render(request, "publish_lost.html")


# 渲染publish_found
def publish_found(request):
    return render(request, "publish_found.html")