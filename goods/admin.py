from django.contrib import admin
from .models import Goods, GoodsClass, GoodsComment, GoodsCarousel, GoodsIndexShow


class GoodsAdmin(admin.ModelAdmin):
    fields = ['commodity_name', 'commodity_class', 'commodity_image', 'commodity_price', 'commodity_introduce',
              'commodity_pub_date','commodity_upload',]


admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsComment)
admin.site.register(GoodsClass)
admin.site.register(GoodsCarousel)
admin.site.register(GoodsIndexShow)
