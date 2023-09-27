from django.urls import path
from . import views
from .views import LayoutDataView

urlpatterns = [
    # Другие URL-маршруты
    path('all-slides/', views.AllSlides.as_view(), name='all-slides'),
    path('layoutdata/', LayoutDataView.as_view(), name='layout-data'),
]
