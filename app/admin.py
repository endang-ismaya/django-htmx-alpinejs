from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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
class UserProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Groups", {"fields": ("groups", "user_permissions")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": ("email", "password1", "password2"),
                "classes": ("wide",),
            },
        ),
        ("Personal info", {"fields": ("first_name", "last_name")}),
    )
    list_display = ["email", "first_name", "last_name", "is_staff", "is_active"]
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    readonly_fields = ("last_login", "date_joined")
