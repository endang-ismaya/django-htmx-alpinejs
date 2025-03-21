from django.contrib import admin

from app.models import Article, UserProfile


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "word_count",
        "status",
        "created_at",
        "updated_at",
        "creator_fullname",
    ]
    list_filter = ("status",)
    search_fields = ("title", "content")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    readonly_fields = ("word_count", "created_at", "updated_at")

    @admin.display(description="creator")
    def creator_fullname(self, obj: Article):
        if obj.creator:
            creator: UserProfile = obj.creator
            return f"{creator.first_name} {creator.last_name}"
        return "No Creator"


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
