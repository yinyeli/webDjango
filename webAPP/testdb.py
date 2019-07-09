# -*- coding: utf-8 -*-
import win32api

import win32con
from django.http import HttpResponse
from django.shortcuts import render_to_response

from webAPP.models import User, BookInfo


#数据库操作


def xq(request):
    txt_id = request.GET.get('p1')
    books = BookInfo.objects.filter(id=txt_id)
    # books = BookInfo.objects.filter(id=1)
    return render_to_response("web/商品详情.html", locals())

#def onsale(request):
    #response = ""
    #response1 = ""
def fenlei(request):
    reponse = ""
    reponse1 = ""
    fenleis = BookInfo.objects.all()
    return render_to_response("web/search.html",locals())
def detail(request):
    txt_id = request.GET.get("p2")
    txt_price = request.GET.get("p5")
    request.session['book_id'] = txt_id
    request.session['book_price'] = txt_price
    details = BookInfo.objects.filter(id = txt_id)
    # details = BookInfo.objects.filter(id=1)
    return render_to_response("web/商品详情2.html",locals())

