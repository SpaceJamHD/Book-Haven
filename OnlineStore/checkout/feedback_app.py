from django.shortcuts import redirect, render
from django.contrib import messages

from models import Feedback

def submit_feedback(request):
    if request.method == 'POST':
        # Получаем данные из формы
        comment_text = request.POST.get('comment')
        rating = request.POST.get('rating')
        item_id = request.POST.get('item_id')  # Предполагая, что вы отправляете ID товара через форму

        # Проверяем, что пользователь аутентифицирован
        if request.user.is_authenticated:
            # Создаем комментарий и сохраняем его в базе данных
            feedback = Feedback.objects.create(
                user=request.user,
                comment=comment_text,
                rating=rating
            )
            messages.success(request, 'Комментарий успешно добавлен.')
        else:
            # Если пользователь не аутентифицирован, перенаправляем на страницу входа
            messages.error(request, 'Чтобы оставить комментарий, вам нужно войти в систему.')
            return redirect('login')  # Замените 'login' на имя вашего представления для входа

        # Перенаправляем на страницу товара или другую страницу
        return redirect('item_detail', item_id=item_id)  # Замените 'item_detail' на имя вашего представления для отображения деталей товара
    else:
        # Если запрос не POST, перенаправляем на главную страницу
        return redirect('home')  # Замените 'home' на имя вашего представления для главной страницы
