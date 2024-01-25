from django.contrib import admin
from django.urls import path
from demoapp.views import index, add_demo, edit_demo

urlpatterns = [
    path('admin/', admin.site.urls),
	
    path('', index, name='index'),
    path('add_demo/', add_demo, name='add_demo'),
    path('edit_demo/<int:pk>/', edit_demo, name='edit_demo')
]
