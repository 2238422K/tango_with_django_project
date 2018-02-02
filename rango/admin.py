from rango.models import Category, Page

from django.contrib import admin

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display=('title','category','url')

from rango.models import Category, Page
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

