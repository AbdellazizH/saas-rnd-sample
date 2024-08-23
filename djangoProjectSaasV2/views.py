from django.shortcuts import render

from visits.models import PageVisit


def home_page_view(request):
    page_title = "Home Page"
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)

    PageVisit.objects.create(path=request.path)

    context = {
        "page_title": page_title,
        "page_visit_count": page_qs.count(),
        "percent": round(page_qs.count() * 100 / qs.count(), 1),
        "total_visit_count": qs.count(),
    }
    return render(request, 'home/home.html', context)
