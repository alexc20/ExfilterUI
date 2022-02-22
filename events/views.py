from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from eventapi.models import EgressEvent
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
def event_view(request):
    events_list = EgressEvent.objects.all().order_by("-Timestamp_ns")
    page = request.GET.get('page', 1)
    paginator = Paginator(events_list, 10)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    return render(request, 'events.html', {"events": events})