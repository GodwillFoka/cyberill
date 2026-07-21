from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'language', 'published', 'created_at']
    list_filter = ['published', 'language', 'category', 'created_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    actions = ['publish_articles', 'unpublish_articles']

    def publish_articles(self, request, queryset):
        queryset.update(published=True)
    publish_articles.short_description = "Publier les articles sélectionnés"

    def unpublish_articles(self, request, queryset):
        queryset.update(published=False)
    unpublish_articles.short_description = "Dépublier les articles sélectionnés"
