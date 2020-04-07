from django.shortcuts import render
from .forms import Appform
from .logic import playStore, appStore
# Create your views here.

def index(request):


    if request.method == "POST":

        form = Appform(request.POST)


        if form.is_valid():

            if form.data['play_app'] != "":

                url = "https://play.google.com/store/apps/details?id=" + form.data['play_app']

                data_dict = playStore(url)


            elif form.data['ios_app'] != "" and form.data['ios_app_no'] !="":


                url = "https://apps.apple.com/in/app/"+ form.data['ios_app'] + "/id"+str(form.data['ios_app_no'])

                data_dict = appStore(url)

            form = Appform

            print(data_dict)

            return render(request, 'index.html',{'form':form,'data':data_dict})


        form = Appform

    else:

        form = Appform()



    return render(request,'index.html',{'form':form,'data':False})