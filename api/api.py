import time
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token

# from api.form import photoForm
# from api.form import NicEditImageForm
from goods import models
from goods.models import Goods, GoodsClass

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login as django_login, logout as django_logout, authenticate as django_auth

import json

# 错误码
ERROR_LOGIN_OK = 100
ERROR_LOGIN_WRONG_PARAMS = 101
ERROR_LOGIN_WRONG_USERNAME_PASSWORD = 102
ERROR_LOGIN_ONLY_POST = 103
ERROR_LOGOUT_OK = 200


def carousel(request):
    carouselList = []
    carouselListAll = models.GoodsCarousel.objects.all()
    for carousel in carouselListAll:
        carouselListName = carousel.CarouselName
        carouselListImg = carousel.CarouselImg
        carouselData = {
            'carouselListName': carouselListName,
            'carouselListImg': carouselListImg,
        }
        carouselList.append(carouselData)
    carouselData = {
        'status': '200',
        'carouselList': carouselList
    }
    return JsonResponse(carouselData)


def goodsClass(request):
    goodsClassList = []
    goodsClassListAll = models.GoodsClass.objects.all()

    for goodsClass in goodsClassListAll:
        goodsClasListsName = goodsClass.GoodsClass
        goodsClassListImg = goodsClass.GoogsClassImg
        GoodsId = goodsClass.id
        goodsClassData = {
            'GoodsId': GoodsId,
            'goodsClassListsName': goodsClasListsName,
            'goodsClassListImg': goodsClassListImg
        }
        goodsClassList.append(goodsClassData)

    goodsClassData = {
        'status': '200',
        'goodsClassList': goodsClassList
    }
    return JsonResponse(goodsClassData)


@csrf_exempt
def goodsClassParams(request, class_id):
    goodsCLassPageList = []
    goodsListAll = Goods.objects.filter(commodity_class_id=class_id)
    for goods in goodsListAll:
        goodsId = goods.id
        goodsName = goods.commodity_name
        goodsPrice = goods.commodity_price
        goodsIntro = goods.commodity_introduce
        goodsImg = goods.commodity_image
        goodsClassPageData = {
            'goodsId': goodsId,
            'goodsName': goodsName,
            'goodsPrice': goodsPrice,
            'goodsIntro': goodsIntro,
            'goodsImg': goodsImg
        }
        goodsCLassPageList.append(goodsClassPageData)
    goodsClassPage = {
        'status': '200',
        'goodsClassPageList': goodsCLassPageList
    }
    return JsonResponse(goodsClassPage)


def goodsIndexShow(request):
    goodsIndexShowList = []
    goodsIndexShowListAll = models.GoodsIndexShow.objects.all()
    for goodsIndexShow in goodsIndexShowListAll:
        goodsIndexShowListName = goodsIndexShow.GoodsIndexShowName
        goodsIndexShowListIntro = goodsIndexShow.GoodsIndexShowIntro
        goodsIndexShowListPrice = goodsIndexShow.GoodsIndexShowPrice
        goodsIndexShowListImg = goodsIndexShow.GoodsIndexShowImg
        goodsIndexShowListData = {
            'goodsIndexShowListName': goodsIndexShowListName,
            'goodsIndexShowListIntro': goodsIndexShowListIntro,
            'goodsIndexShowListPrice': goodsIndexShowListPrice,
            'goodsIndexShowListImg': goodsIndexShowListImg
        }
        goodsIndexShowList.append(goodsIndexShowListData)

    goodsIndexShowData = {
        'status': '200',
        'goodsIndexShowList': goodsIndexShowList
    }
    return JsonResponse(goodsIndexShowData)


def goodsInit(request):
    goodsInitList = []
    goodsInitListAll = models.Goods.objects.all()
    for goods in goodsInitListAll:
        goodsInitListName = goods.commodity_name
        goodsInitListId = goods.id
        goodsInitListData = {
            'value': goodsInitListName,
            'goodsInitListId': goodsInitListId,
        }
        goodsInitList.append(goodsInitListData)

    goodsInitListData = {
        'goodsInitList': goodsInitList,
        'status': '200'
    }
    return JsonResponse(goodsInitListData)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = request.POST.get('username', json_data.get('username'))
        password = request.POST.get('password', json_data.get('password'))
        # headers = request.POST.get('headers', json_data.get('headers'))
        # print("headers:  "+headers)
        print("username: " + username + "password" + password)
        user = django_auth(username=username, password=password)
        if user is None:
            # 用户名/密码非法
            res = JsonResponse({
                'code': ERROR_LOGIN_WRONG_USERNAME_PASSWORD
            })
            return res
        else:
            django_login(request, user)
            res = JsonResponse({
                'name': user.username,
                'code': ERROR_LOGIN_OK,
                'user_email': user.email,
                'user_s': user.is_superuser,
                'success': True,
                'token': default_token_generator.make_token(user),
                'user': user.pk,
            })
            return res
            # token = Token.objects.get(user=user)
            # serializer = TokenSerializer(token)
            # return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    return None


@csrf_exempt
def goods_list(request):
    goods = Goods.objects.all()
    goodsList = []
    for goods in goods:
        goodsName = goods.commodity_name
        goodsId = goods.id
        goodsClass = str(goods.commodity_class)
        goodsPrice = goods.commodity_price
        goodsImage = goods.commodity_image
        goodsPubDate = goods.commodity_pub_date
        goodsIntro = goods.commodity_introduce
        goodsListData = {
            'goodsName': goodsName,
            'goodsId': goodsId,
            'goodsClass': goodsClass,
            'goodsPrice': goodsPrice,
            'goodsImage': goodsImage,
            'goodsPubDate': goodsPubDate,
            'goodsIntro': goodsIntro,
        }
        goodsList.append(goodsListData)

    goodsListData = {
        'goodsList': goodsList,
        'status': '200'
    }
    return JsonResponse(goodsListData)


@csrf_exempt
def updateGoods(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        goods_id = request.POST.get('goodsId', json_data.get('goodsId'))
        goods_name = request.POST.get('goodsName', json_data.get('goodsName'))
        goods_class = request.POST.get('goodsClass', json_data.get('goodsClass'))
        goods_price = request.POST.get('goodsPrice', json_data.get('goodsPrice'))
        goods_class_id = GoodsClass.objects.all().get(GoodsClass=goods_class).id
        Goods.objects.filter(id=goods_id).update(commodity_name=goods_name, commodity_class=goods_class_id,
                                                 commodity_price=goods_price)
        returnData = {
            'status': '200'
        }
        return JsonResponse(returnData)


@csrf_exempt
def deleteGoods(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        goods_id = request.POST.get('goodsId', json_data.get('goodsId'))
        Goods.objects.filter(id=goods_id).delete()
        returnData = {
            'status': '200'
        }
        return JsonResponse(returnData)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = request.POST.get('username', json_data.get('username'))
        password = request.POST.get('password', json_data.get('password'))
        email = request.POST.get('email', json_data.get('email'))

        User.objects.create_user(username, email, password)
        returnData = {
            'status': '200'
        }
        return JsonResponse(returnData)


@csrf_exempt
def getUserList(request):
    userList = []
    userListAll = User.objects.all()
    for user in userListAll:
        userId = user.id
        userName = user.username
        userIsSuperuser = user.is_superuser
        userLoginTime = user.last_login
        if userIsSuperuser:
            userIsSuperuser = '管理员'
        else:
            userIsSuperuser = '用户'
        userData = {
            'userId': userId,
            'userName': userName,
            'userIsSuperuser': userIsSuperuser,
            'userLoginTime': userLoginTime
        }
        userList.append(userData)
    returnUserData = {
        'status': '200',
        'userList': userList
    }
    print(returnUserData)
    return JsonResponse(returnUserData)


@csrf_exempt
def deleteUser(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        userId = request.POST.get('userId', json_data.get('userId'))
        User.objects.filter(id=userId).delete()
    returnData = {
        'status': '200'
    }
    return JsonResponse(returnData)


@csrf_exempt
def updateGoodsClass(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        userId = request.POST.get('goodsId', json_data.get('goodsId'))
        className = request.POST.get('className', json_data.get('className'))
        GoodsClass.objects.filter(id=userId).update(GoodsClass=className)
    returnData = {
        'status': '200'
    }
    return JsonResponse(returnData)


@csrf_exempt
def goodsIntro(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        goodsId = request.POST.get('params', json_data.get('params'))
        goodsData = Goods.objects.get(id=goodsId)
        goodsImg = goodsData.commodity_image
        goodsName = goodsData.commodity_name
        goodsPrice = goodsData.commodity_price
        goodsIntro = goodsData.commodity_introduce
        goodsClass = str(goodsData.commodity_class)
        goodsList = {
            'goodsId': goodsId,
            'goodsImg': goodsImg,
            'goodsName': goodsName,
            'goodsPrice': goodsPrice,
            'goodsIntro': goodsIntro,
            'goodsClass': goodsClass
        }
        goodsDataList = {
            'status': '200',
            'goodsList': goodsList
        }
    return JsonResponse(goodsDataList)


@csrf_exempt
def cart(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        userId = request.POST.get('userId', json_data.get('userId'))
        goodsId = request.POST.get('goodsId', json_data.get('goodsId'))
        goodsPrice = request.POST.get('goodsPrice', json_data.get('goodsPrice'))
        # models.cart.
        models.cart(goodsNum=1, goodsId=goodsId, userId=userId, goodsPrice=goodsPrice).save()
        returnData = {
            'status': '200'
        }
        return JsonResponse(returnData)


@csrf_exempt
def getorder(request):
    if request.method == 'POST':
        cartList = []
        json_data = json.loads(request.body)
        userId = request.POST.get('userId', json_data.get('userId'))
        print(userId)
        orders = models.cart.objects.filter(userId=userId)
        for cart in orders:
            goodsName = Goods.objects.get(pk=cart.goodsId).commodity_name
            userId = cart.userId
            goodsNum = cart.goodsNum
            goodsId = cart.goodsId
            goodsPrice = cart.goodsPrice
            cartListData = {
                'goodsName': goodsName,
                'userId': userId,
                'goodsNum': goodsNum,
                'goodsId': goodsId,
                'goodsPrice': goodsPrice
            }
            if cartListData not in cartList:
                cartList.append(cartListData)
        cartListReturn = {
            'status': '200',
            'cartList': cartList
        }
        print(cartList)
        return JsonResponse(cartListReturn)


@csrf_exempt
def deleteCart(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        userId = request.POST.get('userId', json_data.get('userId'))
        models.cart.objects.filter(userId=userId).delete()
        returnData = {
            'status': '200'
        }
        return JsonResponse(returnData)


@csrf_exempt
def getems(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        userid = request.POST.get('userid', json_data.get('userid'))
        userName = request.POST.get('userName', json_data.get('userName'))
        address = request.POST.get('address', json_data.get('address'))
        detailAddress = request.POST.get('detailAddress', json_data.get('detailAddress'))
        getdate = request.POST.get('date', json_data.get('date'))
        ems = request.POST.get('ems', json_data.get('ems'))
        phone = request.POST.get('phone', json_data.get('phone'))
        models.address(userId=userid, userName=userName, address=address, detailAddress=detailAddress, date=getdate,
                       ems=ems, phone=phone).save()
        returnData = {
            'status': '200'
        }
        return JsonResponse(returnData)


@csrf_exempt
def getorder(request):
    if request.method == 'POST':
        cartList = []
        json_data = json.loads(request.body)
        userId = request.POST.get('userId', json_data.get('userId'))
        address = models.address.objects.get(userId=userId)
        orders = models.cart.objects.filter(userId=userId)
        for cart in orders:
            goodsName = Goods.objects.get(pk=cart.goodsId).commodity_name
            userId = cart.userId
            goodsNum = cart.goodsNum
            goodsId = cart.goodsId
            goodsPrice = cart.goodsPrice
            cartListData = {
                'goodsName': goodsName,
                'userId': userId,
                'goodsNum': goodsNum,
                'goodsId': goodsId,
                'goodsPrice': goodsPrice
            }
            if cartListData not in cartList:
                cartList.append(cartListData)
        addressList = {
            'id': address.id,
            'userId': address.userId,
            'userName': address.userName,
            'address': address.address,
            'detailAddress': address.detailAddress,
            'date': address.date,
            'phone': address.phone
        }
        address = {
            'address': addressList
        }
        orderList = {
            'status': '200',
            'address': address,
            'cartList': cartList
        }
        return JsonResponse(orderList)


@csrf_exempt
def addgoods(request):
    if request.method == 'POST':
        cartList = []
        json_data = json.loads(request.body)
        goodsName = request.POST.get('goodsName', json_data.get('goodsName'))
        goodsClass = request.POST.get('goodsClass', json_data.get('goodsClass'))
        goodsPrice = request.POST.get('goodsPrice', json_data.get('goodsPrice'))
        goodsdesc = request.POST.get('goodsdesc', json_data.get('goodsdesc'))
        goodsClass_id = GoodsClass.objects.all().get(GoodsClass=goodsClass).id
        models.Goods(commodity_class=goodsClass_id, commodity_name=str(goodsName), commodity_price=goodsPrice,
                     commodity_introduce=goodsdesc).save()
        returnData = {
            'status': '200'
        }
        return JsonResponse(returnData)

# @csrf_exempt
# def upload(request):
#     if request.method == 'POST':
#         # form = photoForm(request.POST, request.FILES)
#         Goods.commodity_upload.save('1', save=False)
#         Goods.save()
#         # form = NicEditImageForm(request.POST or None, request.FILES or None)
#         # image.name = str(time) + '.png'
#         # image = form.save()
#         # s = Goods(image=image)
#         # s.save()
#         returnData = {
#             'status': '200',
#             # 'imgname': image.name
#         }
#         return JsonResponse(returnData)

# @csrf_exempt
# def goods_list(request):
#     goods = Goods.objects.all()
#     serializer = SnippetSerializer(goods,)
# @csrf_exempt
# def goods_list(request, pk):
#     try:
#         goods = Goods.objects.get(pk=pk)
#     except Goods.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         goods =
