from django.db import models
from django.urls import reverse


class Member(models.Model):
    
    name = models.CharField(max_length=200)
    tc = models.IntegerField(max_length=11)
    phone = models.IntegerField(max_length=11)
    address = models.CharField(max_length=240)

    def get_absolute_url(self):
        return reverse("members:member-list")
    
    def get_update_url(self):
        return reverse("members:member-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("members:member-delete", kwargs={"id": self.id})
        
    def __str__(self):
        return self.name