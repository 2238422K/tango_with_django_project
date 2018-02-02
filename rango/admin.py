from django.contrib import admin

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display=('title','category','url')

from rango.models import Category, Page
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
