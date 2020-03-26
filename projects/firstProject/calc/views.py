from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    #return HttpResponse("Hello World") #This is one method just to return the content
    #return HttpResponse("<h1> Hello World </h1>") #this is another method to return as HTML response
    #the below method is to return the html page from templates dir
    return render(request,'multiplyNumbers.html',{'name': 'Nimmo'})
    #return render(request, 'hello.html', {'name': 'Nimmo'})

def add(request):

    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2

    return render(request,'result.html', {'result': res})


def multiplied(request):

    num1 = int(request.POST["val1"])
    num2 = int(request.POST["val2"])
    mult = num1 * num2

    return render(request,'result.html',{'result':mult})