from django.contrib import admin
from django.urls import path
from recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.receipes),
    path('update_receipe/<id>', views.update_receipe, name='update_receipe'),
   path('delete_receipe/<id>', views.delete_receipe, name='delete_receipe'),
]