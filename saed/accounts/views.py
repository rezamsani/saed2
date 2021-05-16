from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def home_page_after_login(request):            
    return render(request, 'accounts/home_page_after_login.html')

