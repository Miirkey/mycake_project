from django.contrib import admin

from .models import Baker

class BakerAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'is_mvp', 'email', 'hire_date')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 25

admin.site.register(Baker, BakerAdmin)