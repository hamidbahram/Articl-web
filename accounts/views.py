from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
import json
import requests
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def signup_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # user = form.save()
            #log the user in
            # login(request, user)
            # return redirect('articles:list')
            #recaptcha
            clientkey = request.POST['g-recaptcha-response']
            secretkey = '6LfF7MUUAAAAAOQsXKZyLppbrTFlUzU2A03xsKnB'
            captchaData = {
                'secret' : secretkey,
                'response' : clientkey
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = captchaData)
            print(r.text)
            response = json.loads(r.text)
            verify = response['success']
            print('your success is : ',verify)
            if verify:
                user = form.save()
                login(request, user)
                return redirect('articles:list')
            else:
                form = UserCreationForm
            return render(request, 'accounts/signup.html', {'form':form})
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})
    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
