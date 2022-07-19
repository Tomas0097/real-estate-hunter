from django.contrib import admin

from web.models import Marketplace


@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    pass
