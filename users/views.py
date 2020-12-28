from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, QuoteInsertForm
from django.contrib.auth.decorators import login_required
#from .models import Quotes
# Create your views here.

#Views are used to display a template to your website url 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! {username} is able to login')
            return redirect('website-home')
    else:
        form = UserRegisterForm()
        
    return render(request , 'users/register.html', {'form':form})

@login_required
def userprofile(request):
    
    
    if request.method == 'POST':  
        
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES ,instance = request.user.profile)
        q_form = QuoteInsertForm(request.POST, instance = request.user.profile.quotes)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            if q_form.is_valid():
                q_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
            
        
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
        q_form = QuoteInsertForm(instance=request.user.profile.quotes)
        
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'q_form': q_form,
    }
    return render(request, 'users/profile.html', context)



            
        
    