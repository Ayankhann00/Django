from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  #return HttpResponse("hey, u are welcome to Home Page")
  return render(request,'index.html')
def about(request):
  return HttpResponse("hey, u are welcome to About Page")

def contact(request):
  return HttpResponse("hey, u are welcome to Contact Page")
