from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def submit(request):
    # if request.method=='POST':
    #     name=request.POST['name']
    #     email=request.POST['email']
    print("Hi")
    return render(request,'update.html')
