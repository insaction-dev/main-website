from django.contrib import admin
from rules.contrib.admin import ObjectPermissionsModelAdmin
from .models import Category, Article, Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(ObjectPermissionsModelAdmin):
    date_hierarchy = 'created'
    readonly_fields = ('created', 'modified', 'slug')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
