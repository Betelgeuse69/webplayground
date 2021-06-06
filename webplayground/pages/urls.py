from django.contrib.auth import login
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PageDelete, PageUpdate, PagesListView, PageDetailView, PageCreate, PageDelete

#Cambiamos urlpatterns por pages_patterns (ese nombre es libre) y cambiamos de lista a tupla añadiendo un paréntesis y un parámetro:
pages_patterns = ([
    path('', login_required(PagesListView.as_view()), name='pages'),
    path('<int:pk>/<slug:slug>/', login_required(PageDetailView.as_view()), name='page'),
    path('create/', login_required(PageCreate.as_view()), name='create'),
    path('update/<int:pk>/', login_required(PageUpdate.as_view()), name='update'),
    path('delete/<int:pk>/', login_required(PageDelete.as_view()), name='delete'),
], 'pages')