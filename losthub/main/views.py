from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import NormalUserForm, NormalUserChangeForm
from .models import StudentForm, LostItemData, FoundItemData
from django.contrib.auth.models import User


# 渲染home
def home(request):
    return render(request, "home.html")


# 渲染lost
def lost(request):
    book_amount_lost = 0
    val_amount_lost = 0
    study_amount_lost = 0
    live_amount_lost = 0
    card_amount_lost = 0
    elec_amount_lost = 0
    other_amount_lost = 0
    for item in LostItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_lost += 1
        elif item.item_type == "书籍类":
            book_amount_lost += 1
        elif item.item_type == "学习用品":
            study_amount_lost += 1
        elif item.item_type == "生活用品":
            live_amount_lost += 1
        elif item.item_type == "贵重物品":
            val_amount_lost += 1
        elif item.item_type == "电子产品":
            elec_amount_lost += 1
        elif item.item_type == "其他":
            other_amount_lost += 1
    amount_lost = book_amount_lost + card_amount_lost + elec_amount_lost + other_amount_lost + study_amount_lost + live_amount_lost + val_amount_lost
    if request.method == "POST":
        items = []
        info = str(request.POST["search_info"])
        for item in LostItemData.objects.all():
            if info in item.item_name or info in item.item_type or info in item.item_time or info in item.item_location:
                items.append(item)

        items.reverse()
        content = {"lost_items": items, "all": amount_lost, "card": card_amount_lost, "book": book_amount_lost, "elec": elec_amount_lost, "other": other_amount_lost, "study": study_amount_lost,
                   "live": live_amount_lost, "val": val_amount_lost}
        return render(request, "lost.html", content)
    else:
        items = []
        for item in LostItemData.objects.all():
            items.append(item)
        items.reverse()
        content = {"lost_items": items, "all": amount_lost, "card": card_amount_lost, "book": book_amount_lost, "elec": elec_amount_lost, "other": other_amount_lost, "study": study_amount_lost,
                   "live": live_amount_lost, "val": val_amount_lost}
        return render(request, "lost.html", content)


# 渲染lost
def lost_card(request):
    book_amount_lost = 0
    val_amount_lost = 0
    study_amount_lost = 0
    live_amount_lost = 0
    card_amount_lost = 0
    elec_amount_lost = 0
    other_amount_lost = 0
    for item in LostItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_lost += 1
        elif item.item_type == "书籍类":
            book_amount_lost += 1
        elif item.item_type == "学习用品":
            study_amount_lost += 1
        elif item.item_type == "生活用品":
            live_amount_lost += 1
        elif item.item_type == "贵重物品":
            val_amount_lost += 1
        elif item.item_type == "电子产品":
            elec_amount_lost += 1
        elif item.item_type == "其他":
            other_amount_lost += 1
    amount_lost = book_amount_lost + card_amount_lost + elec_amount_lost + other_amount_lost + study_amount_lost + live_amount_lost + val_amount_lost
    items = []
    for item in LostItemData.objects.all():
        if item.item_type == "校园卡":
            items.append(item)

    items.reverse()
    content = {"lost_items": items, "all": amount_lost, "card": card_amount_lost, "book": book_amount_lost, "elec": elec_amount_lost, "other": other_amount_lost, "study": study_amount_lost, "live": live_amount_lost, "val": val_amount_lost}
    return render(request, "lost.html", content)


# 渲染lost
def lost_book(request):
    book_amount_lost = 0
    val_amount_lost = 0
    study_amount_lost = 0
    live_amount_lost = 0
    card_amount_lost = 0
    elec_amount_lost = 0
    other_amount_lost = 0
    for item in LostItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_lost += 1
        elif item.item_type == "书籍类":
            book_amount_lost += 1
        elif item.item_type == "学习用品":
            study_amount_lost += 1
        elif item.item_type == "生活用品":
            live_amount_lost += 1
        elif item.item_type == "贵重物品":
            val_amount_lost += 1
        elif item.item_type == "电子产品":
            elec_amount_lost += 1
        elif item.item_type == "其他":
            other_amount_lost += 1
    amount_lost = book_amount_lost + card_amount_lost + elec_amount_lost + other_amount_lost + study_amount_lost + live_amount_lost + val_amount_lost
    items = []
    for item in LostItemData.objects.all():
        if item.item_type == "书籍类":
            items.append(item)

    items.reverse()
    content = {"lost_items": items, "all": amount_lost, "card": card_amount_lost, "book": book_amount_lost, "elec": elec_amount_lost, "other": other_amount_lost, "study": study_amount_lost, "live": live_amount_lost, "val": val_amount_lost}
    return render(request, "lost.html", content)


# 渲染lost
def lost_study(request):
    book_amount_lost = 0
    val_amount_lost = 0
    study_amount_lost = 0
    live_amount_lost = 0
    card_amount_lost = 0
    elec_amount_lost = 0
    other_amount_lost = 0
    for item in LostItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_lost += 1
        elif item.item_type == "书籍类":
            book_amount_lost += 1
        elif item.item_type == "学习用品":
            study_amount_lost += 1
        elif item.item_type == "生活用品":
            live_amount_lost += 1
        elif item.item_type == "贵重物品":
            val_amount_lost += 1
        elif item.item_type == "电子产品":
            elec_amount_lost += 1
        elif item.item_type == "其他":
            other_amount_lost += 1
    amount_lost = book_amount_lost + card_amount_lost + elec_amount_lost + other_amount_lost + study_amount_lost + live_amount_lost + val_amount_lost
    items = []
    for item in LostItemData.objects.all():
        if item.item_type == "学习用品":
            items.append(item)

    items.reverse()
    content = {"lost_items": items, "all": amount_lost, "card": card_amount_lost, "book": book_amount_lost, "elec": elec_amount_lost, "other": other_amount_lost, "study": study_amount_lost, "live": live_amount_lost, "val": val_amount_lost}
    return render(request, "lost.html", content)

# 渲染lost
def lost_live(request):
    book_amount_lost = 0
    val_amount_lost = 0
    study_amount_lost = 0
    live_amount_lost = 0
    card_amount_lost = 0
    elec_amount_lost = 0
    other_amount_lost = 0
    for item in LostItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_lost += 1
        elif item.item_type == "书籍类":
            book_amount_lost += 1
        elif item.item_type == "学习用品":
            study_amount_lost += 1
        elif item.item_type == "生活用品":
            live_amount_lost += 1
        elif item.item_type == "贵重物品":
            val_amount_lost += 1
        elif item.item_type == "电子产品":
            elec_amount_lost += 1
        elif item.item_type == "其他":
            other_amount_lost += 1
    amount_lost = book_amount_lost + card_amount_lost + elec_amount_lost + other_amount_lost + study_amount_lost + live_amount_lost + val_amount_lost
    items = []
    for item in LostItemData.objects.all():
        if item.item_type == "生活用品":
            items.append(item)

    items.reverse()
    content = {"lost_items": items, "all": amount_lost, "card": card_amount_lost, "book": book_amount_lost, "elec": elec_amount_lost, "other": other_amount_lost, "study": study_amount_lost, "live": live_amount_lost, "val": val_amount_lost}
    return render(request, "lost.html", content)

# 渲染lost
def lost_val(request):
    book_amount_lost = 0
    val_amount_lost = 0
    study_amount_lost = 0
    live_amount_lost = 0
    card_amount_lost = 0
    elec_amount_lost = 0
    other_amount_lost = 0
    for item in LostItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_lost += 1
        elif item.item_type == "书籍类":
            book_amount_lost += 1
        elif item.item_type == "学习用品":
            study_amount_lost += 1
        elif item.item_type == "生活用品":
            live_amount_lost += 1
        elif item.item_type == "贵重物品":
            val_amount_lost += 1
        elif item.item_type == "电子产品":
            elec_amount_lost += 1
        elif item.item_type == "其他":
            other_amount_lost += 1
    amount_lost = book_amount_lost + card_amount_lost + elec_amount_lost + other_amount_lost + study_amount_lost + live_amount_lost + val_amount_lost
    items = []
    for item in LostItemData.objects.all():
        if item.item_type == "贵重物品":
            items.append(item)

    items.reverse()
    content = {"lost_items": items, "all": amount_lost, "card": card_amount_lost, "book": book_amount_lost, "elec": elec_amount_lost, "other": other_amount_lost, "study": study_amount_lost, "live": live_amount_lost, "val": val_amount_lost}
    return render(request, "lost.html", content)


# 渲染lost
def lost_elec(request):
    book_amount_lost = 0
    val_amount_lost = 0
    study_amount_lost = 0
    live_amount_lost = 0
    card_amount_lost = 0
    elec_amount_lost = 0
    other_amount_lost = 0
    for item in LostItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_lost += 1
        elif item.item_type == "书籍类":
            book_amount_lost += 1
        elif item.item_type == "学习用品":
            study_amount_lost += 1
        elif item.item_type == "生活用品":
            live_amount_lost += 1
        elif item.item_type == "贵重物品":
            val_amount_lost += 1
        elif item.item_type == "电子产品":
            elec_amount_lost += 1
        elif item.item_type == "其他":
            other_amount_lost += 1
    amount_lost = book_amount_lost + card_amount_lost + elec_amount_lost + other_amount_lost + study_amount_lost + live_amount_lost + val_amount_lost
    items = []
    for item in LostItemData.objects.all():
        if item.item_type == "电子产品":
            items.append(item)

    items.reverse()
    content = {"lost_items": items, "all": amount_lost, "card": card_amount_lost, "book": book_amount_lost, "elec": elec_amount_lost, "other": other_amount_lost, "study": study_amount_lost, "live": live_amount_lost, "val": val_amount_lost}
    return render(request, "lost.html", content)


# 渲染lost
def lost_other(request):
    book_amount_lost = 0
    val_amount_lost = 0
    study_amount_lost = 0
    live_amount_lost = 0
    card_amount_lost = 0
    elec_amount_lost = 0
    other_amount_lost = 0
    for item in LostItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_lost += 1
        elif item.item_type == "书籍类":
            book_amount_lost += 1
        elif item.item_type == "学习用品":
            study_amount_lost += 1
        elif item.item_type == "生活用品":
            live_amount_lost += 1
        elif item.item_type == "贵重物品":
            val_amount_lost += 1
        elif item.item_type == "电子产品":
            elec_amount_lost += 1
        elif item.item_type == "其他":
            other_amount_lost += 1
    amount_lost = book_amount_lost + card_amount_lost + elec_amount_lost + other_amount_lost + study_amount_lost + live_amount_lost + val_amount_lost
    items = []
    for item in LostItemData.objects.all():
        if item.item_type == "其他":
            items.append(item)

    items.reverse()
    content = {"lost_items": items, "all": amount_lost, "card": card_amount_lost, "book": book_amount_lost, "elec": elec_amount_lost, "other": other_amount_lost, "study": study_amount_lost, "live": live_amount_lost, "val": val_amount_lost}
    return render(request, "lost.html", content)



# 渲染found
def found(request):
    book_amount_found = 0
    val_amount_found = 0
    study_amount_found = 0
    live_amount_found = 0
    card_amount_found = 0
    elec_amount_found = 0
    other_amount_found = 0
    for item in FoundItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_found += 1
        elif item.item_type == "书籍类":
            book_amount_found += 1
        elif item.item_type == "学习用品":
            study_amount_found += 1
        elif item.item_type == "生活用品":
            live_amount_found += 1
        elif item.item_type == "贵重物品":
            val_amount_found += 1
        elif item.item_type == "电子产品":
            elec_amount_found += 1
        elif item.item_type == "其他":
            other_amount_found += 1
    amount_found = book_amount_found + card_amount_found + elec_amount_found + other_amount_found + study_amount_found + live_amount_found + val_amount_found
    if request.method == "POST":
        items = []
        info = str(request.POST["search_info"])
        for item in FoundItemData.objects.all():
            if info in item.item_name or info in item.item_type or info in item.item_time or info in item.item_location:
                items.append(item)

        items.reverse()
        content = {"found_items": items, "all": amount_found, "card": card_amount_found, "book": book_amount_found, "elec": elec_amount_found, "other": other_amount_found, "study": study_amount_found,
                   "live": live_amount_found, "val": val_amount_found}
        return render(request, "found.html", content)
    else:
        items = []
        for item in FoundItemData.objects.all():
            items.append(item)
        items.reverse()
        content = {"found_items": items, "all": amount_found, "card": card_amount_found, "book": book_amount_found, "elec": elec_amount_found, "other": other_amount_found, "study": study_amount_found,
                   "live": live_amount_found, "val": val_amount_found}
        return render(request, "found.html", content)


# 渲染found
def found_card(request):
    book_amount_found = 0
    val_amount_found = 0
    study_amount_found = 0
    live_amount_found = 0
    card_amount_found = 0
    elec_amount_found = 0
    other_amount_found = 0
    for item in FoundItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_found += 1
        elif item.item_type == "书籍类":
            book_amount_found += 1
        elif item.item_type == "学习用品":
            study_amount_found += 1
        elif item.item_type == "生活用品":
            live_amount_found += 1
        elif item.item_type == "贵重物品":
            val_amount_found += 1
        elif item.item_type == "电子产品":
            elec_amount_found += 1
        elif item.item_type == "其他":
            other_amount_found += 1
    amount_found = book_amount_found + card_amount_found + elec_amount_found + other_amount_found + study_amount_found + live_amount_found + val_amount_found
    items = []
    for item in FoundItemData.objects.all():
        if item.item_type == "校园卡":
            items.append(item)

    items.reverse()
    content = {"found_items": items, "all": amount_found, "card": card_amount_found, "book": book_amount_found, "elec": elec_amount_found, "other": other_amount_found, "study": study_amount_found, "live": live_amount_found, "val": val_amount_found}
    return render(request, "found.html", content)


# 渲染found
def found_book(request):
    book_amount_found = 0
    val_amount_found = 0
    study_amount_found = 0
    live_amount_found = 0
    card_amount_found = 0
    elec_amount_found = 0
    other_amount_found = 0
    for item in FoundItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_found += 1
        elif item.item_type == "书籍类":
            book_amount_found += 1
        elif item.item_type == "学习用品":
            study_amount_found += 1
        elif item.item_type == "生活用品":
            live_amount_found += 1
        elif item.item_type == "贵重物品":
            val_amount_found += 1
        elif item.item_type == "电子产品":
            elec_amount_found += 1
        elif item.item_type == "其他":
            other_amount_found += 1
    amount_found = book_amount_found + card_amount_found + elec_amount_found + other_amount_found + study_amount_found + live_amount_found + val_amount_found
    items = []
    for item in FoundItemData.objects.all():
        if item.item_type == "书籍类":
            items.append(item)

    items.reverse()
    content = {"found_items": items, "all": amount_found, "card": card_amount_found, "book": book_amount_found, "elec": elec_amount_found, "other": other_amount_found, "study": study_amount_found, "live": live_amount_found, "val": val_amount_found}
    return render(request, "found.html", content)


# 渲染found
def found_study(request):
    book_amount_found = 0
    val_amount_found = 0
    study_amount_found = 0
    live_amount_found = 0
    card_amount_found = 0
    elec_amount_found = 0
    other_amount_found = 0
    for item in FoundItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_found += 1
        elif item.item_type == "书籍类":
            book_amount_found += 1
        elif item.item_type == "学习用品":
            study_amount_found += 1
        elif item.item_type == "生活用品":
            live_amount_found += 1
        elif item.item_type == "贵重物品":
            val_amount_found += 1
        elif item.item_type == "电子产品":
            elec_amount_found += 1
        elif item.item_type == "其他":
            other_amount_found += 1
    amount_found = book_amount_found + card_amount_found + elec_amount_found + other_amount_found + study_amount_found + live_amount_found + val_amount_found
    items = []
    for item in FoundItemData.objects.all():
        if item.item_type == "学习用品":
            items.append(item)

    items.reverse()
    content = {"found_items": items, "all": amount_found, "card": card_amount_found, "book": book_amount_found, "elec": elec_amount_found, "other": other_amount_found, "study": study_amount_found, "live": live_amount_found, "val": val_amount_found}
    return render(request, "found.html", content)

# 渲染found
def found_live(request):
    book_amount_found = 0
    val_amount_found = 0
    study_amount_found = 0
    live_amount_found = 0
    card_amount_found = 0
    elec_amount_found = 0
    other_amount_found = 0
    for item in FoundItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_found += 1
        elif item.item_type == "书籍类":
            book_amount_found += 1
        elif item.item_type == "学习用品":
            study_amount_found += 1
        elif item.item_type == "生活用品":
            live_amount_found += 1
        elif item.item_type == "贵重物品":
            val_amount_found += 1
        elif item.item_type == "电子产品":
            elec_amount_found += 1
        elif item.item_type == "其他":
            other_amount_found += 1
    amount_found = book_amount_found + card_amount_found + elec_amount_found + other_amount_found + study_amount_found + live_amount_found + val_amount_found
    items = []
    for item in FoundItemData.objects.all():
        if item.item_type == "生活用品":
            items.append(item)

    items.reverse()
    content = {"found_items": items, "all": amount_found, "card": card_amount_found, "book": book_amount_found, "elec": elec_amount_found, "other": other_amount_found, "study": study_amount_found, "live": live_amount_found, "val": val_amount_found}
    return render(request, "found.html", content)

# 渲染found
def found_val(request):
    book_amount_found = 0
    val_amount_found = 0
    study_amount_found = 0
    live_amount_found = 0
    card_amount_found = 0
    elec_amount_found = 0
    other_amount_found = 0
    for item in FoundItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_found += 1
        elif item.item_type == "书籍类":
            book_amount_found += 1
        elif item.item_type == "学习用品":
            study_amount_found += 1
        elif item.item_type == "生活用品":
            live_amount_found += 1
        elif item.item_type == "贵重物品":
            val_amount_found += 1
        elif item.item_type == "电子产品":
            elec_amount_found += 1
        elif item.item_type == "其他":
            other_amount_found += 1
    amount_found = book_amount_found + card_amount_found + elec_amount_found + other_amount_found + study_amount_found + live_amount_found + val_amount_found
    items = []
    for item in FoundItemData.objects.all():
        if item.item_type == "贵重物品":
            items.append(item)

    items.reverse()
    content = {"found_items": items, "all": amount_found, "card": card_amount_found, "book": book_amount_found, "elec": elec_amount_found, "other": other_amount_found, "study": study_amount_found, "live": live_amount_found, "val": val_amount_found}
    return render(request, "found.html", content)


# 渲染found
def found_elec(request):
    book_amount_found = 0
    val_amount_found = 0
    study_amount_found = 0
    live_amount_found = 0
    card_amount_found = 0
    elec_amount_found = 0
    other_amount_found = 0
    for item in FoundItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_found += 1
        elif item.item_type == "书籍类":
            book_amount_found += 1
        elif item.item_type == "学习用品":
            study_amount_found += 1
        elif item.item_type == "生活用品":
            live_amount_found += 1
        elif item.item_type == "贵重物品":
            val_amount_found += 1
        elif item.item_type == "电子产品":
            elec_amount_found += 1
        elif item.item_type == "其他":
            other_amount_found += 1
    amount_found = book_amount_found + card_amount_found + elec_amount_found + other_amount_found + study_amount_found + live_amount_found + val_amount_found
    items = []
    for item in FoundItemData.objects.all():
        if item.item_type == "电子产品":
            items.append(item)

    items.reverse()
    content = {"found_items": items, "all": amount_found, "card": card_amount_found, "book": book_amount_found, "elec": elec_amount_found, "other": other_amount_found, "study": study_amount_found, "live": live_amount_found, "val": val_amount_found}
    return render(request, "found.html", content)


# 渲染found
def found_other(request):
    book_amount_found = 0
    val_amount_found = 0
    study_amount_found = 0
    live_amount_found = 0
    card_amount_found = 0
    elec_amount_found = 0
    other_amount_found = 0
    for item in FoundItemData.objects.all():
        if item.item_type == "校园卡":
            card_amount_found += 1
        elif item.item_type == "书籍类":
            book_amount_found += 1
        elif item.item_type == "学习用品":
            study_amount_found += 1
        elif item.item_type == "生活用品":
            live_amount_found += 1
        elif item.item_type == "贵重物品":
            val_amount_found += 1
        elif item.item_type == "电子产品":
            elec_amount_found += 1
        elif item.item_type == "其他":
            other_amount_found += 1
    amount_found = book_amount_found + card_amount_found + elec_amount_found + other_amount_found + study_amount_found + live_amount_found + val_amount_found
    items = []
    for item in FoundItemData.objects.all():
        if item.item_type == "其他":
            items.append(item)

    items.reverse()
    content = {"found_items": items, "all": amount_found, "card": card_amount_found, "book": book_amount_found, "elec": elec_amount_found, "other": other_amount_found, "study": study_amount_found, "live": live_amount_found, "val": val_amount_found}
    return render(request, "found.html", content)


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
            edit_form = NormalUserChangeForm(request.POST, instance=request.user)
            if edit_form.is_valid():
                edit_form.save()
                return redirect("main:user_center")
        else:
            edit_form = NormalUserChangeForm(instance=request.user)

        content = {"edit_form": edit_form, "user": request.user}
        return render(request, "info_edit.html", content)

    else:
        return redirect("main:log_in")


# 修改密码
def change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            password_form = PasswordChangeForm(data=request.POST, user=request.user)
            if password_form.is_valid():
                password_form.save()
                return redirect("main:log_in")
        else:
            password_form = PasswordChangeForm(user=request.user)

        content = {"password_form": password_form, "user": request.user}
        return render(request, "change_password.html", content)

    else:
        return redirect("main:log_in")


# 渲染passage_manage
def passage_manage(request):
    return render(request, "passage_manage.html")


# 将物品状态修改为已被认领
def lostitem_return(request, forloop_counter):
    if request.user.is_authenticated:
        items = []
        for item in LostItemData.objects.all():
            items.append(item)
        items.reverse()
        item_change = items[int(forloop_counter)-1]
        item_change.item_status = True
        item_change.save()
        return redirect("main:lost")
    else:
        return redirect("main:log_in")


# 将物品状态修改为已被归还
def founditem_return(request, forloop_counter):
    if request.user.is_authenticated:
        items = []
        for item in FoundItemData.objects.all():
            items.append(item)
        items.reverse()
        item_change = items[int(forloop_counter)-1]
        item_change.item_status = True
        item_change.save()
        return redirect("main:found")
    else:
        return redirect("main:log_in")


# 渲染publish_lost
def publish_lost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST["item_name"]:  # 物品名称必填
                # 分别为物品名称、物品描述、物品类型、丢失时间、丢失地点、物品状态
                # 物品状态默认为False，即未寻回
                new_item = LostItemData(item_name=request.POST["item_name"], item_description=request.POST["item_description"], item_type=request.POST["item_type"], item_time=request.POST["item_time"], item_location=request.POST["item_location"], item_publisher=request.POST["item_publisher"])
                new_item.save()
                return redirect("main:lost")
            else:
                content = {"error": "物品名称必填！"}
                return render(request, "publish_lost.html", content)
        else:  # 外部访问
            return render(request, "publish_lost.html")
    else:
        return redirect("main:log_in")


# 渲染publish_found
def publish_found(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST["item_name"]:  # 物品名称必填
                # 分别为物品名称、物品描述、物品类型、捡到时间、捡到地点、物品状态
                # 物品状态默认为False，即未归还给失主
                new_item = FoundItemData(item_name=request.POST["item_name"], item_description=request.POST["item_description"], item_type=request.POST["item_type"], item_time=request.POST["item_time"], item_location=request.POST["item_location"], item_publisher=request.POST["item_publisher"])
                new_item.save()
                return redirect("main:found")
            else:
                content = {"error": "物品名称必填！", "user": request.user.username}
                return render(request, "publish_found.html", content)
        else:  # 外部访问
            return render(request, "publish_found.html", {"user": request.user.username})
    else:
        return redirect("main:log_in")
