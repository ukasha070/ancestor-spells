from django.db.models import Q
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404

from .models import Service

class ServiceListView(ListView):
    paginate_by = 10
    model = Service
    template_name = 'service/services_list.html'
    context_object_name = 'services'
    ordering = ['-created_at']


def service_detail_view(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, "service/service_detail.html", {"service": service})


class SearchServiceListView(ListView):
    model = Service
    template_name = 'service/services_list.html'
    context_object_name = 'services'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Service.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            ).distinct()
        return Service.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  # Pass the search query back
        return context