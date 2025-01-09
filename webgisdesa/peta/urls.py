from django.urls import path
from . import views

app_name = 'peta'

urlpatterns = [
    path('', views.LihatSuperhero, name='lihat_superhero'),
    path('create', views.createSuperhero, name='buat_superhero'),
    path('simpan/', views.simpan, name='simpan'),
    path('delete/<int:id>', views.deleteSuperhero, name='delete'),
    path('update/<int:id>', views.updateSuperhero, name='update'),
    path('edit/<int:id>', views.update, name='edit'),
]