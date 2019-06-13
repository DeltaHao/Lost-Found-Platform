# main中的urls.py处理网站的所有链接
from django.urls import path
from . import views


app_name = "main"

# 处理链接跳转的函数写在views.py中
urlpatterns = [
    path("", views.lost, name="home"),  # 主页
    path("lost/", views.lost, name="lost"),  # 寻物信息的页面
    path("lost_card/", views.lost_card, name="lost_card"),
    path("lost_study/", views.lost_study, name="lost_study"),
    path("lost_live/", views.lost_live, name="lost_live"),
    path("lost_val/", views.lost_val, name="lost_val"),
    path("lost_book/", views.lost_book, name="lost_book"),
    path("lost_elec/", views.lost_elec, name="lost_elec"),
    path("lost_other/", views.lost_other, name="lost_other"),
    path("found/", views.found, name="found"),  # 捡到物品信息的页面
    path("found_card/", views.found_card, name="found_card"),
    path("found_study/", views.found_study, name="found_study"),
    path("found_live/", views.found_live, name="found_live"),
    path("found_val/", views.found_val, name="found_val"),
    path("found_book/", views.found_book, name="found_book"),
    path("found_elec/", views.found_elec, name="found_elec"),
    path("found_other/", views.found_other, name="found_other"),
    path("register/", views.register, name="register"),  # 注册页面
    path("log_in/", views.log_in, name="log_in"),  # 登录页面
    path("log_out/", views.log_out, name="log_out"),  # 登录页面
    path("user_center/", views.user_center, name="user_center"),  # 个人中心页面
    path("info_edit/", views.info_edit, name="info_edit"),  # 个人信息编辑页面
    path("change_password", views.change_password, name="change_password"),  # 修改密码
    path("passage_manage/", views.passage_manage, name="passage_manage"),  # 个人消息管理页面
    path("publish_lost/", views.publish_lost, name="publish_lost"),  # 发布丢失物品信息的页面
    path("publish_found/", views.publish_found, name="publish_found"),  # 发布捡到物品信息的页面
    path("lostitem_return/<forloop_counter>", views.lostitem_return, name="lostitem_return"),  # 归还物品，作用于lost
    path("founditem_return/<forloop_counter>", views.founditem_return, name="founditem_return"),  # 归还物品，作用于found
]
