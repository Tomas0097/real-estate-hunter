from django.http import HttpResponse
from django.views.generic import TemplateView

from real_estate_hunter.web_parsers import get_web_parser
from web.models import Marketplace


class IndexView(TemplateView):
    template_name = "index.html"


def parse_marketplace(request, marketplace_code):
    web_parser = get_web_parser(marketplace_code)
    marketplace = Marketplace.objects.get(code=marketplace_code)
    properties_amount = web_parser(marketplace)

    return HttpResponse(
        f"<body><div>Parsing marketplace: <strong>{marketplace.name}</strong> completed. "
        f"Properties amount: {properties_amount}.</div></body>"
    )
