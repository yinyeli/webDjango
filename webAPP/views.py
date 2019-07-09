import datetime

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
import logging
from webAPP.models import User,Orders,Store,BookInfo
from django.http import HttpResponse
from django.shortcuts import render_to_response
import random
# Create your views here.

def up_img(req):
    return render(req, 'web/upload_img_text.html')


def first(request):
    return render_to_response("web/登录.html", locals())

def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            try:
                user = User.objects.get(username=username)
            except:
                return render(request, 'web/登录.html',{'login_false':'用户名或密码为空'})
            if user.password == password:
                request.session['login_id'] = user.id
                if user.permission == 1: # 买家用户
                    return redirect('/home/')
                elif user.permission == 2: # 卖家用户
                    return redirect('/mygxin/')
            else:
                return render(request, 'web/登录.html',{'login_false':'用户名或密码错误'})

    return render(request, 'web/登录.html')

def register(request):
    txt_username = request.POST.get('txt_username')
    txt_password = request.POST.get('txt_password')
    txt_repassword = request.POST.get('txt_repassword')
    txt_name = request.POST.get('txt_name')
    txt_age = request.POST.get('txt_age')
    txt_gender = request.POST.get('txt_gender')
    txt_account_kind = request.POST.get('account_kind')

    if txt_username and txt_password and txt_repassword:
        same_username = User.objects.filter(username=txt_username)
        if same_username:
            return render(request, 'web/register.html',{'register_false':'帐号已被注册！'})
        elif txt_password != txt_repassword :
            return render(request, 'web/register.html',{'register_false':'两次密码输入不一致！'})
        else:
            login_user = User()
            login_user.permission = txt_account_kind
            login_user.username = txt_username
            login_user.password = txt_password
            login_user.name = txt_name
            login_user.age = txt_age
            login_user.gender = txt_gender
            login_user.save()
            return render(request, 'web/登录.html')
    else:
        return render(request, 'web/register.html', {'register_false': '请完善信息！'})

def change(request):
    if request.method == "POST":
        username = request.POST.get('z')
        oldpassword = request.POST.get('u')
        newpassword = request.POST.get('p')
        repassword = request.POST.get('rp')
        user = authenticate(username=username, password=oldpassword)
        if (username and oldpassword and newpassword and repassword):
            user = User.objects.get(username=username)
            if (user.password == oldpassword and newpassword == repassword): # 信息正确，修改密码
                user.password = newpassword
                user.save()
                return render(request, 'web/登录.html')
            elif(user or user.password != oldpassword):
                return render(request, 'web/修改密码.html', {'change_false': '账号密码信息错误'})
            elif(newpassword != repassword):
                return render(request, 'web/修改密码.html', {'change_false': '两次输入密码不一致！'})

    return render(request, 'web/修改密码.html')


#商家
def index(request):
    return render(request, 'web/index.html')
def mygxin(request):
    return render(request, 'web/mygxin.html')
def myorderq(request):
    return render(request, 'web/myorderq.html')
def upload(request):
    isbn=request.GET.get('isbn')
    title = request.GET.get('title')
    score = request.GET.get('score')
    author = request.GET.get('author')
    kind = request.GET.get('kind')
    publish = request.GET.get('publish')
    publishyear = request.GET.get('publishyear')
    desc = request.GET.get('desc')
    price = request.GET.get('price')
    img = request.GET.get('img')
    tag = request.GET.get('tag')
    seller = request.session['login_id']

    if title and isbn and img:
        book = BookInfo()
        book.isbn = isbn
        book.title = title
        book.score = score
        book.author = author
        book.kind = kind
        book.tag = tag
        book.publish = publish
        book.description = desc
        book.price = price
        book.publish_year = publishyear
        book.img = img
        book.seller_id = seller
        book.save() # 保存图书信息

        print(book.id,request.session['login_id'])
        store = Store()
        store.books = book.id
        store.seller = request.session['login_id']
        store.save() # 商家拥有的图书列表
        return redirect('/index/')

    else:
        return render(request, 'web/upload_book.html')

def liebiao(request):
    seller_id = request.session['login_id']
    liebiaos = BookInfo.objects.filter(seller_id=seller_id)
    return render_to_response("web/index.html",{'liebiaos':liebiaos})


def tuijian(request):
    rand = random.uniform(1, 100)  # 生成随机数
    books = BookInfo.objects.all()[rand:rand+5]
    return render_to_response("web/主页.html",{'books': books,} )

def home(request):
    return render(request, 'web/主页.html')
def save(request): # 买家--->订单页面
    return render(request, 'web/我的收藏.html')
def shopping_cart(request):
    return render(request, 'web/我的购物车.html')
def order(request):
    return render(request, 'web/订单界面.html')
def writeorder(request):
    return render(request, 'web/writeorder.html')
def search(request):
    return render(request, 'web/search.html')
def orderxq(request):
    return render(request, 'web/订单详情.html')
def objectxq(request):
    return render(request, 'web/商品详情1.html')
def personal(request):
    return render(request, 'web/personal-Info.html')




logger = logging.getLogger('login.views')
def rizhi(request):
    try:
        raise Exception
    except Exception as e:
        logger.debug('views.rizhi()....')
    return render(request, 'web/主页.html', {})

def buy(request):
    book_id = request.GET.get('count_products')
    id = request.session['login_id']
    now_time = datetime.datetime.now()
    buys = Orders()
    buys.time = now_time
    buys.buyer = id
    buys.seller = 1
    buys.book_id = book_id
    buys.save()
    return render(request, 'web/主页.html')

