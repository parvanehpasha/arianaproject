from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created = models.DateTimeField(_("Create"), auto_now_add=True)
    updated = models.DateTimeField(_("Update"), auto_now=True)

    class Meta:
        abstract = True
