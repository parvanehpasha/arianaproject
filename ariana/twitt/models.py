from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created = models.DateTimeField(_("Create"), auto_now_add=True)
    updated = models.DateTimeField(_("Update"), auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    user = models.ForeignKey(User, verbose_name=_("Owner"), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=64)
    text = models.TextField(_("Text"), null=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "post"
        verbose_name = _("post")
        ordering = ['-created']