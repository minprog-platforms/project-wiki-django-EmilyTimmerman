from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/search_entries", views.search_entries, name="search_entries"),
    path("wiki/<str:entry>", views.entry, name="entry")
    ]
