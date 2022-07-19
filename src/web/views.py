from django.http import HttpResponse


def index(request):
    return HttpResponse("Reality Hunter is working :)")
