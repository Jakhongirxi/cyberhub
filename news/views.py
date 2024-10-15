from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import News, Comment
from news.forms import CommentForm
import logging

# Получаем объект логгера для текущего модуля
logger = logging.getLogger(__name__)

def index(request):
    # Логируем параметры запроса
    logger.info("Request GET parameters: %s", request.GET)

    news_list = News.objects.all().order_by('-pub_date')
    paginator = Paginator(news_list, 4)  # Показывать 4 новости на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Логируем текущую страницу пагинации
    logger.info("Current page number: %s", page_obj.number)

    return render(request, 'news/index.html', {'page_obj': page_obj})
def news_view(request):
    # Получаем все новости и сортируем их по дате публикации
    news_list = News.objects.all().order_by('-pub_date')

    # Создаем объект Paginator с 4 новостями на странице
    paginator = Paginator(news_list, 10)

    # Получаем номер текущей страницы из параметров запроса
    page_number = request.GET.get('page')

    # Получаем объекты на текущей странице
    page_obj = paginator.get_page(page_number)

    # Логируем текущую страницу пагинации
    logger.info("Current page number: %s", page_obj.number)

    # Рендерим страницу новостей с передачей объектов на текущей странице
    return render(request, 'news/news.html', {'page_obj': page_obj})


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments = Comment.objects.filter(news=news)
    if request.method == "POST":
        if request.user.is_authenticated:  # Проверьте, авторизован ли пользователь
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.news = news
                comment.user = request.user  # Установите пользователя на текущего авторизованного пользователя
                comment.save()
                return redirect('news:news_detail', pk=news.id)
        else:
            return redirect('users:login')  # Перенаправьте на страницу входа, если пользователь не авторизован
    else:
        form = CommentForm()
    return render(request, 'news/detail.html', {'news': news, 'form': form, 'comments': comments})