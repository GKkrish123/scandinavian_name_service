from django.contrib import admin
from .models import NameVerification

@admin.register(NameVerification)
class NameVerificationAdmin(admin.ModelAdmin):
    list_display = ('input_name', 'suggested_name', 'country', 'is_correct', 'verified_by', 'verified_at')
    list_filter = ('country', 'is_correct')
    search_fields = ('input_name', 'suggested_name')
