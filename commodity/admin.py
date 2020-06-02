# coding: utf-8

from django.contrib import admin

from commodity.models import (
	CommodityModel,
	OrderCommodityMapModel,
	OrderCoupon,
	OrderModel,
	Coupon,
)


admin.site.register([CommodityModel, OrderCommodityMapModel, OrderCoupon, OrderModel, Coupon])
