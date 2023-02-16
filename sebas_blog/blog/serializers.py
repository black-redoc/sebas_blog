from rest_framework.serializers import CharField, ModelSerializer

from .models import Blog


class BlogSerializer(ModelSerializer):
    """
    BlogSerializer
    """

    blog_author = CharField(read_only=True, source="blog_author.username")

    class Meta:
        model = Blog
        fields = ["id", "blog_title", "blog_content", "created_at", "blog_author"]
