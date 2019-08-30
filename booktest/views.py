from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    '''首页'''
    return render(request,'booktest/index.html')

def login(request):
    '''登陆页面'''
    return render(request,'booktest/login.html')

def login_check(request):
    '''登陆页面'''
    #1.获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(password+username)
    #2.登陆校验
    if username == '11' and password == '22':
        #正确跳转到首页
        return redirect('/index')

    else:
        # 错误跳转到登陆
        return redirect('/login')

def ajax_test(request):
    return render(request,'booktest/ajax_test.html')

def ajax_handle(request):

    return JsonResponse({'res':1})

def login_ajax(request):
    '''ajax登陆页面'''
    return render(request,'booktest/login_ajax.html')

def login_ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == '11' and password == '22':
        return JsonResponse({'res':1})
    else:
        return JsonResponse({'res':0})


