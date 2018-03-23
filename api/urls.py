from django.conf.urls import url
from rest_framework.authtoken import views

from . import api

urlpatterns = [
    url(r'^carousel', api.carousel, name='carousel'),
    url(r'^goodsclass', api.goodsClass, name='goodsClass'),
    url(r'^class(?P<class_id>[0-9]+)$', api.goodsClassParams),
    url(r'^goodsindexshow', api.goodsIndexShow, name='goodsindexshow'),
    url(r'^goodsInit', api.goodsInit, name='goodsInit'),
    url(r'^updategoods', api.updateGoods, name='updategoods'),
    url(r'^deletegoods', api.deleteGoods, name='deletegoods'),
    url(r'^register', api.register, name='register'),
    url(r'^goodsintro', api.goodsIntro, name='goodsIntro'),
    url(r'^userlist', api.getUserList, name='getUserList'),
    url(r'^deleteuser', api.deleteUser, name='deleteUser'),
    url(r'^updateclass', api.updateGoodsClass, name='updateGoodsClass'),
    url(r'^login$', api.login, name='login'),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^goodsList', api.goods_list),
    url(r'^cart', api.cart),
    url(r'^getorder', api.getorder),
    url(r'^deletecart', api.deleteCart),
    url(r'^getems', api.getems),
    url(r'^getorder', api.getorder),
    url(r'^addgoods', api.addgoods),
    # url(r'^upload', api.upload),
]
