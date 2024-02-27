from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')

def guard(request):
      return render(request,'guard.html')

def service(request):
      return render(request,'service.html')
def about(request):
     return render(request,'about.html')