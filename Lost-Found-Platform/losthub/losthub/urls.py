from django.contrib import admin
from django.urls import path, include  # 使用include调用app中的文件
import main.urls  # 使用main中的urls.py处理链接跳转

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main.urls))  # 将链接交由main中的urls.py处理
]
