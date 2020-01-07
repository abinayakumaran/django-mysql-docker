from django.urls import include, path, re_path
from . import views


urlpatterns = [
    path('api/v1/news/<uuid:pk>/', # Url to get update or delete a news
        views.get_delete_update_news.as_view(),
        name='get_delete_update_news'
    ),
    path('api/v1/news/', # urls list all and create new one
        views.get_post_news.as_view(),
        name='get_post_news'
    )
]