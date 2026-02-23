from django.contrib import admin
from .models import BlogPost, Comment, ContactMessage, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'description': ('name',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_categories', 'datetime_created')
    filter_horizontal = ('categories',)

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

    display_categories.short_description = 'دسته‌بندی‌ها'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'status', 'stars', 'datetime_created')
    list_filter = ('status', 'stars', 'datetime_created')
    search_fields = ('content', 'author__username', 'post__title')
    list_editable = ('status', 'stars')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'is_read', 'datetime_created')
    list_filter = ('is_read', 'datetime_created')
    search_fields = ('name', 'email', 'subject', 'message')

    list_editable = ('is_read',)