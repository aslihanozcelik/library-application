from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .forms import MemberModelForm
from .models import Member


class MemberCreateView(CreateView):
    template_name = 'members/member_create.html'
    form_class = MemberModelForm
    queryset = Member.objects.all() 


    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class MemberListView(ListView):
    template_name = 'members/member_list.html'
    queryset = Member.objects.all() 



class MemberUpdateView(UpdateView):
    template_name = 'members/member_update.html'
    form_class = MemberModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Member, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class MemberDeleteView(DeleteView):
    template_name = 'members/member_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Member, id=id_)

    def get_success_url(self):
        return reverse('members:member-list')
