from django.contrib import admin

# Register your models here.
from webAPP.models import User,BookInfo,Orders,Store

admin.site.register(User)
admin.site.register(BookInfo)
admin.site.register(Orders)
admin.site.register(Store)