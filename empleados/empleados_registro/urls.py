from django.urls import path
from . import views

# urlpatterns = [
#   path('', views.empleados_form),
#  path('lista/', views.empleados_list),
# ]
urlpatterns = [
    path('', views.empleados_form, name='empleados_insert'),
    path('<int:id>/', views.empleados_form, name='empleados_update'),
    path('delete/<int:id>/', views.empleados_delete, name='empleados_delete'),
    path('lista/', views.empleados_list, name='empleados_list')
]