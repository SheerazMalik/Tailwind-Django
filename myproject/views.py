
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, Your at Pakistani and coding Home page")

    return render(request, "index.html")