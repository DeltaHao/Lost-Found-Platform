from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import StudentForm


# Register your models here.
class StudentFormInline(admin.TabularInline):
    model = StudentForm
    can_delete = False
    verbose_name_plural = "StudentForm"


class UserAdmin(BaseUserAdmin):
    inlines = (StudentFormInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

