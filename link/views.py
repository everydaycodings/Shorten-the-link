from django.shortcuts import render, HttpResponse
import bitly_api
# Create your views here.

def index(request):

    context = {}
  
    if request.method == "GET":
        BITLY_ACCESS_TOKEN = "a091b1da90ec1b14fa0f616afbb7fa833e925bfd"

        b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN) 
        
        linkget = request.GET.get("link")
        response = b.shorten(linkget) 
        short_url = response["url"]
        print(short_url)

        context = {"url": short_url}
    else:
        print("not post")
    

    return render(request, "link/index.html", context)



def result(request):
    return render(request, "link/result.html")