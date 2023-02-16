from django.db import models
from django.utils.translation import gettext_lazy as _

from config.settings.base import AUTH_USER_MODEL as User


class Blog(models.Model):
    """
    Blogs model
    """

    blog_title = models.CharField(_("blog_title"), max_length=80)
    blog_content = models.TextField(_("blog_content"))
    created_at = models.DateTimeField(_("blog_created_at"), auto_now_add=True)
    blog_author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return "[{}:{}:{}] ({}...)".format(
            self.blog_title,
            "" if not self.blog_author else self.blog_author.username,
            self.created_at.strftime("%d/%m/%Y"),
            self.blog_content[:15],
        )
