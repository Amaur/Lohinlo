from django.shortcuts import render,HttpResponse

# Create your views here.

def Index(request):
    return render(request, 'inicio/index.html')

def About(request):
    return render(request, 'inicio/about.html')

def Cat(request):
    return render(request, 'category/cat.html')

def Archive(request):
    return render(request, 'inicio/archive.html')

def Login(request):
    return render(request, 'inicio/signin.html')
def Register(request):
    return render(request, 'inicio/register.html')


def Search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        print "Done..."
        message = q
    else:
        print "Failed..!"
        message = 'Failed..!'
    
    return render(request, 'inicio/search.html', {'mes':message})
    

