from django.shortcuts import render
from django.http import HttpResponse

def faq(request):
     return render(request,'faq.html')
