from django.shortcuts import render

from visits.models import PageVisit


def home_view(request):
    print(request.user.is_authenticated, request.user)
    return about_page_view(request)


def about_page_view(request):
    page_title = "Home Page"
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)

    try:
        percent = round(page_qs.count() * 100 / qs.count(), 1)
    except:
        percent = 0

    PageVisit.objects.create(path=request.path)

    context = {
        "page_title": page_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count(),
    }
    return render(request, 'home/home.html', context)

