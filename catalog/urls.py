from django.urls import path

from catalog.views import (index,
                           LiteraryFormatListView,
                           BookListView,
                           AuthorListView,
                           book_detail_view,
                           AuthorDetailView)

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", book_detail_view, name="book-detail"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
]

app_name = "catalog"