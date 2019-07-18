from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
site = {
    'name':'AdminLTE',
    'version':'0.1.0'
}

def index(request):
    context={
        'site':site
    }
    return render(request, 'adminlte/index.html',context)

def index2(request):
    context={
        'site':site
    }
    return render(request, 'adminlte/index2.html',context)

def signin(request):
    context={
        'site':site
    }
    return render(request, 'adminlte/signin.html',context)

def signout(request):
    context={
        'site':site
    }
    response = HttpResponseRedirect('/signin/',context)
    return response
