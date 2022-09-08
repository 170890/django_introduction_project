from django.contrib import admin
from .models import People, Contact

@admin.action(description='Enable all people')
def enableAll(modeladmin, request, queryset):
    queryset.update(active=True)

@admin.action(description='Disable all people')
def disableAll(modeladmin, request, queryset):
    queryset.update(active=True)

class peopleAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'birthday',
        'active'
    ]
    list_filter = [
        'active',
        'birthday'
    ]
    search_fields = [
        'full_name'
    ]
    actions = [
        enableAll,
        disableAll
    ]

admin.site.register(People, peopleAdmin)
admin.site.register(Contact)


