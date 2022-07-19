from django.db import models
from django.utils.translation import gettext_lazy as _

from real_estate_hunter.models import IdModel


class Marketplace(IdModel):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=40,
        blank=False,
        null=False,
    )
    homepage_link = models.URLField(
        verbose_name=_("Homepage link"),
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Marketplace")
        verbose_name_plural = _("Marketplaces")
