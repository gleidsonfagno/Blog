from django.contrib import admin

from gameblog.models import News, Category
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "content", "author", "published_at", "source_link", "tags",  "slug", "category",)
    search_fields = ("title", "subtitle", "author", "published_at", "image",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)