from django.contrib import admin
from .models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=['id','ti']
    search_fields=['ti','co']

admin.site.register(Article,ArticleAdmin)
