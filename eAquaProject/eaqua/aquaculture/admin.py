from django.contrib import admin

from .models import FishDisease


class FishDiseaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'severity', 'updated_at')
    list_filter = ('severity', 'created_at')
    search_fields = ('name', 'symptoms')
    fieldsets = (
        (None, {
            'fields': ('name', 'severity')
        }),
        ('Disease Details', {
            'fields': ('symptoms', 'causes', 'prevention', 'treatment')
        }),
    )


admin.site.register(FishDisease, FishDiseaseAdmin)
