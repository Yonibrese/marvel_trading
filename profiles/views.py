from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . import forms


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_psw = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_psw)
            login(request, user)
            return redirect('welcome')
    else:
        form = forms.SignUpForm()
    return render(request, 'profiles/signup.html', {'form': form})
