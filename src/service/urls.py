from django.urls import path
from .views import ServiceListView, service_detail_view, SearchServiceListView

urlpatterns = [
    path("", ServiceListView.as_view(), name="service_list"),  # List of services
    path("<int:pk>/", service_detail_view, name="service_detail"),  # Service details
    path("services/search/", SearchServiceListView.as_view(), name="search_services"),
]