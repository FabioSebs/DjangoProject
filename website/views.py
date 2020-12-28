from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
import website.tweepy_streamer as ts
import website.spotify as sp
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

def spotify(request):
    song = sp.Song()
    context= {
        'Bluebird' : song.getSong('Blue Bird'),
        'Netsujo' : song.getSong('Netsujo No Spectrum') , 
        'Sign' : song.getSong('Sign') , 
        'Again' : song.getSong('Again') , 
        'Totsegi' : song.getSong('Totsegi') , 
        'DBZ' : song.getSong('DBZ') ,
        'DeathNote' : song.getSong('DeathNote'),
        'Departure' : song.getSong('Departure'),
    }
    
    return render(request, 'website/spotify.html', context)