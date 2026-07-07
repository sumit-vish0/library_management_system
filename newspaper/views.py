from django.shortcuts import render
from newsapi import NewsApiClient

def daily_newspaper(request):
    newsapi = NewsApiClient(api_key='dca60eece19e42ca80f3ae7d782a4405')
    articles = []
    
    try:
        # Fetch global headlines in English 
        top_headlines = newsapi.get_top_headlines(language='en')
        articles = top_headlines.get('articles', [])
    except Exception as e:
        print(f"Error fetching news: {e}")
        
    context = {'news_list': articles}
    return render(request, 'newspaper/dashboard.html', context)