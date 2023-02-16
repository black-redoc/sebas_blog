from rest_framework.generics import (
    DestroyAPIView,
    GenericAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from .models import Blog
from .serializers import BlogSerializer


class BaseBlogAPIView(GenericAPIView):
    """
    BaseBlogAPIView
    Parent class with all base properties to allow inherit them
    to classes that need this base behavior like queryset
    and serializer_class.
    """

    serializer_class = BlogSerializer

    def get_queryset(self):
        """
        get_queryset
        Retrieves the Blog from the sessioned user, like a little
        tenant system.
        """
        author = self.request.user
        return Blog.objects.filter(blog_author=author)


class BlogListCreateAPIView(BaseBlogAPIView, ListCreateAPIView):
    """
    Create and List Blogs
    eg:
        GET /blogs/list
        Retrieves a list of blogs

        POST /blogs/list
        body: {
            "blog_title": "new_blog_title",
            "blog_content": "new_blog_content"
        }
        Retrieves 201 CREATED status code
    """

    def perform_create(self, serializer):
        """
        perform_create
        Performs a custom creation blog function. The releation
        between django bultin user/author and blog is needed to to
        create a new blog, this uses the current user session,
        just providing the jwt token in request headers is needed
        to perform the blog creation.
        """
        blog = serializer.validated_data
        author = self.request.user
        Blog.objects.create(
            blog_title=blog.get("blog_title"),
            blog_content=blog.get("blog_content"),
            blog_author=author,
        )


class BlogRetrieveAPIView(BaseBlogAPIView, RetrieveAPIView):
    """
    Get one Blog by id
    eg:
        GET /blogs/retrieve/{id}
        Retrieves the blog by {id}
    """


class BlogDestroyAPIView(BaseBlogAPIView, DestroyAPIView):
    """
    Destroy a blog by id
    eg:
        DELETE /blogs/destroy/{id}
        Destroys the blog with {id}
        Retrieves a 204 NO CONTENT status code
    """


class BlogUpdateAPIView(BaseBlogAPIView, UpdateAPIView):
    """
    Update a blog by id
    eg:
        PUT /blogs/update/{id}
        body: {
            "blog_title": "updated_blog_title"
            "blog_content": "updated_blog_content"
        }
        Retrieves a 200 OK status code
    """
