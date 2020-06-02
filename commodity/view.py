# coding: utf-8


from django.http.response import HttpResponse
from django.views import View


class CommodityView(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse("hello")
