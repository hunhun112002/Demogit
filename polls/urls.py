from django.urls import path
from . import views
from .view2 import ItemListView


urlpatterns = [
    path('detail/<int:question_id>', views.viewsdetail , name='detail'),
    path('list/', views.viewlist, name='viewlist'),
    path('', views.index ,name='index'),
    path('items/' , ItemListView.as_view(),name='items-list') 
]   
