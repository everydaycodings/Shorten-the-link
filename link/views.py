from django.shortcuts import render, HttpResponse, redirect
import bitly_api
# Create your views here.

def index(request):

    if request.method == "POST":
        BITLY_ACCESS_TOKEN = "a091b1da90ec1b14fa0f616afbb7fa833e925bfd"

        b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN) 
        global short_url
        linkget = request.POST.get("link")
        response = b.shorten(linkget) 
        short_url = response["url"]       
        print(short_url)
        return redirect("result")
    

    return render(request, "link/index.html")



def result(request):
    url = short_url
    context = {"link": url}

    return render(request, "link/result.html", context
    )