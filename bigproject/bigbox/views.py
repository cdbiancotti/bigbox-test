from django.shortcuts import get_object_or_404, redirect, render
from .models import Box, Activity
from django.core.paginator import Paginator


def index(request):
    return render(request, 'bigbox/index.html')


def boxes(request):
    if request.method == 'POST':
        slug = request.POST['box_slug']
        return redirect(f'/box/{slug}')
    boxes = Box.objects.all()
    return render(request, 'bigbox/boxes.html', {'boxes': boxes})


def box_by_slug(request, box_slug):
    box = get_object_or_404(Box, slug=box_slug)
    box_activities = box.activities.all()[:5]
    return render(request, 'bigbox/box_detail.html', {'box': box, 'box_activities': box_activities})


def box(request, box_id):
    box = get_object_or_404(Box, pk=box_id)
    box_activities = box.activities.all()[:5]
    return render(request, 'bigbox/box_detail.html', {'box': box, 'box_activities': box_activities})


def box_activities(request, box_id):
    page_number = request.GET.get('page')
    box = get_object_or_404(Box, pk=box_id)
    box_activities = box.activities.order_by('name')
    pages = Paginator(box_activities, 20)
    page_selected = pages.page(page_number)
    return render(request, 'bigbox/box_activities.html', {'box_id': box_id, 'page_selected': page_selected})


def activity(request, box_id, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'bigbox/activity_detail.html', {'activity': activity})
