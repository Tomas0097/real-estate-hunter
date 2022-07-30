from django.http import HttpResponse

from real_estate_hunter.web_parsers import get_web_parser

from web.models import Marketplace


def index(request):
    return HttpResponse("Real estate Hunter is working :)")


def parse_marketplace(request, marketplace_code):
    stats = {
        "properties_amount": 0,
        "properties_with_price": 0,
        "properties_without_price": 0,
        "properties_price_together": 0
    }
    parser = get_web_parser(marketplace_code)

    marketplace = Marketplace.objects.get(code=marketplace_code)
    for starting_source in marketplace.marketplacesourcelink_set.all():
        stats["properties_amount"] += parser(starting_source.link)

    return HttpResponse(f"Parsing {marketplace.name} completed. Number of flats: {stats['properties_amount']}.")
