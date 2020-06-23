"""
	気象データダッシュボード
	url定義

	Filename urls.py
	Date: 2020.6.15
	Written by Nobuharu Shimazu
"""

from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
	path("", views.IndexView.as_view(), name="index"),
	path("add", views.WeatherDataImport.as_view(), name="import_csv"),
	path("data/<int:pk>.js", views.GraphView.as_view(), name="plot"),
]