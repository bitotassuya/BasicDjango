from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    tags = ["น้ำตกทรายขวว", "น้ำตกลำพะยา", "พุปาโกย", "สนามช้าง"]
    rating = 4
    return render(request, 'index.html',
                  {'name': 'บทความท่องเที่ยวภาคเหนือ',
                   'Author': 'จิรพงษ์', 'tags': tags,

                   'rating': rating
                   })


def page1(request):
    return render(request, 'page1.html')


def createFrom(request):
    return render(request, "form.html")


def addForm(request):
    name = request.POST['name']
    description = request.POST['description']
    return render(request, "result.html",
                  {'name': name,
                   'description': description,
                   })


def addtest(request):
    return render(request, "addtest.html")


def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2

    return render(request, "result.html", {'result': res})
