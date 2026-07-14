from django.contrib import admin
from .models import Case

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ["reference", "client", "opponent", "status", "responsible_lawyer"]
    list_filter = ["status", "area_of_law"]
    search_fields = ["reference", "client", "opponent"]