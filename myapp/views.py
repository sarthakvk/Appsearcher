
from django.http import JsonResponse
from django.shortcuts import render

from .forms import Appform
from .logic import appStore
from .logic import playStore


# Create your views here.


def home ( request ) :
    return render ( request , template_name = "home.html" )


def appsearch ( request ) :
    form = Appform ( )

    return render ( request , "appsearch.html" , { "form" : form } )


def ajaxsearch ( request ) :
    data = { }

    if request.method == "POST" and request.is_ajax ( ) :

        if request.POST.get ( "store" ) == "1" :

            data [ "play_app" ] = request.POST.get ( "play_app" )

            if data [ "play_app" ] != "" :

                url = ("https://play.google.com/store/apps/details?id=" +
                       data [ "play_app" ])

                data_dict = playStore ( url )

                if data_dict [ "ERROR" ] :
                    return JsonResponse ( { "success" : False } , status = 400 )

            else :

                return JsonResponse ( { "success" : False } , status = 400 )

        else :

            data [ "ios_app" ] = request.POST.get ( "ios_app" )

            data [ "ios_app_no" ] = request.POST.get ( "ios_app_no" )

            if data [ "ios_app" ] != "" and data [ "ios_app_no" ] != "" :

                url = ("https://apps.apple.com/in/app/" + data [ "ios_app" ] +
                       "/id" + str ( data [ "ios_app_no" ] ))

                data_dict = appStore ( url )

                if data_dict [ "ERROR" ] :
                    return JsonResponse ( { "success" : False } , status = 400 )

            else :

                return JsonResponse ( { "success" : False } , status = 400 )

        return JsonResponse ( data_dict , status = 200 )

    return JsonResponse ( { "success" : False } , status = 400 )
