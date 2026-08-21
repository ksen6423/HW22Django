from django.contrib import admin

from openpage.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "preview", "creation_date")
    list_filter = ("title",)
    search_fields = ("title",)
