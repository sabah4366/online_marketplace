
from django.urls import path
from .import views

app_name='item'

urlpatterns = [
   
    path('<int:pk>/', views.detail , name="detail"),
    path('<int:pk>/delete/',views.deleteitem , name='delete'),
    path('new/', views.newitem , name='new'),
    path('items/', views.items , name='items'),
    path('<int:pk>/edit/',views.edititem, name='edit'),
]
