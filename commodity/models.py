# coding: utf-8

from datetime import datetime
from enum import Enum

from django.db import models


class CommodityModel(models.Model):

    class Meta:
        verbose_name = '商品'
        db_table = 'commodity'

    id = models.AutoField(verbose_name="主键", primary_key=True)
    name = models.CharField(verbose_name="名称", max_length=128, default="")
    price = models.IntegerField(verbose_name="单价", default=0)
    discounts_price = models.IntegerField(verbose_name="优惠价格", default=0)
    genre = models.IntegerField(verbose_name="商品类型", default=1)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)


class OrderModel(models.Model):

    class Meta:
        verbose_name = '订单'
        db_table = 'order'

    id = models.AutoField(verbose_name="主键", primary_key=True)
    user_id = models.IntegerField(verbose_name="用户id", default=0)
    payment = models.IntegerField(verbose_name="付款", default=0)
    amount = models.IntegerField(verbose_name="订单金额", default=0)
    status = models.IntegerField(verbose_name="状态", default=0)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)


class OrderCommodityMapModel(models.Model):

    class Meta:
        verbose_name = '订单商品映射表'
        db_table = 'order_commodity_map'

    id = models.AutoField(verbose_name="主键", primary_key=True)
    order_id = models.IntegerField(verbose_name="订单id", default=0)
    commodity_id = models.IntegerField(verbose_name="商品id", default=0)
    status = models.IntegerField(verbose_name="状态", default=0)
    count = models.IntegerField(verbose_name="商品个数", default=0)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)


class Coupon(models.Model):

    class Meta:
        verbose_name = '优惠券'
        db_table = 'coupon'

    id = models.AutoField(verbose_name="主键", primary_key=True)
    money = models.IntegerField(verbose_name="金额", default=0)
    genre = models.IntegerField(verbose_name="优惠券类型", default=0)
    commodity_genre = models.IntegerField(verbose_name="支持优惠券的商品类型", default=0)
    is_online = models.IntegerField(verbose_name="是否上线", default=0)
    online_time = models.DateTimeField(verbose_name="上线时间", default=datetime(1970, 1, 1))
    offline_time = models.DateTimeField(verbose_name="下线时间", default=datetime(1970, 1, 1))
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)


class OrderCoupon(models.Model):

    class Meta:
        verbose_name = '订单优惠券'
        db_table = 'order_coupon'

    id = models.AutoField(verbose_name="主键", primary_key=True)
    order_id = models.IntegerField(verbose_name="订单id", default=0)
    coupon_id = models.IntegerField(verbose_name="优惠券id", default=0)
    status = models.IntegerField(verbose_name="状态", default=0)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
