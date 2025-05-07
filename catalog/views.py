from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Book, Author, LiteraryFormat


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_literary_formats = LiteraryFormat.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_literary_formats": num_literary_formats,
        "num_visits": num_visits + 1,
    }
    return render(request, "catalog/index.html", context=context)


class LiteraryFormatListView(LoginRequiredMixin, generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"


class LiteraryFormatCreateView(LoginRequiredMixin, generic.CreateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary-format-list")
    template_name = "catalog/literary_format_form.html"


class LiteraryFormatUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary-format-list")
    template_name = "catalog/literary_format_form.html"


class LiteraryFormatDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_confirm_delete.html"
    success_url = reverse_lazy("catalog:literary-format-list")


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    queryset = Book.objects.select_related("format")
    paginate_by = 4


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


# @login_required
# def book_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         raise Http404("Book does not exist")
#     context = {
#         "book": book,
#     }
#     return render(request, "catalog/book_detail.html", context=context)


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    queryset = Author.objects.prefetch_related("books")
    paginate_by = 4


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author


# def author_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
#     try:
#         author = Author.objects.get(pk=pk)
#     except Author.DoesNotExist:
#         raise Http404("Author does not exist")
#     context = {
#         "author": author,
#     }
#     return render(request, "catalog/author_detail.html", context=context)

# def test_session_view(request: HttpRequest) -> HttpResponse:
#     return HttpResponse(
#         "<h1>Test Session</h1>"
#     )

