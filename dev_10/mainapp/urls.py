import mainapp.views as mainapp
from django.urls import path


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('news_page/<int:pk>', mainapp.news_page, name='news_page'),
    # path('news/', mainapp.news, name='news'),

]
