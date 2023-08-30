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
    title = models.CharField(_("Title"), max_length=64, null=False)
    body = models.TextField(_("Body"), null=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "post"
        verbose_name = _("post")
        ordering = ['-created']


class ReplyPost(BaseModel):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_("Post"), on_delete=models.CASCADE)
    reply = models.TextField(_("Reply"), null=False)
    parent_reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.reply

    class Meta:
        db_table = "reply_post"
        verbose_name = _("reply_post")
        ordering = ['-reply']


class LikePost(BaseModel):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_("Post"), on_delete=models.CASCADE)
    like = models.BooleanField(_("Like"), default=False)

    def __str__(self):
        return self.post.title

    class Meta:
        db_table = "like_post"
        verbose_name = _("like_post")
        ordering = ['-created']


