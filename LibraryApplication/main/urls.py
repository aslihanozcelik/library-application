from django.contrib import admin
from django.urls import include, path

from book.views import home_view


urlpatterns = [
    path('book/', include('book.urls')),
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
]


