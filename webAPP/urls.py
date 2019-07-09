from django.shortcuts import render
from django.urls import path

from . import testdb,views
from django.contrib import admin




urlpatterns = [
    path('up_img', views.up_img),
    path('',views.first), # 第一个页面转到登录界面
    path('login/', views.login), # 传递登录参数
    path('register/', views.register), # 转到登录界面，传递登录参数

    # yyl
    path('mygxin/', views.mygxin),  # 商家，我的信息页面
    path('myorderq/', views.myorderq),  # 查看我的订单，完成无数据
    path('xq/', testdb.xq),  # 图书详情,完成
    path('object2/', testdb.detail),  # 商品详情2，完成
    path('upload/', views.upload),  # 商品添加，完成
    path('change/', views.change),  # 修改密码，完成
    path('buy/',views.buy),
    path('index/', views.liebiao), # 商家图书列表


 # 16个url
    #fyh
    path('home/',views.tuijian),
    path('home/',views.home),
    path('save/',views.save),
    path('shopping_cart/',views.shopping_cart),
    path('order/',views.order),

    # fzy
    path('write/',views.write),
    path('search/',testdb.fenlei),
    path('orderxq/',views.orderxq),
    path('objectxq/',views.objectxq),
    path('personal/',views.personal),

    path('writeorder/',views.writeorder),
]