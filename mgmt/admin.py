from django.contrib import admin
from .models import Group, Campus, Person

# Register your models here.

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    readonly_fields = ("oid",)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ("oid",)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ("oid",)
