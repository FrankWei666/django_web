from django.contrib import admin
from .models import Test, Contact, Tag

# Register your models here.


# class ContactAdmin(admin.ModelAdmin):
#     """第一种"""
#     fields = ('name', 'email')


# class ContactAdmin(admin.ModelAdmin):
#     """第二种"""
#     fieldsets = (
#         ['Main', {
#             'fields': ('name', 'email'),
#         }],
#         ['others', {
#             'classes': ('collapse',),
#             'fields': ('age',),
#         }]
#     )


"""第三种"""


class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['others', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
