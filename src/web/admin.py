from django.contrib import admin

from web.models import Marketplace, MarketplaceSourceLink


@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    pass


@admin.register(MarketplaceSourceLink)
class MarkeplaceSourceLinkAdmin(admin.ModelAdmin):
    pass
