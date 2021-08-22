from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from members.models import Member

from .forms import BookModelForm
from .models import Book


class BookCreateView(CreateView):
    template_name = 'books/book_create.html'
    form_class = BookModelForm
    queryset = Book.objects.all() 
   
    def form_valid(self, form):
        
        print(form.cleaned_data)
        return super().form_valid(form)


class BookListView(ListView):
    template_name = 'books/book_list.html'
    queryset = Book.objects.all().order_by('isbn')[0:30]


class BookUpdateView(UpdateView):
    template_name = 'books/book_update.html'
    form_class = BookModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class BookDeleteView(DeleteView):
    template_name = 'books/book_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)

    def get_success_url(self):
        return reverse('books:book-list')


def home_view(request, *args, **kwargs): 
    print(request.user)
    return render(request, "home.html", {})






