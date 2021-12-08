from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("newpage", views.new, name="new_page")
    ]
