from django.urls import path

from .views import SearchAdvert
urlpatterns = [
    path("", SearchAdvert.as_view()),
]
