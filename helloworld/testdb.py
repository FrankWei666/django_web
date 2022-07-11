from django.http import HttpResponse
from testModel.models import Test


def testdb(request):
    """添加数据"""
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse('<p> 数据添加成功！</p>')


def getdb(request):
    # 初始化
    response = ""
    response1 = ""

    all_db_list = Test.objects.all()  # 相当于select * from

    response2 = Test.objects.filter(id=1)

    response3 = Test.objects.get(id=1)

    # for var in all_db_list:
    #     response1 += var.name + " "

    for var in response2:
        response1 += var.name + " "

    response = response1

    # return HttpResponse("<p>" + response + '\t' + response2 + '\t' + response3 + "</p>")
    # return HttpResponse("<p>" + response + "</p>")
    return HttpResponse(response)


def update_db(request):
    """更新数据"""
    # test1 = Test.objects.get(id=1)
    # test1.name = 'Google'
    # test1.save()
    Test.objects.filter(id=1).update(name='Google')
    return HttpResponse('<H1>修改成功</H1>')


def del_db(request):
    """删除数据"""
    Test.objects.filter(id=1).delete()

    return HttpResponse('<H1>删除成功</H1>')
