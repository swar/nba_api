from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("這是首頁")  # 或使用 render 回傳 HTML 模板
