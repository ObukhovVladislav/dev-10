from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from mainapp.models import News


@login_required()
def index(request):
    news_list = News.objects.all()
    pagination = Paginator(news_list, 5)  # показывает 5 новостей
    page_number = request.GET.get('page', 1)
    page = pagination.get_page(page_number)
    is_pagination = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page{}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page{}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'title': 'главная',
        'page': page,
        'is_pagination': is_pagination,
        'next_url': next_url,
        'prev_url': prev_url,
    }
    return render(request, 'mainapp/index.html', context)


def news_page(request, pk):
    news_list = News.objects.filter(id=pk)
    context = {
        'title': 'Новости',
        'news_list': news_list,
    }
    return render(request, 'mainapp/news_page.html', context)
