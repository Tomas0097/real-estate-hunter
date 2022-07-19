from django.db import models
from django.utils.translation import gettext_lazy as _


# The data of this model are not shown in the admin section in the table's column yet.
class IdModel(models.Model):
    id = models.BigAutoField(unique=True, primary_key=True)
    inserted = models.DateTimeField(
        verbose_name=_("Inserted"), auto_now_add=True
    )
    updated = models.DateTimeField(verbose_name=_("Updated"), auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        abstract = True
