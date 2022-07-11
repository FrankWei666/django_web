from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse


# Create your views here.

def index(request, year, month):
    print(year, month)
    return HttpResponse(year + '/' + month)


def login(request):
    if request.method == "GET":
        return HttpResponse('hello')
    else:
        username = request.POST['username']
        pwd = request.POST['pwd']
        if username == 'hello' and pwd == 'hello':
            return HttpResponse('hello hi')
        else:
            return redirect(reverse('login', kwargs={'year': 2022}))


def hello(request):
    return HttpResponse('hello world 2022')


def sun(request):
    context = dict()
    context['hello'] = 'hello world 1314'
    return render(request, 'hello.html', context)


def edu(request):
    views_name = '菜菜----菜鸟教程'
    return render(request, 'runoob.html', {'name': views_name})


def cal_size(request):
    context = '我爱你'
    num = 1024
    return render(request, 'runoob.html', {'context': context, 'num': num})


def get_name(request):
    # name = request.GET.get('name')
    name = request.GET['name']
    return HttpResponse('姓名：{}'.format(name))


def get_body(request):
    name = request.body
    print(name)
    return HttpResponse('ojbk')


def get_path(request):
    name = request.path
    print(name)
    return HttpResponse('okkkkk')


def get_method(request):
    name = request.method
    print(name)
    return HttpResponse('get method')
