from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    pname = request.GET.get('play-name')

    if pname == "":
        play = False
        pname = request.GET.get('app-name')
        pid = request.GET.get('app-id')
        print(pname,pid)
    else:
        play = True
        print(pname)

    return render(request,'index.html')