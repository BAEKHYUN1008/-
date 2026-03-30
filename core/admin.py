from django.contrib import admin
from .models import User, Law, Synonym, Subscription

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role',)

@admin.register(Law)
class LawAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'created_at')
    search_fields = ('title', 'content')

@admin.register(Synonym)
class SynonymAdmin(admin.ModelAdmin):
    list_display = ('term', 'synonyms')
    search_fields = ('term',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'scene', 'created_at')
    list_filter = ('scene',)
