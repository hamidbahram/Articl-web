from django.shortcuts import render

# Create your views here.

def signup_views(request):
    return render(request, 'accounts/signup.html')