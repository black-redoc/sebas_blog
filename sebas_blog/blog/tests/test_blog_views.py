from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from sebas_blog.blog.models import Blog
from sebas_blog.users.models import User

USERNAME = "test_user"
PASSWORD = "test_user"


class TestBlogAPIView(TestCase):
    def setUp(self):
        self.author = User.objects.create(
            username=USERNAME, password=make_password(PASSWORD)
        )
        token = Token.objects.create(user=self.author)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token %s" % token.key)

    def test_blog_list_view_returns_two_blogs(self):
        expected_status = 200
        expected_count = 2

        blogs = [
            Blog(blog_title="title1", blog_content="content1", blog_author=self.author),
            Blog(blog_title="title2", blog_content="content2", blog_author=self.author),
        ]
        Blog.objects.bulk_create(blogs)
        response = self.client.get(reverse("blogs:list_create"))
        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_count, len(response.json()))

    def test_blog_create_view_returns_created(self):
        expected_status = 201
        expected_title = "blog1"

        blog_data = {"blog_title": expected_title, "blog_content": "content1"}
        response = self.client.post(reverse("blogs:list_create"), data=blog_data)
        new_blog = Blog.objects.get(
            blog_title=blog_data["blog_title"], blog_author=self.author
        )
        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_title, new_blog.blog_title)

    def test_blog_retrieve_view_returns_a_blog(self):
        expected_status = 200
        expected_title = "blog1"
        blog = Blog.objects.create(
            blog_title=expected_title, blog_content="content1", blog_author=self.author
        )
        response = self.client.get(reverse("blogs:retrieve", kwargs={"pk": blog.pk}))

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_title, response.json()["blog_title"])

    def test_blog_destroy_view_returns_no_content(self):
        expected_status = 204
        expected_count = 0

        blog = Blog.objects.create(
            blog_title="blog1", blog_content="content1", blog_author=self.author
        )

        response = self.client.delete(reverse("blogs:destroy", kwargs={"pk": blog.pk}))
        blog_count = Blog.objects.filter(
            blog_title=blog.blog_title, blog_author=self.author
        ).count()

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_count, blog_count)

    def test_blog_update_view_returns_no_content(self):
        expected_status = 200
        expected_title = "updated_title"
        blog_content = "content1"
        blog = Blog.objects.create(
            blog_title="blog1", blog_content=blog_content, blog_author=self.author
        )

        blog_data = {"blog_title": expected_title, "blog_content": blog_content}

        response = self.client.put(
            reverse("blogs:update", kwargs={"pk": blog.pk}), data=blog_data
        )
        updated_title = Blog.objects.get(pk=blog.pk).blog_title

        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_title, updated_title)
        self.assertNotEqual("blog1", updated_title)
