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
    code = models.CharField(
        verbose_name=_("Code"),
        help_text=_("The app is selecting a parser according to this code."),
        max_length=40,
        blank=False,
        null=False
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


# class Flat(IdModel):
#     SIZE_1kk = "1+kk"
#     SIZE_11 = "1+1"
#     SIZE_2kk = "2+kk"
#     SIZE_21 = "2+1"
#     SIZE_3kk = "3+kk"
#     SIZE_31 = "3+1"
#     SIZE_4_AND_MORE = "4+"
#     SIZE_CHOICES = [
#         (SIZE_1kk, "1+kk"),
#         (SIZE_11, "1+1"),
#         (SIZE_2kk, "2+kk"),
#         (SIZE_21, "2+1"),
#         (SIZE_3kk, "3+kk"),
#         (SIZE_31, "3+1"),
#         (SIZE_4_AND_MORE, _("4 and more")),
#     ]
#     size = models.CharField(
#         verbose_name=_("Size"),
#         choices=SIZE_CHOICES,
#         max_length=10,
#     )

class MarketplaceSourceLink(IdModel):
    marketplace = models.ForeignKey(
        Marketplace,
        verbose_name=_("Marketplace"),
        on_delete=models.RESTRICT,
        blank=False,
        null=False,
    )
    link = models.URLField(
        verbose_name=_("Link"),
        blank=False,
        null=False,
    )

