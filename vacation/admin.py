from django.contrib import admin

# Register your models here.
from .models import Vacation

class VacationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'begin', 'last', 'note')
    list_filter = (
        ('user', admin.RelatedOnlyFieldListFilter),
        ('begin', admin.DateFieldListFilter),
    )

admin.site.register(Vacation, VacationAdmin)
