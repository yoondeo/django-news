from django.shortcuts import render

# Create your views here.

def index(request):
    import requests
    import json

    webp_news = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=bfbd724567e94a0694d7d87e3c06c682")
    api = json.loads(webp_news.content)

    return render(request, 'index.html', {'api': api})