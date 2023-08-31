from django.urls import path
from .views import ApprenticesView

urlpatterns = [
    path('apprentices/', ApprenticesView.as_view(), name='apprentice_list'),
    path('apprentices/<int:id>', ApprenticesView.as_view())
]