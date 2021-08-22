from django.db import models
from django.urls import reverse
from members.models import Member

class Book(models.Model):
    user = models.ForeignKey(Member, related_name='book',on_delete=models.CASCADE)
    LANGUAGES = (
       ('eng', ('İngilizce')),
       ('de', ('Almanca')),
       ('tr', ('Türkçe')),
   )
    title = models.CharField(max_length=240)
    author = models.CharField(max_length=240)
    isbn = models.CharField(max_length=30)
    numberOfPages = models.IntegerField()
    language = models.CharField(
       max_length=40,
       choices=LANGUAGES,
       default='İngilizce',
   )
    publisher = models.CharField(max_length=240)
    #dateOfEntry = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("books:book-list")
    
    def get_update_url(self):
        return reverse("books:book-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("books:book-delete", kwargs={"id": self.id})
        

