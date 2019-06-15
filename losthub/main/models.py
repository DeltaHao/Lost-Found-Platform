from django.db import models
from django.contrib.auth.models import User


i_type = (("CARD", "校园卡"), ("BOOK", "书籍类"), ("STUDY", "学习用品"),  ("LIVE", "生活用品"), ("ELEC", "电子产品"), ("VAL", "贵重物品"), ("OTHER", "其他"))


class StudentForm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    StudentID = models.CharField(blank=False, max_length=10)
    Phone = models.CharField(blank=False, max_length=11)
    Gender = models.CharField(blank=True, null=True, max_length=1)

    class Meta:
        verbose_name_plural = "StudentForm"


class LostItemData(models.Model):
    item_name = models.CharField(max_length=20)
    item_description = models.CharField(max_length=50, default="")
    item_type = models.CharField(choices=i_type, max_length=20, default="")
    item_time = models.CharField(max_length=20)
    item_location = models.CharField(max_length=50)
    item_status = models.BooleanField(default=False)
    item_publisher = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.item_name


class FoundItemData(models.Model):
    item_name = models.CharField(max_length=20)
    item_description = models.CharField(max_length=50, default="")
    item_type = models.CharField(choices=i_type, max_length=20, default="")
    item_time = models.CharField(max_length=20)
    item_location = models.CharField(max_length=50)
    item_status = models.BooleanField(default=False)
    item_publisher = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.item_name
