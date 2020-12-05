from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
import website.tweepy_streamer as ts
# Create your views here.
def home(request):
    return render(request, 'website/mainpage.html')

def javascriptversion(request):
    return render(request, 'website/index.html')

class PostListView(ListView):
    model = Post
    template_name = 'website/mainpage.html'
    
def tweets(request):
    context ={
        'quotes' : ts.CreateTweets(),
        'translated': ts.TweetsTranslated()
        } 
    
    return render(request, 'website/tweets.html', context)