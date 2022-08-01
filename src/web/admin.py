from django.contrib import admin

from web.models import Marketplace, MarketplaceData


@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(MarketplaceData)
class MarketplaceDataAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "marketplace",
        "start_scanning_date",
        "end_scanning_date",
        "properties_amount",
    )
