from django.contrib import admin

from web.models import Marketplace, MarketplaceData


@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    pass


@admin.register(MarketplaceData)
class MarketplaceDataAdmin(admin.ModelAdmin):
    pass
