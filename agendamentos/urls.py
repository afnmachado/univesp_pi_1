from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('agendar/', views.agendar, name = 'agendar'),
    path('modificar/', views.excluir, name = 'excluir'),
    path('itinerario/', views.itinerario, name = 'itinerario'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('agenda/', views.agenda, name = 'agenda'),
    #path('itinerario/', views.list_view, name = 'list_view'),
    path('<id>/update', views.update_view, name = 'update_view'),
    path('<id>', views.detail_view, name = 'detail_view'),
]