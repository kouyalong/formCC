# coding: utf-8


from django.test.client import Client
from django.test.testcases import TestCase


class CommodityTestCase(TestCase):

	def test_hello(self):
		client = Client()
		response = client.get("/hello")
		print(response.status_code, response.content)
