from django.urls import path

from .views import (
    BlogDestroyAPIView,
    BlogListCreateAPIView,
    BlogRetrieveAPIView,
    BlogUpdateAPIView,
)

app_name = "blog"
urlpatterns = [
    path("list/", view=BlogListCreateAPIView.as_view(), name="list_create"),
    path("destroy/<int:pk>/", view=BlogDestroyAPIView.as_view(), name="destroy"),
    path("retrieve/<int:pk>/", view=BlogRetrieveAPIView.as_view(), name="retrieve"),
    path("update/<int:pk>/", view=BlogUpdateAPIView.as_view(), name="update"),
]
