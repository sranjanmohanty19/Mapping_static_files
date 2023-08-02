from django.shortcuts import render

# Create your views here.
def demon(request):
    return render(request,'demon.html')