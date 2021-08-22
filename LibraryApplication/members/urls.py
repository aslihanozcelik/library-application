from django.urls import path
from .views import (
    MemberListView,
    MemberCreateView,
    MemberUpdateView,
    MemberDeleteView

)

app_name = 'members'
urlpatterns = [
    path('', MemberListView.as_view(), name='member-list'),
    path('create/', MemberCreateView.as_view(), name='member-create'), 
    path('<int:id>/update/', MemberUpdateView.as_view(), name='member-update'),
    path('<int:id>/delete/', MemberDeleteView.as_view(), name='member-delete'),
]