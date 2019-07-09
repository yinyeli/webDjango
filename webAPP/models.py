from django.db import models

# Create your models here.

# 用户信息
class User(models.Model):
    username = models.CharField(max_length=20) # 账号
    password = models.CharField(max_length=20) # 密码
    permission = models.IntegerField() # 用户类别：0：超级用户admin  1：买方用户 2：卖方用户
    name = models.CharField(max_length=256) #姓名
    age = models.CharField(max_length=10)  # 年龄
    gender = models.CharField(max_length=10) # 性别
    # gender = models.IntegerField()

# 图书信息
class BookInfo(models.Model):
    isbn = models.CharField(max_length=256) #isbn
    title = models.CharField(max_length=256) # 书名
    author = models.CharField(max_length=256) # 作者
    publish = models.CharField(max_length=256)# 出版社
    publish_year = models.CharField(max_length=256)# 出版年份
    score = models.CharField(max_length=256) # 评分
    price = models.CharField(max_length=256) # 价格
    description = models.TextField() # 内容介绍
    img = models.ImageField(upload_to='imgs')
    kind = models.CharField(max_length=256) # 类别
    tag = models.CharField(max_length=256) # 标签
    seller_id = models.IntegerField()


# 订单信息
class Orders(models.Model):
    time = models.CharField(max_length=256) # 时间
    buyer = models.CharField(max_length=256) # 买方用户id
    seller = models.CharField(max_length=256) # 卖方用户id
    book_id = models.CharField(max_length=256)# book id
    count_product = models.CharField(max_length=256)# 商品数量
    money = models.CharField(max_length=256) # 总价

# 店铺信息
class Store(models.Model):
    store_name = models.CharField(max_length=256) # 店铺名称
    seller = models.IntegerField() # 卖家的id