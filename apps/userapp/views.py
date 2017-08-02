# __*__coding:utf-8__*__
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
from userapp.service.originalElectricityService import originalElectricityService


def DefaultView(request):
    return render(request, 'main.html')


def liuyanView(request):
    return render(request, 'liuyan.html')


def ajaxView(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')
    # return HttpResponse('大萍',content_type='application/json')


@csrf_exempt
def testView(request):
    if request.is_ajax():
        ret = {'status': True, 'error': ""}
        try:
            print(request.POST)
            names = request.POST.getlist('names456[]')
            for x in names:
                print(x)
        except Exception as e:
            ret['status'] = False
            ret['error'] = str(e)
        #return HttpResponse(json.dumps(ret))
        return JsonResponse(ret)
    else:
        return render(request, 'testInput.html')
