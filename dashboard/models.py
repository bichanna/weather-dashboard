"""
	気象データダッシュボード
	データモデル

	Filename models.py
	Date; 2020.6.8
	Written by Nobuharu Shimazu

"""
from django.db import models
from django.utils import timezone


class Location(models.Model):
	"""
		場所用のテーブル
		name: 場所の名前
		created: 作成日

	"""
	name = models.CharField(max_length=255, verbose_name="場所")
	created = models.DateTimeField(verbose_name="作成日",default=timezone.now)
	def __str__(self):
		return self.name

class WeatherData(models.Model):
	"""
		気象データ
		location: 観測場所
		max_temp: 最高気温
		min_temp: 最低気温
		humidity: 最近湿度
		date : 日付
	"""
	location = models.ForeignKey(Location, verbose_name="場所",on_delete=models.CASCADE)
	max_temp = models.FloatField(verbose_name="最高気温")
	min_temp = models.FloatField(verbose_name="最低気温")
	humidity = models.FloatField(verbose_name="湿度")
	date = models.DateField(verbose_name="日付")


	def __str__(self):
		return "{}:{}".format(self.location.name, self.date)