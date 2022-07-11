from django.shortcuts import render
#from django.http import HttpResponse

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
