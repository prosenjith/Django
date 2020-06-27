from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('This is Homepage')
    return render(request,'homepage.html')
def about(request):
    #return HttpResponse("About : Prosenjith Roy Shuvo")
    return render(request,'about.html')
