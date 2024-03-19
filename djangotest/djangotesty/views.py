from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def page_one(request):
    return render(request, 'page_one.html')
def page_two(request):
    return render(request, 'page_two.html')
def page_three(request):
    return render(request, 'page_three.html')
@login_required(login_url='/admin/login/')
def admin_only_page(request):
# Это представление требует, чтобы пользователь был вошедшим в систему
    return render(request, 'admin_only_page.html')

@login_required
def my_view(request):
    # Пользовательские данные, которые мы хотим отобразить на странице
    context = {
        'username': request.user.username,
        'email': request.user.email,
        # Вы можете добавить сюда любые другие данные, которые хотите отобразить
    }
    # Передача данных в шаблон `my_template.html`
    return render(request, 'djangotesty/my_template.html', context)