"""
	気象データダッシュボード
	フォーム

	Filename forms.py
	Date: 2020.6.8
	Written by Nobuharu Shimazu

"""
from django import forms

class CSVUpdateForm(forms.Form):
	"""
		CSVを登録するためのフォーム
	"""
	file = forms.FileField(label="CSVファイル",help_text="拡張子がCSVのファイルをアップロードしてください。")