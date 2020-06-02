# coding: utf-8


from django.urls import path

from .view import CommodityView

commodity_urls = [
	path('hello', CommodityView.as_view(), name='commodity-view'),
]
