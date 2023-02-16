from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = _("Blogs")
    name = "sebas_blog.blog"

    def ready(self):
        try:
            import sebas_blog.blog.signals  # noqa F401
        except ImportError:
            pass
