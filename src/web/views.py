from django.http import HttpResponse


def index(request):
    return HttpResponse("Real estate Hunter is working :)")
