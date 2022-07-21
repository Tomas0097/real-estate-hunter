from django.http import HttpResponse

from real_estate_hunter.web_parsers import get_parser_by_marketplace_code

from web.models import Marketplace


def index(request):
    return HttpResponse("Real estate Hunter is working :)")


STAT_NUMBER_OF_FLATS = "number_of_flats"


def parse_marketplace(request, marketplace_code):
    stats = {STAT_NUMBER_OF_FLATS: 0}
    parser = get_parser_by_marketplace_code(marketplace_code)

    marketplace = Marketplace.objects.get(code=marketplace_code)
    for source_link in marketplace.marketplacesourcelink_set.all():
        stats[STAT_NUMBER_OF_FLATS] += parser(source_link)

    return HttpResponse(f"Parsing {marketplace.name} completed. Number of flats: {stats[STAT_NUMBER_OF_FLATS]}.")
