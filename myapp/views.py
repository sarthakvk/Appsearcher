from django.http import JsonResponse
from django.shortcuts import render

from .forms import Appform
from .forms import Keyform
from .keywordFinder import key_man
from .search import appStore
from .search import playStore

# Create your views here.


def home(request):
    """
    Home View

    """
    return render(request, template_name="home.html")


def appsearch(request):
    """
    App search View

    """
    form = Appform()

    return render(request, "appsearch.html", {"form": form})


def ajaxsearch(request):
    """
    Function for ajax request to
    App searching and response

    """

    data = {}

    if request.method == "POST" and request.is_ajax():

        if request.POST.get("store") == "1":

            data["play_app"] = request.POST.get("play_app")

            if data["play_app"] != "":

                url = ("https://play.google.com/store/apps/details?id=" +
                       data["play_app"])

                data_dict = playStore(url)

                if data_dict["ERROR"]:
                    return JsonResponse({"success": False}, status=400)

            else:

                return JsonResponse({"success": False}, status=400)

        else:

            data["ios_app"] = request.POST.get("ios_app")

            data["ios_app_no"] = request.POST.get("ios_app_no")

            if data["ios_app"] != "" and data["ios_app_no"] != "":

                url = ("https://apps.apple.com/in/app/" + data["ios_app"] +
                       "/id" + str(data["ios_app_no"]))

                data_dict = appStore(url)

                if data_dict["ERROR"]:
                    return JsonResponse({"success": False}, status=400)

            else:

                return JsonResponse({"success": False}, status=400)

        return JsonResponse(data_dict, status=200)

    return JsonResponse({"success": False}, status=400)


def key_view(request):
    """
    View for Keyword finder page

    """
    form = Keyform()

    return render(request, "keywords.html", {"form": form})


def key_view_ajax(request):
    """
    response to AJAX request for
    keyword finder

    """

    if request.method == "POST" and request.is_ajax():

        url = request.POST.get("url")

        obj = key_man(url)

        keywords = obj.keyword_finder()

        if len(keywords) == 0:

            return JsonResponse({"keywords": "No Keywords Found"}, status=200)

        obj.key_saver(keywords)

        related_url = obj.related_urls(keywords)

        keywords_of_related_url = obj.key_of_related_urls(related_url)

        recommended_keywords = obj.recommender(related_url)

        print(keywords)
        print(keywords_of_related_url)
        print(recommended_keywords)
        print(related_url)

        if len(keywords) == 0:
            keywords = False
        if len(list(keywords_of_related_url.keys())) == 0:
            keywords_of_related_url = False
        if len(recommended_keywords) == 0:
            recommended_keywords = False

        return JsonResponse(
            {
                "keywords": keywords,
                "recommended": recommended_keywords,
                "related": keywords_of_related_url,
            },
            status=200,
        )

    else:

        return JsonResponse({"success": False}, status=400)
