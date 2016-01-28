from django.contrib import admin
from . import models
from models import Article, Comments
class Article_Inline(admin.StackedInline):
    model = Comments
    extra = 1
class Article_admin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date']
    inlines = [Article_Inline]
    list_filter = ['article_date']
admin.site.register(Article, Article_admin)