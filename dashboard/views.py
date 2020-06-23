"""
	気象データダッシュボード
	ビュー定義


	Filename views.py
	Date; 2020.6.15
	Written by Nobuharu Shimazu
"""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CSVUpdateForm
from .models import WeatherData, Location
from django.contrib.auth.mixins import LoginRequiredMixin 
import io
import pandas as pd
import numpy as np



class IndexView(generic.ListView):
	"""
		ホーム
	"""
	model = Location
	paginate_by = 5
	ordering = ["-created"]
	template_name = "dashboard/index.html"


class WeatherDataImport(LoginRequiredMixin, generic.FormView):
	"""
		天気でーたインポート用のビュー
	"""
	template_name = "dashboard/import.html"
	success_url = reverse_lazy("dashboard:index")
	form_class = CSVUpdateForm

	def form_valid(self, form):    #予想通りの内容だったら呼び出される。.
		#データの読み込み                                                  ↓文字コードのルール
		csvfile = io.TextIOWrapper(form.cleaned_data["file"], encoding="cp932")         #文字コードは文字の番号
		df = pd.read_csv(csvfile,
				encoding="cp932",
				usecols=[0,1,4,7],
				names=["date","high","low","humidity"],
				)
		location_name = df["high"][2]
		location, created = Location.objects.get_or_create(name=location_name)

		df = df[6:]

		#datetimeに変換
		df["date"] = pd.to_datetime(df["date"], format="%Y/%m/%d")

		#一行ずつ取り出してデータを作成
		df = df.fillna("")  #欠損値を空文字列に変換
		data_np = np.asarray(df)
		
		for row in data_np:
			defaults = {
				"max_temp":row[1],
				"min_temp":row[2],
				"humidity":row[3],
				"location":location,
			}
			data, created = WeatherData.objects.get_or_create(date=row[0], location=location, defaults=defaults)

			if not created:
				data.max_temp = row[1]
				data.min_temp = row[2]
				data.humidity = row[3]
				data.location = location
				data.save()

		return super().form_valid(form)





class GraphView(generic.View):
	"""
		グラフ表示用のJavascriptを生成するビュー
	"""
	template_name = "dashboard/script.js"

	def get(self, request, *args, **kwargs):
		"""
			getメソッド呼び出し時にjavascriptを生成
		"""
		pk = kwargs["pk"]

		#指定されたロケーションの気象データ
		weather_data = WeatherData.objects.select_related("location").filter(location_id=pk)
		#データのプロット
		context = {}
		context["pk"] = pk
		context["date"] = [data.date.strftime("%Y/%m/%d") for data in weather_data]
		context["max_temp"] = [data.max_temp for data in weather_data]
		context["min_temp"] = [data.min_temp for data in weather_data]		
		context["humidity"] = [data.humidity for data in weather_data]

		return render(request, self.template_name, context, content_type="text/javascript")























