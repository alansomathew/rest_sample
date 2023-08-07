from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.getData),
    path('view/',views.getItems),
    path('add/',views.add_item),
    path('detail/<int:pk>/',views.detailView),
    path('update/<int:pk>/',views.updateItem),
    path('delete/<int:pk>/',views.deleteItem),

]