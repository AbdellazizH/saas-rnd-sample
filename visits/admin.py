from django.contrib import admin

from visits.models import PageVisit


@admin.register(PageVisit)
class PageVisitsAdmin(admin.ModelAdmin):
    class Meta:
        model = PageVisit
        fields = '__all__'
