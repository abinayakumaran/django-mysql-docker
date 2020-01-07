from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/category/(?P<pk>[0-9]+)$', # Url to get update or delete a news
        views.get_delete_update_category.as_view(),
        name='get_delete_update_category'
    ),
    path('api/v1/category/', # urls list all and create new one
        views.get_post_category.as_view(),
        name='get_post_category'
    )
]