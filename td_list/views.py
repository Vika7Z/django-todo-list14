from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    # host = request.META["HTTP_HOST"]  # получаем адрес сервера
    # user_agent = request.META["HTTP_USER_AGENT"]  # получаем данные браузера
    # path = request.path  # получаем запрошенный путь
    #
    # return HttpResponse(f"""
    #         <p>Host: {host}</p>
    #         <p>Path: {path}</p>
    #         <p>User-agent: {user_agent}</p>
    #     """)

    # return HttpResponse('Главная(index): hello to do list!')

    return render(request, 'index.html')


def about(request):
    return HttpResponse('О сайте(about)')


def to_do_list(request):
    return HttpResponse('Список(to_do_list)')
