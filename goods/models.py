from django.db import models


class GoodsClass(models.Model):
    GoodsClass = models.CharField('商品类别', max_length=100)
    GoogsClassImg = models.CharField("商品类别图片", max_length=200, blank=True)

    def __str__(self):
        return self.GoodsClass


class Goods(models.Model):
    commodity_upload = models.ImageField(upload_to='goods', blank=True, null=True)
    commodity_class = models.ForeignKey(GoodsClass, verbose_name='商品类别')
    commodity_name = models.CharField('商品名称', max_length=100)
    commodity_price = models.IntegerField('商品价格')
    commodity_pub_date = models.DateField('发布日期')
    commodity_image = models.CharField('商品图片', blank=True, max_length=100)
    commodity_introduce = models.TextField('商品介绍')

    def __str__(self):
        return self.commodity_name


class GoodsComment(models.Model):
    goods = models.ForeignKey(Goods)
    goodsComent = models.TextField('商品评价', max_length=200)


class GoodsCarousel(models.Model):
    CarouselName = models.CharField('Carousel名称', max_length=100)
    CarouselImg = models.CharField('Carousel地址', max_length=100)


class GoodsIndexShow(models.Model):
    GoodsIndexShowName = models.CharField('首页展示商品名称', max_length=100)
    GoodsIndexShowIntro = models.CharField('首页展示商品介绍', max_length=100)
    GoodsIndexShowPrice = models.CharField('首页展示商品价格', max_length=50)
    GoodsIndexShowImg = models.CharField('首页展示商品图片', max_length=100, blank=True)


class order(models.Model):
    goodsId = models.ForeignKey(Goods)


class cart(models.Model):
    goodsId = models.IntegerField(blank=True)
    userId = models.IntegerField()
    goodsNum = models.IntegerField(blank=True)
    goodsPrice = models.CharField(max_length=10, blank=True)


class address(models.Model):
    userId = models.CharField(max_length=10)
    userName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    detailAddress = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    ems = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    finished = models.BooleanField(default=False)
