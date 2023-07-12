"""
URL configuration for table_builder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.views import TableCreateView, TableUpdateView, TableRowCreateView, TableRowListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/table', TableCreateView.as_view(), name='table-create'),
    path('api/table/<int:pk>', TableUpdateView.as_view(), name='table-update'),
    path('api/table/<int:id>/row', TableRowCreateView.as_view(), name='table-row-create'),
    path('api/table/<int:id>/rows', TableRowListView.as_view(), name='table-row-list'),
]
