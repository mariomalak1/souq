from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from django.utils.html import format_html

# Register your models here.

admin.site.site_title = "M&G products "
admin.site.site_header ="M&G product"

class Product_Admin(admin.ModelAdmin):
    def photo_tag(self,obj):
        return format_html(f'<img src = "/media/{obj.image]}" style= "height:200px;width:80px">')


class Order_Admin(admin.ModelAdmin):
    fields = ("complete",)


admin.site.unregister(Group),
admin.site.register(Product,Product_Admin),
admin.site.register(Man),
admin.site.register(Order,Order_Admin),